# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import failure_pb2, failure_pb2_grpc
from enum import Enum


class FailureUnit(Enum):
    """
     A failure unit.

     Values
     ------
     SENSOR_GYRO
          Gyro

     SENSOR_ACCEL
          Accelerometer

     SENSOR_MAG
          Magnetometer

     SENSOR_BARO
          Barometer

     SENSOR_GPS
          GPS

     SENSOR_OPTICAL_FLOW
          Optical flow

     SENSOR_VIO
          Visual inertial odometry

     SENSOR_DISTANCE_SENSOR
          Distance sensor

     SENSOR_AIRSPEED
          Airspeed

     SYSTEM_BATTERY
          Battery

     SYSTEM_MOTOR
          Motor

     SYSTEM_SERVO
          Servo

     SYSTEM_AVOIDANCE
          Avoidance

     SYSTEM_RC_SIGNAL
          RC signal

     SYSTEM_MAVLINK_SIGNAL
          MAVLink signal

     """

    
    SENSOR_GYRO = 0
    SENSOR_ACCEL = 1
    SENSOR_MAG = 2
    SENSOR_BARO = 3
    SENSOR_GPS = 4
    SENSOR_OPTICAL_FLOW = 5
    SENSOR_VIO = 6
    SENSOR_DISTANCE_SENSOR = 7
    SENSOR_AIRSPEED = 8
    SYSTEM_BATTERY = 9
    SYSTEM_MOTOR = 10
    SYSTEM_SERVO = 11
    SYSTEM_AVOIDANCE = 12
    SYSTEM_RC_SIGNAL = 13
    SYSTEM_MAVLINK_SIGNAL = 14

    def translate_to_rpc(self):
        if self == FailureUnit.SENSOR_GYRO:
            return failure_pb2.FAILURE_UNIT_SENSOR_GYRO
        if self == FailureUnit.SENSOR_ACCEL:
            return failure_pb2.FAILURE_UNIT_SENSOR_ACCEL
        if self == FailureUnit.SENSOR_MAG:
            return failure_pb2.FAILURE_UNIT_SENSOR_MAG
        if self == FailureUnit.SENSOR_BARO:
            return failure_pb2.FAILURE_UNIT_SENSOR_BARO
        if self == FailureUnit.SENSOR_GPS:
            return failure_pb2.FAILURE_UNIT_SENSOR_GPS
        if self == FailureUnit.SENSOR_OPTICAL_FLOW:
            return failure_pb2.FAILURE_UNIT_SENSOR_OPTICAL_FLOW
        if self == FailureUnit.SENSOR_VIO:
            return failure_pb2.FAILURE_UNIT_SENSOR_VIO
        if self == FailureUnit.SENSOR_DISTANCE_SENSOR:
            return failure_pb2.FAILURE_UNIT_SENSOR_DISTANCE_SENSOR
        if self == FailureUnit.SENSOR_AIRSPEED:
            return failure_pb2.FAILURE_UNIT_SENSOR_AIRSPEED
        if self == FailureUnit.SYSTEM_BATTERY:
            return failure_pb2.FAILURE_UNIT_SYSTEM_BATTERY
        if self == FailureUnit.SYSTEM_MOTOR:
            return failure_pb2.FAILURE_UNIT_SYSTEM_MOTOR
        if self == FailureUnit.SYSTEM_SERVO:
            return failure_pb2.FAILURE_UNIT_SYSTEM_SERVO
        if self == FailureUnit.SYSTEM_AVOIDANCE:
            return failure_pb2.FAILURE_UNIT_SYSTEM_AVOIDANCE
        if self == FailureUnit.SYSTEM_RC_SIGNAL:
            return failure_pb2.FAILURE_UNIT_SYSTEM_RC_SIGNAL
        if self == FailureUnit.SYSTEM_MAVLINK_SIGNAL:
            return failure_pb2.FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_GYRO:
            return FailureUnit.SENSOR_GYRO
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_ACCEL:
            return FailureUnit.SENSOR_ACCEL
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_MAG:
            return FailureUnit.SENSOR_MAG
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_BARO:
            return FailureUnit.SENSOR_BARO
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_GPS:
            return FailureUnit.SENSOR_GPS
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_OPTICAL_FLOW:
            return FailureUnit.SENSOR_OPTICAL_FLOW
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_VIO:
            return FailureUnit.SENSOR_VIO
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_DISTANCE_SENSOR:
            return FailureUnit.SENSOR_DISTANCE_SENSOR
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SENSOR_AIRSPEED:
            return FailureUnit.SENSOR_AIRSPEED
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_BATTERY:
            return FailureUnit.SYSTEM_BATTERY
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_MOTOR:
            return FailureUnit.SYSTEM_MOTOR
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_SERVO:
            return FailureUnit.SYSTEM_SERVO
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_AVOIDANCE:
            return FailureUnit.SYSTEM_AVOIDANCE
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_RC_SIGNAL:
            return FailureUnit.SYSTEM_RC_SIGNAL
        if rpc_enum_value == failure_pb2.FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL:
            return FailureUnit.SYSTEM_MAVLINK_SIGNAL

    def __str__(self):
        return self.name


