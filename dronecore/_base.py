# -*- coding: utf-8 -*-
from rx import Observable


class Base(object):
    """
    Base implementation for the gRPC connection
    """

    def __init__(self, plugin_manager=None):
        self.init_plugin(plugin_manager)

    def init_plugin(self, plugin_manager):
        """
        Sort of "registers" the plugin to the backend
        """
        if plugin_manager:
            self._setup_stub(plugin_manager.channel)
            self._scheduler = plugin_manager.scheduler
            plugin_manager.register_plugin(self)

    def _setup_stub(self, channel):
        """
        Actual stub setup for the Plugins
        """
        raise NotImplementedError()

    def _create_call_observable(self, f):
        """
        Helper for creating "direct" call observable
        """
        return Observable.create(f).subscribe_on(self._scheduler.new_thread)

    def _create_stream_observable(self, iterable):
        """
        Helper for creating a published stream observable
        """
        tmp_observable = Observable.from_iterable(iterable) \
            .subscribe_on(self._scheduler.new_thread) \
            .publish()

        # Connect so that subscribers get only relevant/recent information!
        tmp_observable.connect()
        return tmp_observable
