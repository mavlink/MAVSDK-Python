# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import modes_pb2, modes_pb2_grpc
from enum import Enum


class Mode:
    """
    Mode type.

    Parameters
    ----------
    name : std::string
         Name of the mode, e.g. "Position" or "Stabilize"

    custom_mode : uint32_t
         Autopilot specific custom mode

    is_standard : bool
         True if this is a MAVLink standard mode, e.g. "Position" or "Mission"

    is_user_selectable : bool
         True if the mode can be set by the user

    is_advanced : bool
         True if the mode is for advanced users only

    is_auto_mode : bool
         True if the mode runs autonomously, e.g. Mission or Land

    """

    def __init__(
        self,
        name,
        custom_mode,
        is_standard,
        is_user_selectable,
        is_advanced,
        is_auto_mode,
    ):
        """Initializes the Mode object"""
        self.name = name
        self.custom_mode = custom_mode
        self.is_standard = is_standard
        self.is_user_selectable = is_user_selectable
        self.is_advanced = is_advanced
        self.is_auto_mode = is_auto_mode

    def __eq__(self, to_compare):
        """Checks if two Mode are the same"""
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Mode object
            return (
                (self.name == to_compare.name)
                and (self.custom_mode == to_compare.custom_mode)
                and (self.is_standard == to_compare.is_standard)
                and (self.is_user_selectable == to_compare.is_user_selectable)
                and (self.is_advanced == to_compare.is_advanced)
                and (self.is_auto_mode == to_compare.is_auto_mode)
            )

        except AttributeError:
            return False

    def __str__(self):
        """Mode in string representation"""
        struct_repr = ", ".join(
            [
                "name: " + str(self.name),
                "custom_mode: " + str(self.custom_mode),
                "is_standard: " + str(self.is_standard),
                "is_user_selectable: " + str(self.is_user_selectable),
                "is_advanced: " + str(self.is_advanced),
                "is_auto_mode: " + str(self.is_auto_mode),
            ]
        )

        return f"Mode: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMode):
        """Translates a gRPC struct to the SDK equivalent"""
        return Mode(
            rpcMode.name,
            rpcMode.custom_mode,
            rpcMode.is_standard,
            rpcMode.is_user_selectable,
            rpcMode.is_advanced,
            rpcMode.is_auto_mode,
        )

    def translate_to_rpc(self, rpcMode):
        """Translates this SDK object into its gRPC equivalent"""

        rpcMode.name = self.name

        rpcMode.custom_mode = self.custom_mode

        rpcMode.is_standard = self.is_standard

        rpcMode.is_user_selectable = self.is_user_selectable

        rpcMode.is_advanced = self.is_advanced

        rpcMode.is_auto_mode = self.is_auto_mode


