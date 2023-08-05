# Copyright (c) 2016 Mirantis Inc.
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an AS IS BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and#
# limitations under the License.

import logging

from oslo_config import cfg

from cloudferry.lib.base import exception
from cloudferry.lib.utils import extensions
from cloudferry.lib.utils import files
from cloudferry.lib.utils import remote_runner

LOG = logging.getLogger(__name__)
CONF = cfg.CONF


class FileCopyError(exception.CFBaseException):
    message = ("Error copying file from '{host_src}:{path_src}' "
               "to '{host_dst}:{path_dst}'")


class BaseCopier(object):
    name = None

    def __init__(self, src_cloud, dst_cloud):
        self.src_cloud = src_cloud
        self.dst_cloud = dst_cloud

    def transfer(self, data):
        """
        Transfer a file between the hosts.

        :param data: The dictionary with necessary information
        :raise FileCopyFailure if verification failed
        """
        raise NotImplementedError()

    def clean_dst(self, host_dst, path_dst):
        """
        Remove the file on destination.

        :param host_dst: The destination host
        :param path_dst: The path of file on destination host
        """
        files.remote_rm(self.runner(host_dst, 'dst'), path_dst,
                        ignoring_errors=True)

    def runner(self, host, position, gateway=None, **kwargs):
        """
        Alias for creating a RemoteRunner

        :param host: Host
        :param position: 'src' or 'dst' cloud
        :param gateway: Gateway for a runner
        :return: RemoteRunner
        """
        if position == 'src':
            user = CONF.src.ssh_user
            password = CONF.src.ssh_sudo_password
        else:
            user = CONF.dst.ssh_user
            password = CONF.dst.ssh_sudo_password
        return remote_runner.RemoteRunner(
            host,
            user,
            password=password,
            sudo=True,
            gateway=gateway,
            **kwargs)

    def check_usage(self, data):  # pylint: disable=unused-argument
        """
        Checking the possibility of using a copier.

        :param data: The dictionary with necessary information
        :return: True or False
        """
        return True

    @classmethod
    def get_name(cls):
        return cls.name or cls.__name__


class CopierAddingWritePermissionsInDestination(object):
    """Decorates concrete copiers.

    When running migration as unprivileged user (non-root), destination
    node may not have write permissions to write file over network using
    rsync, bbcp, or scp. This copier wrapper resolves the problem by
    temporarily chmod'ing destination folder to 777 and reverting
    permissions back once done."""

    def __init__(self, copier, config):
        self.config = config
        self.copier = copier

    def transfer(self, data):
        dst_host = data['host_dst']
        dst_path = data['path_dst']

        dst_runner = remote_runner.RemoteRunner(
            host=dst_host,
            user=self.config.dst.ssh_user,
            password=self.config.dst.ssh_sudo_password,
            sudo=True)

        with files.grant_all_permissions(dst_runner, dst_path):
            self.copier.transfer(data)

    def __getattr__(self, item):
        return getattr(self.copier, item)

    def __repr__(self):
        return self.__class__.__name__ + repr(self.copier)


class CopierNotFound(exception.AbortMigrationError):
    message = "Copier '{name}' not found"


class CopierCannotBeUsed(CopierNotFound):
    message = ("Copier '{name}' cannot be used on hosts '{host_src}' and/or "
               "'{host_dst}'")


def get_copier_class(name=None):
    """
    Returns the copier by its name or default copier if name is None

    :param name: Name of copier or None
    :return: A copier's class
    """
    name = name or CONF.migrate.copy_backend
    copiers = extensions.available_extensions(BaseCopier,
                                              'cloudferry.lib.copy_engines')
    for copier in copiers:
        if copier.get_name() == name:
            return copier
    raise CopierNotFound(name)


def get_copier(src_cloud, dst_cloud, driver=None):
    """
    Get a default copier initialize it and check the possibility of using
    the copier on the hosts.

    :param driver: copier driver class
    :param src_cloud: The object of source cloud
    :param dst_cloud: The object of destination cloud
    :return: a copier
    """
    copier_class = get_copier_class(driver)
    unsafe_copier = copier_class(src_cloud, dst_cloud)
    copier = CopierAddingWritePermissionsInDestination(unsafe_copier, CONF)
    return copier


def get_copier_checked(src_cloud, dst_cloud, data, driver=None):
    """
    Same as `get_copier()`, but additionally verifies if copier can be used
    on host and raises `CopierCannotBeUsed` exception if cannot.

    :param src_cloud: The object of source cloud
    :param dst_cloud: The object of destination cloud
    :param data: The data to check usage a copier on the hosts
    :param driver: copier driver class
    :raises CopierCannotBeUsed: in case
    :return: a copier
    """
    copier = get_copier(src_cloud, dst_cloud, driver)
    if not copier.check_usage(data):
        raise CopierCannotBeUsed(name=copier.get_name(),
                                 host_src=data['host_src'],
                                 host_dst=data['host_dst'])
    return copier
