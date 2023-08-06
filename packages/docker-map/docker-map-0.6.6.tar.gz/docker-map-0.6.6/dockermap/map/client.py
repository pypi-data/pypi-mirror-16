# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import docker

from .config import ClientConfiguration
from .container import ContainerMap
from .policy import ResumeUpdatePolicy


class MappingDockerClient(object):
    """
    Reflects a :class:`~dockermap.map.container.ContainerMap` instance on a Docker client
    (:class:`~docker.client.Client` or a subclass, e.g. :class:`~dockermap.map.base.DockerClientWrapper`).
    The ``policy_class`` determines if and how dependencies are being considered during creation, starting, stopping,
    and removal of containers.

    If only one container map is provided, it will be the default map for all operations. If multiple container maps
    are used, the list can contain instances of clients to be used. In that case, the ``docker_client`` argument is
    ignored.

    Image names, container status, and dependencies are cached. In order to force a refresh, use :meth:`refresh_names`.
    It is also cleared on every change of ``policy_class``.

    :param container_maps: :class:`~dockermap.map.container.ContainerMap` instance or a tuple or list of such instances
      along with an associated instance.
    :type container_maps: dockermap.map.container.ContainerMap or
      list[dockermap.map.container.ContainerMap] | dict[unicode | str, dockermap.map.container.ContainerMap]
    :param docker_client: Default :class:`~docker.client.Client` instance or configuration.
    :type docker_client: dockermap.map.config.ClientConfiguration or docker.client.Client
    :param clients: Dictionary of client configurations
    :type clients: dict[unicode | str, dockermap.map.config.ClientConfiguration]
    :param policy_class: Policy class based on :class:`~dockermap.map.policy.base.BasePolicy` for generating container
      actions.
    :type policy_class: class
    """
    configuration_class = ClientConfiguration

    def __init__(self, container_maps=None, docker_client=None, clients=None, policy_class=ResumeUpdatePolicy):
        if container_maps:
            if isinstance(container_maps, ContainerMap):
                self._default_map = container_maps.name
                self._maps = {container_maps.name: container_maps}
            elif isinstance(container_maps, (list, tuple)):
                self._default_map = None
                self._maps = {c_map.name: c_map for c_map in container_maps}
            elif isinstance(container_maps, dict):
                self._default_map = None
                self._maps = container_maps
            else:
                raise ValueError("Unexpected type of 'container_maps' argument: {0}".format(type(container_maps)))
        else:
            self._default_map = None
            self._maps = {}
        if clients and isinstance(clients, (list, tuple)):
            self._clients = dict(clients)
        else:
            self._clients = clients or {}

        if docker_client:
            if isinstance(docker_client, docker.Client):
                default_client = self.configuration_class.from_client(docker_client)
            elif isinstance(docker_client, ClientConfiguration):
                default_client = docker_client
            else:
                raise ValueError("Unexpected type of 'docker_client' argument: {0}".format(type(docker_client)))
            default_name = policy_class.get_default_client_name()
            self._clients[default_name] = default_client
        self._policy_class = policy_class
        self._policy = None

    def get_policy(self):
        """
        Returns an instance of :attr:`~policy_class`.

        :return: An instance of the current policy class.
        :rtype: dockermap.map.policy.base.BasePolicy
        """
        if not self._policy:
            self._policy = self._policy_class(self._maps, self._clients)
        return self._policy

    def create(self, container, instances=None, map_name=None, **kwargs):
        """
        Creates container instances for a container configuration.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance name to create. If not specified, will create all instances as specified in the
         configuration (or just one default instance).
        :type instances: tuple | list
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :param kwargs: Additional kwargs. If multiple actions are resulting from this, they will only be applied to
          the main container creation.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().create_actions(map_name or self._default_map, container, instances, **kwargs)

    def start(self, container, instances=None, map_name=None, **kwargs):
        """
        Starts instances for a container configuration.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to start. If not specified, will start all instances as specified in the
         configuration (or just one default instance).
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :type instances: iterable
        :param kwargs: Additional kwargs. If multiple actions are resulting from this, they will only be applied to
          the main container start.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().start_actions(map_name or self._default_map, container, instances, **kwargs)

    def restart(self, container, instances=None, map_name=None, **kwargs):
        """
        Restarts instances for a container configuration.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to stop. If not specified, will restart all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :param kwargs: Additional kwargs. If multiple actions are resulting from this, they will only be applied to
          the main container restart.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().restart_actions(map_name or self._default_map, container, instances, **kwargs)

    def stop(self, container, instances=None, map_name=None, **kwargs):
        """
        Stops instances for a container configuration.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to stop. If not specified, will stop all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :param raise_on_error: Errors on stop and removal may result from Docker volume problems, that do not further
          affect further actions. Such errors are always logged, but do not raise an exception unless this is set to
          ``True``. Please note that 404 errors (on non-existing containers) are always ignored on stop and removal.
        :type raise_on_error: bool
        :param kwargs: Additional kwargs. If multiple actions are resulting from this, they will only be applied to
          the main container stop.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().stop_actions(map_name or self._default_map, container, instances, **kwargs)

    def remove(self, container, instances=None, map_name=None, **kwargs):
        """
        Remove instances from a container configuration.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to remove. If not specified, will remove all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :param kwargs: Additional kwargs. If multiple actions are resulting from this, they will only be applied to
          the main container removal.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().remove_actions(map_name or self._default_map, container, instances, **kwargs)

    def startup(self, container, instances=None, map_name=None):
        """
        Start up container instances from a container configuration. Typically this means creating and starting
        containers and their dependencies. Note that not all policy classes necessarily implement this method.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to remove. If not specified, will remove all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().startup_actions(map_name or self._default_map, container, instances)

    def shutdown(self, container, instances=None, map_name=None):
        """
        Shut down container instances from a container configuration. Typically this means stopping and removing
        containers. Note that not all policy classes necessarily implement this method.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to remove. If not specified, will remove all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().shutdown_actions(map_name or self._default_map, container, instances)

    def update(self, container, instances=None, map_name=None):
        """
        Updates instances from a container configuration. Typically this means restarting or recreating containers based
        on detected changes in the configuration or environment.  Note that not all policy classes necessarily implement
        this method.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to remove. If not specified, will remove all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        return self.get_policy().update_actions(map_name or self._default_map, container, instances)

    def call(self, action_name, container, instances=None, map_name=None, **kwargs):
        """
        Generic function for running container actions based on a policy.

        :param container: Container name.
        :type container: unicode | str
        :param instances: Instance names to remove. If not specified, runs on all instances as specified in the
         configuration (or just one default instance).
        :type instances: iterable
        :param map_name: Container map name. Optional - if not provided the default map is used.
        :type map_name: unicode | str
        :param kwargs: Additional kwargs for the policy method.
        :return: Return values of created main containers.
        :rtype: list[(unicode | str, dict)]
        """
        method_name = '{0}_actions'.format(action_name)
        action_method = getattr(self.get_policy(), method_name)
        if callable(action_method):
            return action_method(map_name or self._default_map, container, instances=instances, **kwargs)
        raise ValueError("The selected policy does not provide a method '{0}' for generating actions.".format(method_name))

    def run_script(self, container, instance=None, map_name=None, **kwargs):
        """
        Runs a script or single command in the context of a container. By the default implementation this means creating
        the container along with all of its dependencies, mounting the script path, and running the script. The result
        is recorded in a dictionary per client, before the container is removed. Dependencies are not removed. For
        details, see :meth:`dockermap.map.policy.script.ScriptMixin.run_script`.

        :param map_name: Container map name.
        :type map_name: unicode | str
        :param instance: Instance name. Optional, if not specified runs the default instance.
        :type instance: unicode | str
        :param container: Container configuration name.
        :type container: unicode | str
        :param script_path: Path to the script on the Docker host.
        :param kwargs: Keyword arguments to the script runner function.
        :return: A dictionary of client names with their log output and exit codes.
        :rtype: dict[unicode | str, dict]
        """
        return self.get_policy().run_script(map_name or self._default_map, container, instance=instance, **kwargs)

    def refresh_names(self):
        """
        Invalidates the policy name and status cache.
        """
        self._policy = None

    def list_persistent_containers(self, map_name=None):
        """
        Lists the names of all persistent containers on the specified map or all maps. Attached containers are always
        considered persistent.

        :param map_name: Container map name. Optional, only returns persistent containers from the specified map.
        :type map_name: unicode | str
        :return: List of container names.
        :rtype: list[unicode | str]
        """
        if map_name:
            maps = [self._maps[map_name].get_extended_map()]
        else:
            maps = [m.get_extended_map() for m in self._maps.values()]
        cname_func = self._policy_class.cname
        aname_func = self._policy_class.aname
        c_names = []
        for c_map in maps:
            m_name = c_map.name
            attached, persistent = c_map.get_persistent_items()
            if c_map.use_attached_parent_name:
                c_names.extend([aname_func(m_name, ca, c_name)
                                for c_name, ca in attached])
            else:
                c_names.extend([aname_func(m_name, ca[1])
                                for ca in attached])
            c_names.extend([cname_func(m_name, c_name, ci)
                            for c_name, ci in persistent])
        return c_names

    @property
    def maps(self):
        """
        Container maps.

        :return: A dictionary with container map names as keys, and the container maps values.
        :rtype: dict[unicode | str, dockermap.map.container.ContainerMap]
        """
        return self._maps

    @property
    def clients(self):
        """
        Clients and their configuration objects.

        :return: Dictionary of client names, with their client instance and a configuration object as values.
        :rtype: dict[unicode | str, dockermap.map.config.ClientConfiguration]
        """
        return self._clients

    @property
    def default_map(self):
        """
        The default map to use for any actions, if not otherwise specified.

        :return: Container map name.
        :rtype: unicode | str
        """
        return self._default_map

    @default_map.setter
    def default_map(self, value):
        if value not in self._maps:
            raise ValueError("Default name must match an available map name.")
        self._default_map = value

    @property
    def policy_class(self):
        """
        The policy class, that transforms commands into actions on containers, considering potential dependencies.

        :return: Subclass of :class:`~dockermap.map.policy.base.BasePolicy`.
        :rtype: class
        """
        return self._policy_class

    @policy_class.setter
    def policy_class(self, value):
        self._policy = None
        self._policy_class = value
