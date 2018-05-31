# -*- coding: utf-8 -*-
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
