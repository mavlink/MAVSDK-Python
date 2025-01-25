# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import action_pb2, action_pb2_grpc
from enum import Enum


class OrbitYawBehavior(Enum):
    """
     Yaw behaviour during orbit flight.

     Values
     ------
     HOLD_FRONT_TO_CIRCLE_CENTER
          Vehicle front points to the center (default)

     HOLD_INITIAL_HEADING
          Vehicle front holds heading when message received

     UNCONTROLLED
          Yaw uncontrolled

     HOLD_FRONT_TANGENT_TO_CIRCLE
          Vehicle front follows flight path (tangential to circle)

     RC_CONTROLLED
          Yaw controlled by RC input

     """

    
    HOLD_FRONT_TO_CIRCLE_CENTER = 0
    HOLD_INITIAL_HEADING = 1
    UNCONTROLLED = 2
    HOLD_FRONT_TANGENT_TO_CIRCLE = 3
    RC_CONTROLLED = 4

    def translate_to_rpc(self):
        if self == OrbitYawBehavior.HOLD_FRONT_TO_CIRCLE_CENTER:
            return action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_FRONT_TO_CIRCLE_CENTER
        if self == OrbitYawBehavior.HOLD_INITIAL_HEADING:
            return action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_INITIAL_HEADING
        if self == OrbitYawBehavior.UNCONTROLLED:
            return action_pb2.ORBIT_YAW_BEHAVIOR_UNCONTROLLED
        if self == OrbitYawBehavior.HOLD_FRONT_TANGENT_TO_CIRCLE:
            return action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_FRONT_TANGENT_TO_CIRCLE
        if self == OrbitYawBehavior.RC_CONTROLLED:
            return action_pb2.ORBIT_YAW_BEHAVIOR_RC_CONTROLLED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_FRONT_TO_CIRCLE_CENTER:
            return OrbitYawBehavior.HOLD_FRONT_TO_CIRCLE_CENTER
        if rpc_enum_value == action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_INITIAL_HEADING:
            return OrbitYawBehavior.HOLD_INITIAL_HEADING
        if rpc_enum_value == action_pb2.ORBIT_YAW_BEHAVIOR_UNCONTROLLED:
            return OrbitYawBehavior.UNCONTROLLED
        if rpc_enum_value == action_pb2.ORBIT_YAW_BEHAVIOR_HOLD_FRONT_TANGENT_TO_CIRCLE:
            return OrbitYawBehavior.HOLD_FRONT_TANGENT_TO_CIRCLE
        if rpc_enum_value == action_pb2.ORBIT_YAW_BEHAVIOR_RC_CONTROLLED:
            return OrbitYawBehavior.RC_CONTROLLED

    def __str__(self):
        return self.name


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

         UNSUPPORTED
              Action not supported

         FAILED
              Action failed

         INVALID_ARGUMENT
              Invalid argument

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
        UNSUPPORTED = 12
        FAILED = 13
        INVALID_ARGUMENT = 14

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
            if self == ActionResult.Result.UNSUPPORTED:
                return action_pb2.ActionResult.RESULT_UNSUPPORTED
            if self == ActionResult.Result.FAILED:
                return action_pb2.ActionResult.RESULT_FAILED
            if self == ActionResult.Result.INVALID_ARGUMENT:
                return action_pb2.ActionResult.RESULT_INVALID_ARGUMENT

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
            if rpc_enum_value == action_pb2.ActionResult.RESULT_UNSUPPORTED:
                return ActionResult.Result.UNSUPPORTED
            if rpc_enum_value == action_pb2.ActionResult.RESULT_FAILED:
                return ActionResult.Result.FAILED
            if rpc_enum_value == action_pb2.ActionResult.RESULT_INVALID_ARGUMENT:
                return ActionResult.Result.INVALID_ARGUMENT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ActionResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
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

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "arm()")
        

    async def arm_force(self):
        """
         Send command to force-arm the drone without any checks.

         Attention: this is not to be used for normal flying but only bench tests!

         Arming a drone normally causes motors to spin at idle.
         Before arming take all safety precautions and stand clear of the drone!

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.ArmForceRequest()
        response = await self._stub.ArmForce(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "arm_force()")
        

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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "shutdown()")
        

    async def terminate(self):
        """
         Send command to terminate the drone.

         This will run the terminate routine as configured on the drone (e.g. disarm and open the parachute).

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.TerminateRequest()
        response = await self._stub.Terminate(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "terminate()")
        

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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "goto_location()", latitude_deg, longitude_deg, absolute_altitude_m, yaw_deg)
        

    async def do_orbit(self, radius_m, velocity_ms, yaw_behavior, latitude_deg, longitude_deg, absolute_altitude_m):
        """
         Send command do orbit to the drone.

         This will run the orbit routine with the given parameters.

         Parameters
         ----------
         radius_m : float
              Radius of circle (in meters)

         velocity_ms : float
              Tangential velocity (in m/s)

         yaw_behavior : OrbitYawBehavior
              Yaw behavior of vehicle (ORBIT_YAW_BEHAVIOUR)

         latitude_deg : double
              Center point latitude in degrees. NAN: use current latitude for center

         longitude_deg : double
              Center point longitude in degrees. NAN: use current longitude for center

         absolute_altitude_m : double
              Center point altitude in meters. NAN: use current altitude for center

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.DoOrbitRequest()
        request.radius_m = radius_m
        request.velocity_ms = velocity_ms
        
        request.yaw_behavior = yaw_behavior.translate_to_rpc()
                
            
        request.latitude_deg = latitude_deg
        request.longitude_deg = longitude_deg
        request.absolute_altitude_m = absolute_altitude_m
        response = await self._stub.DoOrbit(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "do_orbit()", radius_m, velocity_ms, yaw_behavior, latitude_deg, longitude_deg, absolute_altitude_m)
        

    async def hold(self):
        """
         Send command to hold position (a.k.a. "Loiter").

         Sends a command to drone to change to Hold flight mode, causing the
         vehicle to stop and maintain its current GPS position and altitude.

         Note: this command is specific to the PX4 Autopilot flight stack as
         it implies a change to a PX4-specific mode.

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.HoldRequest()
        response = await self._stub.Hold(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "hold()")
        

    async def set_actuator(self, index, value):
        """
         Send command to set the value of an actuator.

         Note that the index of the actuator starts at 1 and that the value goes from -1 to 1.

         Parameters
         ----------
         index : int32_t
              Index of actuator (starting with 1)

         value : float
              Value to set the actuator to (normalized from [-1..1])

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.SetActuatorRequest()
        request.index = index
        request.value = value
        response = await self._stub.SetActuator(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_actuator()", index, value)
        

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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_takeoff_altitude()", altitude)
        

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

        if result.result != ActionResult.Result.SUCCESS:
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

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_return_to_launch_altitude()", relative_altitude_m)
        

    async def set_current_speed(self, speed_m_s):
        """
         Set current speed.

         This will set the speed during a mission, reposition, and similar.
         It is ephemeral, so not stored on the drone and does not survive a reboot.

         Parameters
         ----------
         speed_m_s : float
              Speed in meters/second

         Raises
         ------
         ActionError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_pb2.SetCurrentSpeedRequest()
        request.speed_m_s = speed_m_s
        response = await self._stub.SetCurrentSpeed(request)

        
        result = self._extract_result(response)

        if result.result != ActionResult.Result.SUCCESS:
            raise ActionError(result, "set_current_speed()", speed_m_s)
        