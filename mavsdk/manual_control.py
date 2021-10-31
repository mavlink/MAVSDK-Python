# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import manual_control_pb2, manual_control_pb2_grpc
from enum import Enum


class ManualControlResult:
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
         Possible results returned for manual control requests.

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

         COMMAND_DENIED
              Command refused by vehicle

         TIMEOUT
              Request timed out

         INPUT_OUT_OF_RANGE
              Input out of range

         INPUT_NOT_SET
              No Input set

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        INPUT_OUT_OF_RANGE = 7
        INPUT_NOT_SET = 8

        def translate_to_rpc(self):
            if self == ManualControlResult.Result.UNKNOWN:
                return manual_control_pb2.ManualControlResult.RESULT_UNKNOWN
            if self == ManualControlResult.Result.SUCCESS:
                return manual_control_pb2.ManualControlResult.RESULT_SUCCESS
            if self == ManualControlResult.Result.NO_SYSTEM:
                return manual_control_pb2.ManualControlResult.RESULT_NO_SYSTEM
            if self == ManualControlResult.Result.CONNECTION_ERROR:
                return manual_control_pb2.ManualControlResult.RESULT_CONNECTION_ERROR
            if self == ManualControlResult.Result.BUSY:
                return manual_control_pb2.ManualControlResult.RESULT_BUSY
            if self == ManualControlResult.Result.COMMAND_DENIED:
                return manual_control_pb2.ManualControlResult.RESULT_COMMAND_DENIED
            if self == ManualControlResult.Result.TIMEOUT:
                return manual_control_pb2.ManualControlResult.RESULT_TIMEOUT
            if self == ManualControlResult.Result.INPUT_OUT_OF_RANGE:
                return manual_control_pb2.ManualControlResult.RESULT_INPUT_OUT_OF_RANGE
            if self == ManualControlResult.Result.INPUT_NOT_SET:
                return manual_control_pb2.ManualControlResult.RESULT_INPUT_NOT_SET

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_UNKNOWN:
                return ManualControlResult.Result.UNKNOWN
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_SUCCESS:
                return ManualControlResult.Result.SUCCESS
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_NO_SYSTEM:
                return ManualControlResult.Result.NO_SYSTEM
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_CONNECTION_ERROR:
                return ManualControlResult.Result.CONNECTION_ERROR
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_BUSY:
                return ManualControlResult.Result.BUSY
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_COMMAND_DENIED:
                return ManualControlResult.Result.COMMAND_DENIED
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_TIMEOUT:
                return ManualControlResult.Result.TIMEOUT
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_INPUT_OUT_OF_RANGE:
                return ManualControlResult.Result.INPUT_OUT_OF_RANGE
            if rpc_enum_value == manual_control_pb2.ManualControlResult.RESULT_INPUT_NOT_SET:
                return ManualControlResult.Result.INPUT_NOT_SET

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ManualControlResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ManualControlResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ManualControlResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ManualControlResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ManualControlResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcManualControlResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ManualControlResult(
                
                ManualControlResult.Result.translate_from_rpc(rpcManualControlResult.result),
                
                
                rpcManualControlResult.result_str
                )

    def translate_to_rpc(self, rpcManualControlResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcManualControlResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcManualControlResult.result_str = self.result_str
            
        
        



class ManualControlError(Exception):
    """ Raised when a ManualControlResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ManualControl(AsyncBase):
    """
     Enable manual control using e.g. a joystick or gamepad.

     Generated by dcsdkgen - MAVSDK ManualControl API
    """

    # Plugin name
    name = "ManualControl"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = manual_control_pb2_grpc.ManualControlServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ManualControlResult.translate_from_rpc(response.manual_control_result)
    

    async def start_position_control(self):
        """
         Start position control using e.g. joystick input.

         Requires manual control input to be sent regularly already.
         Requires a valid position using e.g. GPS, external vision, or optical flow.

         Raises
         ------
         ManualControlError
             If the request fails. The error contains the reason for the failure.
        """

        request = manual_control_pb2.StartPositionControlRequest()
        response = await self._stub.StartPositionControl(request)

        
        result = self._extract_result(response)

        if result.result != ManualControlResult.Result.SUCCESS:
            raise ManualControlError(result, "start_position_control()")
        

    async def start_altitude_control(self):
        """
         Start altitude control

         Requires manual control input to be sent regularly already.
         Does not require a  valid position e.g. GPS.

         Raises
         ------
         ManualControlError
             If the request fails. The error contains the reason for the failure.
        """

        request = manual_control_pb2.StartAltitudeControlRequest()
        response = await self._stub.StartAltitudeControl(request)

        
        result = self._extract_result(response)

        if result.result != ManualControlResult.Result.SUCCESS:
            raise ManualControlError(result, "start_altitude_control()")
        

    async def set_manual_control_input(self, x, y, z, r):
        """
         Set manual control input

         The manual control input needs to be sent at a rate high enough to prevent
         triggering of RC loss, a good minimum rate is 10 Hz.

         Parameters
         ----------
         x : float
              value between -1. to 1. negative -> backwards, positive -> forwards

         y : float
              value between -1. to 1. negative -> left, positive -> right

         z : float
              value between -1. to 1. negative -> down, positive -> up (usually for now, for multicopter 0 to 1 is expected)

         r : float
              value between -1. to 1. negative -> turn anti-clockwise (towards the left), positive -> turn clockwise (towards the right)

         Raises
         ------
         ManualControlError
             If the request fails. The error contains the reason for the failure.
        """

        request = manual_control_pb2.SetManualControlInputRequest()
        request.x = x
        request.y = y
        request.z = z
        request.r = r
        response = await self._stub.SetManualControlInput(request)

        
        result = self._extract_result(response)

        if result.result != ManualControlResult.Result.SUCCESS:
            raise ManualControlError(result, "set_manual_control_input()", x, y, z, r)
        