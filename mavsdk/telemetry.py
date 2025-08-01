# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import telemetry_pb2, telemetry_pb2_grpc
from enum import Enum


class FixType(Enum):
    """
     GPS fix type.

     Values
     ------
     NO_GPS
          No GPS connected

     NO_FIX
          No position information, GPS is connected

     FIX_2D
          2D position

     FIX_3D
          3D position

     FIX_DGPS
          DGPS/SBAS aided 3D position

     RTK_FLOAT
          RTK float, 3D position

     RTK_FIXED
          RTK Fixed, 3D position

     """

    
    NO_GPS = 0
    NO_FIX = 1
    FIX_2D = 2
    FIX_3D = 3
    FIX_DGPS = 4
    RTK_FLOAT = 5
    RTK_FIXED = 6

    def translate_to_rpc(self):
        if self == FixType.NO_GPS:
            return telemetry_pb2.FIX_TYPE_NO_GPS
        if self == FixType.NO_FIX:
            return telemetry_pb2.FIX_TYPE_NO_FIX
        if self == FixType.FIX_2D:
            return telemetry_pb2.FIX_TYPE_FIX_2D
        if self == FixType.FIX_3D:
            return telemetry_pb2.FIX_TYPE_FIX_3D
        if self == FixType.FIX_DGPS:
            return telemetry_pb2.FIX_TYPE_FIX_DGPS
        if self == FixType.RTK_FLOAT:
            return telemetry_pb2.FIX_TYPE_RTK_FLOAT
        if self == FixType.RTK_FIXED:
            return telemetry_pb2.FIX_TYPE_RTK_FIXED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_NO_GPS:
            return FixType.NO_GPS
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_NO_FIX:
            return FixType.NO_FIX
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_FIX_2D:
            return FixType.FIX_2D
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_FIX_3D:
            return FixType.FIX_3D
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_FIX_DGPS:
            return FixType.FIX_DGPS
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_RTK_FLOAT:
            return FixType.RTK_FLOAT
        if rpc_enum_value == telemetry_pb2.FIX_TYPE_RTK_FIXED:
            return FixType.RTK_FIXED

    def __str__(self):
        return self.name


class BatteryFunction(Enum):
    """
     Battery function type.

     Values
     ------
     UNKNOWN
          Battery function is unknown

     ALL
          Battery supports all flight systems

     PROPULSION
          Battery for the propulsion system

     AVIONICS
          Avionics battery

     PAYLOAD
          Payload battery

     """

    
    UNKNOWN = 0
    ALL = 1
    PROPULSION = 2
    AVIONICS = 3
    PAYLOAD = 4

    def translate_to_rpc(self):
        if self == BatteryFunction.UNKNOWN:
            return telemetry_pb2.BATTERY_FUNCTION_UNKNOWN
        if self == BatteryFunction.ALL:
            return telemetry_pb2.BATTERY_FUNCTION_ALL
        if self == BatteryFunction.PROPULSION:
            return telemetry_pb2.BATTERY_FUNCTION_PROPULSION
        if self == BatteryFunction.AVIONICS:
            return telemetry_pb2.BATTERY_FUNCTION_AVIONICS
        if self == BatteryFunction.PAYLOAD:
            return telemetry_pb2.BATTERY_FUNCTION_PAYLOAD

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.BATTERY_FUNCTION_UNKNOWN:
            return BatteryFunction.UNKNOWN
        if rpc_enum_value == telemetry_pb2.BATTERY_FUNCTION_ALL:
            return BatteryFunction.ALL
        if rpc_enum_value == telemetry_pb2.BATTERY_FUNCTION_PROPULSION:
            return BatteryFunction.PROPULSION
        if rpc_enum_value == telemetry_pb2.BATTERY_FUNCTION_AVIONICS:
            return BatteryFunction.AVIONICS
        if rpc_enum_value == telemetry_pb2.BATTERY_FUNCTION_PAYLOAD:
            return BatteryFunction.PAYLOAD

    def __str__(self):
        return self.name


class FlightMode(Enum):
    """
     Flight modes.

     For more information about flight modes, check out
     https://docs.px4.io/master/en/config/flight_mode.html.

     Values
     ------
     UNKNOWN
          Mode not known

     READY
          Armed and ready to take off

     TAKEOFF
          Taking off

     HOLD
          Holding (hovering in place (or circling for fixed-wing vehicles)

     MISSION
          In mission

     RETURN_TO_LAUNCH
          Returning to launch position (then landing)

     LAND
          Landing

     OFFBOARD
          In 'offboard' mode

     FOLLOW_ME
          In 'follow-me' mode

     MANUAL
          In 'Manual' mode

     ALTCTL
          In 'Altitude Control' mode

     POSCTL
          In 'Position Control' mode

     ACRO
          In 'Acro' mode

     STABILIZED
          In 'Stabilize' mode

     RATTITUDE
          In 'Rattitude' mode

     """

    
    UNKNOWN = 0
    READY = 1
    TAKEOFF = 2
    HOLD = 3
    MISSION = 4
    RETURN_TO_LAUNCH = 5
    LAND = 6
    OFFBOARD = 7
    FOLLOW_ME = 8
    MANUAL = 9
    ALTCTL = 10
    POSCTL = 11
    ACRO = 12
    STABILIZED = 13
    RATTITUDE = 14

    def translate_to_rpc(self):
        if self == FlightMode.UNKNOWN:
            return telemetry_pb2.FLIGHT_MODE_UNKNOWN
        if self == FlightMode.READY:
            return telemetry_pb2.FLIGHT_MODE_READY
        if self == FlightMode.TAKEOFF:
            return telemetry_pb2.FLIGHT_MODE_TAKEOFF
        if self == FlightMode.HOLD:
            return telemetry_pb2.FLIGHT_MODE_HOLD
        if self == FlightMode.MISSION:
            return telemetry_pb2.FLIGHT_MODE_MISSION
        if self == FlightMode.RETURN_TO_LAUNCH:
            return telemetry_pb2.FLIGHT_MODE_RETURN_TO_LAUNCH
        if self == FlightMode.LAND:
            return telemetry_pb2.FLIGHT_MODE_LAND
        if self == FlightMode.OFFBOARD:
            return telemetry_pb2.FLIGHT_MODE_OFFBOARD
        if self == FlightMode.FOLLOW_ME:
            return telemetry_pb2.FLIGHT_MODE_FOLLOW_ME
        if self == FlightMode.MANUAL:
            return telemetry_pb2.FLIGHT_MODE_MANUAL
        if self == FlightMode.ALTCTL:
            return telemetry_pb2.FLIGHT_MODE_ALTCTL
        if self == FlightMode.POSCTL:
            return telemetry_pb2.FLIGHT_MODE_POSCTL
        if self == FlightMode.ACRO:
            return telemetry_pb2.FLIGHT_MODE_ACRO
        if self == FlightMode.STABILIZED:
            return telemetry_pb2.FLIGHT_MODE_STABILIZED
        if self == FlightMode.RATTITUDE:
            return telemetry_pb2.FLIGHT_MODE_RATTITUDE

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_UNKNOWN:
            return FlightMode.UNKNOWN
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_READY:
            return FlightMode.READY
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_TAKEOFF:
            return FlightMode.TAKEOFF
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_HOLD:
            return FlightMode.HOLD
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_MISSION:
            return FlightMode.MISSION
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_RETURN_TO_LAUNCH:
            return FlightMode.RETURN_TO_LAUNCH
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_LAND:
            return FlightMode.LAND
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_OFFBOARD:
            return FlightMode.OFFBOARD
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_FOLLOW_ME:
            return FlightMode.FOLLOW_ME
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_MANUAL:
            return FlightMode.MANUAL
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_ALTCTL:
            return FlightMode.ALTCTL
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_POSCTL:
            return FlightMode.POSCTL
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_ACRO:
            return FlightMode.ACRO
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_STABILIZED:
            return FlightMode.STABILIZED
        if rpc_enum_value == telemetry_pb2.FLIGHT_MODE_RATTITUDE:
            return FlightMode.RATTITUDE

    def __str__(self):
        return self.name


class StatusTextType(Enum):
    """
     Status types.

     Values
     ------
     DEBUG
          Debug

     INFO
          Information

     NOTICE
          Notice

     WARNING
          Warning

     ERROR
          Error

     CRITICAL
          Critical

     ALERT
          Alert

     EMERGENCY
          Emergency

     """

    
    DEBUG = 0
    INFO = 1
    NOTICE = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    ALERT = 6
    EMERGENCY = 7

    def translate_to_rpc(self):
        if self == StatusTextType.DEBUG:
            return telemetry_pb2.STATUS_TEXT_TYPE_DEBUG
        if self == StatusTextType.INFO:
            return telemetry_pb2.STATUS_TEXT_TYPE_INFO
        if self == StatusTextType.NOTICE:
            return telemetry_pb2.STATUS_TEXT_TYPE_NOTICE
        if self == StatusTextType.WARNING:
            return telemetry_pb2.STATUS_TEXT_TYPE_WARNING
        if self == StatusTextType.ERROR:
            return telemetry_pb2.STATUS_TEXT_TYPE_ERROR
        if self == StatusTextType.CRITICAL:
            return telemetry_pb2.STATUS_TEXT_TYPE_CRITICAL
        if self == StatusTextType.ALERT:
            return telemetry_pb2.STATUS_TEXT_TYPE_ALERT
        if self == StatusTextType.EMERGENCY:
            return telemetry_pb2.STATUS_TEXT_TYPE_EMERGENCY

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_DEBUG:
            return StatusTextType.DEBUG
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_INFO:
            return StatusTextType.INFO
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_NOTICE:
            return StatusTextType.NOTICE
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_WARNING:
            return StatusTextType.WARNING
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_ERROR:
            return StatusTextType.ERROR
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_CRITICAL:
            return StatusTextType.CRITICAL
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_ALERT:
            return StatusTextType.ALERT
        if rpc_enum_value == telemetry_pb2.STATUS_TEXT_TYPE_EMERGENCY:
            return StatusTextType.EMERGENCY

    def __str__(self):
        return self.name


class LandedState(Enum):
    """
     Landed State enumeration.

     Values
     ------
     UNKNOWN
          Landed state is unknown

     ON_GROUND
          The vehicle is on the ground

     IN_AIR
          The vehicle is in the air

     TAKING_OFF
          The vehicle is taking off

     LANDING
          The vehicle is landing

     """

    
    UNKNOWN = 0
    ON_GROUND = 1
    IN_AIR = 2
    TAKING_OFF = 3
    LANDING = 4

    def translate_to_rpc(self):
        if self == LandedState.UNKNOWN:
            return telemetry_pb2.LANDED_STATE_UNKNOWN
        if self == LandedState.ON_GROUND:
            return telemetry_pb2.LANDED_STATE_ON_GROUND
        if self == LandedState.IN_AIR:
            return telemetry_pb2.LANDED_STATE_IN_AIR
        if self == LandedState.TAKING_OFF:
            return telemetry_pb2.LANDED_STATE_TAKING_OFF
        if self == LandedState.LANDING:
            return telemetry_pb2.LANDED_STATE_LANDING

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.LANDED_STATE_UNKNOWN:
            return LandedState.UNKNOWN
        if rpc_enum_value == telemetry_pb2.LANDED_STATE_ON_GROUND:
            return LandedState.ON_GROUND
        if rpc_enum_value == telemetry_pb2.LANDED_STATE_IN_AIR:
            return LandedState.IN_AIR
        if rpc_enum_value == telemetry_pb2.LANDED_STATE_TAKING_OFF:
            return LandedState.TAKING_OFF
        if rpc_enum_value == telemetry_pb2.LANDED_STATE_LANDING:
            return LandedState.LANDING

    def __str__(self):
        return self.name


class VtolState(Enum):
    """
     VTOL State enumeration

     Values
     ------
     UNDEFINED
          MAV is not configured as VTOL

     TRANSITION_TO_FW
          VTOL is in transition from multicopter to fixed-wing

     TRANSITION_TO_MC
          VTOL is in transition from fixed-wing to multicopter

     MC
          VTOL is in multicopter state

     FW
          VTOL is in fixed-wing state

     """

    
    UNDEFINED = 0
    TRANSITION_TO_FW = 1
    TRANSITION_TO_MC = 2
    MC = 3
    FW = 4

    def translate_to_rpc(self):
        if self == VtolState.UNDEFINED:
            return telemetry_pb2.VTOL_STATE_UNDEFINED
        if self == VtolState.TRANSITION_TO_FW:
            return telemetry_pb2.VTOL_STATE_TRANSITION_TO_FW
        if self == VtolState.TRANSITION_TO_MC:
            return telemetry_pb2.VTOL_STATE_TRANSITION_TO_MC
        if self == VtolState.MC:
            return telemetry_pb2.VTOL_STATE_MC
        if self == VtolState.FW:
            return telemetry_pb2.VTOL_STATE_FW

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_pb2.VTOL_STATE_UNDEFINED:
            return VtolState.UNDEFINED
        if rpc_enum_value == telemetry_pb2.VTOL_STATE_TRANSITION_TO_FW:
            return VtolState.TRANSITION_TO_FW
        if rpc_enum_value == telemetry_pb2.VTOL_STATE_TRANSITION_TO_MC:
            return VtolState.TRANSITION_TO_MC
        if rpc_enum_value == telemetry_pb2.VTOL_STATE_MC:
            return VtolState.MC
        if rpc_enum_value == telemetry_pb2.VTOL_STATE_FW:
            return VtolState.FW

    def __str__(self):
        return self.name


