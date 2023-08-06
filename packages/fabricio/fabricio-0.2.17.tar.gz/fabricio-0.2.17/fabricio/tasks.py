import contextlib
import functools
import os
import sys
import types
import weakref

import six

from fabric import api as fab, colors
from fabric.contrib import console
from fabric.main import is_task_object
from fabric.tasks import WrappedCallableTask

import fabricio

from fabricio import docker
from fabricio.utils import patch, strtobool, Options

__all__ = [
    'infrastructure',
    'skip_unknown_host',
    'DockerTasks',
    'PullDockerTasks',
    'BuildDockerTasks',
]


def infrastructure(
    confirm=True,
    color=colors.yellow,
    autoconfirm_env_var='FABRICIO_INFRASTRUCTURE_AUTOCONFIRM',
):
    def _decorator(task):
        @functools.wraps(task)
        def _task(*args, **kwargs):
            if confirm:
                confirmed = strtobool(os.environ.get(autoconfirm_env_var, 0))
                if not confirmed and not console.confirm(
                    'Are you sure you want to select {infrastructure} '
                    'infrastructure to run task(s) on?'.format(
                        infrastructure=color(task.__name__),
                    ),
                    default=False,
                ):
                    fab.abort('Aborted')
            fab.env.infrastructure = task.__name__
            return task(*args, **kwargs)
        _task.wrapped = task  # compatibility with '--display <task>' option
        return fab.task(_task)
    fab.env.setdefault('infrastructure', None)
    if callable(confirm):
        func, confirm = confirm, six.get_function_defaults(infrastructure)[0]
        return _decorator(func)
    return _decorator


def skip_unknown_host(task):
    @functools.wraps(task)
    def _task(*args, **kwargs):
        if fab.env.get('host_string', False):
            return task(*args, **kwargs)
        fabricio.log('task `{task}` skipped (no host provided)'.format(
            task=fab.env.command,
        ))
    _task.wrapped = task  # compatibility with '--display <task>' option
    return _task


class IgnoreHostsTask(WrappedCallableTask):

    hosts = roles = property(lambda self: (), lambda self, value: None)


class Tasks(object):

    @property
    def __name__(self):
        return self

    __class__ = types.ModuleType

    def __new__(cls, **kwargs):
        self = object.__new__(cls)
        _self = weakref.proxy(self)
        for attr in dir(cls):
            attr_value = getattr(cls, attr)
            if is_task_object(attr_value):
                task_decorator = fab.task(
                    default=attr_value.is_default,
                    name=attr_value.name,
                    aliases=attr_value.aliases,
                    task_class=attr_value.__class__,
                )
                task = task_decorator(functools.wraps(attr_value)(
                    functools.partial(attr_value.wrapped, _self),
                ))
                setattr(self, attr, task)
        return self

    def __init__(self, roles=(), hosts=(), create_default_roles=True):
        if create_default_roles:
            for role in roles:
                fab.env.roledefs.setdefault(role, [])
        for task in self:
            task.roles = roles
            task.hosts = hosts

    def __iter__(self):
        for name, attr_value in vars(self).items():
            if is_task_object(attr_value):
                yield attr_value


class DockerTasks(Tasks):

    def __init__(
        self,
        container,
        registry=None,
        migrate_commands=False,
        backup_commands=False,
        **kwargs
    ):
        super(DockerTasks, self).__init__(**kwargs)
        self.registry = registry and docker.Registry(registry)
        self.container = container  # type: docker.Container
        self.backup.use_task_objects = backup_commands
        self.restore.use_task_objects = backup_commands
        self.migrate.use_task_objects = migrate_commands
        self.migrate_back.use_task_objects = migrate_commands

    @property
    def image(self):
        return self.container.__class__.image

    @fab.task
    @skip_unknown_host
    def revert(self):
        """
        revert - revert Docker container to previous version
        """
        self.container.revert()

    @fab.task
    @fab.serial
    @skip_unknown_host
    def migrate(self, tag=None):
        """
        migrate[:tag=None] - apply migrations
        """
        self.container.migrate(tag=tag, registry=self.registry)

    @fab.task
    @fab.serial
    @skip_unknown_host
    def migrate_back(self):
        """
        migrate_back - remove applied migrations returning to previous state
        """
        self.container.migrate_back()

    @fab.task(task_class=IgnoreHostsTask)
    def rollback(self, migrate_back=True):
        """
        rollback[:migrate_back=yes] - migrate_back -> revert
        """
        if strtobool(migrate_back):
            fab.execute(self.migrate_back)
        fab.execute(self.revert)

    @fab.task
    @fab.serial
    @skip_unknown_host
    def backup(self):
        """
        backup - backup data
        """
        self.container.backup()

    @fab.task
    @fab.serial
    @skip_unknown_host
    def restore(self, backup_name=None):
        """
        restore[backup_name=None] - restore data
        """
        self.container.restore(backup_name=backup_name)

    @fab.task
    @skip_unknown_host
    def pull(self, tag=None):
        """
        pull[:tag=None] - pull Docker image from registry
        """
        fabricio.run(
            'docker pull {image}'.format(image=self.image[self.registry:tag]),
            quiet=False,
        )

    @fab.task
    @skip_unknown_host
    def update(self, force=False, tag=None):
        """
        update[:force=no,tag=None] - recreate Docker container
        """
        self.container.update(
            force=strtobool(force),
            tag=tag,
            registry=self.registry,
        )

    @fab.task(default=True, task_class=IgnoreHostsTask)
    def deploy(self, force=False, tag=None, migrate=True, backup=False):
        """
        deploy[:force=no,tag=None,migrate=yes,backup=no] - \
backup -> pull -> migrate -> update
        """
        if strtobool(backup):
            fab.execute(self.backup)
        fab.execute(self.pull, tag=tag)
        if strtobool(migrate):
            fab.execute(self.migrate, tag=tag)
        fab.execute(self.update, force=force, tag=tag)


