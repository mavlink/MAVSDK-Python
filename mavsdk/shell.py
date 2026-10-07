# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import shell_pb2, shell_pb2_grpc
from enum import Enum


class Device(Enum):
    """
    MAVLink SERIAL_CONTROL_DEV values used by the shell plugin.

    Values
    ------
    TELEM1
         SERIAL_CONTROL_DEV_TELEM1

    TELEM2
         SERIAL_CONTROL_DEV_TELEM2

    GPS1
         SERIAL_CONTROL_DEV_GPS1

    GPS2
         SERIAL_CONTROL_DEV_GPS2

    SHELL
         SERIAL_CONTROL_DEV_SHELL (default)

    SERIAL0
         SERIAL_CONTROL_SERIAL0

    SERIAL1
         SERIAL_CONTROL_SERIAL1

    SERIAL2
         SERIAL_CONTROL_SERIAL2

    SERIAL3
         SERIAL_CONTROL_SERIAL3

    SERIAL4
         SERIAL_CONTROL_SERIAL4

    SERIAL5
         SERIAL_CONTROL_SERIAL5

    SERIAL6
         SERIAL_CONTROL_SERIAL6

    SERIAL7
         SERIAL_CONTROL_SERIAL7

    SERIAL8
         SERIAL_CONTROL_SERIAL8

    SERIAL9
         SERIAL_CONTROL_SERIAL9

    """

    TELEM1 = 0
    TELEM2 = 1
    GPS1 = 2
    GPS2 = 3
    SHELL = 4
    SERIAL0 = 5
    SERIAL1 = 6
    SERIAL2 = 7
    SERIAL3 = 8
    SERIAL4 = 9
    SERIAL5 = 10
    SERIAL6 = 11
    SERIAL7 = 12
    SERIAL8 = 13
    SERIAL9 = 14

    def translate_to_rpc(self):
        if self == Device.TELEM1:
            return shell_pb2.DEVICE_TELEM1
        if self == Device.TELEM2:
            return shell_pb2.DEVICE_TELEM2
        if self == Device.GPS1:
            return shell_pb2.DEVICE_GPS1
        if self == Device.GPS2:
            return shell_pb2.DEVICE_GPS2
        if self == Device.SHELL:
            return shell_pb2.DEVICE_SHELL
        if self == Device.SERIAL0:
            return shell_pb2.DEVICE_SERIAL0
        if self == Device.SERIAL1:
            return shell_pb2.DEVICE_SERIAL1
        if self == Device.SERIAL2:
            return shell_pb2.DEVICE_SERIAL2
        if self == Device.SERIAL3:
            return shell_pb2.DEVICE_SERIAL3
        if self == Device.SERIAL4:
            return shell_pb2.DEVICE_SERIAL4
        if self == Device.SERIAL5:
            return shell_pb2.DEVICE_SERIAL5
        if self == Device.SERIAL6:
            return shell_pb2.DEVICE_SERIAL6
        if self == Device.SERIAL7:
            return shell_pb2.DEVICE_SERIAL7
        if self == Device.SERIAL8:
            return shell_pb2.DEVICE_SERIAL8
        if self == Device.SERIAL9:
            return shell_pb2.DEVICE_SERIAL9

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """Parses a gRPC response"""
        if rpc_enum_value == shell_pb2.DEVICE_TELEM1:
            return Device.TELEM1
        if rpc_enum_value == shell_pb2.DEVICE_TELEM2:
            return Device.TELEM2
        if rpc_enum_value == shell_pb2.DEVICE_GPS1:
            return Device.GPS1
        if rpc_enum_value == shell_pb2.DEVICE_GPS2:
            return Device.GPS2
        if rpc_enum_value == shell_pb2.DEVICE_SHELL:
            return Device.SHELL
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL0:
            return Device.SERIAL0
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL1:
            return Device.SERIAL1
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL2:
            return Device.SERIAL2
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL3:
            return Device.SERIAL3
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL4:
            return Device.SERIAL4
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL5:
            return Device.SERIAL5
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL6:
            return Device.SERIAL6
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL7:
            return Device.SERIAL7
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL8:
            return Device.SERIAL8
        if rpc_enum_value == shell_pb2.DEVICE_SERIAL9:
            return Device.SERIAL9

    def __str__(self):
        return self.name


class Receive:
    """
    Received shell data and source device.

    Parameters
    ----------
    data : std::string
         Received data.

    device : Device
         SERIAL_CONTROL device the data came from.

    """

    def __init__(self, data, device):
        """Initializes the Receive object"""
        self.data = data
        self.device = device

    def __eq__(self, to_compare):
        """Checks if two Receive are the same"""
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Receive object
            return (self.data == to_compare.data) and (self.device == to_compare.device)

        except AttributeError:
            return False

    def __str__(self):
        """Receive in string representation"""
        struct_repr = ", ".join(
            ["data: " + str(self.data), "device: " + str(self.device)]
        )

        return f"Receive: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcReceive):
        """Translates a gRPC struct to the SDK equivalent"""
        return Receive(rpcReceive.data, Device.translate_from_rpc(rpcReceive.device))

    def translate_to_rpc(self, rpcReceive):
        """Translates this SDK object into its gRPC equivalent"""

        rpcReceive.data = self.data

        rpcReceive.device = self.device.translate_to_rpc()


