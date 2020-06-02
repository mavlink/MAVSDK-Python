# -*- coding: utf-8 -*-

from .async_plugin_manager import AsyncPluginManager
from .generated import Action
from .generated import Calibration
from .generated import Camera
from .generated import Core
from .generated import FollowMe
from .generated import Ftp
from .generated import Geofence
from .generated import Gimbal
from .generated import Info
from .generated import LogFiles
from .generated import Mission
from .generated import MissionRaw
from .generated import Mocap
from .generated import Offboard
from .generated import Param
from .generated import Shell
from .generated import Telemetry
from .generated import Tune

from . import bin


class System:
    _core_plugins = [
        "Action",
        "Calibration",
        "Camera",
        "Core",
        "FollowMe",
        "Ftp",
        "Geofence",
        "Gimbal",
        "Info",
        "LogFiles",
        "Mission",
        "MissionRaw",
        "Mocap",
        "Offboard",
        "Param",
        "Shell",
        "Telemetry",
        "Tune",
    ]

    def __init__(self, mavsdk_server_address=None, port=50051):
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
        self._mavsdk_server_address = mavsdk_server_address
        self._port = port

        self._plugins = {}

    async def connect(self, system_address=None):
        """
        Connect the System object to a remote system.

        Parameters
        ----------
        system_address: str
            The address of the remote system. If None, it will
            default to udp://:14540. Supported URL formats:

                - Serial: serial:///path/to/serial/dev[:baudrate]
                - UDP: udp://[bind_host][:bind_port]
                - TCP: tcp://[server_host][:server_port]

        """
        if self._mavsdk_server_address is None:
            self._mavsdk_server_address = 'localhost'
            self._start_mavsdk_server(system_address)

        await self._init_plugins(self._mavsdk_server_address, self._port)

    async def _init_plugins(self, host, port):
        plugin_manager = await AsyncPluginManager.create(host=host, port=port)

        for plugin in self._core_plugins:
            self._plugins[plugin.lower()] = globals()[plugin](plugin_manager)

    @staticmethod
    def error_uninitialized(plugin_name: str) -> str:
        return "{plugin_name} plugin has not been initialized!" \
            "Did you run `System.connect()`?"

    @property
    def action(self) -> Action:
        if "action" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Action"))
        return self._plugins["action"]

    @property
    def calibration(self) -> Calibration:
        if "calibration" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Calibration"))
        return self._plugins["calibration"]

    @property
    def camera(self) -> Camera:
        if "camera" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Camera"))
        return self._plugins["camera"]

    @property
    def core(self) -> Core:
        if "core" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Core"))
        return self._plugins["core"]

    @property
    def follow_me(self) -> FollowMe:
        if "follow_me" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("FollowMe"))
        return self._plugins["follow_me"]

    @property
    def ftp(self) -> Ftp:
        if "ftp" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Ftp"))
        return self._plugins["Ftp"]

    @property
    def geofence(self) -> Geofence:
        if "geofence" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Geofence"))
        return self._plugins["geofence"]

    @property
    def gimbal(self) -> Gimbal:
        if "gimbal" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Gimbal"))
        return self._plugins["gimbal"]

    @property
    def info(self) -> Info:
        if "info" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Info"))
        return self._plugins["info"]

    @property
    def log_files(self) -> LogFiles:
        if "log_files" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("LogFiles"))
        return self._plugins["log_files"]

    @property
    def mission(self) -> Mission:
        if "mission" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Mission"))
        return self._plugins["mission"]

    @property
    def mission_raw(self) -> MissionRaw:
        if "mission_raw" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("MissionRaw"))
        return self._plugins["mission_raw"]

    @property
    def mocap(self) -> Mocap:
        if "mocap" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Mocap"))
        return self._plugins["mocap"]

    @property
    def offboard(self) -> Offboard:
        if "offboard" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Offboard"))
        return self._plugins["offboard"]

    @property
    def param(self) -> Param:
        if "param" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Param"))
        return self._plugins["param"]

    @property
    def shell(self) -> Shell:
        if "shell" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Shell"))
        return self._plugins["shell"]

    @property
    def telemetry(self) -> Telemetry:
        if "telemetry" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Telemetry"))
        return self._plugins["telemetry"]

    @property
    def tune(self) -> Tune:
        if "tune" not in self._plugins:
            raise RuntimeError(self.error_uninitialized("Tune"))
        return self._plugins["tune"]

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

        try:
            with path(bin, 'mavsdk_server') as backend:
                bin_path_and_args = [os.fspath(backend), "-p", "50051"]
                if system_address:
                    bin_path_and_args.append(system_address)
                p = subprocess.Popen(bin_path_and_args,
                                     shell=False,
                                     stdout=subprocess.DEVNULL,
                                     stderr=subprocess.DEVNULL)
        except FileNotFoundError:
            print("""
This installation does not provide an embedded 'mavsdk_server' binary.
If you installed using pip, this means that 'mavsdk_server' is not distributed
for your platform yet (e.g. arm).

You will need to get and run the 'mavsdk_server' binary manually:

  1. Download 'mavsdk_server' from: https://github.com/mavlink/mavsdk/releases
     or build it from source.

  2. Run it, e.g. on port 50051:
     './mavsdk_server -p 50051'

  3. Set the 'mavsdk_server_address' and port when creating the System:
     'drone = System(mavsdk_server_address='localhost', port=50051)'
""")
            sys.exit(1)

        def cleanup():
            p.kill()

        atexit.register(cleanup)