class FailureType(Enum):
    """
     A failure type

     Values
     ------
     OK
          No failure injected, used to reset a previous failure

     OFF
          Sets unit off, so completely non-responsive

     STUCK
          Unit is stuck e.g. keeps reporting the same value

     GARBAGE
          Unit is reporting complete garbage

     WRONG
          Unit is consistently wrong

     SLOW
          Unit is slow, so e.g. reporting at slower than expected rate

     DELAYED
          Data of unit is delayed in time

     INTERMITTENT
          Unit is sometimes working, sometimes not

     """

    
    OK = 0
    OFF = 1
    STUCK = 2
    GARBAGE = 3
    WRONG = 4
    SLOW = 5
    DELAYED = 6
    INTERMITTENT = 7

    def translate_to_rpc(self):
        if self == FailureType.OK:
            return failure_pb2.FAILURE_TYPE_OK
        if self == FailureType.OFF:
            return failure_pb2.FAILURE_TYPE_OFF
        if self == FailureType.STUCK:
            return failure_pb2.FAILURE_TYPE_STUCK
        if self == FailureType.GARBAGE:
            return failure_pb2.FAILURE_TYPE_GARBAGE
        if self == FailureType.WRONG:
            return failure_pb2.FAILURE_TYPE_WRONG
        if self == FailureType.SLOW:
            return failure_pb2.FAILURE_TYPE_SLOW
        if self == FailureType.DELAYED:
            return failure_pb2.FAILURE_TYPE_DELAYED
        if self == FailureType.INTERMITTENT:
            return failure_pb2.FAILURE_TYPE_INTERMITTENT

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_OK:
            return FailureType.OK
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_OFF:
            return FailureType.OFF
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_STUCK:
            return FailureType.STUCK
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_GARBAGE:
            return FailureType.GARBAGE
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_WRONG:
            return FailureType.WRONG
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_SLOW:
            return FailureType.SLOW
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_DELAYED:
            return FailureType.DELAYED
        if rpc_enum_value == failure_pb2.FAILURE_TYPE_INTERMITTENT:
            return FailureType.INTERMITTENT

    def __str__(self):
        return self.name


class FailureResult:
    """
 

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for failure requests.

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

         UNSUPPORTED
              Failure not supported

         DENIED
              Failure injection denied

         DISABLED
              Failure injection is disabled

         TIMEOUT
              Request timed out

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        UNSUPPORTED = 4
        DENIED = 5
        DISABLED = 6
        TIMEOUT = 7

        def translate_to_rpc(self):
            if self == FailureResult.Result.UNKNOWN:
                return failure_pb2.FailureResult.RESULT_UNKNOWN
            if self == FailureResult.Result.SUCCESS:
                return failure_pb2.FailureResult.RESULT_SUCCESS
            if self == FailureResult.Result.NO_SYSTEM:
                return failure_pb2.FailureResult.RESULT_NO_SYSTEM
            if self == FailureResult.Result.CONNECTION_ERROR:
                return failure_pb2.FailureResult.RESULT_CONNECTION_ERROR
            if self == FailureResult.Result.UNSUPPORTED:
                return failure_pb2.FailureResult.RESULT_UNSUPPORTED
            if self == FailureResult.Result.DENIED:
                return failure_pb2.FailureResult.RESULT_DENIED
            if self == FailureResult.Result.DISABLED:
                return failure_pb2.FailureResult.RESULT_DISABLED
            if self == FailureResult.Result.TIMEOUT:
                return failure_pb2.FailureResult.RESULT_TIMEOUT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_UNKNOWN:
                return FailureResult.Result.UNKNOWN
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_SUCCESS:
                return FailureResult.Result.SUCCESS
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_NO_SYSTEM:
                return FailureResult.Result.NO_SYSTEM
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_CONNECTION_ERROR:
                return FailureResult.Result.CONNECTION_ERROR
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_UNSUPPORTED:
                return FailureResult.Result.UNSUPPORTED
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_DENIED:
                return FailureResult.Result.DENIED
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_DISABLED:
                return FailureResult.Result.DISABLED
            if rpc_enum_value == failure_pb2.FailureResult.RESULT_TIMEOUT:
                return FailureResult.Result.TIMEOUT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the FailureResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two FailureResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FailureResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ FailureResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"FailureResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFailureResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return FailureResult(
                
                FailureResult.Result.translate_from_rpc(rpcFailureResult.result),
                
                
                rpcFailureResult.result_str
                )

    def translate_to_rpc(self, rpcFailureResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFailureResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcFailureResult.result_str = self.result_str
            
        
        



class FailureError(Exception):
    """ Raised when a FailureResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Failure(AsyncBase):
    """
     Inject failures into system to test failsafes.

     Generated by dcsdkgen - MAVSDK Failure API
    """

    # Plugin name
    name = "Failure"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = failure_pb2_grpc.FailureServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return FailureResult.translate_from_rpc(response.failure_result)
    

    async def inject(self, failure_unit, failure_type, instance):
        """
         Injects a failure.

         Parameters
         ----------
         failure_unit : FailureUnit
              The failure unit to send

         failure_type : FailureType
              The failure type to send

         instance : int32_t
              Instance to affect (0 for all)

         Raises
         ------
         FailureError
             If the request fails. The error contains the reason for the failure.
        """

        request = failure_pb2.InjectRequest()
        
        request.failure_unit = failure_unit.translate_to_rpc()
                
            
        
        request.failure_type = failure_type.translate_to_rpc()
                
            
        request.instance = instance
        response = await self._stub.Inject(request)

        
        result = self._extract_result(response)

        if result.result != FailureResult.Result.SUCCESS:
            raise FailureError(result, "inject()", failure_unit, failure_type, instance)
        