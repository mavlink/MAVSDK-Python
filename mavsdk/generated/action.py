# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import action_pb2, action_pb2_grpc
from enum import Enum


class ActionResult:
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
         Possible results returned for action requests.

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

         COMMAND_DENIED_LANDED_STATE_UNKNOWN
              Command refused because landed state is unknown

         COMMAND_DENIED_NOT_LANDED
              Command refused because vehicle not landed

         TIMEOUT
              Request timed out

         VTOL_TRANSITION_SUPPORT_UNKNOWN
              Hybrid/VTOL transition support is unknown

         NO_VTOL_TRANSITION_SUPPORT
              Vehicle does not support hybrid/VTOL transitions

         PARAMETER_ERROR
              Error getting or setting parameter

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        COMMAND_DENIED_LANDED_STATE_UNKNOWN = 6
        COMMAND_DENIED_NOT_LANDED = 7
        TIMEOUT = 8
        VTOL_TRANSITION_SUPPORT_UNKNOWN = 9
        NO_VTOL_TRANSITION_SUPPORT = 10
        PARAMETER_ERROR = 11

        def translate_to_rpc(self):
            if self == ActionResult.Result.UNKNOWN:
                return action_pb2.ActionResult.RESULT_UNKNOWN
            if self == ActionResult.Result.SUCCESS:
                return action_pb2.ActionResult.RESULT_SUCCESS
            if self == ActionResult.Result.NO_SYSTEM:
                return action_pb2.ActionResult.RESULT_NO_SYSTEM
            if self == ActionResult.Result.CONNECTION_ERROR:
                return action_pb2.ActionResult.RESULT_CONNECTION_ERROR
            if self == ActionResult.Result.BUSY:
                return action_pb2.ActionResult.RESULT_BUSY
            if self == ActionResult.Result.COMMAND_DENIED:
                return action_pb2.ActionResult.RESULT_COMMAND_DENIED
            if self == ActionResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return action_pb2.ActionResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if self == ActionResult.Result.COMMAND_DENIED_NOT_LANDED:
                return action_pb2.ActionResult.RESULT_COMMAND_DENIED_NOT_LANDED
            if self == ActionResult.Result.TIMEOUT:
                return action_pb2.ActionResult.RESULT_TIMEOUT
            if self == ActionResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return action_pb2.ActionResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN
            if self == ActionResult.Result.NO_VTOL_TRANSITION_SUPPORT:
                return action_pb2.ActionResult.RESULT_NO_VTOL_TRANSITION_SUPPORT
            if self == ActionResult.Result.PARAMETER_ERROR:
                return action_pb2.ActionResult.RESULT_PARAMETER_ERROR

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == action_pb2.ActionResult.RESULT_UNKNOWN:
                return ActionResult.Result.UNKNOWN
            if rpc_enum_value == action_pb2.ActionResult.RESULT_SUCCESS:
                return ActionResult.Result.SUCCESS
            if rpc_enum_value == action_pb2.ActionResult.RESULT_NO_SYSTEM:
                return ActionResult.Result.NO_SYSTEM
            if rpc_enum_value == action_pb2.ActionResult.RESULT_CONNECTION_ERROR:
                return ActionResult.Result.CONNECTION_ERROR
            if rpc_enum_value == action_pb2.ActionResult.RESULT_BUSY:
                return ActionResult.Result.BUSY
            if rpc_enum_value == action_pb2.ActionResult.RESULT_COMMAND_DENIED:
                return ActionResult.Result.COMMAND_DENIED
            if rpc_enum_value == action_pb2.ActionResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return ActionResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if rpc_enum_value == action_pb2.ActionResult.RESULT_COMMAND_DENIED_NOT_LANDED:
                return ActionResult.Result.COMMAND_DENIED_NOT_LANDED
            if rpc_enum_value == action_pb2.ActionResult.RESULT_TIMEOUT:
                return ActionResult.Result.TIMEOUT
            if rpc_enum_value == action_pb2.ActionResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return ActionResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN
            if rpc_enum_value == action_pb2.ActionResult.RESULT_NO_VTOL_TRANSITION_SUPPORT:
                return ActionResult.Result.NO_VTOL_TRANSITION_SUPPORT
            if rpc_enum_value == action_pb2.ActionResult.RESULT_PARAMETER_ERROR:
                return ActionResult.Result.PARAMETER_ERROR

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ActionResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two ActionResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActionResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ActionResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ActionResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActionResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActionResult(
                
                ActionResult.Result.translate_from_rpc(rpcActionResult.result),
                
                
                rpcActionResult.result_str
                )

    def translate_to_rpc(self, rpcActionResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcActionResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcActionResult.result_str = self.result_str
            
        
        



class ActionError(Exception):
    """ Raised when a ActionResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Action(AsyncBase):
    """
     Enable simple actions such as arming, taking off, and landing.

     Generated by dcsdkgen - MAVSDK Action API
    """

    # Plugin name
    name = "Action"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = action_pb2_grpc.ActionServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ActionResult.translate_from_rpc(response.action_result)
    

    async def arm(self):
        """
         Send command to arm the drone.

         Arming a drone normally causes motors to spin at idle.
         Before arming take all safety precautions and stand clear of the drone!

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.ArmRequest()
        response = await self._stub.Arm(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "arm()")
        

    async def disarm(self):
        """
         Send command to disarm the drone.

         This will disarm a drone that considers itself landed. If flying, the drone should
         reject the disarm command. Disarming means that all motors will stop.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.DisarmRequest()
        response = await self._stub.Disarm(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "disarm()")
        

    async def takeoff(self):
        """
         Send command to take off and hover.

         This switches the drone into position control mode and commands
         it to take off and hover at the takeoff altitude.

         Note that the vehicle must be armed before it can take off.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.TakeoffRequest()
        response = await self._stub.Takeoff(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "takeoff()")
        

    async def land(self):
        """
         Send command to land at the current position.

         This switches the drone to 'Land' flight mode.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.LandRequest()
        response = await self._stub.Land(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "land()")
        

    async def reboot(self):
        """
         Send command to reboot the drone components.

         This will reboot the autopilot, companion computer, camera and gimbal.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.RebootRequest()
        response = await self._stub.Reboot(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "reboot()")
        

    async def shutdown(self):
        """
         Send command to shut down the drone components.

         This will shut down the autopilot, onboard computer, camera and gimbal.
         This command should only be used when the autopilot is disarmed and autopilots commonly
         reject it if they are not already ready to shut down.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.ShutdownRequest()
        response = await self._stub.Shutdown(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "shutdown()")
        

    async def kill(self):
        """
         Send command to kill the drone.

         This will disarm a drone irrespective of whether it is landed or flying.
         Note that the drone will fall out of the sky if this command is used while flying.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.KillRequest()
        response = await self._stub.Kill(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "kill()")
        

    async def return_to_launch(self):
        """
         Send command to return to the launch (takeoff) position and land.

         This switches the drone into [Return mode](https://docs.px4.io/master/en/flight_modes/return.html) which
         generally means it will rise up to a certain altitude to clear any obstacles before heading
         back to the launch (takeoff) position and land there.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.ReturnToLaunchRequest()
        response = await self._stub.ReturnToLaunch(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "return_to_launch()")
        

    async def goto_location(self, latitude_deg, longitude_deg, absolute_altitude_m, yaw_deg):
        """
         Send command to move the vehicle to a specific global position.

         The latitude and longitude are given in degrees (WGS84 frame) and the altitude
         in meters AMSL (above mean sea level).

         The yaw angle is in degrees (frame is NED, 0 is North, positive is clockwise).

         Parameters
         ----------
         latitude_deg : double
              Latitude (in degrees)

         longitude_deg : double
              Longitude (in degrees)

         absolute_altitude_m : float
              Altitude AMSL (in meters)

         yaw_deg : float
              Yaw angle (in degrees, frame is NED, 0 is North, positive is clockwise)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.GotoLocationRequest()
        request.latitude_deg = latitude_deg
        request.longitude_deg = longitude_deg
        request.absolute_altitude_m = absolute_altitude_m
        request.yaw_deg = yaw_deg
        response = await self._stub.GotoLocation(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "goto_location()", latitude_deg, longitude_deg, absolute_altitude_m, yaw_deg)
        

    async def transition_to_fixedwing(self):
        """
         Send command to transition the drone to fixedwing.

         The associated action will only be executed for VTOL vehicles (on other vehicle types the
         command will fail). The command will succeed if called when the vehicle
         is already in fixedwing mode.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.TransitionToFixedwingRequest()
        response = await self._stub.TransitionToFixedwing(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "transition_to_fixedwing()")
        

    async def transition_to_multicopter(self):
        """
         Send command to transition the drone to multicopter.

         The associated action will only be executed for VTOL vehicles (on other vehicle types the
         command will fail). The command will succeed if called when the vehicle
         is already in multicopter mode.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.TransitionToMulticopterRequest()
        response = await self._stub.TransitionToMulticopter(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "transition_to_multicopter()")
        

    async def get_takeoff_altitude(self):
        """
         Get the takeoff altitude (in meters above ground).

         Returns
         -------
         altitude : float
              Takeoff altitude relative to ground/takeoff location (in meters)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.GetTakeoffAltitudeRequest()
        response = await self._stub.GetTakeoffAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_takeoff_altitude()")
        

        return response.altitude
        

    async def set_takeoff_altitude(self, altitude):
        """
         Set takeoff altitude (in meters above ground).

         Parameters
         ----------
         altitude : float
              Takeoff altitude relative to ground/takeoff location (in meters)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.SetTakeoffAltitudeRequest()
        request.altitude = altitude
        response = await self._stub.SetTakeoffAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_takeoff_altitude()", altitude)
        

    async def get_maximum_speed(self):
        """
         Get the vehicle maximum speed (in metres/second).

         Returns
         -------
         speed : float
              Maximum speed (in metres/second)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.GetMaximumSpeedRequest()
        response = await self._stub.GetMaximumSpeed(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_maximum_speed()")
        

        return response.speed
        

    async def set_maximum_speed(self, speed):
        """
         Set vehicle maximum speed (in metres/second).

         Parameters
         ----------
         speed : float
              Maximum speed (in metres/second)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.SetMaximumSpeedRequest()
        request.speed = speed
        response = await self._stub.SetMaximumSpeed(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_maximum_speed()", speed)
        

    async def get_return_to_launch_altitude(self):
        """
         Get the return to launch minimum return altitude (in meters).

         Returns
         -------
         relative_altitude_m : float
              Return altitude relative to takeoff location (in meters)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.GetReturnToLaunchAltitudeRequest()
        response = await self._stub.GetReturnToLaunchAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "get_return_to_launch_altitude()")
        

        return response.relative_altitude_m
        

    async def set_return_to_launch_altitude(self, relative_altitude_m):
        """
         Set the return to launch minimum return altitude (in meters).

         Parameters
         ----------
         relative_altitude_m : float
              Return altitude relative to takeoff location (in meters)

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.SetReturnToLaunchAltitudeRequest()
        request.relative_altitude_m = relative_altitude_m
        response = await self._stub.SetReturnToLaunchAltitude(request)

        
        result = self._extract_result(response)

        if result.result is not ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_return_to_launch_altitude()", relative_altitude_m)
        