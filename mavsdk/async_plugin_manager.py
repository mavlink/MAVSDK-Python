# -*- coding: utf-8 -*-
import logging
import aiogrpc


class AsyncPluginManager:
    """
    Connects to a running mavsdk server or starts one and manages plugins
    """
    @classmethod
    async def create(cls, host, port=50051):

        self = AsyncPluginManager()

        self.host = host
        self.port = port
        self.plugins = {}

        await self._connect_backend()

        return self

    async def _connect_backend(self):
        """
        Initializes the connection to the running backend
        """

        #: gRPC channel
        self._channel = aiogrpc.insecure_channel(
            "{}:{}".format(self.host, self.port),
            standalone_pool_for_streaming=True
        )

        logger = logging.getLogger(__name__)
        logger.addHandler(logging.NullHandler())  # Avoid errors when user has not configured logging

        logger.debug("Waiting for mavsdk_server to be ready...")
        await aiogrpc.channel_ready_future(self._channel)
        logger.debug("Connected to mavsdk_server!")

    @property
    def channel(self):
        """
        gRPC channel to the backend
        """
        return self._channel
