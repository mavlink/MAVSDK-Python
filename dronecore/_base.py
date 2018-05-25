""" Base class for the plugins """
from rx import Observable


class Base(object):
    """
    Base implementation for the gRPC connection
    """

    def __init__(self, core=None):
        self.init_core(core)

    def init_core(self, core):
        """
        Sort of "registers" the plugin to the backend
        """
        if core:
            self._setup_stub(core.channel)
            self._scheduler = core.scheduler
            core.register_plugin(self)

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

    def _create_stream_observable(self, f):
        """
        Helper for creating a published stream observable
        """
        return Observable.create(f) \
                         .subscribe_on(self._scheduler.new_thread) \
                         .publish()
