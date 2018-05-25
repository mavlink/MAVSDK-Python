""" Core """
import multiprocessing
import grpc
from rx.concurrency import ThreadPoolScheduler


class Core(object):
    """
    Core which connects to a running dronecore backend or starts one

    :param host: IP address of host running the backend
    :param port: Port number
    :param secure: Use an SSL Layer (currently not supported)

    Initialize the backend:

    >>> core = Core(host="127.0.0.1")

    There are two (uniform) ways to register a plugin to the backend:

    >>> action = Action(core)

    or

    >>> action = Action()
        action.init_core(core)

    """

    def __init__(self, host=None, port=50051, secure=False, num_threads=None):

        self.host, self.port, self.secure = host, port, secure
        self.plugins = {}

        if host:
            # Connect to the backend when there is a hostname passed
            self._connect_backend()
        else:
            # Spinup a backend
            raise NotImplementedError()

        # Setup the scheduler
        self._setup_scheduler(num_threads)

    def _connect_backend(self):
        """
        Initializes the connection to the running backend
        """
        if self.secure:
            # For now just allow insecure connections in the development
            # phase
            raise NotImplementedError()

        # Initialize gRPC channel
        self._channel = grpc.insecure_channel(
            "{}:{}".format(self.host, self.port)
        )

    def _spinup_backend(self):
        """
        Spinup a backend and connect to it
        """
        raise NotImplementedError()
        # Set host port to localhost
        # self.port = "127.0.0.1"
        # Connect to the new backend
        # self._connect_backend()

    def _setup_scheduler(self, num_threads):
        """
        Setup the scheduler for the reactivex framework
        """

        if not type(num_threads) is int:
            # Set the number of threads to the number of available cpu
            # cores when no value is submitted
            num_threads = multiprocessing.cpu_count()

        # ThreadPoolScheduler should be available in Python 2.7 and 3.x
        self._scheduler = ThreadPoolScheduler(num_threads)

    @property
    def scheduler(self):
        """
        RxPy Scheduler
        """
        return self._scheduler

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
            self.plugins[plugin.name] = plugin

    def get_plugin(self, name):
        """
        :returns: the requested plugin or None if it is not registered
        """
        if name in self.plugins.keys():
            return self.plugins[name]
