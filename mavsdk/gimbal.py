# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import gimbal_pb2, gimbal_pb2_grpc
from enum import Enum


class GimbalMode(Enum):
    """
     Gimbal mode type.

     Values
     ------
     YAW_FOLLOW
          Yaw follow will point the gimbal to the vehicle heading

     YAW_LOCK
          Yaw lock will fix the gimbal poiting to an absolute direction

     """

    
    YAW_FOLLOW = 0
    YAW_LOCK = 1

    def translate_to_rpc(self):
        if self == GimbalMode.YAW_FOLLOW:
            return gimbal_pb2.GIMBAL_MODE_YAW_FOLLOW
        if self == GimbalMode.YAW_LOCK:
            return gimbal_pb2.GIMBAL_MODE_YAW_LOCK

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == gimbal_pb2.GIMBAL_MODE_YAW_FOLLOW:
            return GimbalMode.YAW_FOLLOW
        if rpc_enum_value == gimbal_pb2.GIMBAL_MODE_YAW_LOCK:
            return GimbalMode.YAW_LOCK

    def __str__(self):
        return self.name


class ControlMode(Enum):
    """
     Control mode

     Values
     ------
     NONE
          Indicates that the component does not have control over the gimbal

     PRIMARY
          To take primary control over the gimbal

     SECONDARY
          To take secondary control over the gimbal

     """

    
    NONE = 0
    PRIMARY = 1
    SECONDARY = 2

    def translate_to_rpc(self):
        if self == ControlMode.NONE:
            return gimbal_pb2.CONTROL_MODE_NONE
        if self == ControlMode.PRIMARY:
            return gimbal_pb2.CONTROL_MODE_PRIMARY
        if self == ControlMode.SECONDARY:
            return gimbal_pb2.CONTROL_MODE_SECONDARY

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == gimbal_pb2.CONTROL_MODE_NONE:
            return ControlMode.NONE
        if rpc_enum_value == gimbal_pb2.CONTROL_MODE_PRIMARY:
            return ControlMode.PRIMARY
        if rpc_enum_value == gimbal_pb2.CONTROL_MODE_SECONDARY:
            return ControlMode.SECONDARY

    def __str__(self):
        return self.name


