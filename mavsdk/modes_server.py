# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import modes_server_pb2, modes_server_pb2_grpc
from enum import Enum


class ModeFeedback(Enum):
    """
    Possible answers to a mode change request.

    Values
    ------
    UNKNOWN
         Unknown

    ACCEPTED
         The vehicle switches to the mode

    BUSY
         The vehicle can't switch to the mode right now, e.g. it has no GPS

    DENIED
         The vehicle doesn't allow switching to the mode

    FAILED
         Switching to the mode failed

    """

    UNKNOWN = 0
    ACCEPTED = 1
    BUSY = 2
    DENIED = 3
    FAILED = 4

    def translate_to_rpc(self):
        if self == ModeFeedback.UNKNOWN:
            return modes_server_pb2.MODE_FEEDBACK_UNKNOWN
        if self == ModeFeedback.ACCEPTED:
            return modes_server_pb2.MODE_FEEDBACK_ACCEPTED
        if self == ModeFeedback.BUSY:
            return modes_server_pb2.MODE_FEEDBACK_BUSY
        if self == ModeFeedback.DENIED:
            return modes_server_pb2.MODE_FEEDBACK_DENIED
        if self == ModeFeedback.FAILED:
            return modes_server_pb2.MODE_FEEDBACK_FAILED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """Parses a gRPC response"""
        if rpc_enum_value == modes_server_pb2.MODE_FEEDBACK_UNKNOWN:
            return ModeFeedback.UNKNOWN
        if rpc_enum_value == modes_server_pb2.MODE_FEEDBACK_ACCEPTED:
            return ModeFeedback.ACCEPTED
        if rpc_enum_value == modes_server_pb2.MODE_FEEDBACK_BUSY:
            return ModeFeedback.BUSY
        if rpc_enum_value == modes_server_pb2.MODE_FEEDBACK_DENIED:
            return ModeFeedback.DENIED
        if rpc_enum_value == modes_server_pb2.MODE_FEEDBACK_FAILED:
            return ModeFeedback.FAILED

    def __str__(self):
        return self.name


class Mode:
    """
    Mode type.

    Parameters
    ----------
    name : std::string
         Name of the mode, for a standard mode one of the standard names, e.g. "Position" or "Mission"

    custom_mode : uint32_t
         Autopilot specific custom mode, needs to be unique

    is_standard : bool
         True if this is a MAVLink standard mode

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


class ModesServerResult:
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

        INVALID_MODES
             Modes are invalid, e.g. none are given, a name or custom mode is used twice, or a standard mode name is unknown

        MODE_NOT_FOUND
             No available mode with this name

        NO_REQUEST
             There is no mode change request to respond to

        INVALID_FEEDBACK
             The feedback is unknown

        """

        UNKNOWN = 0
        SUCCESS = 1
        INVALID_MODES = 2
        MODE_NOT_FOUND = 3
        NO_REQUEST = 4
        INVALID_FEEDBACK = 5

        def translate_to_rpc(self):
            if self == ModesServerResult.Result.UNKNOWN:
                return modes_server_pb2.ModesServerResult.RESULT_UNKNOWN
            if self == ModesServerResult.Result.SUCCESS:
                return modes_server_pb2.ModesServerResult.RESULT_SUCCESS
            if self == ModesServerResult.Result.INVALID_MODES:
                return modes_server_pb2.ModesServerResult.RESULT_INVALID_MODES
            if self == ModesServerResult.Result.MODE_NOT_FOUND:
                return modes_server_pb2.ModesServerResult.RESULT_MODE_NOT_FOUND
            if self == ModesServerResult.Result.NO_REQUEST:
                return modes_server_pb2.ModesServerResult.RESULT_NO_REQUEST
            if self == ModesServerResult.Result.INVALID_FEEDBACK:
                return modes_server_pb2.ModesServerResult.RESULT_INVALID_FEEDBACK

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """Parses a gRPC response"""
            if rpc_enum_value == modes_server_pb2.ModesServerResult.RESULT_UNKNOWN:
                return ModesServerResult.Result.UNKNOWN
            if rpc_enum_value == modes_server_pb2.ModesServerResult.RESULT_SUCCESS:
                return ModesServerResult.Result.SUCCESS
            if (
                rpc_enum_value
                == modes_server_pb2.ModesServerResult.RESULT_INVALID_MODES
            ):
                return ModesServerResult.Result.INVALID_MODES
            if (
                rpc_enum_value
                == modes_server_pb2.ModesServerResult.RESULT_MODE_NOT_FOUND
            ):
                return ModesServerResult.Result.MODE_NOT_FOUND
            if rpc_enum_value == modes_server_pb2.ModesServerResult.RESULT_NO_REQUEST:
                return ModesServerResult.Result.NO_REQUEST
            if (
                rpc_enum_value
                == modes_server_pb2.ModesServerResult.RESULT_INVALID_FEEDBACK
            ):
                return ModesServerResult.Result.INVALID_FEEDBACK

        def __str__(self):
            return self.name

    def __init__(self, result, result_str):
        """Initializes the ModesServerResult object"""
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """Checks if two ModesServerResult are the same"""
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ModesServerResult object
            return (self.result == to_compare.result) and (
                self.result_str == to_compare.result_str
            )

        except AttributeError:
            return False

    def __str__(self):
        """ModesServerResult in string representation"""
        struct_repr = ", ".join(
            ["result: " + str(self.result), "result_str: " + str(self.result_str)]
        )

        return f"ModesServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcModesServerResult):
        """Translates a gRPC struct to the SDK equivalent"""
        return ModesServerResult(
            ModesServerResult.Result.translate_from_rpc(rpcModesServerResult.result),
            rpcModesServerResult.result_str,
        )

    def translate_to_rpc(self, rpcModesServerResult):
        """Translates this SDK object into its gRPC equivalent"""

        rpcModesServerResult.result = self.result.translate_to_rpc()

        rpcModesServerResult.result_str = self.result_str


