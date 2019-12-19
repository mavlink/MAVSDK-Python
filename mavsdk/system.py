# -*- coding: utf-8 -*-

from .async_plugin_manager import AsyncPluginManager # NOQA
from .generated import * # NOQA

from . import bin


class System:
    _core_plugins = [
        "Action",
        "Calibration",
        "Camera",
        "Core",
        "Geofence",
        "Gimbal",
        "Info",
        "Mission",
        "Mocap",
        "Param",
        "Offboard",
        "Shell",
        "Telemetry"
    ]

    """Instantiate a System object, that will serve as a proxy to
       all the MAVSDK plugins.

       Parameters
       ----------
       mavsdk_server_address: str
           Address of a running mavsdk_server instance. If None,
           an instance of mavsdk_server will be automatically
           started (on localhost).

       port: int
           Port of the running mavsdk_server instance specified by
           mavsdk_server_address.

    """
    def __init__(self, mavsdk_server_address=None, port=50051):
        self._mavsdk_server_address = mavsdk_server_address
        self._port = port

        self._plugins = {}

    """Connect the System object to a remote system.

       Parameters
       ----------
       system_address: str
           The address of the remote system. If None, it will
           default to udp://:14540. Supported URL formats:
               - Serial: serial:///path/to/serial/dev[:baudrate]
               - UDP: udp://[bind_host][:bind_port]
               - TCP: tcp://[server_host][:server_port]

    """
    async def connect(self, system_address=None):
        if self._mavsdk_server_address is None:
            self._mavsdk_server_address = 'localhost'
            self._start_mavsdk_server(system_address)

        await self._init_plugins(self._mavsdk_server_address, self._port)

    async def _init_plugins(self, host, port):
        plugin_manager = await AsyncPluginManager.create(host=host, port=port)

        for plugin in self._core_plugins:
            self._plugins[plugin.lower()] = globals()[plugin](plugin_manager)

    @property
    def action(self) -> Action:
        if "action" not in self._plugins:
            raise RuntimeError("Action plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["action"]

    @property
    def calibration(self) -> Calibration:
        if "calibration" not in self._plugins:
            raise RuntimeError("Calibration plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["calibration"]

    @property
    def camera(self) -> Camera:
        if "camera" not in self._plugins:
            raise RuntimeError("Camera plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["camera"]

    @property
    def core(self) -> Core:
        if "core" not in self._plugins:
            raise RuntimeError("Core plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["core"]

    @property
    def geofence(self) -> Geofence:
        if "geofence" not in self._plugins:
            raise RuntimeError("Geofence plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["geofence"]

    @property
    def gimbal(self) -> Gimbal:
        if "gimbal" not in self._plugins:
            raise RuntimeError("Gimbal plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["gimbal"]

    @property
    def info(self) -> Info:
        if "info" not in self._plugins:
            raise RuntimeError("Info plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["info"]

    @property
    def mission(self) -> Mission:
        if "mission" not in self._plugins:
            raise RuntimeError("Mission plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["mission"]

    @property
    def param(self) -> Param:
        if "param" not in self._plugins:
            raise RuntimeError("Param plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["param"]

    @property
    def offboard(self) -> Offboard:
        if "offboard" not in self._plugins:
            raise RuntimeError("Offboard plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["offboard"]

    @property
    def telemetry(self) -> Telemetry:
        if "telemetry" not in self._plugins:
            raise RuntimeError("Telemetry plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["telemetry"]

    @property
    def shell(self) -> Shell:
        if "shell" not in self._plugins:
            raise RuntimeError("Shell plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["shell"]

    @property
    def mocap(self) -> Mocap:
        if "mocap" not in self._plugins:
            raise RuntimeError("Mocap plugin has not been initialized! Did you run `System.connect()`?")
        return self._plugins["mocap"]

    @staticmethod
    def _start_mavsdk_server(system_address=None):
        """
        Starts the gRPC server in a subprocess, listening on localhost:50051
        """
        import atexit
        import os
        import subprocess
        import sys

        if sys.version_info >= (3, 7):
            from importlib.resources import path
        else:
            from importlib_resources import path

        with path(bin, 'mavsdk_server') as backend:
            bin_path_and_args = [os.fspath(backend), "-p", "50051"]
            if system_address:
                bin_path_and_args.append(system_address)
            p = subprocess.Popen(bin_path_and_args,
                                 shell=False,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)

        def cleanup():
            p.kill()

        atexit.register(cleanup)
