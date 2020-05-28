# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import offboard_pb2, offboard_pb2_grpc
from enum import Enum


class Attitude:
    """
     Type for attitude body angles in NED reference frame (roll, pitch, yaw and thrust)

     Parameters
     ----------
     roll_deg : float
          Roll angle (in degrees, positive is right side down)

     pitch_deg : float
          Pitch angle (in degrees, positive is nose up)

     yaw_deg : float
          Yaw angle (in degrees, positive is move nose to the right)

     thrust_value : float
          Thrust (range: 0 to 1)

     """

    

    def __init__(
            self,
            roll_deg,
            pitch_deg,
            yaw_deg,
            thrust_value):
        """ Initializes the Attitude object """
        self.roll_deg = roll_deg
        self.pitch_deg = pitch_deg
        self.yaw_deg = yaw_deg
        self.thrust_value = thrust_value

    def __equals__(self, to_compare):
        """ Checks if two Attitude are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Attitude object
            return \
                (self.roll_deg == to_compare.roll_deg) and \
                (self.pitch_deg == to_compare.pitch_deg) and \
                (self.yaw_deg == to_compare.yaw_deg) and \
                (self.thrust_value == to_compare.thrust_value)

        except AttributeError:
            return False

    def __str__(self):
        """ Attitude in string representation """
        struct_repr = ", ".join([
                "roll_deg: " + str(self.roll_deg),
                "pitch_deg: " + str(self.pitch_deg),
                "yaw_deg: " + str(self.yaw_deg),
                "thrust_value: " + str(self.thrust_value)
                ])

        return f"Attitude: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAttitude):
        """ Translates a gRPC struct to the SDK equivalent """
        return Attitude(
                
                rpcAttitude.roll_deg,
                
                
                rpcAttitude.pitch_deg,
                
                
                rpcAttitude.yaw_deg,
                
                
                rpcAttitude.thrust_value
                )

    def translate_to_rpc(self, rpcAttitude):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAttitude.roll_deg = self.roll_deg
            
        
        
        
            
        rpcAttitude.pitch_deg = self.pitch_deg
            
        
        
        
            
        rpcAttitude.yaw_deg = self.yaw_deg
            
        
        
        
            
        rpcAttitude.thrust_value = self.thrust_value
            
        
        


class ActuatorControlGroup:
    """
     Eight controls that will be given to the group. Each control is a normalized
     (-1..+1) command value, which will be mapped and scaled through the mixer.

     Parameters
     ----------
     controls : [float]
          Controls in the group

     """

    

    def __init__(
            self,
            controls):
        """ Initializes the ActuatorControlGroup object """
        self.controls = controls

    def __equals__(self, to_compare):
        """ Checks if two ActuatorControlGroup are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActuatorControlGroup object
            return \
                (self.controls == to_compare.controls)

        except AttributeError:
            return False

    def __str__(self):
        """ ActuatorControlGroup in string representation """
        struct_repr = ", ".join([
                "controls: " + str(self.controls)
                ])

        return f"ActuatorControlGroup: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActuatorControlGroup):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActuatorControlGroup(
                
                rpcActuatorControlGroup.controls
                )

    def translate_to_rpc(self, rpcActuatorControlGroup):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        for elem in self.controls:
          rpcActuatorControlGroup.controls.append(elem)
            
        
        


