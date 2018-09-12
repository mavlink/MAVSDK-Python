# -*- coding: utf-8 -*-


class AsyncBase:
    """
    Base implementation for the async gRPC connection
    """

    def __init__(self, async_plugin_manager=None):
        self.init_plugin(async_plugin_manager)

    def init_plugin(self, async_plugin_manager):
        """
        Sort of "registers" the plugin to the backend
        """
        if async_plugin_manager:
            self._loop = async_plugin_manager.loop
            self._setup_stub(async_plugin_manager.channel)
            async_plugin_manager.register_plugin(self)

    def _setup_stub(self, channel):
        """
        Actual stub setup for the Plugins
        """
        raise NotImplementedError()