class Position:
    """
     Position type in global coordinates.

     Parameters
     ----------
     latitude_deg : double
          Latitude in degrees (range: -90 to +90)

     longitude_deg : double
          Longitude in degrees (range: -180 to +180)

     absolute_altitude_m : float
          Altitude AMSL (above mean sea level) in metres

     relative_altitude_m : float
          Altitude relative to takeoff altitude in metres

     """

    

    def __init__(
            self,
            latitude_deg,
            longitude_deg,
            absolute_altitude_m,
            relative_altitude_m):
        """ Initializes the Position object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.absolute_altitude_m = absolute_altitude_m
        self.relative_altitude_m = relative_altitude_m

    def __eq__(self, to_compare):
        """ Checks if two Position are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Position object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m) and \
                (self.relative_altitude_m == to_compare.relative_altitude_m)

        except AttributeError:
            return False

    def __str__(self):
        """ Position in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "absolute_altitude_m: " + str(self.absolute_altitude_m),
                "relative_altitude_m: " + str(self.relative_altitude_m)
                ])

        return f"Position: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPosition):
        """ Translates a gRPC struct to the SDK equivalent """
        return Position(
                
                rpcPosition.latitude_deg,
                
                
                rpcPosition.longitude_deg,
                
                
                rpcPosition.absolute_altitude_m,
                
                
                rpcPosition.relative_altitude_m
                )

    def translate_to_rpc(self, rpcPosition):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPosition.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcPosition.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcPosition.absolute_altitude_m = self.absolute_altitude_m
            
        
        
        
            
        rpcPosition.relative_altitude_m = self.relative_altitude_m
            
        
        


class Heading:
    """
     Heading type used for global position

     Parameters
     ----------
     heading_deg : double
          Heading in degrees (range: 0 to +360)

     """

    

    def __init__(
            self,
            heading_deg):
        """ Initializes the Heading object """
        self.heading_deg = heading_deg

    def __eq__(self, to_compare):
        """ Checks if two Heading are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Heading object
            return \
                (self.heading_deg == to_compare.heading_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ Heading in string representation """
        struct_repr = ", ".join([
                "heading_deg: " + str(self.heading_deg)
                ])

        return f"Heading: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHeading):
        """ Translates a gRPC struct to the SDK equivalent """
        return Heading(
                
                rpcHeading.heading_deg
                )

    def translate_to_rpc(self, rpcHeading):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcHeading.heading_deg = self.heading_deg
            
        
        


class Quaternion:
    """
     Quaternion type.

     All rotations and axis systems follow the right-hand rule.
     The Hamilton quaternion product definition is used.
     A zero-rotation quaternion is represented by (1,0,0,0).
     The quaternion could also be written as w + xi + yj + zk.

     For more info see: https://en.wikipedia.org/wiki/Quaternion

     Parameters
     ----------
     w : float
          Quaternion entry 0, also denoted as a

     x : float
          Quaternion entry 1, also denoted as b

     y : float
          Quaternion entry 2, also denoted as c

     z : float
          Quaternion entry 3, also denoted as d

     timestamp_us : uint64_t
          Timestamp in microseconds

     """

    

    def __init__(
            self,
            w,
            x,
            y,
            z,
            timestamp_us):
        """ Initializes the Quaternion object """
        self.w = w
        self.x = x
        self.y = y
        self.z = z
        self.timestamp_us = timestamp_us

    def __eq__(self, to_compare):
        """ Checks if two Quaternion are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Quaternion object
            return \
                (self.w == to_compare.w) and \
                (self.x == to_compare.x) and \
                (self.y == to_compare.y) and \
                (self.z == to_compare.z) and \
                (self.timestamp_us == to_compare.timestamp_us)

        except AttributeError:
            return False

    def __str__(self):
        """ Quaternion in string representation """
        struct_repr = ", ".join([
                "w: " + str(self.w),
                "x: " + str(self.x),
                "y: " + str(self.y),
                "z: " + str(self.z),
                "timestamp_us: " + str(self.timestamp_us)
                ])

        return f"Quaternion: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcQuaternion):
        """ Translates a gRPC struct to the SDK equivalent """
        return Quaternion(
                
                rpcQuaternion.w,
                
                
                rpcQuaternion.x,
                
                
                rpcQuaternion.y,
                
                
                rpcQuaternion.z,
                
                
                rpcQuaternion.timestamp_us
                )

    def translate_to_rpc(self, rpcQuaternion):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcQuaternion.w = self.w
            
        
        
        
            
        rpcQuaternion.x = self.x
            
        
        
        
            
        rpcQuaternion.y = self.y
            
        
        
        
            
        rpcQuaternion.z = self.z
            
        
        
        
            
        rpcQuaternion.timestamp_us = self.timestamp_us
            
        
        


class EulerAngle:
    """
     Euler angle type.

     All rotations and axis systems follow the right-hand rule.
     The Euler angles follow the convention of a 3-2-1 intrinsic Tait-Bryan rotation sequence.

     For more info see https://en.wikipedia.org/wiki/Euler_angles

     Parameters
     ----------
     roll_deg : float
          Roll angle in degrees, positive is banking to the right

     pitch_deg : float
          Pitch angle in degrees, positive is pitching nose up

     yaw_deg : float
          Yaw angle in degrees, positive is clock-wise seen from above

     timestamp_us : uint64_t
          Timestamp in microseconds

     """

    

    def __init__(
            self,
            roll_deg,
            pitch_deg,
            yaw_deg,
            timestamp_us):
        """ Initializes the EulerAngle object """
        self.roll_deg = roll_deg
        self.pitch_deg = pitch_deg
        self.yaw_deg = yaw_deg
        self.timestamp_us = timestamp_us

    def __eq__(self, to_compare):
        """ Checks if two EulerAngle are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # EulerAngle object
            return \
                (self.roll_deg == to_compare.roll_deg) and \
                (self.pitch_deg == to_compare.pitch_deg) and \
                (self.yaw_deg == to_compare.yaw_deg) and \
                (self.timestamp_us == to_compare.timestamp_us)

        except AttributeError:
            return False

    def __str__(self):
        """ EulerAngle in string representation """
        struct_repr = ", ".join([
                "roll_deg: " + str(self.roll_deg),
                "pitch_deg: " + str(self.pitch_deg),
                "yaw_deg: " + str(self.yaw_deg),
                "timestamp_us: " + str(self.timestamp_us)
                ])

        return f"EulerAngle: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcEulerAngle):
        """ Translates a gRPC struct to the SDK equivalent """
        return EulerAngle(
                
                rpcEulerAngle.roll_deg,
                
                
                rpcEulerAngle.pitch_deg,
                
                
                rpcEulerAngle.yaw_deg,
                
                
                rpcEulerAngle.timestamp_us
                )

    def translate_to_rpc(self, rpcEulerAngle):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcEulerAngle.roll_deg = self.roll_deg
            
        
        
        
            
        rpcEulerAngle.pitch_deg = self.pitch_deg
            
        
        
        
            
        rpcEulerAngle.yaw_deg = self.yaw_deg
            
        
        
        
            
        rpcEulerAngle.timestamp_us = self.timestamp_us
            
        
        


class AngularVelocityBody:
    """
     Angular velocity type.

     Parameters
     ----------
     roll_rad_s : float
          Roll angular velocity

     pitch_rad_s : float
          Pitch angular velocity

     yaw_rad_s : float
          Yaw angular velocity

     """

    

    def __init__(
            self,
            roll_rad_s,
            pitch_rad_s,
            yaw_rad_s):
        """ Initializes the AngularVelocityBody object """
        self.roll_rad_s = roll_rad_s
        self.pitch_rad_s = pitch_rad_s
        self.yaw_rad_s = yaw_rad_s

    def __eq__(self, to_compare):
        """ Checks if two AngularVelocityBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AngularVelocityBody object
            return \
                (self.roll_rad_s == to_compare.roll_rad_s) and \
                (self.pitch_rad_s == to_compare.pitch_rad_s) and \
                (self.yaw_rad_s == to_compare.yaw_rad_s)

        except AttributeError:
            return False

    def __str__(self):
        """ AngularVelocityBody in string representation """
        struct_repr = ", ".join([
                "roll_rad_s: " + str(self.roll_rad_s),
                "pitch_rad_s: " + str(self.pitch_rad_s),
                "yaw_rad_s: " + str(self.yaw_rad_s)
                ])

        return f"AngularVelocityBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAngularVelocityBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return AngularVelocityBody(
                
                rpcAngularVelocityBody.roll_rad_s,
                
                
                rpcAngularVelocityBody.pitch_rad_s,
                
                
                rpcAngularVelocityBody.yaw_rad_s
                )

    def translate_to_rpc(self, rpcAngularVelocityBody):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAngularVelocityBody.roll_rad_s = self.roll_rad_s
            
        
        
        
            
        rpcAngularVelocityBody.pitch_rad_s = self.pitch_rad_s
            
        
        
        
            
        rpcAngularVelocityBody.yaw_rad_s = self.yaw_rad_s
            
        
        


