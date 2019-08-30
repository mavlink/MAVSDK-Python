# -*- coding: utf-8 -*-
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
            "{}:{}".format(self.host, self.port)
        )

        print("Waiting for mavsdk_server to be ready...")
        await aiogrpc.channel_ready_future(self._channel)
        print("Connected to mavsdk_server!")

    @property
    def channel(self):
        """
        gRPC channel to the backend
        """
        return self._channel
