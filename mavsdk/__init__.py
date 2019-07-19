# -*- coding: utf-8 -*-

import asyncio
import atexit
import os
import platform
import subprocess
import sys
import time

from mavsdk import bin

# List of the core plugins
CORE_PLUGINS = [
    "Action",
    "Calibration",
    "Camera",
    "Core",
    "Gimbal",
    "Info",
    "Mission",
    "Param",
    "Offboard",
    "Telemetry"
    ]

# Check for compatibility
if float(".".join(platform.python_version_tuple()[0:-1])) < 3.6:
    print("[!] MAVSDK-Python is only available on Python >= 3.6")
    sys.exit(1)

# Do asyncio specific initialization
try:
    # Try to import uvloop, provides _MUCH_ better performance compared to the
    # standart unix selector event loop
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    # No uvloop installed on the system; the default eventloop works as well!
    pass


def get_event_loop():
    """ Asyncio eventloop """
    return asyncio.get_event_loop()


# Plugins rely on the eventloop
from .async_plugin_manager import AsyncPluginManager # NOQA
from .generated import * # NOQA


def connect(*args, **kwargs):
    """
    Generates a dronecore instance with all available Core plugins registered
    and ready to use
    """
    plugin_manager = AsyncPluginManager(*args, **kwargs)

    for plugin in CORE_PLUGINS:
        globals()[plugin](plugin_manager)

    return plugin_manager


if sys.version_info >= (3, 7):
    from importlib.resources import path
else:
    from importlib_resources import path


def start_mavlink(connection_url=None):
    """
    Starts the gRPC server in a subprocess, listening on localhost:50051
    """
    with path(bin, 'mavsdk_server') as backend:
        bin_path_and_args = [os.fspath(backend)]
        if connection_url:
            bin_path_and_args.append(connection_url)
        p = subprocess.Popen(bin_path_and_args,
                             shell=False,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)

    # Wait to make sure the gRPC server is started.
    # There are better, yet more complex ways to do that.
    time.sleep(2)

    def cleanup():
        p.kill()

    atexit.register(cleanup)