class GpsInfo:
    """
     GPS information type.

     Parameters
     ----------
     num_satellites : int32_t
          Number of visible satellites in use

     fix_type : FixType
          Fix type

     """

    

    def __init__(
            self,
            num_satellites,
            fix_type):
        """ Initializes the GpsInfo object """
        self.num_satellites = num_satellites
        self.fix_type = fix_type

    def __eq__(self, to_compare):
        """ Checks if two GpsInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GpsInfo object
            return \
                (self.num_satellites == to_compare.num_satellites) and \
                (self.fix_type == to_compare.fix_type)

        except AttributeError:
            return False

    def __str__(self):
        """ GpsInfo in string representation """
        struct_repr = ", ".join([
                "num_satellites: " + str(self.num_satellites),
                "fix_type: " + str(self.fix_type)
                ])

        return f"GpsInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGpsInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return GpsInfo(
                
                rpcGpsInfo.num_satellites,
                
                
                FixType.translate_from_rpc(rpcGpsInfo.fix_type)
                )

    def translate_to_rpc(self, rpcGpsInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGpsInfo.num_satellites = self.num_satellites
            
        
        
        
            
        rpcGpsInfo.fix_type = self.fix_type.translate_to_rpc()
            
        
        


class RawGps:
    """
     Raw GPS information type.

     Warning: this is an advanced type! If you want the location of the drone, use
     the position instead. This message exposes the raw values of the GNSS sensor.

     Parameters
     ----------
     timestamp_us : uint64_t
          Timestamp in microseconds (UNIX Epoch time or time since system boot, to be inferred)

     latitude_deg : double
          Latitude in degrees (WGS84, EGM96 ellipsoid)

     longitude_deg : double
          Longitude in degrees (WGS84, EGM96 ellipsoid)

     absolute_altitude_m : float
          Altitude AMSL (above mean sea level) in metres

     hdop : float
          GPS HDOP horizontal dilution of position (unitless). If unknown, set to NaN

     vdop : float
          GPS VDOP vertical dilution of position (unitless). If unknown, set to NaN

     velocity_m_s : float
          Ground velocity in metres per second

     cog_deg : float
          Course over ground (NOT heading, but direction of movement) in degrees. If unknown, set to NaN

     altitude_ellipsoid_m : float
          Altitude in metres (above WGS84, EGM96 ellipsoid)

     horizontal_uncertainty_m : float
          Position uncertainty in metres

     vertical_uncertainty_m : float
          Altitude uncertainty in metres

     velocity_uncertainty_m_s : float
          Velocity uncertainty in metres per second

     heading_uncertainty_deg : float
          Heading uncertainty in degrees

     yaw_deg : float
          Yaw in earth frame from north.

     """

    

    def __init__(
            self,
            timestamp_us,
            latitude_deg,
            longitude_deg,
            absolute_altitude_m,
            hdop,
            vdop,
            velocity_m_s,
            cog_deg,
            altitude_ellipsoid_m,
            horizontal_uncertainty_m,
            vertical_uncertainty_m,
            velocity_uncertainty_m_s,
            heading_uncertainty_deg,
            yaw_deg):
        """ Initializes the RawGps object """
        self.timestamp_us = timestamp_us
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.absolute_altitude_m = absolute_altitude_m
        self.hdop = hdop
        self.vdop = vdop
        self.velocity_m_s = velocity_m_s
        self.cog_deg = cog_deg
        self.altitude_ellipsoid_m = altitude_ellipsoid_m
        self.horizontal_uncertainty_m = horizontal_uncertainty_m
        self.vertical_uncertainty_m = vertical_uncertainty_m
        self.velocity_uncertainty_m_s = velocity_uncertainty_m_s
        self.heading_uncertainty_deg = heading_uncertainty_deg
        self.yaw_deg = yaw_deg

    def __eq__(self, to_compare):
        """ Checks if two RawGps are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # RawGps object
            return \
                (self.timestamp_us == to_compare.timestamp_us) and \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m) and \
                (self.hdop == to_compare.hdop) and \
                (self.vdop == to_compare.vdop) and \
                (self.velocity_m_s == to_compare.velocity_m_s) and \
                (self.cog_deg == to_compare.cog_deg) and \
                (self.altitude_ellipsoid_m == to_compare.altitude_ellipsoid_m) and \
                (self.horizontal_uncertainty_m == to_compare.horizontal_uncertainty_m) and \
                (self.vertical_uncertainty_m == to_compare.vertical_uncertainty_m) and \
                (self.velocity_uncertainty_m_s == to_compare.velocity_uncertainty_m_s) and \
                (self.heading_uncertainty_deg == to_compare.heading_uncertainty_deg) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ RawGps in string representation """
        struct_repr = ", ".join([
                "timestamp_us: " + str(self.timestamp_us),
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "absolute_altitude_m: " + str(self.absolute_altitude_m),
                "hdop: " + str(self.hdop),
                "vdop: " + str(self.vdop),
                "velocity_m_s: " + str(self.velocity_m_s),
                "cog_deg: " + str(self.cog_deg),
                "altitude_ellipsoid_m: " + str(self.altitude_ellipsoid_m),
                "horizontal_uncertainty_m: " + str(self.horizontal_uncertainty_m),
                "vertical_uncertainty_m: " + str(self.vertical_uncertainty_m),
                "velocity_uncertainty_m_s: " + str(self.velocity_uncertainty_m_s),
                "heading_uncertainty_deg: " + str(self.heading_uncertainty_deg),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"RawGps: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcRawGps):
        """ Translates a gRPC struct to the SDK equivalent """
        return RawGps(
                
                rpcRawGps.timestamp_us,
                
                
                rpcRawGps.latitude_deg,
                
                
                rpcRawGps.longitude_deg,
                
                
                rpcRawGps.absolute_altitude_m,
                
                
                rpcRawGps.hdop,
                
                
                rpcRawGps.vdop,
                
                
                rpcRawGps.velocity_m_s,
                
                
                rpcRawGps.cog_deg,
                
                
                rpcRawGps.altitude_ellipsoid_m,
                
                
                rpcRawGps.horizontal_uncertainty_m,
                
                
                rpcRawGps.vertical_uncertainty_m,
                
                
                rpcRawGps.velocity_uncertainty_m_s,
                
                
                rpcRawGps.heading_uncertainty_deg,
                
                
                rpcRawGps.yaw_deg
                )

    def translate_to_rpc(self, rpcRawGps):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcRawGps.timestamp_us = self.timestamp_us
            
        
        
        
            
        rpcRawGps.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcRawGps.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcRawGps.absolute_altitude_m = self.absolute_altitude_m
            
        
        
        
            
        rpcRawGps.hdop = self.hdop
            
        
        
        
            
        rpcRawGps.vdop = self.vdop
            
        
        
        
            
        rpcRawGps.velocity_m_s = self.velocity_m_s
            
        
        
        
            
        rpcRawGps.cog_deg = self.cog_deg
            
        
        
        
            
        rpcRawGps.altitude_ellipsoid_m = self.altitude_ellipsoid_m
            
        
        
        
            
        rpcRawGps.horizontal_uncertainty_m = self.horizontal_uncertainty_m
            
        
        
        
            
        rpcRawGps.vertical_uncertainty_m = self.vertical_uncertainty_m
            
        
        
        
            
        rpcRawGps.velocity_uncertainty_m_s = self.velocity_uncertainty_m_s
            
        
        
        
            
        rpcRawGps.heading_uncertainty_deg = self.heading_uncertainty_deg
            
        
        
        
            
        rpcRawGps.yaw_deg = self.yaw_deg
            
        
        


class Battery:
    """
     Battery type.

     Parameters
     ----------
     id : uint32_t
          Battery ID, for systems with multiple batteries

     temperature_degc : float
          Temperature of the battery in degrees Celsius. NAN for unknown temperature

     voltage_v : float
          Voltage in volts

     current_battery_a : float
          Battery current in Amps, NAN if autopilot does not measure the current

     capacity_consumed_ah : float
          Consumed charge in Amp hours, NAN if autopilot does not provide consumption estimate

     remaining_percent : float
          Estimated battery remaining (range: 0 to 100)

     time_remaining_s : float
          Estimated battery usage time remaining 

     battery_function : BatteryFunction
          Function of the battery

     """

    

    def __init__(
            self,
            id,
            temperature_degc,
            voltage_v,
            current_battery_a,
            capacity_consumed_ah,
            remaining_percent,
            time_remaining_s,
            battery_function):
        """ Initializes the Battery object """
        self.id = id
        self.temperature_degc = temperature_degc
        self.voltage_v = voltage_v
        self.current_battery_a = current_battery_a
        self.capacity_consumed_ah = capacity_consumed_ah
        self.remaining_percent = remaining_percent
        self.time_remaining_s = time_remaining_s
        self.battery_function = battery_function

    def __eq__(self, to_compare):
        """ Checks if two Battery are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Battery object
            return \
                (self.id == to_compare.id) and \
                (self.temperature_degc == to_compare.temperature_degc) and \
                (self.voltage_v == to_compare.voltage_v) and \
                (self.current_battery_a == to_compare.current_battery_a) and \
                (self.capacity_consumed_ah == to_compare.capacity_consumed_ah) and \
                (self.remaining_percent == to_compare.remaining_percent) and \
                (self.time_remaining_s == to_compare.time_remaining_s) and \
                (self.battery_function == to_compare.battery_function)

        except AttributeError:
            return False

    def __str__(self):
        """ Battery in string representation """
        struct_repr = ", ".join([
                "id: " + str(self.id),
                "temperature_degc: " + str(self.temperature_degc),
                "voltage_v: " + str(self.voltage_v),
                "current_battery_a: " + str(self.current_battery_a),
                "capacity_consumed_ah: " + str(self.capacity_consumed_ah),
                "remaining_percent: " + str(self.remaining_percent),
                "time_remaining_s: " + str(self.time_remaining_s),
                "battery_function: " + str(self.battery_function)
                ])

        return f"Battery: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcBattery):
        """ Translates a gRPC struct to the SDK equivalent """
        return Battery(
                
                rpcBattery.id,
                
                
                rpcBattery.temperature_degc,
                
                
                rpcBattery.voltage_v,
                
                
                rpcBattery.current_battery_a,
                
                
                rpcBattery.capacity_consumed_ah,
                
                
                rpcBattery.remaining_percent,
                
                
                rpcBattery.time_remaining_s,
                
                
                BatteryFunction.translate_from_rpc(rpcBattery.battery_function)
                )

    def translate_to_rpc(self, rpcBattery):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcBattery.id = self.id
            
        
        
        
            
        rpcBattery.temperature_degc = self.temperature_degc
            
        
        
        
            
        rpcBattery.voltage_v = self.voltage_v
            
        
        
        
            
        rpcBattery.current_battery_a = self.current_battery_a
            
        
        
        
            
        rpcBattery.capacity_consumed_ah = self.capacity_consumed_ah
            
        
        
        
            
        rpcBattery.remaining_percent = self.remaining_percent
            
        
        
        
            
        rpcBattery.time_remaining_s = self.time_remaining_s
            
        
        
        
            
        rpcBattery.battery_function = self.battery_function.translate_to_rpc()
            
        
        


class Health:
    """
     Health type.

     Parameters
     ----------
     is_gyrometer_calibration_ok : bool
          True if the gyrometer is calibrated

     is_accelerometer_calibration_ok : bool
          True if the accelerometer is calibrated

     is_magnetometer_calibration_ok : bool
          True if the magnetometer is calibrated

     is_local_position_ok : bool
          True if the local position estimate is good enough to fly in 'position control' mode

     is_global_position_ok : bool
          True if the global position estimate is good enough to fly in 'position control' mode

     is_home_position_ok : bool
          True if the home position has been initialized properly

     is_armable : bool
          True if system can be armed

     """

    

    def __init__(
            self,
            is_gyrometer_calibration_ok,
            is_accelerometer_calibration_ok,
            is_magnetometer_calibration_ok,
            is_local_position_ok,
            is_global_position_ok,
            is_home_position_ok,
            is_armable):
        """ Initializes the Health object """
        self.is_gyrometer_calibration_ok = is_gyrometer_calibration_ok
        self.is_accelerometer_calibration_ok = is_accelerometer_calibration_ok
        self.is_magnetometer_calibration_ok = is_magnetometer_calibration_ok
        self.is_local_position_ok = is_local_position_ok
        self.is_global_position_ok = is_global_position_ok
        self.is_home_position_ok = is_home_position_ok
        self.is_armable = is_armable

    def __eq__(self, to_compare):
        """ Checks if two Health are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Health object
            return \
                (self.is_gyrometer_calibration_ok == to_compare.is_gyrometer_calibration_ok) and \
                (self.is_accelerometer_calibration_ok == to_compare.is_accelerometer_calibration_ok) and \
                (self.is_magnetometer_calibration_ok == to_compare.is_magnetometer_calibration_ok) and \
                (self.is_local_position_ok == to_compare.is_local_position_ok) and \
                (self.is_global_position_ok == to_compare.is_global_position_ok) and \
                (self.is_home_position_ok == to_compare.is_home_position_ok) and \
                (self.is_armable == to_compare.is_armable)

        except AttributeError:
            return False

    def __str__(self):
        """ Health in string representation """
        struct_repr = ", ".join([
                "is_gyrometer_calibration_ok: " + str(self.is_gyrometer_calibration_ok),
                "is_accelerometer_calibration_ok: " + str(self.is_accelerometer_calibration_ok),
                "is_magnetometer_calibration_ok: " + str(self.is_magnetometer_calibration_ok),
                "is_local_position_ok: " + str(self.is_local_position_ok),
                "is_global_position_ok: " + str(self.is_global_position_ok),
                "is_home_position_ok: " + str(self.is_home_position_ok),
                "is_armable: " + str(self.is_armable)
                ])

        return f"Health: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealth):
        """ Translates a gRPC struct to the SDK equivalent """
        return Health(
                
                rpcHealth.is_gyrometer_calibration_ok,
                
                
                rpcHealth.is_accelerometer_calibration_ok,
                
                
                rpcHealth.is_magnetometer_calibration_ok,
                
                
                rpcHealth.is_local_position_ok,
                
                
                rpcHealth.is_global_position_ok,
                
                
                rpcHealth.is_home_position_ok,
                
                
                rpcHealth.is_armable
                )

    def translate_to_rpc(self, rpcHealth):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcHealth.is_gyrometer_calibration_ok = self.is_gyrometer_calibration_ok
            
        
        
        
            
        rpcHealth.is_accelerometer_calibration_ok = self.is_accelerometer_calibration_ok
            
        
        
        
            
        rpcHealth.is_magnetometer_calibration_ok = self.is_magnetometer_calibration_ok
            
        
        
        
            
        rpcHealth.is_local_position_ok = self.is_local_position_ok
            
        
        
        
            
        rpcHealth.is_global_position_ok = self.is_global_position_ok
            
        
        
        
            
        rpcHealth.is_home_position_ok = self.is_home_position_ok
            
        
        
        
            
        rpcHealth.is_armable = self.is_armable
            
        
        


class RcStatus:
    """
     Remote control status type.

     Parameters
     ----------
     was_available_once : bool
          True if an RC signal has been available once

     is_available : bool
          True if the RC signal is available now

     signal_strength_percent : float
          Signal strength (range: 0 to 100, NaN if unknown)

     """

    

    def __init__(
            self,
            was_available_once,
            is_available,
            signal_strength_percent):
        """ Initializes the RcStatus object """
        self.was_available_once = was_available_once
        self.is_available = is_available
        self.signal_strength_percent = signal_strength_percent

    def __eq__(self, to_compare):
        """ Checks if two RcStatus are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # RcStatus object
            return \
                (self.was_available_once == to_compare.was_available_once) and \
                (self.is_available == to_compare.is_available) and \
                (self.signal_strength_percent == to_compare.signal_strength_percent)

        except AttributeError:
            return False

    def __str__(self):
        """ RcStatus in string representation """
        struct_repr = ", ".join([
                "was_available_once: " + str(self.was_available_once),
                "is_available: " + str(self.is_available),
                "signal_strength_percent: " + str(self.signal_strength_percent)
                ])

        return f"RcStatus: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcRcStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return RcStatus(
                
                rpcRcStatus.was_available_once,
                
                
                rpcRcStatus.is_available,
                
                
                rpcRcStatus.signal_strength_percent
                )

    def translate_to_rpc(self, rpcRcStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcRcStatus.was_available_once = self.was_available_once
            
        
        
        
            
        rpcRcStatus.is_available = self.is_available
            
        
        
        
            
        rpcRcStatus.signal_strength_percent = self.signal_strength_percent
            
        
        


class StatusText:
    """
     StatusText information type.

     Parameters
     ----------
     type : StatusTextType
          Message type

     text : std::string
          MAVLink status message

     """

    

    def __init__(
            self,
            type,
            text):
        """ Initializes the StatusText object """
        self.type = type
        self.text = text

    def __eq__(self, to_compare):
        """ Checks if two StatusText are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # StatusText object
            return \
                (self.type == to_compare.type) and \
                (self.text == to_compare.text)

        except AttributeError:
            return False

    def __str__(self):
        """ StatusText in string representation """
        struct_repr = ", ".join([
                "type: " + str(self.type),
                "text: " + str(self.text)
                ])

        return f"StatusText: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStatusText):
        """ Translates a gRPC struct to the SDK equivalent """
        return StatusText(
                
                StatusTextType.translate_from_rpc(rpcStatusText.type),
                
                
                rpcStatusText.text
                )

    def translate_to_rpc(self, rpcStatusText):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStatusText.type = self.type.translate_to_rpc()
            
        
        
        
            
        rpcStatusText.text = self.text
            
        
        


class ActuatorControlTarget:
    """
     Actuator control target type.

     Parameters
     ----------
     group : int32_t
          An actuator control group is e.g. 'attitude' for the core flight controls, or 'gimbal' for a payload.

     controls : [float]
          Controls normed from -1 to 1, where 0 is neutral position.

     """

    

    def __init__(
            self,
            group,
            controls):
        """ Initializes the ActuatorControlTarget object """
        self.group = group
        self.controls = controls

    def __eq__(self, to_compare):
        """ Checks if two ActuatorControlTarget are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActuatorControlTarget object
            return \
                (self.group == to_compare.group) and \
                (self.controls == to_compare.controls)

        except AttributeError:
            return False

    def __str__(self):
        """ ActuatorControlTarget in string representation """
        struct_repr = ", ".join([
                "group: " + str(self.group),
                "controls: " + str(self.controls)
                ])

        return f"ActuatorControlTarget: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActuatorControlTarget):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActuatorControlTarget(
                
                rpcActuatorControlTarget.group,
                
                
                rpcActuatorControlTarget.controls
                )

    def translate_to_rpc(self, rpcActuatorControlTarget):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcActuatorControlTarget.group = self.group
            
        
        
        
            
        for elem in self.controls:
          rpcActuatorControlTarget.controls.append(elem)
            
        
        


