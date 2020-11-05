# -*- coding: utf-8 -*-


class AsyncBase:
    """
    Base implementation for the async gRPC connection
    """

    def __init__(self, async_plugin_manager):
        """
        Initialize the plugin.

        Args:
            self: (todo): write your description
            async_plugin_manager: (todo): write your description
        """
        self._init_plugin(async_plugin_manager)

    def _init_plugin(self, async_plugin_manager):
        """
        Sort of "registers" the plugin to the backend
        """
        if async_plugin_manager:
            self._setup_stub(async_plugin_manager.channel)

    def _setup_stub(self, channel):
        """
        Actual stub setup for the Plugins
        """
        raise NotImplementedError()
