# -*- coding: utf-8 -*-
import os
from .plugin_manager import PluginManager
from .plugins import *


CORE_PLUGINS = ["Action", "Telemetry"]


def connect(*args, **kwargs):
    """
    Generates a dronecore instance with all available Core plugins registered
    and ready to use
    """
    plugin_manager = PluginManager(*args, **kwargs)

    for plugin in CORE_PLUGINS:
        globals()[plugin](plugin_manager)

    return plugin_manager


def exit(status):
    """
    Closes all threads including threads started by the scheduler

    :param status: Exit status
    """
    # As RxPy does not expose started threads, the only way to shudown the
    # program without throwing exceptions everywhere is to do it the "hard"
    # way, this should be a temporary solution and propably be fixed in the
    # RxPy framework
    os._exit(status)