class ModesServerError(Exception):
    """Raised when a ModesServerResult is a fail code"""

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ModesServer(AsyncBase):
    """
    Provide the flight modes of an autopilot, the counterpart of the Modes plugin.

    The modes are announced using the MAVLink standard modes protocol
    (AVAILABLE_MODES, AVAILABLE_MODES_MONITOR, CURRENT_MODE).

    Once modes are set, this plugin also handles mode change requests
    (MAV_CMD_DO_SET_STANDARD_MODE, MAV_CMD_DO_SET_MODE and SET_MODE) for those
    modes, instead of the deprecated flight mode API of the ActionServer plugin.

    Generated by dcsdkgen - MAVSDK ModesServer API
    """

    # Plugin name
    name = "ModesServer"

    def _setup_stub(self, channel):
        """Setups the api stub"""
        self._stub = modes_server_pb2_grpc.ModesServerServiceStub(channel)

    def _extract_result(self, response):
        """Returns the response status and description"""
        return ModesServerResult.translate_from_rpc(response.modes_server_result)

    async def set_available_modes(self, modes):
        """
        Set the modes the vehicle provides.

        Ground stations are told that the list changed so they download it again.
        From then on, mode change requests are handled by this plugin.

        Parameters
        ----------
        modes : [Mode]
             The available modes

        Raises
        ------
        ModesServerError
            If the request fails. The error contains the reason for the failure.
        """

        request = modes_server_pb2.SetAvailableModesRequest()

        rpc_elems_list = []
        for elem in modes:
            rpc_elem = modes_server_pb2.Mode()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)

        request.modes.extend(rpc_elems_list)

        response = await self._stub.SetAvailableModes(request)

        result = self._extract_result(response)

        if result.result != ModesServerResult.Result.SUCCESS:
            raise ModesServerError(result, "set_available_modes()", modes)

    async def mode_requested(self):
        """
        Subscribe to mode change requests.

        Requests for a mode in the list are reported here and need to be
        answered with RespondModeRequested. Until then, the ground station is
        told that the request is in progress.

        Yields
        -------
        mode : Mode
             The requested mode


        """

        request = modes_server_pb2.SubscribeModeRequestedRequest()
        mode_requested_stream = self._stub.SubscribeModeRequested(request)

        try:
            async for response in mode_requested_stream:
                yield Mode.translate_from_rpc(response.mode)
        finally:
            mode_requested_stream.cancel()

    async def respond_mode_requested(self, mode_feedback):
        """
        Respond to the last mode change request.

        If the request is accepted, the requested mode becomes the current mode.
        Otherwise the vehicle stays in its current mode, e.g. if it can't switch
        to Position without GPS.

        Parameters
        ----------
        mode_feedback : ModeFeedback
             The answer to the request

        Raises
        ------
        ModesServerError
            If the request fails. The error contains the reason for the failure.
        """

        request = modes_server_pb2.RespondModeRequestedRequest()

        request.mode_feedback = mode_feedback.translate_to_rpc()

        response = await self._stub.RespondModeRequested(request)

        result = self._extract_result(response)

        if result.result != ModesServerResult.Result.SUCCESS:
            raise ModesServerError(result, "respond_mode_requested()", mode_feedback)

    async def set_current_mode(self, name):
        """
        Set the mode the vehicle is in.

        Parameters
        ----------
        name : std::string
             Name of the mode, one of the available modes

        Raises
        ------
        ModesServerError
            If the request fails. The error contains the reason for the failure.
        """

        request = modes_server_pb2.SetCurrentModeRequest()
        request.name = name
        response = await self._stub.SetCurrentMode(request)

        result = self._extract_result(response)

        if result.result != ModesServerResult.Result.SUCCESS:
            raise ModesServerError(result, "set_current_mode()", name)