class ActuatorOutputStatus:
    """
     Actuator output status type.

     Parameters
     ----------
     active : uint32_t
          Active outputs

     actuator : [float]
          Servo/motor output values

     """

    

    def __init__(
            self,
            active,
            actuator):
        """ Initializes the ActuatorOutputStatus object """
        self.active = active
        self.actuator = actuator

    def __eq__(self, to_compare):
        """ Checks if two ActuatorOutputStatus are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActuatorOutputStatus object
            return \
                (self.active == to_compare.active) and \
                (self.actuator == to_compare.actuator)

        except AttributeError:
            return False

    def __str__(self):
        """ ActuatorOutputStatus in string representation """
        struct_repr = ", ".join([
                "active: " + str(self.active),
                "actuator: " + str(self.actuator)
                ])

        return f"ActuatorOutputStatus: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActuatorOutputStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActuatorOutputStatus(
                
                rpcActuatorOutputStatus.active,
                
                
                rpcActuatorOutputStatus.actuator
                )

    def translate_to_rpc(self, rpcActuatorOutputStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcActuatorOutputStatus.active = self.active
            
        
        
        
            
        for elem in self.actuator:
          rpcActuatorOutputStatus.actuator.append(elem)
            
        
        


class Covariance:
    """
     Covariance type.

     Row-major representation of a 6x6 cross-covariance matrix
     upper right triangle.
     Set first to NaN if unknown.

     Parameters
     ----------
     covariance_matrix : [float]
          Representation of a covariance matrix.

     """

    

    def __init__(
            self,
            covariance_matrix):
        """ Initializes the Covariance object """
        self.covariance_matrix = covariance_matrix

    def __eq__(self, to_compare):
        """ Checks if two Covariance are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Covariance object
            return \
                (self.covariance_matrix == to_compare.covariance_matrix)

        except AttributeError:
            return False

    def __str__(self):
        """ Covariance in string representation """
        struct_repr = ", ".join([
                "covariance_matrix: " + str(self.covariance_matrix)
                ])

        return f"Covariance: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCovariance):
        """ Translates a gRPC struct to the SDK equivalent """
        return Covariance(
                
                rpcCovariance.covariance_matrix
                )

    def translate_to_rpc(self, rpcCovariance):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        for elem in self.covariance_matrix:
          rpcCovariance.covariance_matrix.append(elem)
            
        
        


class VelocityBody:
    """
     Velocity type, represented in the Body (X Y Z) frame and in metres/second.

     Parameters
     ----------
     x_m_s : float
          Velocity in X in metres/second

     y_m_s : float
          Velocity in Y in metres/second

     z_m_s : float
          Velocity in Z in metres/second

     """

    

    def __init__(
            self,
            x_m_s,
            y_m_s,
            z_m_s):
        """ Initializes the VelocityBody object """
        self.x_m_s = x_m_s
        self.y_m_s = y_m_s
        self.z_m_s = z_m_s

    def __eq__(self, to_compare):
        """ Checks if two VelocityBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityBody object
            return \
                (self.x_m_s == to_compare.x_m_s) and \
                (self.y_m_s == to_compare.y_m_s) and \
                (self.z_m_s == to_compare.z_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityBody in string representation """
        struct_repr = ", ".join([
                "x_m_s: " + str(self.x_m_s),
                "y_m_s: " + str(self.y_m_s),
                "z_m_s: " + str(self.z_m_s)
                ])

        return f"VelocityBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityBody(
                
                rpcVelocityBody.x_m_s,
                
                
                rpcVelocityBody.y_m_s,
                
                
                rpcVelocityBody.z_m_s
                )

    def translate_to_rpc(self, rpcVelocityBody):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityBody.x_m_s = self.x_m_s
            
        
        
        
            
        rpcVelocityBody.y_m_s = self.y_m_s
            
        
        
        
            
        rpcVelocityBody.z_m_s = self.z_m_s
            
        
        


class PositionBody:
    """
     Position type, represented in the Body (X Y Z) frame

     Parameters
     ----------
     x_m : float
          X Position in metres.

     y_m : float
          Y Position in metres.

     z_m : float
          Z Position in metres.

     """

    

    def __init__(
            self,
            x_m,
            y_m,
            z_m):
        """ Initializes the PositionBody object """
        self.x_m = x_m
        self.y_m = y_m
        self.z_m = z_m

    def __eq__(self, to_compare):
        """ Checks if two PositionBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionBody object
            return \
                (self.x_m == to_compare.x_m) and \
                (self.y_m == to_compare.y_m) and \
                (self.z_m == to_compare.z_m)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionBody in string representation """
        struct_repr = ", ".join([
                "x_m: " + str(self.x_m),
                "y_m: " + str(self.y_m),
                "z_m: " + str(self.z_m)
                ])

        return f"PositionBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionBody(
                
                rpcPositionBody.x_m,
                
                
                rpcPositionBody.y_m,
                
                
                rpcPositionBody.z_m
                )

    def translate_to_rpc(self, rpcPositionBody):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPositionBody.x_m = self.x_m
            
        
        
        
            
        rpcPositionBody.y_m = self.y_m
            
        
        
        
            
        rpcPositionBody.z_m = self.z_m
            
        
        


class Odometry:
    """
     Odometry message type.

     Parameters
     ----------
     time_usec : uint64_t
          Timestamp (0 to use Backend timestamp).

     frame_id : MavFrame
          Coordinate frame of reference for the pose data.

     child_frame_id : MavFrame
          Coordinate frame of reference for the velocity in free space (twist) data.

     position_body : PositionBody
          Position.

     q : Quaternion
          Quaternion components, w, x, y, z (1 0 0 0 is the null-rotation).

     velocity_body : VelocityBody
          Linear velocity (m/s).

     angular_velocity_body : AngularVelocityBody
          Angular velocity (rad/s).

     pose_covariance : Covariance
          Pose cross-covariance matrix.

     velocity_covariance : Covariance
          Velocity cross-covariance matrix.

     """

    
    
    class MavFrame(Enum):
        """
         Mavlink frame id

         Values
         ------
         UNDEF
              Frame is undefined.

         BODY_NED
              Setpoint in body NED frame. This makes sense if all position control is externalized - e.g. useful to command 2 m/s^2 acceleration to the right.

         VISION_NED
              Odometry local coordinate frame of data given by a vision estimation system, Z-down (x: north, y: east, z: down).

         ESTIM_NED
              Odometry local coordinate frame of data given by an estimator running onboard the vehicle, Z-down (x: north, y: east, z: down).

         """

        
        UNDEF = 0
        BODY_NED = 1
        VISION_NED = 2
        ESTIM_NED = 3

        def translate_to_rpc(self):
            if self == Odometry.MavFrame.UNDEF:
                return telemetry_pb2.Odometry.MAV_FRAME_UNDEF
            if self == Odometry.MavFrame.BODY_NED:
                return telemetry_pb2.Odometry.MAV_FRAME_BODY_NED
            if self == Odometry.MavFrame.VISION_NED:
                return telemetry_pb2.Odometry.MAV_FRAME_VISION_NED
            if self == Odometry.MavFrame.ESTIM_NED:
                return telemetry_pb2.Odometry.MAV_FRAME_ESTIM_NED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == telemetry_pb2.Odometry.MAV_FRAME_UNDEF:
                return Odometry.MavFrame.UNDEF
            if rpc_enum_value == telemetry_pb2.Odometry.MAV_FRAME_BODY_NED:
                return Odometry.MavFrame.BODY_NED
            if rpc_enum_value == telemetry_pb2.Odometry.MAV_FRAME_VISION_NED:
                return Odometry.MavFrame.VISION_NED
            if rpc_enum_value == telemetry_pb2.Odometry.MAV_FRAME_ESTIM_NED:
                return Odometry.MavFrame.ESTIM_NED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            time_usec,
            frame_id,
            child_frame_id,
            position_body,
            q,
            velocity_body,
            angular_velocity_body,
            pose_covariance,
            velocity_covariance):
        """ Initializes the Odometry object """
        self.time_usec = time_usec
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        self.position_body = position_body
        self.q = q
        self.velocity_body = velocity_body
        self.angular_velocity_body = angular_velocity_body
        self.pose_covariance = pose_covariance
        self.velocity_covariance = velocity_covariance

    def __eq__(self, to_compare):
        """ Checks if two Odometry are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Odometry object
            return \
                (self.time_usec == to_compare.time_usec) and \
                (self.frame_id == to_compare.frame_id) and \
                (self.child_frame_id == to_compare.child_frame_id) and \
                (self.position_body == to_compare.position_body) and \
                (self.q == to_compare.q) and \
                (self.velocity_body == to_compare.velocity_body) and \
                (self.angular_velocity_body == to_compare.angular_velocity_body) and \
                (self.pose_covariance == to_compare.pose_covariance) and \
                (self.velocity_covariance == to_compare.velocity_covariance)

        except AttributeError:
            return False

    def __str__(self):
        """ Odometry in string representation """
        struct_repr = ", ".join([
                "time_usec: " + str(self.time_usec),
                "frame_id: " + str(self.frame_id),
                "child_frame_id: " + str(self.child_frame_id),
                "position_body: " + str(self.position_body),
                "q: " + str(self.q),
                "velocity_body: " + str(self.velocity_body),
                "angular_velocity_body: " + str(self.angular_velocity_body),
                "pose_covariance: " + str(self.pose_covariance),
                "velocity_covariance: " + str(self.velocity_covariance)
                ])

        return f"Odometry: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcOdometry):
        """ Translates a gRPC struct to the SDK equivalent """
        return Odometry(
                
                rpcOdometry.time_usec,
                
                
                Odometry.MavFrame.translate_from_rpc(rpcOdometry.frame_id),
                
                
                Odometry.MavFrame.translate_from_rpc(rpcOdometry.child_frame_id),
                
                
                PositionBody.translate_from_rpc(rpcOdometry.position_body),
                
                
                Quaternion.translate_from_rpc(rpcOdometry.q),
                
                
                VelocityBody.translate_from_rpc(rpcOdometry.velocity_body),
                
                
                AngularVelocityBody.translate_from_rpc(rpcOdometry.angular_velocity_body),
                
                
                Covariance.translate_from_rpc(rpcOdometry.pose_covariance),
                
                
                Covariance.translate_from_rpc(rpcOdometry.velocity_covariance)
                )

    def translate_to_rpc(self, rpcOdometry):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcOdometry.time_usec = self.time_usec
            
        
        
        
            
        rpcOdometry.frame_id = self.frame_id.translate_to_rpc()
            
        
        
        
            
        rpcOdometry.child_frame_id = self.child_frame_id.translate_to_rpc()
            
        
        
        
            
        self.position_body.translate_to_rpc(rpcOdometry.position_body)
            
        
        
        
            
        self.q.translate_to_rpc(rpcOdometry.q)
            
        
        
        
            
        self.velocity_body.translate_to_rpc(rpcOdometry.velocity_body)
            
        
        
        
            
        self.angular_velocity_body.translate_to_rpc(rpcOdometry.angular_velocity_body)
            
        
        
        
            
        self.pose_covariance.translate_to_rpc(rpcOdometry.pose_covariance)
            
        
        
        
            
        self.velocity_covariance.translate_to_rpc(rpcOdometry.velocity_covariance)
            
        
        


class DistanceSensor:
    """
     DistanceSensor message type.

     Parameters
     ----------
     minimum_distance_m : float
          Minimum distance the sensor can measure, NaN if unknown.

     maximum_distance_m : float
          Maximum distance the sensor can measure, NaN if unknown.

     current_distance_m : float
          Current distance reading, NaN if unknown.

     orientation : EulerAngle
          Sensor Orientation reading.

     """

    

    def __init__(
            self,
            minimum_distance_m,
            maximum_distance_m,
            current_distance_m,
            orientation):
        """ Initializes the DistanceSensor object """
        self.minimum_distance_m = minimum_distance_m
        self.maximum_distance_m = maximum_distance_m
        self.current_distance_m = current_distance_m
        self.orientation = orientation

    def __eq__(self, to_compare):
        """ Checks if two DistanceSensor are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # DistanceSensor object
            return \
                (self.minimum_distance_m == to_compare.minimum_distance_m) and \
                (self.maximum_distance_m == to_compare.maximum_distance_m) and \
                (self.current_distance_m == to_compare.current_distance_m) and \
                (self.orientation == to_compare.orientation)

        except AttributeError:
            return False

    def __str__(self):
        """ DistanceSensor in string representation """
        struct_repr = ", ".join([
                "minimum_distance_m: " + str(self.minimum_distance_m),
                "maximum_distance_m: " + str(self.maximum_distance_m),
                "current_distance_m: " + str(self.current_distance_m),
                "orientation: " + str(self.orientation)
                ])

        return f"DistanceSensor: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcDistanceSensor):
        """ Translates a gRPC struct to the SDK equivalent """
        return DistanceSensor(
                
                rpcDistanceSensor.minimum_distance_m,
                
                
                rpcDistanceSensor.maximum_distance_m,
                
                
                rpcDistanceSensor.current_distance_m,
                
                
                EulerAngle.translate_from_rpc(rpcDistanceSensor.orientation)
                )

    def translate_to_rpc(self, rpcDistanceSensor):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcDistanceSensor.minimum_distance_m = self.minimum_distance_m
            
        
        
        
            
        rpcDistanceSensor.maximum_distance_m = self.maximum_distance_m
            
        
        
        
            
        rpcDistanceSensor.current_distance_m = self.current_distance_m
            
        
        
        
            
        self.orientation.translate_to_rpc(rpcDistanceSensor.orientation)
            
        
        