class PullDockerTasks(DockerTasks):

    def __init__(
        self,
        registry='localhost:5000',
        local_registry='localhost:5000',
        **kwargs
    ):
        super(PullDockerTasks, self).__init__(registry=registry, **kwargs)
        self.local_registry = docker.Registry(local_registry)

    @fab.task(task_class=IgnoreHostsTask)
    def push(self, tag=None):
        """
        push[:tag=None] - push Docker image to registry
        """
        local_tag = str(self.image[self.local_registry:tag])
        fabricio.local(
            'docker tag {image} {tag}'.format(
                image=self.image[tag],
                tag=local_tag,
            ),
            use_cache=True,
        )
        fabricio.local(
            'docker push {tag}'.format(tag=local_tag),
            quiet=False,
            use_cache=True,
        )
        fabricio.local(
            'docker rmi {tag}'.format(tag=local_tag),
            use_cache=True,
        )

    @fab.task
    @skip_unknown_host
    def pull(self, tag=None):
        """
        pull[:tag=None] - pull Docker image from registry
        """
        with contextlib.closing(open(os.devnull, 'w')) as output:
            with patch(sys, 'stdout', output):
                # forward sys.stdout to os.devnull to prevent
                # printing debug messages by fab.remote_tunnel

                with fab.remote_tunnel(
                    remote_port=self.registry.port,
                    local_port=self.local_registry.port,
                    local_host=self.local_registry.host,
                ):
                    DockerTasks.pull(self, tag=tag)

    @fab.task(task_class=IgnoreHostsTask)
    def prepare(self, tag=None):
        """
        prepare[:tag=None] - prepare Docker image
        """
        fabricio.local(
            'docker pull {image}'.format(image=self.image[tag]),
            quiet=False,
            use_cache=True,
        )
        self.remove_obsolete_images()

    @fab.task(default=True, task_class=IgnoreHostsTask)
    def deploy(self, force=False, tag=None, *args, **kwargs):
        """
        deploy[:force=no,tag=None,migrate=yes,backup=no] - \
prepare -> push -> backup -> pull -> migrate -> update
        """
        fab.execute(self.prepare, tag=tag)
        fab.execute(self.push, tag=tag)
        DockerTasks.deploy(self, force=force, tag=tag, *args, **kwargs)

    @staticmethod
    def remove_obsolete_images():
        fabricio.local(
            'docker rmi $(docker images --filter "dangling=true" --quiet)',
            ignore_errors=True,
        )


class BuildDockerTasks(PullDockerTasks):

    def __init__(self, build_path='.', **kwargs):
        super(BuildDockerTasks, self).__init__(**kwargs)
        self.build_path = build_path

    @fab.task(task_class=IgnoreHostsTask)
    def prepare(self, tag=None, no_cache=False):
        """
        prepare[:tag=None,no_cache=no] - prepare Docker image
        """
        options = Options([
            ('tag', str(self.image[tag])),
            ('no-cache', strtobool(no_cache)),
            ('pull', True),
        ])
        fabricio.local(
            'docker build {options} {build_path}'.format(
                build_path=self.build_path,
                options=options,
            ),
            quiet=False,
            use_cache=True,
        )
        self.remove_obsolete_images()

    @fab.task(default=True, task_class=IgnoreHostsTask)
    def deploy(self, force=False, tag=None, no_cache=False, *args, **kwargs):
        """
        deploy[:force=no,tag=None,migrate=yes,backup=no,no_cache=no] - \
prepare -> push -> backup -> pull -> migrate -> update
        """
        fab.execute(self.prepare, tag=tag, no_cache=no_cache)
        fab.execute(self.push, tag=tag)
        DockerTasks.deploy(self, force=force, tag=tag, *args, **kwargs)
