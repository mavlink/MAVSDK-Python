# -*- coding: utf-8 -*-
import aiogrpc
from . import get_event_loop


class AsyncPluginManager:
    """
    Connects to a running mavsdk server or starts one and manages plugins

    :param host: IP address of host running the backend
    :param port: Port number
    :param secure: Use an SSL Layer (currently not supported)
    :param loop: Event loop MAVSDK is running on

    Initialize the plugin manager:

    >>> manager = AsyncPluginManager(host="127.0.0.1")

    There are two (uniform) ways to register a plugin to the backend:

    >>> action = Action(manager)

    or

    >>> action = Action()
    >>> action.init_core(manager)

    """
    def __init__(
            self,
            host=None,
            port=50051,
            secure=False,
            loop=None):

        self.host, self.port, self.secure = host, port, secure
        self.plugins = {}

        if host:
            # Connect to the backend when there is a hostname passed
            self._connect_backend()
        else:
            # Spinup a backend
            raise NotImplementedError()

        self._loop = loop or get_event_loop()

    def _connect_backend(self):
        """
        Initializes the connection to the running backend
        """
        if self.secure:
            # For now just allow insecure connections
            raise NotImplementedError()

        #: gRPC channel
        self._channel = aiogrpc.insecure_channel(
            "{}:{}".format(self.host, self.port)
        )

    def _spinup_backend(self):
        """
        Spinup a backend and connect to it
        """
        #: backend is running on localhost
        self.host = "127.0.0.1"
        # Standart port
        self.port = 50051
        # Spinup the backend, not implemented yet
        raise NotImplementedError()
        # connect to the local running backend
        self._connect_backend()

    @property
    def loop(self):
        """ Event loop """
        return self._loop

    @property
    def channel(self):
        """
        gRPC channel to the backend
        """
        return self._channel

    @property
    def available_plugins(self):
        """
        List of registered plugins
        """
        return list(self.plugins.keys())

    def register_plugin(self, plugin):
        """
        Registers a plugin and adds it to the available plugin library
        """
        if plugin and plugin not in self.available_plugins:
            self.plugins[plugin.name.lower()] = plugin

    def __getattr__(self, name):
        """ convenient way to access plugins """
        if name in self.plugins.keys():
            return self.plugins[name]
        else:
            return None