class ScaledPressure:
    """
     Scaled Pressure message type.

     Parameters
     ----------
     timestamp_us : uint64_t
          Timestamp (time since system boot)

     absolute_pressure_hpa : float
          Absolute pressure in hPa

     differential_pressure_hpa : float
          Differential pressure 1 in hPa

     temperature_deg : float
          Absolute pressure temperature (in celsius)

     differential_pressure_temperature_deg : float
          Differential pressure temperature (in celsius, 0 if not available)

     """

    

    def __init__(
            self,
            timestamp_us,
            absolute_pressure_hpa,
            differential_pressure_hpa,
            temperature_deg,
            differential_pressure_temperature_deg):
        """ Initializes the ScaledPressure object """
        self.timestamp_us = timestamp_us
        self.absolute_pressure_hpa = absolute_pressure_hpa
        self.differential_pressure_hpa = differential_pressure_hpa
        self.temperature_deg = temperature_deg
        self.differential_pressure_temperature_deg = differential_pressure_temperature_deg

    def __eq__(self, to_compare):
        """ Checks if two ScaledPressure are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ScaledPressure object
            return \
                (self.timestamp_us == to_compare.timestamp_us) and \
                (self.absolute_pressure_hpa == to_compare.absolute_pressure_hpa) and \
                (self.differential_pressure_hpa == to_compare.differential_pressure_hpa) and \
                (self.temperature_deg == to_compare.temperature_deg) and \
                (self.differential_pressure_temperature_deg == to_compare.differential_pressure_temperature_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ ScaledPressure in string representation """
        struct_repr = ", ".join([
                "timestamp_us: " + str(self.timestamp_us),
                "absolute_pressure_hpa: " + str(self.absolute_pressure_hpa),
                "differential_pressure_hpa: " + str(self.differential_pressure_hpa),
                "temperature_deg: " + str(self.temperature_deg),
                "differential_pressure_temperature_deg: " + str(self.differential_pressure_temperature_deg)
                ])

        return f"ScaledPressure: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcScaledPressure):
        """ Translates a gRPC struct to the SDK equivalent """
        return ScaledPressure(
                
                rpcScaledPressure.timestamp_us,
                
                
                rpcScaledPressure.absolute_pressure_hpa,
                
                
                rpcScaledPressure.differential_pressure_hpa,
                
                
                rpcScaledPressure.temperature_deg,
                
                
                rpcScaledPressure.differential_pressure_temperature_deg
                )

    def translate_to_rpc(self, rpcScaledPressure):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcScaledPressure.timestamp_us = self.timestamp_us
            
        
        
        
            
        rpcScaledPressure.absolute_pressure_hpa = self.absolute_pressure_hpa
            
        
        
        
            
        rpcScaledPressure.differential_pressure_hpa = self.differential_pressure_hpa
            
        
        
        
            
        rpcScaledPressure.temperature_deg = self.temperature_deg
            
        
        
        
            
        rpcScaledPressure.differential_pressure_temperature_deg = self.differential_pressure_temperature_deg
            
        
        


class PositionNed:
    """
     PositionNed message type.

     Parameters
     ----------
     north_m : float
          Position along north direction in metres

     east_m : float
          Position along east direction in metres

     down_m : float
          Position along down direction in metres

     """

    

    def __init__(
            self,
            north_m,
            east_m,
            down_m):
        """ Initializes the PositionNed object """
        self.north_m = north_m
        self.east_m = east_m
        self.down_m = down_m

    def __eq__(self, to_compare):
        """ Checks if two PositionNed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionNed object
            return \
                (self.north_m == to_compare.north_m) and \
                (self.east_m == to_compare.east_m) and \
                (self.down_m == to_compare.down_m)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionNed in string representation """
        struct_repr = ", ".join([
                "north_m: " + str(self.north_m),
                "east_m: " + str(self.east_m),
                "down_m: " + str(self.down_m)
                ])

        return f"PositionNed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionNed):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionNed(
                
                rpcPositionNed.north_m,
                
                
                rpcPositionNed.east_m,
                
                
                rpcPositionNed.down_m
                )

    def translate_to_rpc(self, rpcPositionNed):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPositionNed.north_m = self.north_m
            
        
        
        
            
        rpcPositionNed.east_m = self.east_m
            
        
        
        
            
        rpcPositionNed.down_m = self.down_m
            
        
        


class VelocityNed:
    """
     VelocityNed message type.

     Parameters
     ----------
     north_m_s : float
          Velocity along north direction in metres per second

     east_m_s : float
          Velocity along east direction in metres per second

     down_m_s : float
          Velocity along down direction in metres per second

     """

    

    def __init__(
            self,
            north_m_s,
            east_m_s,
            down_m_s):
        """ Initializes the VelocityNed object """
        self.north_m_s = north_m_s
        self.east_m_s = east_m_s
        self.down_m_s = down_m_s

    def __eq__(self, to_compare):
        """ Checks if two VelocityNed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VelocityNed object
            return \
                (self.north_m_s == to_compare.north_m_s) and \
                (self.east_m_s == to_compare.east_m_s) and \
                (self.down_m_s == to_compare.down_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ VelocityNed in string representation """
        struct_repr = ", ".join([
                "north_m_s: " + str(self.north_m_s),
                "east_m_s: " + str(self.east_m_s),
                "down_m_s: " + str(self.down_m_s)
                ])

        return f"VelocityNed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVelocityNed):
        """ Translates a gRPC struct to the SDK equivalent """
        return VelocityNed(
                
                rpcVelocityNed.north_m_s,
                
                
                rpcVelocityNed.east_m_s,
                
                
                rpcVelocityNed.down_m_s
                )

    def translate_to_rpc(self, rpcVelocityNed):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVelocityNed.north_m_s = self.north_m_s
            
        
        
        
            
        rpcVelocityNed.east_m_s = self.east_m_s
            
        
        
        
            
        rpcVelocityNed.down_m_s = self.down_m_s
            
        
        


class PositionVelocityNed:
    """
     PositionVelocityNed message type.

     Parameters
     ----------
     position : PositionNed
          Position (NED)

     velocity : VelocityNed
          Velocity (NED)

     """

    

    def __init__(
            self,
            position,
            velocity):
        """ Initializes the PositionVelocityNed object """
        self.position = position
        self.velocity = velocity

    def __eq__(self, to_compare):
        """ Checks if two PositionVelocityNed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PositionVelocityNed object
            return \
                (self.position == to_compare.position) and \
                (self.velocity == to_compare.velocity)

        except AttributeError:
            return False

    def __str__(self):
        """ PositionVelocityNed in string representation """
        struct_repr = ", ".join([
                "position: " + str(self.position),
                "velocity: " + str(self.velocity)
                ])

        return f"PositionVelocityNed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPositionVelocityNed):
        """ Translates a gRPC struct to the SDK equivalent """
        return PositionVelocityNed(
                
                PositionNed.translate_from_rpc(rpcPositionVelocityNed.position),
                
                
                VelocityNed.translate_from_rpc(rpcPositionVelocityNed.velocity)
                )

    def translate_to_rpc(self, rpcPositionVelocityNed):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.position.translate_to_rpc(rpcPositionVelocityNed.position)
            
        
        
        
            
        self.velocity.translate_to_rpc(rpcPositionVelocityNed.velocity)
            
        
        


class GroundTruth:
    """
     GroundTruth message type.

     Parameters
     ----------
     latitude_deg : double
          Latitude in degrees (range: -90 to +90)

     longitude_deg : double
          Longitude in degrees (range: -180 to 180)

     absolute_altitude_m : float
          Altitude AMSL (above mean sea level) in metres

     """

    

    def __init__(
            self,
            latitude_deg,
            longitude_deg,
            absolute_altitude_m):
        """ Initializes the GroundTruth object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.absolute_altitude_m = absolute_altitude_m

    def __eq__(self, to_compare):
        """ Checks if two GroundTruth are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GroundTruth object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m)

        except AttributeError:
            return False

    def __str__(self):
        """ GroundTruth in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "absolute_altitude_m: " + str(self.absolute_altitude_m)
                ])

        return f"GroundTruth: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGroundTruth):
        """ Translates a gRPC struct to the SDK equivalent """
        return GroundTruth(
                
                rpcGroundTruth.latitude_deg,
                
                
                rpcGroundTruth.longitude_deg,
                
                
                rpcGroundTruth.absolute_altitude_m
                )

    def translate_to_rpc(self, rpcGroundTruth):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGroundTruth.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcGroundTruth.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcGroundTruth.absolute_altitude_m = self.absolute_altitude_m
            
        
        


class FixedwingMetrics:
    """
     FixedwingMetrics message type.

     Parameters
     ----------
     airspeed_m_s : float
          Current indicated airspeed (IAS) in metres per second

     throttle_percentage : float
          Current throttle setting (0 to 100)

     climb_rate_m_s : float
          Current climb rate in metres per second

     groundspeed_m_s : float
          Current groundspeed metres per second

     heading_deg : float
          Current heading in compass units (0-360, 0=north)

     absolute_altitude_m : float
          Current altitude in metres (MSL)

     """

    

    def __init__(
            self,
            airspeed_m_s,
            throttle_percentage,
            climb_rate_m_s,
            groundspeed_m_s,
            heading_deg,
            absolute_altitude_m):
        """ Initializes the FixedwingMetrics object """
        self.airspeed_m_s = airspeed_m_s
        self.throttle_percentage = throttle_percentage
        self.climb_rate_m_s = climb_rate_m_s
        self.groundspeed_m_s = groundspeed_m_s
        self.heading_deg = heading_deg
        self.absolute_altitude_m = absolute_altitude_m

    def __eq__(self, to_compare):
        """ Checks if two FixedwingMetrics are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FixedwingMetrics object
            return \
                (self.airspeed_m_s == to_compare.airspeed_m_s) and \
                (self.throttle_percentage == to_compare.throttle_percentage) and \
                (self.climb_rate_m_s == to_compare.climb_rate_m_s) and \
                (self.groundspeed_m_s == to_compare.groundspeed_m_s) and \
                (self.heading_deg == to_compare.heading_deg) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m)

        except AttributeError:
            return False

    def __str__(self):
        """ FixedwingMetrics in string representation """
        struct_repr = ", ".join([
                "airspeed_m_s: " + str(self.airspeed_m_s),
                "throttle_percentage: " + str(self.throttle_percentage),
                "climb_rate_m_s: " + str(self.climb_rate_m_s),
                "groundspeed_m_s: " + str(self.groundspeed_m_s),
                "heading_deg: " + str(self.heading_deg),
                "absolute_altitude_m: " + str(self.absolute_altitude_m)
                ])

        return f"FixedwingMetrics: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFixedwingMetrics):
        """ Translates a gRPC struct to the SDK equivalent """
        return FixedwingMetrics(
                
                rpcFixedwingMetrics.airspeed_m_s,
                
                
                rpcFixedwingMetrics.throttle_percentage,
                
                
                rpcFixedwingMetrics.climb_rate_m_s,
                
                
                rpcFixedwingMetrics.groundspeed_m_s,
                
                
                rpcFixedwingMetrics.heading_deg,
                
                
                rpcFixedwingMetrics.absolute_altitude_m
                )

    def translate_to_rpc(self, rpcFixedwingMetrics):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFixedwingMetrics.airspeed_m_s = self.airspeed_m_s
            
        
        
        
            
        rpcFixedwingMetrics.throttle_percentage = self.throttle_percentage
            
        
        
        
            
        rpcFixedwingMetrics.climb_rate_m_s = self.climb_rate_m_s
            
        
        
        
            
        rpcFixedwingMetrics.groundspeed_m_s = self.groundspeed_m_s
            
        
        
        
            
        rpcFixedwingMetrics.heading_deg = self.heading_deg
            
        
        
        
            
        rpcFixedwingMetrics.absolute_altitude_m = self.absolute_altitude_m
            
        
        


class AccelerationFrd:
    """
     AccelerationFrd message type.

     Parameters
     ----------
     forward_m_s2 : float
          Acceleration in forward direction in metres per second^2

     right_m_s2 : float
          Acceleration in right direction in metres per second^2

     down_m_s2 : float
          Acceleration in down direction in metres per second^2

     """

    

    def __init__(
            self,
            forward_m_s2,
            right_m_s2,
            down_m_s2):
        """ Initializes the AccelerationFrd object """
        self.forward_m_s2 = forward_m_s2
        self.right_m_s2 = right_m_s2
        self.down_m_s2 = down_m_s2

    def __eq__(self, to_compare):
        """ Checks if two AccelerationFrd are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AccelerationFrd object
            return \
                (self.forward_m_s2 == to_compare.forward_m_s2) and \
                (self.right_m_s2 == to_compare.right_m_s2) and \
                (self.down_m_s2 == to_compare.down_m_s2)

        except AttributeError:
            return False

    def __str__(self):
        """ AccelerationFrd in string representation """
        struct_repr = ", ".join([
                "forward_m_s2: " + str(self.forward_m_s2),
                "right_m_s2: " + str(self.right_m_s2),
                "down_m_s2: " + str(self.down_m_s2)
                ])

        return f"AccelerationFrd: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAccelerationFrd):
        """ Translates a gRPC struct to the SDK equivalent """
        return AccelerationFrd(
                
                rpcAccelerationFrd.forward_m_s2,
                
                
                rpcAccelerationFrd.right_m_s2,
                
                
                rpcAccelerationFrd.down_m_s2
                )

    def translate_to_rpc(self, rpcAccelerationFrd):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAccelerationFrd.forward_m_s2 = self.forward_m_s2
            
        
        
        
            
        rpcAccelerationFrd.right_m_s2 = self.right_m_s2
            
        
        
        
            
        rpcAccelerationFrd.down_m_s2 = self.down_m_s2
            
        
        