class ModesResult:
    """
    Result type.

    Parameters
    ----------
    result : Result
         Result enum value

    result_str : std::string
         Human-readable English string describing the result

    """

    class Result(Enum):
        """
        Possible results returned for mode requests.

        Values
        ------
        UNKNOWN
             Unknown result

        SUCCESS
             Request was successful

        NO_SYSTEM
             No system is connected

        CONNECTION_ERROR
             Connection error

        BUSY
             Vehicle is busy

        DENIED
             Request was denied, e.g. because the mode can't be entered right now

        UNSUPPORTED
             Mode or command is not supported

        TIMEOUT
             Request timed out

        FAILED
             Request failed

        MODE_NOT_FOUND
             No available mode with this name

        MODES_NOT_KNOWN_YET
             The available modes have not been received yet

        """

        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        DENIED = 5
        UNSUPPORTED = 6
        TIMEOUT = 7
        FAILED = 8
        MODE_NOT_FOUND = 9
        MODES_NOT_KNOWN_YET = 10

        def translate_to_rpc(self):
            if self == ModesResult.Result.UNKNOWN:
                return modes_pb2.ModesResult.RESULT_UNKNOWN
            if self == ModesResult.Result.SUCCESS:
                return modes_pb2.ModesResult.RESULT_SUCCESS
            if self == ModesResult.Result.NO_SYSTEM:
                return modes_pb2.ModesResult.RESULT_NO_SYSTEM
            if self == ModesResult.Result.CONNECTION_ERROR:
                return modes_pb2.ModesResult.RESULT_CONNECTION_ERROR
            if self == ModesResult.Result.BUSY:
                return modes_pb2.ModesResult.RESULT_BUSY
            if self == ModesResult.Result.DENIED:
                return modes_pb2.ModesResult.RESULT_DENIED
            if self == ModesResult.Result.UNSUPPORTED:
                return modes_pb2.ModesResult.RESULT_UNSUPPORTED
            if self == ModesResult.Result.TIMEOUT:
                return modes_pb2.ModesResult.RESULT_TIMEOUT
            if self == ModesResult.Result.FAILED:
                return modes_pb2.ModesResult.RESULT_FAILED
            if self == ModesResult.Result.MODE_NOT_FOUND:
                return modes_pb2.ModesResult.RESULT_MODE_NOT_FOUND
            if self == ModesResult.Result.MODES_NOT_KNOWN_YET:
                return modes_pb2.ModesResult.RESULT_MODES_NOT_KNOWN_YET

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """Parses a gRPC response"""
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_UNKNOWN:
                return ModesResult.Result.UNKNOWN
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_SUCCESS:
                return ModesResult.Result.SUCCESS
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_NO_SYSTEM:
                return ModesResult.Result.NO_SYSTEM
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_CONNECTION_ERROR:
                return ModesResult.Result.CONNECTION_ERROR
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_BUSY:
                return ModesResult.Result.BUSY
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_DENIED:
                return ModesResult.Result.DENIED
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_UNSUPPORTED:
                return ModesResult.Result.UNSUPPORTED
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_TIMEOUT:
                return ModesResult.Result.TIMEOUT
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_FAILED:
                return ModesResult.Result.FAILED
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_MODE_NOT_FOUND:
                return ModesResult.Result.MODE_NOT_FOUND
            if rpc_enum_value == modes_pb2.ModesResult.RESULT_MODES_NOT_KNOWN_YET:
                return ModesResult.Result.MODES_NOT_KNOWN_YET

        def __str__(self):
            return self.name

    def __init__(self, result, result_str):
        """Initializes the ModesResult object"""
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """Checks if two ModesResult are the same"""
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ModesResult object
            return (self.result == to_compare.result) and (
                self.result_str == to_compare.result_str
            )

        except AttributeError:
            return False

    def __str__(self):
        """ModesResult in string representation"""
        struct_repr = ", ".join(
            ["result: " + str(self.result), "result_str: " + str(self.result_str)]
        )

        return f"ModesResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcModesResult):
        """Translates a gRPC struct to the SDK equivalent"""
        return ModesResult(
            ModesResult.Result.translate_from_rpc(rpcModesResult.result),
            rpcModesResult.result_str,
        )

    def translate_to_rpc(self, rpcModesResult):
        """Translates this SDK object into its gRPC equivalent"""

        rpcModesResult.result = self.result.translate_to_rpc()

        rpcModesResult.result_str = self.result_str


class ModesError(Exception):
    """Raised when a ModesResult is a fail code"""

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Modes(AsyncBase):
    """
    Discover and set flight modes at runtime.

    The modes are queried from the vehicle using the MAVLink standard modes
    protocol (AVAILABLE_MODES, CURRENT_MODE). For autopilots that don't
    implement it, a list of known modes is used as a fallback.

    Modes are identified by name. Standard modes have a fixed name, e.g.
    "Position" or "Mission", other modes use the name reported by the vehicle.
    Setting a mode works the same way for both.

    Generated by dcsdkgen - MAVSDK Modes API
    """

    # Plugin name
    name = "Modes"

    def _setup_stub(self, channel):
        """Setups the api stub"""
        self._stub = modes_pb2_grpc.ModesServiceStub(channel)

    def _extract_result(self, response):
        """Returns the response status and description"""
        return ModesResult.translate_from_rpc(response.modes_result)

    async def available_modes(self):
        """
        Subscribe to the list of available modes.

        The list is updated whenever the vehicle reports that its modes have changed.

        Yields
        -------
        modes : [Mode]
             The available modes


        """

        request = modes_pb2.SubscribeAvailableModesRequest()
        available_modes_stream = self._stub.SubscribeAvailableModes(request)

        try:
            async for response in available_modes_stream:
                yield [Mode.translate_from_rpc(x) for x in response.modes]
        finally:
            available_modes_stream.cancel()

    async def current_mode(self):
        """
        Subscribe to the current mode.

        Yields
        -------
        mode : Mode
             The current mode


        """

        request = modes_pb2.SubscribeCurrentModeRequest()
        current_mode_stream = self._stub.SubscribeCurrentMode(request)

        try:
            async for response in current_mode_stream:
                yield Mode.translate_from_rpc(response.mode)
        finally:
            current_mode_stream.cancel()

    async def set_mode(self, name):
        """
        Set mode by name.

        The name needs to match exactly (case-sensitive) the name of one of the available modes.

        Parameters
        ----------
        name : std::string
             Name of the mode to set

        Raises
        ------
        ModesError
            If the request fails. The error contains the reason for the failure.
        """

        request = modes_pb2.SetModeRequest()
        request.name = name
        response = await self._stub.SetMode(request)

        result = self._extract_result(response)

        if result.result != ModesResult.Result.SUCCESS:
            raise ModesError(result, "set_mode()", name)
