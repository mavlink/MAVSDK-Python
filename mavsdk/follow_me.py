# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import follow_me_pb2, follow_me_pb2_grpc
from enum import Enum


class Config:
    """
     Configuration type.

     Parameters
     ----------
     min_height_m : float
          Minimum height for the vehicle in meters (recommended minimum 8 meters)

     follow_distance_m : float
          Distance from target for vehicle to follow in meters (recommended minimum 1 meter)

     follow_direction : FollowDirection
          Direction to follow in

     responsiveness : float
          How responsive the vehicle is to the motion of the target (range 0.0 to 1.0)

     """

    
    
    class FollowDirection(Enum):
        """
         Direction relative to the target that the vehicle should follow

         Values
         ------
         NONE
              Do not follow

         BEHIND
              Follow from behind

         FRONT
              Follow from front

         FRONT_RIGHT
              Follow from front right

         FRONT_LEFT
              Follow from front left

         """

        
        NONE = 0
        BEHIND = 1
        FRONT = 2
        FRONT_RIGHT = 3
        FRONT_LEFT = 4

        def translate_to_rpc(self):
            if self == Config.FollowDirection.NONE:
                return follow_me_pb2.Config.FOLLOW_DIRECTION_NONE
            if self == Config.FollowDirection.BEHIND:
                return follow_me_pb2.Config.FOLLOW_DIRECTION_BEHIND
            if self == Config.FollowDirection.FRONT:
                return follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT
            if self == Config.FollowDirection.FRONT_RIGHT:
                return follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT_RIGHT
            if self == Config.FollowDirection.FRONT_LEFT:
                return follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT_LEFT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == follow_me_pb2.Config.FOLLOW_DIRECTION_NONE:
                return Config.FollowDirection.NONE
            if rpc_enum_value == follow_me_pb2.Config.FOLLOW_DIRECTION_BEHIND:
                return Config.FollowDirection.BEHIND
            if rpc_enum_value == follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT:
                return Config.FollowDirection.FRONT
            if rpc_enum_value == follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT_RIGHT:
                return Config.FollowDirection.FRONT_RIGHT
            if rpc_enum_value == follow_me_pb2.Config.FOLLOW_DIRECTION_FRONT_LEFT:
                return Config.FollowDirection.FRONT_LEFT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            min_height_m,
            follow_distance_m,
            follow_direction,
            responsiveness):
        """ Initializes the Config object """
        self.min_height_m = min_height_m
        self.follow_distance_m = follow_distance_m
        self.follow_direction = follow_direction
        self.responsiveness = responsiveness

    def __eq__(self, to_compare):
        """ Checks if two Config are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Config object
            return \
                (self.min_height_m == to_compare.min_height_m) and \
                (self.follow_distance_m == to_compare.follow_distance_m) and \
                (self.follow_direction == to_compare.follow_direction) and \
                (self.responsiveness == to_compare.responsiveness)

        except AttributeError:
            return False

    def __str__(self):
        """ Config in string representation """
        struct_repr = ", ".join([
                "min_height_m: " + str(self.min_height_m),
                "follow_distance_m: " + str(self.follow_distance_m),
                "follow_direction: " + str(self.follow_direction),
                "responsiveness: " + str(self.responsiveness)
                ])

        return f"Config: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcConfig):
        """ Translates a gRPC struct to the SDK equivalent """
        return Config(
                
                rpcConfig.min_height_m,
                
                
                rpcConfig.follow_distance_m,
                
                
                Config.FollowDirection.translate_from_rpc(rpcConfig.follow_direction),
                
                
                rpcConfig.responsiveness
                )

    def translate_to_rpc(self, rpcConfig):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcConfig.min_height_m = self.min_height_m
            
        
        
        
            
        rpcConfig.follow_distance_m = self.follow_distance_m
            
        
        
        
            
        rpcConfig.follow_direction = self.follow_direction.translate_to_rpc()
            
        
        
        
            
        rpcConfig.responsiveness = self.responsiveness
            
        
        


class TargetLocation:
    """
     Target location for the vehicle to follow

     Parameters
     ----------
     latitude_deg : double
          Target latitude in degrees

     longitude_deg : double
          Target longitude in degrees

     absolute_altitude_m : float
          Target altitude in meters above MSL

     velocity_x_m_s : float
          Target velocity in X axis, in meters per second

     velocity_y_m_s : float
          Target velocity in Y axis, in meters per second

     velocity_z_m_s : float
          Target velocity in Z axis, in meters per second

     """

    

    def __init__(
            self,
            latitude_deg,
            longitude_deg,
            absolute_altitude_m,
            velocity_x_m_s,
            velocity_y_m_s,
            velocity_z_m_s):
        """ Initializes the TargetLocation object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.absolute_altitude_m = absolute_altitude_m
        self.velocity_x_m_s = velocity_x_m_s
        self.velocity_y_m_s = velocity_y_m_s
        self.velocity_z_m_s = velocity_z_m_s

    def __eq__(self, to_compare):
        """ Checks if two TargetLocation are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TargetLocation object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m) and \
                (self.velocity_x_m_s == to_compare.velocity_x_m_s) and \
                (self.velocity_y_m_s == to_compare.velocity_y_m_s) and \
                (self.velocity_z_m_s == to_compare.velocity_z_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ TargetLocation in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "absolute_altitude_m: " + str(self.absolute_altitude_m),
                "velocity_x_m_s: " + str(self.velocity_x_m_s),
                "velocity_y_m_s: " + str(self.velocity_y_m_s),
                "velocity_z_m_s: " + str(self.velocity_z_m_s)
                ])

        return f"TargetLocation: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTargetLocation):
        """ Translates a gRPC struct to the SDK equivalent """
        return TargetLocation(
                
                rpcTargetLocation.latitude_deg,
                
                
                rpcTargetLocation.longitude_deg,
                
                
                rpcTargetLocation.absolute_altitude_m,
                
                
                rpcTargetLocation.velocity_x_m_s,
                
                
                rpcTargetLocation.velocity_y_m_s,
                
                
                rpcTargetLocation.velocity_z_m_s
                )

    def translate_to_rpc(self, rpcTargetLocation):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTargetLocation.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcTargetLocation.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcTargetLocation.absolute_altitude_m = self.absolute_altitude_m
            
        
        
        
            
        rpcTargetLocation.velocity_x_m_s = self.velocity_x_m_s
            
        
        
        
            
        rpcTargetLocation.velocity_y_m_s = self.velocity_y_m_s
            
        
        
        
            
        rpcTargetLocation.velocity_z_m_s = self.velocity_z_m_s
            
        
        


class FollowMeResult:
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
         Possible results returned for followme operations

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command denied

         TIMEOUT
              Request timed out

         NOT_ACTIVE
              FollowMe is not active

         SET_CONFIG_FAILED
              Failed to set FollowMe configuration

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        NOT_ACTIVE = 7
        SET_CONFIG_FAILED = 8

        def translate_to_rpc(self):
            if self == FollowMeResult.Result.UNKNOWN:
                return follow_me_pb2.FollowMeResult.RESULT_UNKNOWN
            if self == FollowMeResult.Result.SUCCESS:
                return follow_me_pb2.FollowMeResult.RESULT_SUCCESS
            if self == FollowMeResult.Result.NO_SYSTEM:
                return follow_me_pb2.FollowMeResult.RESULT_NO_SYSTEM
            if self == FollowMeResult.Result.CONNECTION_ERROR:
                return follow_me_pb2.FollowMeResult.RESULT_CONNECTION_ERROR
            if self == FollowMeResult.Result.BUSY:
                return follow_me_pb2.FollowMeResult.RESULT_BUSY
            if self == FollowMeResult.Result.COMMAND_DENIED:
                return follow_me_pb2.FollowMeResult.RESULT_COMMAND_DENIED
            if self == FollowMeResult.Result.TIMEOUT:
                return follow_me_pb2.FollowMeResult.RESULT_TIMEOUT
            if self == FollowMeResult.Result.NOT_ACTIVE:
                return follow_me_pb2.FollowMeResult.RESULT_NOT_ACTIVE
            if self == FollowMeResult.Result.SET_CONFIG_FAILED:
                return follow_me_pb2.FollowMeResult.RESULT_SET_CONFIG_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_UNKNOWN:
                return FollowMeResult.Result.UNKNOWN
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_SUCCESS:
                return FollowMeResult.Result.SUCCESS
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_NO_SYSTEM:
                return FollowMeResult.Result.NO_SYSTEM
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_CONNECTION_ERROR:
                return FollowMeResult.Result.CONNECTION_ERROR
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_BUSY:
                return FollowMeResult.Result.BUSY
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_COMMAND_DENIED:
                return FollowMeResult.Result.COMMAND_DENIED
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_TIMEOUT:
                return FollowMeResult.Result.TIMEOUT
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_NOT_ACTIVE:
                return FollowMeResult.Result.NOT_ACTIVE
            if rpc_enum_value == follow_me_pb2.FollowMeResult.RESULT_SET_CONFIG_FAILED:
                return FollowMeResult.Result.SET_CONFIG_FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the FollowMeResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two FollowMeResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FollowMeResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ FollowMeResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"FollowMeResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFollowMeResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return FollowMeResult(
                
                FollowMeResult.Result.translate_from_rpc(rpcFollowMeResult.result),
                
                
                rpcFollowMeResult.result_str
                )

    def translate_to_rpc(self, rpcFollowMeResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFollowMeResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcFollowMeResult.result_str = self.result_str
            
        
        



class FollowMeError(Exception):
    """ Raised when a FollowMeResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class FollowMe(AsyncBase):
    """
     Allow users to command the vehicle to follow a specific target.
     The target is provided as a GPS coordinate and altitude.

     Generated by dcsdkgen - MAVSDK FollowMe API
    """

    # Plugin name
    name = "FollowMe"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = follow_me_pb2_grpc.FollowMeServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return FollowMeResult.translate_from_rpc(response.follow_me_result)
    

    async def get_config(self):
        """
         Get current configuration.

         Returns
         -------
         config : Config
              The current configuration

         
        """

        request = follow_me_pb2.GetConfigRequest()
        response = await self._stub.GetConfig(request)

        

        return Config.translate_from_rpc(response.config)
            

    async def set_config(self, config):
        """
         Apply configuration by sending it to the system.

         Parameters
         ----------
         config : Config
              The new configuration to be set

         Raises
         ------
         FollowMeError
             If the request fails. The error contains the reason for the failure.
        """

        request = follow_me_pb2.SetConfigRequest()
        
        config.translate_to_rpc(request.config)
                
            
        response = await self._stub.SetConfig(request)

        
        result = self._extract_result(response)

        if result.result != FollowMeResult.Result.SUCCESS:
            raise FollowMeError(result, "set_config()", config)
        

    async def is_active(self):
        """
         Check if FollowMe is active.

         Returns
         -------
         is_active : bool
              Whether follow me is active or not

         
        """

        request = follow_me_pb2.IsActiveRequest()
        response = await self._stub.IsActive(request)

        

        return response.is_active
        

    async def set_target_location(self, location):
        """
         Set location of the moving target.

         Parameters
         ----------
         location : TargetLocation
              The new TargetLocation to follow

         Raises
         ------
         FollowMeError
             If the request fails. The error contains the reason for the failure.
        """

        request = follow_me_pb2.SetTargetLocationRequest()
        
        location.translate_to_rpc(request.location)
                
            
        response = await self._stub.SetTargetLocation(request)

        
        result = self._extract_result(response)

        if result.result != FollowMeResult.Result.SUCCESS:
            raise FollowMeError(result, "set_target_location()", location)
        

    async def get_last_location(self):
        """
         Get the last location of the target.

         Returns
         -------
         location : TargetLocation
              The last target location that was set

         
        """

        request = follow_me_pb2.GetLastLocationRequest()
        response = await self._stub.GetLastLocation(request)

        

        return TargetLocation.translate_from_rpc(response.location)
            

    async def start(self):
        """
         Start FollowMe mode.

         Raises
         ------
         FollowMeError
             If the request fails. The error contains the reason for the failure.
        """

        request = follow_me_pb2.StartRequest()
        response = await self._stub.Start(request)

        
        result = self._extract_result(response)

        if result.result != FollowMeResult.Result.SUCCESS:
            raise FollowMeError(result, "start()")
        

    async def stop(self):
        """
         Stop FollowMe mode.

         Raises
         ------
         FollowMeError
             If the request fails. The error contains the reason for the failure.
        """

        request = follow_me_pb2.StopRequest()
        response = await self._stub.Stop(request)

        
        result = self._extract_result(response)

        if result.result != FollowMeResult.Result.SUCCESS:
            raise FollowMeError(result, "stop()")
        