class AngularVelocityFrd:
    """
     AngularVelocityFrd message type.

     Parameters
     ----------
     forward_rad_s : float
          Angular velocity in forward direction in radians per second

     right_rad_s : float
          Angular velocity in right direction in radians per second

     down_rad_s : float
          Angular velocity in Down direction in radians per second

     """

    

    def __init__(
            self,
            forward_rad_s,
            right_rad_s,
            down_rad_s):
        """ Initializes the AngularVelocityFrd object """
        self.forward_rad_s = forward_rad_s
        self.right_rad_s = right_rad_s
        self.down_rad_s = down_rad_s

    def __eq__(self, to_compare):
        """ Checks if two AngularVelocityFrd are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AngularVelocityFrd object
            return \
                (self.forward_rad_s == to_compare.forward_rad_s) and \
                (self.right_rad_s == to_compare.right_rad_s) and \
                (self.down_rad_s == to_compare.down_rad_s)

        except AttributeError:
            return False

    def __str__(self):
        """ AngularVelocityFrd in string representation """
        struct_repr = ", ".join([
                "forward_rad_s: " + str(self.forward_rad_s),
                "right_rad_s: " + str(self.right_rad_s),
                "down_rad_s: " + str(self.down_rad_s)
                ])

        return f"AngularVelocityFrd: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAngularVelocityFrd):
        """ Translates a gRPC struct to the SDK equivalent """
        return AngularVelocityFrd(
                
                rpcAngularVelocityFrd.forward_rad_s,
                
                
                rpcAngularVelocityFrd.right_rad_s,
                
                
                rpcAngularVelocityFrd.down_rad_s
                )

    def translate_to_rpc(self, rpcAngularVelocityFrd):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAngularVelocityFrd.forward_rad_s = self.forward_rad_s
            
        
        
        
            
        rpcAngularVelocityFrd.right_rad_s = self.right_rad_s
            
        
        
        
            
        rpcAngularVelocityFrd.down_rad_s = self.down_rad_s
            
        
        


class MagneticFieldFrd:
    """
     MagneticFieldFrd message type.

     Parameters
     ----------
     forward_gauss : float
          Magnetic field in forward direction measured in Gauss

     right_gauss : float
          Magnetic field in East direction measured in Gauss

     down_gauss : float
          Magnetic field in Down direction measured in Gauss

     """

    

    def __init__(
            self,
            forward_gauss,
            right_gauss,
            down_gauss):
        """ Initializes the MagneticFieldFrd object """
        self.forward_gauss = forward_gauss
        self.right_gauss = right_gauss
        self.down_gauss = down_gauss

    def __eq__(self, to_compare):
        """ Checks if two MagneticFieldFrd are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MagneticFieldFrd object
            return \
                (self.forward_gauss == to_compare.forward_gauss) and \
                (self.right_gauss == to_compare.right_gauss) and \
                (self.down_gauss == to_compare.down_gauss)

        except AttributeError:
            return False

    def __str__(self):
        """ MagneticFieldFrd in string representation """
        struct_repr = ", ".join([
                "forward_gauss: " + str(self.forward_gauss),
                "right_gauss: " + str(self.right_gauss),
                "down_gauss: " + str(self.down_gauss)
                ])

        return f"MagneticFieldFrd: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMagneticFieldFrd):
        """ Translates a gRPC struct to the SDK equivalent """
        return MagneticFieldFrd(
                
                rpcMagneticFieldFrd.forward_gauss,
                
                
                rpcMagneticFieldFrd.right_gauss,
                
                
                rpcMagneticFieldFrd.down_gauss
                )

    def translate_to_rpc(self, rpcMagneticFieldFrd):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMagneticFieldFrd.forward_gauss = self.forward_gauss
            
        
        
        
            
        rpcMagneticFieldFrd.right_gauss = self.right_gauss
            
        
        
        
            
        rpcMagneticFieldFrd.down_gauss = self.down_gauss
            
        
        


class Imu:
    """
     Imu message type.

     Parameters
     ----------
     acceleration_frd : AccelerationFrd
          Acceleration

     angular_velocity_frd : AngularVelocityFrd
          Angular velocity

     magnetic_field_frd : MagneticFieldFrd
          Magnetic field

     temperature_degc : float
          Temperature

     timestamp_us : uint64_t
          Timestamp in microseconds

     """

    

    def __init__(
            self,
            acceleration_frd,
            angular_velocity_frd,
            magnetic_field_frd,
            temperature_degc,
            timestamp_us):
        """ Initializes the Imu object """
        self.acceleration_frd = acceleration_frd
        self.angular_velocity_frd = angular_velocity_frd
        self.magnetic_field_frd = magnetic_field_frd
        self.temperature_degc = temperature_degc
        self.timestamp_us = timestamp_us

    def __eq__(self, to_compare):
        """ Checks if two Imu are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Imu object
            return \
                (self.acceleration_frd == to_compare.acceleration_frd) and \
                (self.angular_velocity_frd == to_compare.angular_velocity_frd) and \
                (self.magnetic_field_frd == to_compare.magnetic_field_frd) and \
                (self.temperature_degc == to_compare.temperature_degc) and \
                (self.timestamp_us == to_compare.timestamp_us)

        except AttributeError:
            return False

    def __str__(self):
        """ Imu in string representation """
        struct_repr = ", ".join([
                "acceleration_frd: " + str(self.acceleration_frd),
                "angular_velocity_frd: " + str(self.angular_velocity_frd),
                "magnetic_field_frd: " + str(self.magnetic_field_frd),
                "temperature_degc: " + str(self.temperature_degc),
                "timestamp_us: " + str(self.timestamp_us)
                ])

        return f"Imu: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcImu):
        """ Translates a gRPC struct to the SDK equivalent """
        return Imu(
                
                AccelerationFrd.translate_from_rpc(rpcImu.acceleration_frd),
                
                
                AngularVelocityFrd.translate_from_rpc(rpcImu.angular_velocity_frd),
                
                
                MagneticFieldFrd.translate_from_rpc(rpcImu.magnetic_field_frd),
                
                
                rpcImu.temperature_degc,
                
                
                rpcImu.timestamp_us
                )

    def translate_to_rpc(self, rpcImu):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.acceleration_frd.translate_to_rpc(rpcImu.acceleration_frd)
            
        
        
        
            
        self.angular_velocity_frd.translate_to_rpc(rpcImu.angular_velocity_frd)
            
        
        
        
            
        self.magnetic_field_frd.translate_to_rpc(rpcImu.magnetic_field_frd)
            
        
        
        
            
        rpcImu.temperature_degc = self.temperature_degc
            
        
        
        
            
        rpcImu.timestamp_us = self.timestamp_us
            
        
        


class GpsGlobalOrigin:
    """
     Gps global origin type.

     Parameters
     ----------
     latitude_deg : double
          Latitude of the origin

     longitude_deg : double
          Longitude of the origin

     altitude_m : float
          Altitude AMSL (above mean sea level) in metres

     """

    

    def __init__(
            self,
            latitude_deg,
            longitude_deg,
            altitude_m):
        """ Initializes the GpsGlobalOrigin object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.altitude_m = altitude_m

    def __eq__(self, to_compare):
        """ Checks if two GpsGlobalOrigin are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GpsGlobalOrigin object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.altitude_m == to_compare.altitude_m)

        except AttributeError:
            return False

    def __str__(self):
        """ GpsGlobalOrigin in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "altitude_m: " + str(self.altitude_m)
                ])

        return f"GpsGlobalOrigin: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGpsGlobalOrigin):
        """ Translates a gRPC struct to the SDK equivalent """
        return GpsGlobalOrigin(
                
                rpcGpsGlobalOrigin.latitude_deg,
                
                
                rpcGpsGlobalOrigin.longitude_deg,
                
                
                rpcGpsGlobalOrigin.altitude_m
                )

    def translate_to_rpc(self, rpcGpsGlobalOrigin):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGpsGlobalOrigin.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcGpsGlobalOrigin.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcGpsGlobalOrigin.altitude_m = self.altitude_m
            
        
        


