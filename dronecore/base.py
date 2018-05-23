""" Base class for the plugins """


class Base(object):
    """
    Base implementation for the gRPC connection
    """

    def __init__(self, backend=None):
        self.available = False
        self.init_backend(backend)

    def init_backend(self, backend):
        """
        Sort of "registers" the plugin to the backend
        """
        if backend:
            self._setup_stub(backend.channel)
            backend.register_plugin(self)

    def _setup_stub(self, channel):
        """
        Actual stub setup for the Plugins
        """
        raise NotImplementedError()