class ControlStatus:
    """
     Control status

     Parameters
     ----------
     control_mode : ControlMode
          Control mode (none, primary or secondary)

     sysid_primary_control : int32_t
          Sysid of the component that has primary control over the gimbal (0 if no one is in control)

     compid_primary_control : int32_t
          Compid of the component that has primary control over the gimbal (0 if no one is in control)

     sysid_secondary_control : int32_t
          Sysid of the component that has secondary control over the gimbal (0 if no one is in control)

     compid_secondary_control : int32_t
          Compid of the component that has secondary control over the gimbal (0 if no one is in control)

     """

    

    def __init__(
            self,
            control_mode,
            sysid_primary_control,
            compid_primary_control,
            sysid_secondary_control,
            compid_secondary_control):
        """ Initializes the ControlStatus object """
        self.control_mode = control_mode
        self.sysid_primary_control = sysid_primary_control
        self.compid_primary_control = compid_primary_control
        self.sysid_secondary_control = sysid_secondary_control
        self.compid_secondary_control = compid_secondary_control

    def __eq__(self, to_compare):
        """ Checks if two ControlStatus are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ControlStatus object
            return \
                (self.control_mode == to_compare.control_mode) and \
                (self.sysid_primary_control == to_compare.sysid_primary_control) and \
                (self.compid_primary_control == to_compare.compid_primary_control) and \
                (self.sysid_secondary_control == to_compare.sysid_secondary_control) and \
                (self.compid_secondary_control == to_compare.compid_secondary_control)

        except AttributeError:
            return False

    def __str__(self):
        """ ControlStatus in string representation """
        struct_repr = ", ".join([
                "control_mode: " + str(self.control_mode),
                "sysid_primary_control: " + str(self.sysid_primary_control),
                "compid_primary_control: " + str(self.compid_primary_control),
                "sysid_secondary_control: " + str(self.sysid_secondary_control),
                "compid_secondary_control: " + str(self.compid_secondary_control)
                ])

        return f"ControlStatus: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcControlStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return ControlStatus(
                
                ControlMode.translate_from_rpc(rpcControlStatus.control_mode),
                
                
                rpcControlStatus.sysid_primary_control,
                
                
                rpcControlStatus.compid_primary_control,
                
                
                rpcControlStatus.sysid_secondary_control,
                
                
                rpcControlStatus.compid_secondary_control
                )

    def translate_to_rpc(self, rpcControlStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcControlStatus.control_mode = self.control_mode.translate_to_rpc()
            
        
        
        
            
        rpcControlStatus.sysid_primary_control = self.sysid_primary_control
            
        
        
        
            
        rpcControlStatus.compid_primary_control = self.compid_primary_control
            
        
        
        
            
        rpcControlStatus.sysid_secondary_control = self.sysid_secondary_control
            
        
        
        
            
        rpcControlStatus.compid_secondary_control = self.compid_secondary_control
            
        
        


class GimbalResult:
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
         Possible results returned for gimbal commands.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Command was accepted

         ERROR
              Error occurred sending the command

         TIMEOUT
              Command timed out

         UNSUPPORTED
              Functionality not supported

         NO_SYSTEM
              No system connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        ERROR = 2
        TIMEOUT = 3
        UNSUPPORTED = 4
        NO_SYSTEM = 5

        def translate_to_rpc(self):
            if self == GimbalResult.Result.UNKNOWN:
                return gimbal_pb2.GimbalResult.RESULT_UNKNOWN
            if self == GimbalResult.Result.SUCCESS:
                return gimbal_pb2.GimbalResult.RESULT_SUCCESS
            if self == GimbalResult.Result.ERROR:
                return gimbal_pb2.GimbalResult.RESULT_ERROR
            if self == GimbalResult.Result.TIMEOUT:
                return gimbal_pb2.GimbalResult.RESULT_TIMEOUT
            if self == GimbalResult.Result.UNSUPPORTED:
                return gimbal_pb2.GimbalResult.RESULT_UNSUPPORTED
            if self == GimbalResult.Result.NO_SYSTEM:
                return gimbal_pb2.GimbalResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_UNKNOWN:
                return GimbalResult.Result.UNKNOWN
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_SUCCESS:
                return GimbalResult.Result.SUCCESS
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_ERROR:
                return GimbalResult.Result.ERROR
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_TIMEOUT:
                return GimbalResult.Result.TIMEOUT
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_UNSUPPORTED:
                return GimbalResult.Result.UNSUPPORTED
            if rpc_enum_value == gimbal_pb2.GimbalResult.RESULT_NO_SYSTEM:
                return GimbalResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the GimbalResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two GimbalResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GimbalResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ GimbalResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"GimbalResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGimbalResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return GimbalResult(
                
                GimbalResult.Result.translate_from_rpc(rpcGimbalResult.result),
                
                
                rpcGimbalResult.result_str
                )

    def translate_to_rpc(self, rpcGimbalResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGimbalResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcGimbalResult.result_str = self.result_str
            
        
        



class GimbalError(Exception):
    """ Raised when a GimbalResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Gimbal(AsyncBase):
    """
     Provide control over a gimbal.

     Generated by dcsdkgen - MAVSDK Gimbal API
    """

    # Plugin name
    name = "Gimbal"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = gimbal_pb2_grpc.GimbalServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return GimbalResult.translate_from_rpc(response.gimbal_result)
    

    async def set_pitch_and_yaw(self, pitch_deg, yaw_deg):
        """
         Set gimbal pitch and yaw angles.

         This sets the desired pitch and yaw angles of a gimbal.
         Will return when the command is accepted, however, it might
         take the gimbal longer to actually be set to the new angles.

         Parameters
         ----------
         pitch_deg : float
              Pitch angle in degrees (negative points down)

         yaw_deg : float
              Yaw angle in degrees (positive is clock-wise, range: -180 to 180 or 0 to 360)

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.SetPitchAndYawRequest()
        request.pitch_deg = pitch_deg
        request.yaw_deg = yaw_deg
        response = await self._stub.SetPitchAndYaw(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "set_pitch_and_yaw()", pitch_deg, yaw_deg)
        

    async def set_pitch_rate_and_yaw_rate(self, pitch_rate_deg_s, yaw_rate_deg_s):
        """
         Set gimbal angular rates around pitch and yaw axes.

         This sets the desired angular rates around pitch and yaw axes of a gimbal.
         Will return when the command is accepted, however, it might
         take the gimbal longer to actually reach the angular rate.

         Parameters
         ----------
         pitch_rate_deg_s : float
              Angular rate around pitch axis in degrees/second (negative downward)

         yaw_rate_deg_s : float
              Angular rate around yaw axis in degrees/second (positive is clock-wise)

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.SetPitchRateAndYawRateRequest()
        request.pitch_rate_deg_s = pitch_rate_deg_s
        request.yaw_rate_deg_s = yaw_rate_deg_s
        response = await self._stub.SetPitchRateAndYawRate(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "set_pitch_rate_and_yaw_rate()", pitch_rate_deg_s, yaw_rate_deg_s)
        

    async def set_mode(self, gimbal_mode):
        """
         Set gimbal mode.

         This sets the desired yaw mode of a gimbal.
         Will return when the command is accepted. However, it might
         take the gimbal longer to actually be set to the new angles.

         Parameters
         ----------
         gimbal_mode : GimbalMode
              The mode to be set.

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.SetModeRequest()
        
        request.gimbal_mode = gimbal_mode.translate_to_rpc()
                
            
        response = await self._stub.SetMode(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "set_mode()", gimbal_mode)
        

    async def set_roi_location(self, latitude_deg, longitude_deg, altitude_m):
        """
         Set gimbal region of interest (ROI).

         This sets a region of interest that the gimbal will point to.
         The gimbal will continue to point to the specified region until it
         receives a new command.
         The function will return when the command is accepted, however, it might
         take the gimbal longer to actually rotate to the ROI.

         Parameters
         ----------
         latitude_deg : double
              Latitude in degrees

         longitude_deg : double
              Longitude in degrees

         altitude_m : float
              Altitude in metres (AMSL)

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.SetRoiLocationRequest()
        request.latitude_deg = latitude_deg
        request.longitude_deg = longitude_deg
        request.altitude_m = altitude_m
        response = await self._stub.SetRoiLocation(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "set_roi_location()", latitude_deg, longitude_deg, altitude_m)
        

    async def take_control(self, control_mode):
        """
         Take control.

         There can be only two components in control of a gimbal at any given time.
         One with "primary" control, and one with "secondary" control. The way the
         secondary control is implemented is not specified and hence depends on the
         vehicle.

         Components are expected to be cooperative, which means that they can
         override each other and should therefore do it carefully.

         Parameters
         ----------
         control_mode : ControlMode
              Control mode (primary or secondary)

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.TakeControlRequest()
        
        request.control_mode = control_mode.translate_to_rpc()
                
            
        response = await self._stub.TakeControl(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "take_control()", control_mode)
        

    async def release_control(self):
        """
         Release control.

         Release control, such that other components can control the gimbal.

         Raises
         ------
         GimbalError
             If the request fails. The error contains the reason for the failure.
        """

        request = gimbal_pb2.ReleaseControlRequest()
        response = await self._stub.ReleaseControl(request)

        
        result = self._extract_result(response)

        if result.result != GimbalResult.Result.SUCCESS:
            raise GimbalError(result, "release_control()")
        

    async def control(self):
        """
         Subscribe to control status updates.

         This allows a component to know if it has primary, secondary or
         no control over the gimbal. Also, it gives the system and component ids
         of the other components in control (if any).

         Yields
         -------
         control_status : ControlStatus
              Control status

         
        """

        request = gimbal_pb2.SubscribeControlRequest()
        control_stream = self._stub.SubscribeControl(request)

        try:
            async for response in control_stream:
                

            
                yield ControlStatus.translate_from_rpc(response.control_status)
        finally:
            control_stream.cancel()