class ActuatorControl:
    """
     Type for actuator control.

     Control members should be normed to -1..+1 where 0 is neutral position.
     Throttle for single rotation direction motors is 0..1, negative range for reverse direction.

     One group support eight controls.

     Up to 16 actuator controls can be set. To ignore an output group, set all it conrols to NaN.
     If one or more controls in group is not NaN, then all NaN controls will sent as zero.
     The first 8 actuator controls internally map to control group 0, the latter 8 actuator
     controls map to control group 1. Depending on what controls are set (instead of NaN) 1 or 2
     MAVLink messages are actually sent.

     In PX4 v1.9.0 Only first four Control Groups are supported
     (https://github.com/PX4/Firmware/blob/v1.9.0/src/modules/mavlink/mavlink_receiver.cpp#L980).

     Parameters
     ----------
     groups : [ActuatorControlGroup]
          Control groups.

     """

    

    def __init__(
            self,
            groups):
        """ Initializes the ActuatorControl object """
        self.groups = groups

    def __equals__(self, to_compare):
        """ Checks if two ActuatorControl are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActuatorControl object
            return \
                (self.groups == to_compare.groups)

        except AttributeError:
            return False

    def __str__(self):
        """ ActuatorControl in string representation """
        struct_repr = ", ".join([
                "groups: " + str(self.groups)
                ])

        return f"ActuatorControl: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActuatorControl):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActuatorControl(
                
                ActuatorControlGroup.translate_from_rpc(rpcActuatorControl.groups)
                )

    def translate_to_rpc(self, rpcActuatorControl):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.groups:
            rpc_elem = offboard_pb2.ActuatorControlGroup()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        rpcActuatorControl.groups.extend(rpc_elems_list)
            
        
        


class AttitudeRate:
    """
     Type for attitude rate commands in body coordinates (roll, pitch, yaw angular rate and thrust)

     Parameters
     ----------
     roll_deg_s : float
          Roll angular rate (in degrees/second, positive for clock-wise looking from front)

     pitch_deg_s : float
          Pitch angular rate (in degrees/second, positive for head/front moving up)

     yaw_deg_s : float
          Yaw angular rate (in degrees/second, positive for clock-wise looking from above)

     thrust_value : float
          Thrust (range: 0 to 1)

     """

    

    def __init__(
            self,
            roll_deg_s,
            pitch_deg_s,
            yaw_deg_s,
            thrust_value):
        """ Initializes the AttitudeRate object """
        self.roll_deg_s = roll_deg_s
        self.pitch_deg_s = pitch_deg_s
        self.yaw_deg_s = yaw_deg_s
        self.thrust_value = thrust_value

    def __equals__(self, to_compare):
        """ Checks if two AttitudeRate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AttitudeRate object
            return \
                (self.roll_deg_s == to_compare.roll_deg_s) and \
                (self.pitch_deg_s == to_compare.pitch_deg_s) and \
                (self.yaw_deg_s == to_compare.yaw_deg_s) and \
                (self.thrust_value == to_compare.thrust_value)

        except AttributeError:
            return False

    def __str__(self):
        """ AttitudeRate in string representation """
        struct_repr = ", ".join([
                "roll_deg_s: " + str(self.roll_deg_s),
                "pitch_deg_s: " + str(self.pitch_deg_s),
                "yaw_deg_s: " + str(self.yaw_deg_s),
                "thrust_value: " + str(self.thrust_value)
                ])

        return f"AttitudeRate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAttitudeRate):
        """ Translates a gRPC struct to the SDK equivalent """
        return AttitudeRate(
                
                rpcAttitudeRate.roll_deg_s,
                
                
                rpcAttitudeRate.pitch_deg_s,
                
                
                rpcAttitudeRate.yaw_deg_s,
                
                
                rpcAttitudeRate.thrust_value
                )

    def translate_to_rpc(self, rpcAttitudeRate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAttitudeRate.roll_deg_s = self.roll_deg_s
            
        
        
        
            
        rpcAttitudeRate.pitch_deg_s = self.pitch_deg_s
            
        
        
        
            
        rpcAttitudeRate.yaw_deg_s = self.yaw_deg_s
            
        
        
        
            
        rpcAttitudeRate.thrust_value = self.thrust_value
            
        
        


class PositionNedYaw:
    """
     Type for position commands in NED (North East Down) coordinates and yaw.

     Parameters
     ----------
     north_m : float
          Position North (in metres)

     east_m : float
          Position East (in metres)

     down_m : float
          Position Down (in metres)

     yaw_deg : float
          Yaw in degrees (0 North, positive is clock-wise looking from above)

     """

    

    def __init__(
            self,
            north_m,
            east_m,
            down_m,
            yaw_deg):
        """ Initializes the PositionNedYaw object """
        self.north_m = north_m
        self.east_m = east_m
        self.down_m = down_m
        self.yaw_deg = yaw_deg

    def __equals__(self, to_compare):
        """ Checks if two PositionNedYaw are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionNedYaw object
            return \
                (self.north_m == to_compare.north_m) and \
                (self.east_m == to_compare.east_m) and \
                (self.down_m == to_compare.down_m) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionNedYaw in string representation """
        struct_repr = ", ".join([
                "north_m: " + str(self.north_m),
                "east_m: " + str(self.east_m),
                "down_m: " + str(self.down_m),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"PositionNedYaw: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionNedYaw):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionNedYaw(
                
                rpcPositionNedYaw.north_m,
                
                
                rpcPositionNedYaw.east_m,
                
                
                rpcPositionNedYaw.down_m,
                
                
                rpcPositionNedYaw.yaw_deg
                )

    def translate_to_rpc(self, rpcPositionNedYaw):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPositionNedYaw.north_m = self.north_m
            
        
        
        
            
        rpcPositionNedYaw.east_m = self.east_m
            
        
        
        
            
        rpcPositionNedYaw.down_m = self.down_m
            
        
        
        
            
        rpcPositionNedYaw.yaw_deg = self.yaw_deg
            
        
        


class VelocityBodyYawspeed:
    """
     Type for velocity commands in body coordinates.

     Parameters
     ----------
     forward_m_s : float
          Velocity forward (in metres/second)

     right_m_s : float
          Velocity right (in metres/second)

     down_m_s : float
          Velocity down (in metres/second)

     yawspeed_deg_s : float
          Yaw angular rate (in degrees/second, positive for clock-wise looking from above)

     """

    

    def __init__(
            self,
            forward_m_s,
            right_m_s,
            down_m_s,
            yawspeed_deg_s):
        """ Initializes the VelocityBodyYawspeed object """
        self.forward_m_s = forward_m_s
        self.right_m_s = right_m_s
        self.down_m_s = down_m_s
        self.yawspeed_deg_s = yawspeed_deg_s

    def __equals__(self, to_compare):
        """ Checks if two VelocityBodyYawspeed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityBodyYawspeed object
            return \
                (self.forward_m_s == to_compare.forward_m_s) and \
                (self.right_m_s == to_compare.right_m_s) and \
                (self.down_m_s == to_compare.down_m_s) and \
                (self.yawspeed_deg_s == to_compare.yawspeed_deg_s)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityBodyYawspeed in string representation """
        struct_repr = ", ".join([
                "forward_m_s: " + str(self.forward_m_s),
                "right_m_s: " + str(self.right_m_s),
                "down_m_s: " + str(self.down_m_s),
                "yawspeed_deg_s: " + str(self.yawspeed_deg_s)
                ])

        return f"VelocityBodyYawspeed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityBodyYawspeed):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityBodyYawspeed(
                
                rpcVelocityBodyYawspeed.forward_m_s,
                
                
                rpcVelocityBodyYawspeed.right_m_s,
                
                
                rpcVelocityBodyYawspeed.down_m_s,
                
                
                rpcVelocityBodyYawspeed.yawspeed_deg_s
                )

    def translate_to_rpc(self, rpcVelocityBodyYawspeed):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityBodyYawspeed.forward_m_s = self.forward_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.right_m_s = self.right_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.down_m_s = self.down_m_s
            
        
        
        
            
        rpcVelocityBodyYawspeed.yawspeed_deg_s = self.yawspeed_deg_s
            
        
        


class VelocityNedYaw:
    """
     Type for velocity commands in NED (North East Down) coordinates and yaw.

     Parameters
     ----------
     north_m_s : float
          Velocity North (in metres/second)

     east_m_s : float
          Velocity East (in metres/second)

     down_m_s : float
          Velocity Down (in metres/second)

     yaw_deg : float
          Yaw in degrees (0 North, positive is clock-wise looking from above)

     """

    

    def __init__(
            self,
            north_m_s,
            east_m_s,
            down_m_s,
            yaw_deg):
        """ Initializes the VelocityNedYaw object """
        self.north_m_s = north_m_s
        self.east_m_s = east_m_s
        self.down_m_s = down_m_s
        self.yaw_deg = yaw_deg

    def __equals__(self, to_compare):
        """ Checks if two VelocityNedYaw are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityNedYaw object
            return \
                (self.north_m_s == to_compare.north_m_s) and \
                (self.east_m_s == to_compare.east_m_s) and \
                (self.down_m_s == to_compare.down_m_s) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityNedYaw in string representation """
        struct_repr = ", ".join([
                "north_m_s: " + str(self.north_m_s),
                "east_m_s: " + str(self.east_m_s),
                "down_m_s: " + str(self.down_m_s),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"VelocityNedYaw: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityNedYaw):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityNedYaw(
                
                rpcVelocityNedYaw.north_m_s,
                
                
                rpcVelocityNedYaw.east_m_s,
                
                
                rpcVelocityNedYaw.down_m_s,
                
                
                rpcVelocityNedYaw.yaw_deg
                )

    def translate_to_rpc(self, rpcVelocityNedYaw):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityNedYaw.north_m_s = self.north_m_s
            
        
        
        
            
        rpcVelocityNedYaw.east_m_s = self.east_m_s
            
        
        
        
            
        rpcVelocityNedYaw.down_m_s = self.down_m_s
            
        
        
        
            
        rpcVelocityNedYaw.yaw_deg = self.yaw_deg
            
        
        


class OffboardResult:
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
         Possible results returned for offboard requests

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

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command denied

         TIMEOUT
              Request timed out

         NO_SETPOINT_SET
              Cannot start without setpoint set

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        NO_SETPOINT_SET = 7

        def translate_to_rpc(self):
            if self == OffboardResult.Result.UNKNOWN:
                return offboard_pb2.OffboardResult.RESULT_UNKNOWN
            if self == OffboardResult.Result.SUCCESS:
                return offboard_pb2.OffboardResult.RESULT_SUCCESS
            if self == OffboardResult.Result.NO_SYSTEM:
                return offboard_pb2.OffboardResult.RESULT_NO_SYSTEM
            if self == OffboardResult.Result.CONNECTION_ERROR:
                return offboard_pb2.OffboardResult.RESULT_CONNECTION_ERROR
            if self == OffboardResult.Result.BUSY:
                return offboard_pb2.OffboardResult.RESULT_BUSY
            if self == OffboardResult.Result.COMMAND_DENIED:
                return offboard_pb2.OffboardResult.RESULT_COMMAND_DENIED
            if self == OffboardResult.Result.TIMEOUT:
                return offboard_pb2.OffboardResult.RESULT_TIMEOUT
            if self == OffboardResult.Result.NO_SETPOINT_SET:
                return offboard_pb2.OffboardResult.RESULT_NO_SETPOINT_SET

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_UNKNOWN:
                return OffboardResult.Result.UNKNOWN
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_SUCCESS:
                return OffboardResult.Result.SUCCESS
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_NO_SYSTEM:
                return OffboardResult.Result.NO_SYSTEM
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_CONNECTION_ERROR:
                return OffboardResult.Result.CONNECTION_ERROR
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_BUSY:
                return OffboardResult.Result.BUSY
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_COMMAND_DENIED:
                return OffboardResult.Result.COMMAND_DENIED
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_TIMEOUT:
                return OffboardResult.Result.TIMEOUT
            if rpc_enum_value == offboard_pb2.OffboardResult.RESULT_NO_SETPOINT_SET:
                return OffboardResult.Result.NO_SETPOINT_SET

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the OffboardResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two OffboardResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # OffboardResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ OffboardResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"OffboardResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcOffboardResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return OffboardResult(
                
                OffboardResult.Result.translate_from_rpc(rpcOffboardResult.result),
                
                
                rpcOffboardResult.result_str
                )

    def translate_to_rpc(self, rpcOffboardResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcOffboardResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcOffboardResult.result_str = self.result_str
            
        
        



class OffboardError(Exception):
    """ Raised when a OffboardResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Offboard(AsyncBase):
    """
     *
     Control a drone with position, velocity, attitude or motor commands.

     The module is called offboard because the commands can be sent from external sources
     as opposed to onboard control right inside the autopilot "board".

     Client code must specify a setpoint before starting offboard mode.
     Mavsdk automatically sends setpoints at 20Hz (PX4 Offboard mode requires that setpoints
     are minimally sent at 2Hz).

     Generated by dcsdkgen - MAVSDK Offboard API
    """

    # Plugin name
    name = "Offboard"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = offboard_pb2_grpc.OffboardServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return OffboardResult.translate_from_rpc(response.offboard_result)
    

    async def start(self):
        """
         Start offboard control.

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.StartRequest()
        response = await self._stub.Start(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "start()")
        

    async def stop(self):
        """
         Stop offboard control.

         The vehicle will be put into Hold mode: https://docs.px4.io/en/flight_modes/hold.html

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.StopRequest()
        response = await self._stub.Stop(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "stop()")
        

    async def is_active(self):
        """
         Check if offboard control is active.

         True means that the vehicle is in offboard mode and we are actively sending
         setpoints.

         Returns
         -------
         is_active : bool
              True if offboard is active

         
        """

        request = offboard_pb2.IsActiveRequest()
        response = await self._stub.IsActive(request)

        

        return response.is_active
        

    async def set_attitude(self, attitude):
        """
         Set the attitude in terms of roll, pitch and yaw in degrees with thrust.

         Parameters
         ----------
         attitude : Attitude
              Attitude roll, pitch and yaw along with thrust

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetAttitudeRequest()
        
        attitude.translate_to_rpc(request.attitude)
                
            
        response = await self._stub.SetAttitude(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_attitude()", attitude)
        

    async def set_actuator_control(self, actuator_control):
        """
         Set direct actuator control values to groups #0 and #1.

         First 8 controls will go to control group 0, the following 8 controls to control group 1 (if
         actuator_control.num_controls more than 8).

         Parameters
         ----------
         actuator_control : ActuatorControl
              Actuator control values

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetActuatorControlRequest()
        
        actuator_control.translate_to_rpc(request.actuator_control)
                
            
        response = await self._stub.SetActuatorControl(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_actuator_control()", actuator_control)
        

    async def set_attitude_rate(self, attitude_rate):
        """
         Set the attitude rate in terms of pitch, roll and yaw angular rate along with thrust.

         Parameters
         ----------
         attitude_rate : AttitudeRate
              Attitude rate roll, pitch and yaw angular rate along with thrust

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetAttitudeRateRequest()
        
        attitude_rate.translate_to_rpc(request.attitude_rate)
                
            
        response = await self._stub.SetAttitudeRate(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_attitude_rate()", attitude_rate)
        

    async def set_position_ned(self, position_ned_yaw):
        """
         Set the position in NED coordinates and yaw.

         Parameters
         ----------
         position_ned_yaw : PositionNedYaw
              Position and yaw

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetPositionNedRequest()
        
        position_ned_yaw.translate_to_rpc(request.position_ned_yaw)
                
            
        response = await self._stub.SetPositionNed(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_position_ned()", position_ned_yaw)
        

    async def set_velocity_body(self, velocity_body_yawspeed):
        """
         Set the velocity in body coordinates and yaw angular rate.

         Parameters
         ----------
         velocity_body_yawspeed : VelocityBodyYawspeed
              Velocity and yaw angular rate

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetVelocityBodyRequest()
        
        velocity_body_yawspeed.translate_to_rpc(request.velocity_body_yawspeed)
                
            
        response = await self._stub.SetVelocityBody(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_velocity_body()", velocity_body_yawspeed)
        

    async def set_velocity_ned(self, velocity_ned_yaw):
        """
         Set the velocity in NED coordinates and yaw.

         Parameters
         ----------
         velocity_ned_yaw : VelocityNedYaw
              Velocity and yaw

         Raises
         ------
         OffboardError
             If the request fails. The error contains the reason for the failure.
        """

        request = offboard_pb2.SetVelocityNedRequest()
        
        velocity_ned_yaw.translate_to_rpc(request.velocity_ned_yaw)
                
            
        response = await self._stub.SetVelocityNed(request)

        
        result = self._extract_result(response)

        if result.result is not OffboardResult.Result.SUCCESS:
            raise OffboardError(result, "set_velocity_ned()", velocity_ned_yaw)
        