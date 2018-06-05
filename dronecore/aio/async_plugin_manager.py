# -*- coding: utf-8 -*-
import aiogrpc
from . import get_event_loop
from .. import PluginManager


class AsyncPluginManager(PluginManager):
    """ Async implementation of the PluginManager """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._loop = get_event_loop()

    # Only function that needs to be overrridden in order to support asyncio
    def _connect_backend(self):
        """
        Initializes the connection to the running backend
        """
        if self.secure:
            # For now just allow insecure connections in the development
            # phase
            raise NotImplementedError()

        #: gRPC channel
        self._channel = aiogrpc.insecure_channel(
            "{}:{}".format(self.host, self.port)
        )

    @property
    def loop(self):
        """ Event loop """
        return self._loop