class ShellResult:
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
        Possible results returned for shell requests

        Values
        ------
        UNKNOWN
             Unknown result

        SUCCESS
             Request succeeded

        NO_SYSTEM
             No system is connected

        CONNECTION_ERROR
             Connection error

        NO_RESPONSE
             Response was not received

        BUSY
             Shell busy (transfer in progress)

        INVALID_ARGUMENT
             Invalid device / argument

        """

        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        NO_RESPONSE = 4
        BUSY = 5
        INVALID_ARGUMENT = 6

        def translate_to_rpc(self):
            if self == ShellResult.Result.UNKNOWN:
                return shell_pb2.ShellResult.RESULT_UNKNOWN
            if self == ShellResult.Result.SUCCESS:
                return shell_pb2.ShellResult.RESULT_SUCCESS
            if self == ShellResult.Result.NO_SYSTEM:
                return shell_pb2.ShellResult.RESULT_NO_SYSTEM
            if self == ShellResult.Result.CONNECTION_ERROR:
                return shell_pb2.ShellResult.RESULT_CONNECTION_ERROR
            if self == ShellResult.Result.NO_RESPONSE:
                return shell_pb2.ShellResult.RESULT_NO_RESPONSE
            if self == ShellResult.Result.BUSY:
                return shell_pb2.ShellResult.RESULT_BUSY
            if self == ShellResult.Result.INVALID_ARGUMENT:
                return shell_pb2.ShellResult.RESULT_INVALID_ARGUMENT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """Parses a gRPC response"""
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_UNKNOWN:
                return ShellResult.Result.UNKNOWN
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_SUCCESS:
                return ShellResult.Result.SUCCESS
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_NO_SYSTEM:
                return ShellResult.Result.NO_SYSTEM
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_CONNECTION_ERROR:
                return ShellResult.Result.CONNECTION_ERROR
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_NO_RESPONSE:
                return ShellResult.Result.NO_RESPONSE
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_BUSY:
                return ShellResult.Result.BUSY
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_INVALID_ARGUMENT:
                return ShellResult.Result.INVALID_ARGUMENT

        def __str__(self):
            return self.name

    def __init__(self, result, result_str):
        """Initializes the ShellResult object"""
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """Checks if two ShellResult are the same"""
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ShellResult object
            return (self.result == to_compare.result) and (
                self.result_str == to_compare.result_str
            )

        except AttributeError:
            return False

    def __str__(self):
        """ShellResult in string representation"""
        struct_repr = ", ".join(
            ["result: " + str(self.result), "result_str: " + str(self.result_str)]
        )

        return f"ShellResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcShellResult):
        """Translates a gRPC struct to the SDK equivalent"""
        return ShellResult(
            ShellResult.Result.translate_from_rpc(rpcShellResult.result),
            rpcShellResult.result_str,
        )

    def translate_to_rpc(self, rpcShellResult):
        """Translates this SDK object into its gRPC equivalent"""

        rpcShellResult.result = self.result.translate_to_rpc()

        rpcShellResult.result_str = self.result_str


class ShellError(Exception):
    """Raised when a ShellResult is a fail code"""

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Shell(AsyncBase):
    """
    Allow to communicate with the vehicle's system shell.

    Under the hood this uses MAVLink SERIAL_CONTROL. The default device is
    SERIAL_CONTROL_DEV_SHELL. Callers can pass another SERIAL_CONTROL_DEV on
    Send (and observe the device on Receive) when the same framing is used for
    non-nsh serial bridges (for example TELEM2).

    Generated by dcsdkgen - MAVSDK Shell API
    """

    # Plugin name
    name = "Shell"

    def _setup_stub(self, channel):
        """Setups the api stub"""
        self._stub = shell_pb2_grpc.ShellServiceStub(channel)

    def _extract_result(self, response):
        """Returns the response status and description"""
        return ShellResult.translate_from_rpc(response.shell_result)

    async def send(self, command, device):
        """
        Send a command line.

        Parameters
        ----------
        command : std::string
             The command line to send

        device : Device

        Raises
        ------
        ShellError
            If the request fails. The error contains the reason for the failure.
        """

        request = shell_pb2.SendRequest()
        request.command = command

        request.device = device.translate_to_rpc()

        response = await self._stub.Send(request)

        result = self._extract_result(response)

        if result.result != ShellResult.Result.SUCCESS:
            raise ShellError(result, "send()", command, device)

    async def receive(self):
        """
        Receive feedback from a sent command line.

        This subscription needs to be made before a command line is sent, otherwise, no response will be sent.

        Yields
        -------
        receive : Receive
             Received data.


        """

        request = shell_pb2.SubscribeReceiveRequest()
        receive_stream = self._stub.SubscribeReceive(request)

        try:
            async for response in receive_stream:
                yield Receive.translate_from_rpc(response.receive)
        finally:
            receive_stream.cancel()