class Altitude:
    """
     Altitude message type

     Parameters
     ----------
     altitude_monotonic_m : float
          Altitude in meters is initialized on system boot and monotonic

     altitude_amsl_m : float
           Altitude AMSL (above mean sea level) in meters

     altitude_local_m : float
          Local altitude in meters

     altitude_relative_m : float
          Altitude above home position in meters

     altitude_terrain_m : float
          Altitude above terrain in meters

     bottom_clearance_m : float
          This is not the altitude, but the clear space below the system according to the fused clearance estimate in meters.

     """

    

    def __init__(
            self,
            altitude_monotonic_m,
            altitude_amsl_m,
            altitude_local_m,
            altitude_relative_m,
            altitude_terrain_m,
            bottom_clearance_m):
        """ Initializes the Altitude object """
        self.altitude_monotonic_m = altitude_monotonic_m
        self.altitude_amsl_m = altitude_amsl_m
        self.altitude_local_m = altitude_local_m
        self.altitude_relative_m = altitude_relative_m
        self.altitude_terrain_m = altitude_terrain_m
        self.bottom_clearance_m = bottom_clearance_m

    def __eq__(self, to_compare):
        """ Checks if two Altitude are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Altitude object
            return \
                (self.altitude_monotonic_m == to_compare.altitude_monotonic_m) and \
                (self.altitude_amsl_m == to_compare.altitude_amsl_m) and \
                (self.altitude_local_m == to_compare.altitude_local_m) and \
                (self.altitude_relative_m == to_compare.altitude_relative_m) and \
                (self.altitude_terrain_m == to_compare.altitude_terrain_m) and \
                (self.bottom_clearance_m == to_compare.bottom_clearance_m)

        except AttributeError:
            return False

    def __str__(self):
        """ Altitude in string representation """
        struct_repr = ", ".join([
                "altitude_monotonic_m: " + str(self.altitude_monotonic_m),
                "altitude_amsl_m: " + str(self.altitude_amsl_m),
                "altitude_local_m: " + str(self.altitude_local_m),
                "altitude_relative_m: " + str(self.altitude_relative_m),
                "altitude_terrain_m: " + str(self.altitude_terrain_m),
                "bottom_clearance_m: " + str(self.bottom_clearance_m)
                ])

        return f"Altitude: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAltitude):
        """ Translates a gRPC struct to the SDK equivalent """
        return Altitude(
                
                rpcAltitude.altitude_monotonic_m,
                
                
                rpcAltitude.altitude_amsl_m,
                
                
                rpcAltitude.altitude_local_m,
                
                
                rpcAltitude.altitude_relative_m,
                
                
                rpcAltitude.altitude_terrain_m,
                
                
                rpcAltitude.bottom_clearance_m
                )

    def translate_to_rpc(self, rpcAltitude):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAltitude.altitude_monotonic_m = self.altitude_monotonic_m
            
        
        
        
            
        rpcAltitude.altitude_amsl_m = self.altitude_amsl_m
            
        
        
        
            
        rpcAltitude.altitude_local_m = self.altitude_local_m
            
        
        
        
            
        rpcAltitude.altitude_relative_m = self.altitude_relative_m
            
        
        
        
            
        rpcAltitude.altitude_terrain_m = self.altitude_terrain_m
            
        
        
        
            
        rpcAltitude.bottom_clearance_m = self.bottom_clearance_m
            
        
        


class Wind:
    """
     Wind message type

     Parameters
     ----------
     wind_x_ned_m_s : float
          Wind in North (NED) direction

     wind_y_ned_m_s : float
           Wind in East (NED) direction

     wind_z_ned_m_s : float
          Wind in down (NED) direction

     horizontal_variability_stddev_m_s : float
          Variability of wind in XY, 1-STD estimated from a 1 Hz lowpassed wind estimate

     vertical_variability_stddev_m_s : float
          Variability of wind in Z, 1-STD estimated from a 1 Hz lowpassed wind estimate

     wind_altitude_msl_m : float
          Altitude (MSL) that this measurement was taken at

     horizontal_wind_speed_accuracy_m_s : float
          Horizontal speed 1-STD accuracy 

     vertical_wind_speed_accuracy_m_s : float
          Vertical speed 1-STD accuracy

     """

    

    def __init__(
            self,
            wind_x_ned_m_s,
            wind_y_ned_m_s,
            wind_z_ned_m_s,
            horizontal_variability_stddev_m_s,
            vertical_variability_stddev_m_s,
            wind_altitude_msl_m,
            horizontal_wind_speed_accuracy_m_s,
            vertical_wind_speed_accuracy_m_s):
        """ Initializes the Wind object """
        self.wind_x_ned_m_s = wind_x_ned_m_s
        self.wind_y_ned_m_s = wind_y_ned_m_s
        self.wind_z_ned_m_s = wind_z_ned_m_s
        self.horizontal_variability_stddev_m_s = horizontal_variability_stddev_m_s
        self.vertical_variability_stddev_m_s = vertical_variability_stddev_m_s
        self.wind_altitude_msl_m = wind_altitude_msl_m
        self.horizontal_wind_speed_accuracy_m_s = horizontal_wind_speed_accuracy_m_s
        self.vertical_wind_speed_accuracy_m_s = vertical_wind_speed_accuracy_m_s

    def __eq__(self, to_compare):
        """ Checks if two Wind are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Wind object
            return \
                (self.wind_x_ned_m_s == to_compare.wind_x_ned_m_s) and \
                (self.wind_y_ned_m_s == to_compare.wind_y_ned_m_s) and \
                (self.wind_z_ned_m_s == to_compare.wind_z_ned_m_s) and \
                (self.horizontal_variability_stddev_m_s == to_compare.horizontal_variability_stddev_m_s) and \
                (self.vertical_variability_stddev_m_s == to_compare.vertical_variability_stddev_m_s) and \
                (self.wind_altitude_msl_m == to_compare.wind_altitude_msl_m) and \
                (self.horizontal_wind_speed_accuracy_m_s == to_compare.horizontal_wind_speed_accuracy_m_s) and \
                (self.vertical_wind_speed_accuracy_m_s == to_compare.vertical_wind_speed_accuracy_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ Wind in string representation """
        struct_repr = ", ".join([
                "wind_x_ned_m_s: " + str(self.wind_x_ned_m_s),
                "wind_y_ned_m_s: " + str(self.wind_y_ned_m_s),
                "wind_z_ned_m_s: " + str(self.wind_z_ned_m_s),
                "horizontal_variability_stddev_m_s: " + str(self.horizontal_variability_stddev_m_s),
                "vertical_variability_stddev_m_s: " + str(self.vertical_variability_stddev_m_s),
                "wind_altitude_msl_m: " + str(self.wind_altitude_msl_m),
                "horizontal_wind_speed_accuracy_m_s: " + str(self.horizontal_wind_speed_accuracy_m_s),
                "vertical_wind_speed_accuracy_m_s: " + str(self.vertical_wind_speed_accuracy_m_s)
                ])

        return f"Wind: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcWind):
        """ Translates a gRPC struct to the SDK equivalent """
        return Wind(
                
                rpcWind.wind_x_ned_m_s,
                
                
                rpcWind.wind_y_ned_m_s,
                
                
                rpcWind.wind_z_ned_m_s,
                
                
                rpcWind.horizontal_variability_stddev_m_s,
                
                
                rpcWind.vertical_variability_stddev_m_s,
                
                
                rpcWind.wind_altitude_msl_m,
                
                
                rpcWind.horizontal_wind_speed_accuracy_m_s,
                
                
                rpcWind.vertical_wind_speed_accuracy_m_s
                )

    def translate_to_rpc(self, rpcWind):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcWind.wind_x_ned_m_s = self.wind_x_ned_m_s
            
        
        
        
            
        rpcWind.wind_y_ned_m_s = self.wind_y_ned_m_s
            
        
        
        
            
        rpcWind.wind_z_ned_m_s = self.wind_z_ned_m_s
            
        
        
        
            
        rpcWind.horizontal_variability_stddev_m_s = self.horizontal_variability_stddev_m_s
            
        
        
        
            
        rpcWind.vertical_variability_stddev_m_s = self.vertical_variability_stddev_m_s
            
        
        
        
            
        rpcWind.wind_altitude_msl_m = self.wind_altitude_msl_m
            
        
        
        
            
        rpcWind.horizontal_wind_speed_accuracy_m_s = self.horizontal_wind_speed_accuracy_m_s
            
        
        
        
            
        rpcWind.vertical_wind_speed_accuracy_m_s = self.vertical_wind_speed_accuracy_m_s
            
        
        


class TelemetryResult:
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
         Possible results returned for telemetry requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Success: the telemetry command was accepted by the vehicle

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         TIMEOUT
              Request timed out

         UNSUPPORTED
              Request not supported

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6
        UNSUPPORTED = 7

        def translate_to_rpc(self):
            if self == TelemetryResult.Result.UNKNOWN:
                return telemetry_pb2.TelemetryResult.RESULT_UNKNOWN
            if self == TelemetryResult.Result.SUCCESS:
                return telemetry_pb2.TelemetryResult.RESULT_SUCCESS
            if self == TelemetryResult.Result.NO_SYSTEM:
                return telemetry_pb2.TelemetryResult.RESULT_NO_SYSTEM
            if self == TelemetryResult.Result.CONNECTION_ERROR:
                return telemetry_pb2.TelemetryResult.RESULT_CONNECTION_ERROR
            if self == TelemetryResult.Result.BUSY:
                return telemetry_pb2.TelemetryResult.RESULT_BUSY
            if self == TelemetryResult.Result.COMMAND_DENIED:
                return telemetry_pb2.TelemetryResult.RESULT_COMMAND_DENIED
            if self == TelemetryResult.Result.TIMEOUT:
                return telemetry_pb2.TelemetryResult.RESULT_TIMEOUT
            if self == TelemetryResult.Result.UNSUPPORTED:
                return telemetry_pb2.TelemetryResult.RESULT_UNSUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_UNKNOWN:
                return TelemetryResult.Result.UNKNOWN
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_SUCCESS:
                return TelemetryResult.Result.SUCCESS
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_NO_SYSTEM:
                return TelemetryResult.Result.NO_SYSTEM
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_CONNECTION_ERROR:
                return TelemetryResult.Result.CONNECTION_ERROR
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_BUSY:
                return TelemetryResult.Result.BUSY
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_COMMAND_DENIED:
                return TelemetryResult.Result.COMMAND_DENIED
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_TIMEOUT:
                return TelemetryResult.Result.TIMEOUT
            if rpc_enum_value == telemetry_pb2.TelemetryResult.RESULT_UNSUPPORTED:
                return TelemetryResult.Result.UNSUPPORTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TelemetryResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TelemetryResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TelemetryResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TelemetryResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TelemetryResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTelemetryResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TelemetryResult(
                
                TelemetryResult.Result.translate_from_rpc(rpcTelemetryResult.result),
                
                
                rpcTelemetryResult.result_str
                )

    def translate_to_rpc(self, rpcTelemetryResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTelemetryResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTelemetryResult.result_str = self.result_str
            
        
        



class TelemetryError(Exception):
    """ Raised when a TelemetryResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Telemetry(AsyncBase):
    """
     Allow users to get vehicle telemetry and state information
     (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.

     Generated by dcsdkgen - MAVSDK Telemetry API
    """

    # Plugin name
    name = "Telemetry"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return TelemetryResult.translate_from_rpc(response.telemetry_result)
    

    async def position(self):
        """
         Subscribe to 'position' updates.

         Yields
         -------
         position : Position
              The next position

         
        """

        request = telemetry_pb2.SubscribePositionRequest()
        position_stream = self._stub.SubscribePosition(request)

        try:
            async for response in position_stream:
                

            
                yield Position.translate_from_rpc(response.position)
        finally:
            position_stream.cancel()

    async def home(self):
        """
         Subscribe to 'home position' updates.

         Yields
         -------
         home : Position
              The next home position

         
        """

        request = telemetry_pb2.SubscribeHomeRequest()
        home_stream = self._stub.SubscribeHome(request)

        try:
            async for response in home_stream:
                

            
                yield Position.translate_from_rpc(response.home)
        finally:
            home_stream.cancel()

    async def in_air(self):
        """
         Subscribe to in-air updates.

         Yields
         -------
         is_in_air : bool
              The next 'in-air' state

         
        """

        request = telemetry_pb2.SubscribeInAirRequest()
        in_air_stream = self._stub.SubscribeInAir(request)

        try:
            async for response in in_air_stream:
                

            
                yield response.is_in_air
        finally:
            in_air_stream.cancel()

    async def landed_state(self):
        """
         Subscribe to landed state updates

         Yields
         -------
         landed_state : LandedState
              The next 'landed' state

         
        """

        request = telemetry_pb2.SubscribeLandedStateRequest()
        landed_state_stream = self._stub.SubscribeLandedState(request)

        try:
            async for response in landed_state_stream:
                

            
                yield LandedState.translate_from_rpc(response.landed_state)
        finally:
            landed_state_stream.cancel()

    async def armed(self):
        """
         Subscribe to armed updates.

         Yields
         -------
         is_armed : bool
              The next 'armed' state

         
        """

        request = telemetry_pb2.SubscribeArmedRequest()
        armed_stream = self._stub.SubscribeArmed(request)

        try:
            async for response in armed_stream:
                

            
                yield response.is_armed
        finally:
            armed_stream.cancel()

    async def vtol_state(self):
        """
         subscribe to vtol state Updates

         Yields
         -------
         vtol_state : VtolState
              The next 'vtol' state

         
        """

        request = telemetry_pb2.SubscribeVtolStateRequest()
        vtol_state_stream = self._stub.SubscribeVtolState(request)

        try:
            async for response in vtol_state_stream:
                

            
                yield VtolState.translate_from_rpc(response.vtol_state)
        finally:
            vtol_state_stream.cancel()

    async def attitude_quaternion(self):
        """
         Subscribe to 'attitude' updates (quaternion).

         Yields
         -------
         attitude_quaternion : Quaternion
              The next attitude (quaternion)

         
        """

        request = telemetry_pb2.SubscribeAttitudeQuaternionRequest()
        attitude_quaternion_stream = self._stub.SubscribeAttitudeQuaternion(request)

        try:
            async for response in attitude_quaternion_stream:
                

            
                yield Quaternion.translate_from_rpc(response.attitude_quaternion)
        finally:
            attitude_quaternion_stream.cancel()

    async def attitude_euler(self):
        """
         Subscribe to 'attitude' updates (Euler).

         Yields
         -------
         attitude_euler : EulerAngle
              The next attitude (Euler)

         
        """

        request = telemetry_pb2.SubscribeAttitudeEulerRequest()
        attitude_euler_stream = self._stub.SubscribeAttitudeEuler(request)

        try:
            async for response in attitude_euler_stream:
                

            
                yield EulerAngle.translate_from_rpc(response.attitude_euler)
        finally:
            attitude_euler_stream.cancel()

    async def attitude_angular_velocity_body(self):
        """
         Subscribe to 'attitude' updates (angular velocity)

         Yields
         -------
         attitude_angular_velocity_body : AngularVelocityBody
              The next angular velocity (rad/s)

         
        """

        request = telemetry_pb2.SubscribeAttitudeAngularVelocityBodyRequest()
        attitude_angular_velocity_body_stream = self._stub.SubscribeAttitudeAngularVelocityBody(request)

        try:
            async for response in attitude_angular_velocity_body_stream:
                

            
                yield AngularVelocityBody.translate_from_rpc(response.attitude_angular_velocity_body)
        finally:
            attitude_angular_velocity_body_stream.cancel()

    async def velocity_ned(self):
        """
         Subscribe to 'ground speed' updates (NED).

         Yields
         -------
         velocity_ned : VelocityNed
              The next velocity (NED)

         
        """

        request = telemetry_pb2.SubscribeVelocityNedRequest()
        velocity_ned_stream = self._stub.SubscribeVelocityNed(request)

        try:
            async for response in velocity_ned_stream:
                

            
                yield VelocityNed.translate_from_rpc(response.velocity_ned)
        finally:
            velocity_ned_stream.cancel()

    async def gps_info(self):
        """
         Subscribe to 'GPS info' updates.

         Yields
         -------
         gps_info : GpsInfo
              The next 'GPS info' state

         
        """

        request = telemetry_pb2.SubscribeGpsInfoRequest()
        gps_info_stream = self._stub.SubscribeGpsInfo(request)

        try:
            async for response in gps_info_stream:
                

            
                yield GpsInfo.translate_from_rpc(response.gps_info)
        finally:
            gps_info_stream.cancel()

    async def raw_gps(self):
        """
         Subscribe to 'Raw GPS' updates.

         Yields
         -------
         raw_gps : RawGps
              The next 'Raw GPS' state. Warning: this is an advanced feature, use `Position` updates to get the location of the drone!

         
        """

        request = telemetry_pb2.SubscribeRawGpsRequest()
        raw_gps_stream = self._stub.SubscribeRawGps(request)

        try:
            async for response in raw_gps_stream:
                

            
                yield RawGps.translate_from_rpc(response.raw_gps)
        finally:
            raw_gps_stream.cancel()

    async def battery(self):
        """
         Subscribe to 'battery' updates.

         Yields
         -------
         battery : Battery
              The next 'battery' state

         
        """

        request = telemetry_pb2.SubscribeBatteryRequest()
        battery_stream = self._stub.SubscribeBattery(request)

        try:
            async for response in battery_stream:
                

            
                yield Battery.translate_from_rpc(response.battery)
        finally:
            battery_stream.cancel()

    async def flight_mode(self):
        """
         Subscribe to 'flight mode' updates.

         Yields
         -------
         flight_mode : FlightMode
              The next flight mode

         
        """

        request = telemetry_pb2.SubscribeFlightModeRequest()
        flight_mode_stream = self._stub.SubscribeFlightMode(request)

        try:
            async for response in flight_mode_stream:
                

            
                yield FlightMode.translate_from_rpc(response.flight_mode)
        finally:
            flight_mode_stream.cancel()

    async def health(self):
        """
         Subscribe to 'health' updates.

         Yields
         -------
         health : Health
              The next 'health' state

         
        """

        request = telemetry_pb2.SubscribeHealthRequest()
        health_stream = self._stub.SubscribeHealth(request)

        try:
            async for response in health_stream:
                

            
                yield Health.translate_from_rpc(response.health)
        finally:
            health_stream.cancel()

    async def rc_status(self):
        """
         Subscribe to 'RC status' updates.

         Yields
         -------
         rc_status : RcStatus
              The next RC status

         
        """

        request = telemetry_pb2.SubscribeRcStatusRequest()
        rc_status_stream = self._stub.SubscribeRcStatus(request)

        try:
            async for response in rc_status_stream:
                

            
                yield RcStatus.translate_from_rpc(response.rc_status)
        finally:
            rc_status_stream.cancel()

    async def status_text(self):
        """
         Subscribe to 'status text' updates.

         Yields
         -------
         status_text : StatusText
              The next 'status text'

         
        """

        request = telemetry_pb2.SubscribeStatusTextRequest()
        status_text_stream = self._stub.SubscribeStatusText(request)

        try:
            async for response in status_text_stream:
                

            
                yield StatusText.translate_from_rpc(response.status_text)
        finally:
            status_text_stream.cancel()

    async def actuator_control_target(self):
        """
         Subscribe to 'actuator control target' updates.

         Yields
         -------
         actuator_control_target : ActuatorControlTarget
              The next actuator control target

         
        """

        request = telemetry_pb2.SubscribeActuatorControlTargetRequest()
        actuator_control_target_stream = self._stub.SubscribeActuatorControlTarget(request)

        try:
            async for response in actuator_control_target_stream:
                

            
                yield ActuatorControlTarget.translate_from_rpc(response.actuator_control_target)
        finally:
            actuator_control_target_stream.cancel()

    async def actuator_output_status(self):
        """
         Subscribe to 'actuator output status' updates.

         Yields
         -------
         actuator_output_status : ActuatorOutputStatus
              The next actuator output status

         
        """

        request = telemetry_pb2.SubscribeActuatorOutputStatusRequest()
        actuator_output_status_stream = self._stub.SubscribeActuatorOutputStatus(request)

        try:
            async for response in actuator_output_status_stream:
                

            
                yield ActuatorOutputStatus.translate_from_rpc(response.actuator_output_status)
        finally:
            actuator_output_status_stream.cancel()

    async def odometry(self):
        """
         Subscribe to 'odometry' updates.

         Yields
         -------
         odometry : Odometry
              The next odometry status

         
        """

        request = telemetry_pb2.SubscribeOdometryRequest()
        odometry_stream = self._stub.SubscribeOdometry(request)

        try:
            async for response in odometry_stream:
                

            
                yield Odometry.translate_from_rpc(response.odometry)
        finally:
            odometry_stream.cancel()

    async def position_velocity_ned(self):
        """
         Subscribe to 'position velocity' updates.

         Yields
         -------
         position_velocity_ned : PositionVelocityNed
              The next position and velocity status

         
        """

        request = telemetry_pb2.SubscribePositionVelocityNedRequest()
        position_velocity_ned_stream = self._stub.SubscribePositionVelocityNed(request)

        try:
            async for response in position_velocity_ned_stream:
                

            
                yield PositionVelocityNed.translate_from_rpc(response.position_velocity_ned)
        finally:
            position_velocity_ned_stream.cancel()

    async def ground_truth(self):
        """
         Subscribe to 'ground truth' updates.

         Yields
         -------
         ground_truth : GroundTruth
              Ground truth position information available in simulation

         
        """

        request = telemetry_pb2.SubscribeGroundTruthRequest()
        ground_truth_stream = self._stub.SubscribeGroundTruth(request)

        try:
            async for response in ground_truth_stream:
                

            
                yield GroundTruth.translate_from_rpc(response.ground_truth)
        finally:
            ground_truth_stream.cancel()

    async def fixedwing_metrics(self):
        """
         Subscribe to 'fixedwing metrics' updates.

         Yields
         -------
         fixedwing_metrics : FixedwingMetrics
              The next fixedwing metrics

         
        """

        request = telemetry_pb2.SubscribeFixedwingMetricsRequest()
        fixedwing_metrics_stream = self._stub.SubscribeFixedwingMetrics(request)

        try:
            async for response in fixedwing_metrics_stream:
                

            
                yield FixedwingMetrics.translate_from_rpc(response.fixedwing_metrics)
        finally:
            fixedwing_metrics_stream.cancel()

    async def imu(self):
        """
         Subscribe to 'IMU' updates (in SI units in NED body frame).

         Yields
         -------
         imu : Imu
              The next IMU status

         
        """

        request = telemetry_pb2.SubscribeImuRequest()
        imu_stream = self._stub.SubscribeImu(request)

        try:
            async for response in imu_stream:
                

            
                yield Imu.translate_from_rpc(response.imu)
        finally:
            imu_stream.cancel()

    async def scaled_imu(self):
        """
         Subscribe to 'Scaled IMU' updates.

         Yields
         -------
         imu : Imu
              The next scaled IMU status

         
        """

        request = telemetry_pb2.SubscribeScaledImuRequest()
        scaled_imu_stream = self._stub.SubscribeScaledImu(request)

        try:
            async for response in scaled_imu_stream:
                

            
                yield Imu.translate_from_rpc(response.imu)
        finally:
            scaled_imu_stream.cancel()

    async def raw_imu(self):
        """
         Subscribe to 'Raw IMU' updates (note that units are are incorrect and "raw" as provided by the sensor)

         Yields
         -------
         imu : Imu
              The next raw IMU status

         
        """

        request = telemetry_pb2.SubscribeRawImuRequest()
        raw_imu_stream = self._stub.SubscribeRawImu(request)

        try:
            async for response in raw_imu_stream:
                

            
                yield Imu.translate_from_rpc(response.imu)
        finally:
            raw_imu_stream.cancel()

    async def health_all_ok(self):
        """
         Subscribe to 'HealthAllOk' updates.

         Yields
         -------
         is_health_all_ok : bool
              The next 'health all ok' status

         
        """

        request = telemetry_pb2.SubscribeHealthAllOkRequest()
        health_all_ok_stream = self._stub.SubscribeHealthAllOk(request)

        try:
            async for response in health_all_ok_stream:
                

            
                yield response.is_health_all_ok
        finally:
            health_all_ok_stream.cancel()

    async def unix_epoch_time(self):
        """
         Subscribe to 'unix epoch time' updates.

         Yields
         -------
         time_us : uint64_t
              The next 'unix epoch time' status

         
        """

        request = telemetry_pb2.SubscribeUnixEpochTimeRequest()
        unix_epoch_time_stream = self._stub.SubscribeUnixEpochTime(request)

        try:
            async for response in unix_epoch_time_stream:
                

            
                yield response.time_us
        finally:
            unix_epoch_time_stream.cancel()

    async def distance_sensor(self):
        """
         Subscribe to 'Distance Sensor' updates.

         Yields
         -------
         distance_sensor : DistanceSensor
              The next Distance Sensor status

         
        """

        request = telemetry_pb2.SubscribeDistanceSensorRequest()
        distance_sensor_stream = self._stub.SubscribeDistanceSensor(request)

        try:
            async for response in distance_sensor_stream:
                

            
                yield DistanceSensor.translate_from_rpc(response.distance_sensor)
        finally:
            distance_sensor_stream.cancel()

    async def scaled_pressure(self):
        """
         Subscribe to 'Scaled Pressure' updates.

         Yields
         -------
         scaled_pressure : ScaledPressure
              The next Scaled Pressure status

         
        """

        request = telemetry_pb2.SubscribeScaledPressureRequest()
        scaled_pressure_stream = self._stub.SubscribeScaledPressure(request)

        try:
            async for response in scaled_pressure_stream:
                

            
                yield ScaledPressure.translate_from_rpc(response.scaled_pressure)
        finally:
            scaled_pressure_stream.cancel()

    async def heading(self):
        """
         Subscribe to 'Heading' updates.

         Yields
         -------
         heading_deg : Heading
              The next heading (yaw) in degrees

         
        """

        request = telemetry_pb2.SubscribeHeadingRequest()
        heading_stream = self._stub.SubscribeHeading(request)

        try:
            async for response in heading_stream:
                

            
                yield Heading.translate_from_rpc(response.heading_deg)
        finally:
            heading_stream.cancel()

    async def altitude(self):
        """
         Subscribe to 'Altitude' updates.

         Yields
         -------
         altitude : Altitude
              The next altitude

         
        """

        request = telemetry_pb2.SubscribeAltitudeRequest()
        altitude_stream = self._stub.SubscribeAltitude(request)

        try:
            async for response in altitude_stream:
                

            
                yield Altitude.translate_from_rpc(response.altitude)
        finally:
            altitude_stream.cancel()

    async def wind(self):
        """
         Subscribe to 'Wind Estimated' updates.

         Yields
         -------
         wind : Wind
              The next wind

         
        """

        request = telemetry_pb2.SubscribeWindRequest()
        wind_stream = self._stub.SubscribeWind(request)

        try:
            async for response in wind_stream:
                

            
                yield Wind.translate_from_rpc(response.wind)
        finally:
            wind_stream.cancel()

    async def set_rate_position(self, rate_hz):
        """
         Set rate to 'position' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRatePositionRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRatePosition(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_position()", rate_hz)
        

    async def set_rate_home(self, rate_hz):
        """
         Set rate to 'home position' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateHomeRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateHome(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_home()", rate_hz)
        

    async def set_rate_in_air(self, rate_hz):
        """
         Set rate to in-air updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateInAirRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateInAir(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_in_air()", rate_hz)
        

    async def set_rate_landed_state(self, rate_hz):
        """
         Set rate to landed state updates

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateLandedStateRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateLandedState(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_landed_state()", rate_hz)
        

    async def set_rate_vtol_state(self, rate_hz):
        """
         Set rate to VTOL state updates

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateVtolStateRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateVtolState(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_vtol_state()", rate_hz)
        

    async def set_rate_attitude_quaternion(self, rate_hz):
        """
         Set rate to 'attitude euler angle' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateAttitudeQuaternionRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateAttitudeQuaternion(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_attitude_quaternion()", rate_hz)
        

    async def set_rate_attitude_euler(self, rate_hz):
        """
         Set rate to 'attitude quaternion' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateAttitudeEulerRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateAttitudeEuler(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_attitude_euler()", rate_hz)
        

    async def set_rate_velocity_ned(self, rate_hz):
        """
         Set rate of camera attitude updates.
         Set rate to 'ground speed' updates (NED).

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateVelocityNedRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateVelocityNed(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_velocity_ned()", rate_hz)
        

    async def set_rate_gps_info(self, rate_hz):
        """
         Set rate to 'GPS info' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateGpsInfoRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateGpsInfo(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_gps_info()", rate_hz)
        

    async def set_rate_battery(self, rate_hz):
        """
         Set rate to 'battery' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateBatteryRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateBattery(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_battery()", rate_hz)
        

    async def set_rate_rc_status(self, rate_hz):
        """
         Set rate to 'RC status' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateRcStatusRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateRcStatus(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_rc_status()", rate_hz)
        

    async def set_rate_actuator_control_target(self, rate_hz):
        """
         Set rate to 'actuator control target' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateActuatorControlTargetRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateActuatorControlTarget(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_actuator_control_target()", rate_hz)
        

    async def set_rate_actuator_output_status(self, rate_hz):
        """
         Set rate to 'actuator output status' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateActuatorOutputStatusRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateActuatorOutputStatus(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_actuator_output_status()", rate_hz)
        

    async def set_rate_odometry(self, rate_hz):
        """
         Set rate to 'odometry' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateOdometryRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateOdometry(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_odometry()", rate_hz)
        

    async def set_rate_position_velocity_ned(self, rate_hz):
        """
         Set rate to 'position velocity' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRatePositionVelocityNedRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRatePositionVelocityNed(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_position_velocity_ned()", rate_hz)
        

    async def set_rate_ground_truth(self, rate_hz):
        """
         Set rate to 'ground truth' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateGroundTruthRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateGroundTruth(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_ground_truth()", rate_hz)
        

    async def set_rate_fixedwing_metrics(self, rate_hz):
        """
         Set rate to 'fixedwing metrics' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateFixedwingMetricsRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateFixedwingMetrics(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_fixedwing_metrics()", rate_hz)
        

    async def set_rate_imu(self, rate_hz):
        """
         Set rate to 'IMU' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateImuRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_imu()", rate_hz)
        

    async def set_rate_scaled_imu(self, rate_hz):
        """
         Set rate to 'Scaled IMU' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateScaledImuRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateScaledImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_scaled_imu()", rate_hz)
        

    async def set_rate_raw_imu(self, rate_hz):
        """
         Set rate to 'Raw IMU' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateRawImuRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateRawImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_raw_imu()", rate_hz)
        

    async def set_rate_unix_epoch_time(self, rate_hz):
        """
         Set rate to 'unix epoch time' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateUnixEpochTimeRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateUnixEpochTime(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_unix_epoch_time()", rate_hz)
        

    async def set_rate_distance_sensor(self, rate_hz):
        """
         Set rate to 'Distance Sensor' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateDistanceSensorRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateDistanceSensor(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_distance_sensor()", rate_hz)
        

    async def set_rate_altitude(self, rate_hz):
        """
         Set rate to 'Altitude' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateAltitudeRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateAltitude(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_altitude()", rate_hz)
        

    async def set_rate_health(self, rate_hz):
        """
         Set rate to 'Health' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.SetRateHealthRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateHealth(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "set_rate_health()", rate_hz)
        

    async def get_gps_global_origin(self):
        """
         Get the GPS location of where the estimator has been initialized.

         Returns
         -------
         gps_global_origin : GpsGlobalOrigin
             
         Raises
         ------
         TelemetryError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_pb2.GetGpsGlobalOriginRequest()
        response = await self._stub.GetGpsGlobalOrigin(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryResult.Result.SUCCESS:
            raise TelemetryError(result, "get_gps_global_origin()")
        

        return GpsGlobalOrigin.translate_from_rpc(response.gps_global_origin)
            