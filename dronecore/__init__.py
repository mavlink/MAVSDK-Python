from .core import Core
from .plugins import *


CORE_PLUGINS = ["Action", "Telemetry"]


def connect(*args, **kwargs):
    """
    Generates a dronecore instance with all available Core plugins registered
    and ready to use
    """
    core = Core(*args, **kwargs)

    for plugin in CORE_PLUGINS:
        globals()[plugin](core)

    return core
