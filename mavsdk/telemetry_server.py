# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import telemetry_server_pb2, telemetry_server_pb2_grpc
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
            return telemetry_server_pb2.FIX_TYPE_NO_GPS
        if self == FixType.NO_FIX:
            return telemetry_server_pb2.FIX_TYPE_NO_FIX
        if self == FixType.FIX_2D:
            return telemetry_server_pb2.FIX_TYPE_FIX_2D
        if self == FixType.FIX_3D:
            return telemetry_server_pb2.FIX_TYPE_FIX_3D
        if self == FixType.FIX_DGPS:
            return telemetry_server_pb2.FIX_TYPE_FIX_DGPS
        if self == FixType.RTK_FLOAT:
            return telemetry_server_pb2.FIX_TYPE_RTK_FLOAT
        if self == FixType.RTK_FIXED:
            return telemetry_server_pb2.FIX_TYPE_RTK_FIXED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_NO_GPS:
            return FixType.NO_GPS
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_NO_FIX:
            return FixType.NO_FIX
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_FIX_2D:
            return FixType.FIX_2D
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_FIX_3D:
            return FixType.FIX_3D
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_FIX_DGPS:
            return FixType.FIX_DGPS
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_RTK_FLOAT:
            return FixType.RTK_FLOAT
        if rpc_enum_value == telemetry_server_pb2.FIX_TYPE_RTK_FIXED:
            return FixType.RTK_FIXED

    def __str__(self):
        return self.name


class VtolState(Enum):
    """
     Maps to MAV_VTOL_STATE

     Values
     ------
     UNDEFINED
          Not VTOL

     TRANSITION_TO_FW
          Transitioning to fixed-wing

     TRANSITION_TO_MC
          Transitioning to multi-copter

     MC
          Multi-copter

     FW
          Fixed-wing

     """

    
    UNDEFINED = 0
    TRANSITION_TO_FW = 1
    TRANSITION_TO_MC = 2
    MC = 3
    FW = 4

    def translate_to_rpc(self):
        if self == VtolState.UNDEFINED:
            return telemetry_server_pb2.VTOL_STATE_UNDEFINED
        if self == VtolState.TRANSITION_TO_FW:
            return telemetry_server_pb2.VTOL_STATE_TRANSITION_TO_FW
        if self == VtolState.TRANSITION_TO_MC:
            return telemetry_server_pb2.VTOL_STATE_TRANSITION_TO_MC
        if self == VtolState.MC:
            return telemetry_server_pb2.VTOL_STATE_MC
        if self == VtolState.FW:
            return telemetry_server_pb2.VTOL_STATE_FW

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_server_pb2.VTOL_STATE_UNDEFINED:
            return VtolState.UNDEFINED
        if rpc_enum_value == telemetry_server_pb2.VTOL_STATE_TRANSITION_TO_FW:
            return VtolState.TRANSITION_TO_FW
        if rpc_enum_value == telemetry_server_pb2.VTOL_STATE_TRANSITION_TO_MC:
            return VtolState.TRANSITION_TO_MC
        if rpc_enum_value == telemetry_server_pb2.VTOL_STATE_MC:
            return VtolState.MC
        if rpc_enum_value == telemetry_server_pb2.VTOL_STATE_FW:
            return VtolState.FW

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
            return telemetry_server_pb2.STATUS_TEXT_TYPE_DEBUG
        if self == StatusTextType.INFO:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_INFO
        if self == StatusTextType.NOTICE:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_NOTICE
        if self == StatusTextType.WARNING:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_WARNING
        if self == StatusTextType.ERROR:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_ERROR
        if self == StatusTextType.CRITICAL:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_CRITICAL
        if self == StatusTextType.ALERT:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_ALERT
        if self == StatusTextType.EMERGENCY:
            return telemetry_server_pb2.STATUS_TEXT_TYPE_EMERGENCY

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_DEBUG:
            return StatusTextType.DEBUG
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_INFO:
            return StatusTextType.INFO
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_NOTICE:
            return StatusTextType.NOTICE
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_WARNING:
            return StatusTextType.WARNING
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_ERROR:
            return StatusTextType.ERROR
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_CRITICAL:
            return StatusTextType.CRITICAL
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_ALERT:
            return StatusTextType.ALERT
        if rpc_enum_value == telemetry_server_pb2.STATUS_TEXT_TYPE_EMERGENCY:
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
            return telemetry_server_pb2.LANDED_STATE_UNKNOWN
        if self == LandedState.ON_GROUND:
            return telemetry_server_pb2.LANDED_STATE_ON_GROUND
        if self == LandedState.IN_AIR:
            return telemetry_server_pb2.LANDED_STATE_IN_AIR
        if self == LandedState.TAKING_OFF:
            return telemetry_server_pb2.LANDED_STATE_TAKING_OFF
        if self == LandedState.LANDING:
            return telemetry_server_pb2.LANDED_STATE_LANDING

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == telemetry_server_pb2.LANDED_STATE_UNKNOWN:
            return LandedState.UNKNOWN
        if rpc_enum_value == telemetry_server_pb2.LANDED_STATE_ON_GROUND:
            return LandedState.ON_GROUND
        if rpc_enum_value == telemetry_server_pb2.LANDED_STATE_IN_AIR:
            return LandedState.IN_AIR
        if rpc_enum_value == telemetry_server_pb2.LANDED_STATE_TAKING_OFF:
            return LandedState.TAKING_OFF
        if rpc_enum_value == telemetry_server_pb2.LANDED_STATE_LANDING:
            return LandedState.LANDING

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
     voltage_v : float
          Voltage in volts

     remaining_percent : float
          Estimated battery remaining (range: 0.0 to 1.0)

     """

    

    def __init__(
            self,
            voltage_v,
            remaining_percent):
        """ Initializes the Battery object """
        self.voltage_v = voltage_v
        self.remaining_percent = remaining_percent

    def __eq__(self, to_compare):
        """ Checks if two Battery are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Battery object
            return \
                (self.voltage_v == to_compare.voltage_v) and \
                (self.remaining_percent == to_compare.remaining_percent)

        except AttributeError:
            return False

    def __str__(self):
        """ Battery in string representation """
        struct_repr = ", ".join([
                "voltage_v: " + str(self.voltage_v),
                "remaining_percent: " + str(self.remaining_percent)
                ])

        return f"Battery: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcBattery):
        """ Translates a gRPC struct to the SDK equivalent """
        return Battery(
                
                rpcBattery.voltage_v,
                
                
                rpcBattery.remaining_percent
                )

    def translate_to_rpc(self, rpcBattery):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcBattery.voltage_v = self.voltage_v
            
        
        
        
            
        rpcBattery.remaining_percent = self.remaining_percent
            
        
        


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
                return telemetry_server_pb2.Odometry.MAV_FRAME_UNDEF
            if self == Odometry.MavFrame.BODY_NED:
                return telemetry_server_pb2.Odometry.MAV_FRAME_BODY_NED
            if self == Odometry.MavFrame.VISION_NED:
                return telemetry_server_pb2.Odometry.MAV_FRAME_VISION_NED
            if self == Odometry.MavFrame.ESTIM_NED:
                return telemetry_server_pb2.Odometry.MAV_FRAME_ESTIM_NED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == telemetry_server_pb2.Odometry.MAV_FRAME_UNDEF:
                return Odometry.MavFrame.UNDEF
            if rpc_enum_value == telemetry_server_pb2.Odometry.MAV_FRAME_BODY_NED:
                return Odometry.MavFrame.BODY_NED
            if rpc_enum_value == telemetry_server_pb2.Odometry.MAV_FRAME_VISION_NED:
                return Odometry.MavFrame.VISION_NED
            if rpc_enum_value == telemetry_server_pb2.Odometry.MAV_FRAME_ESTIM_NED:
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

     """

    

    def __init__(
            self,
            minimum_distance_m,
            maximum_distance_m,
            current_distance_m):
        """ Initializes the DistanceSensor object """
        self.minimum_distance_m = minimum_distance_m
        self.maximum_distance_m = maximum_distance_m
        self.current_distance_m = current_distance_m

    def __eq__(self, to_compare):
        """ Checks if two DistanceSensor are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # DistanceSensor object
            return \
                (self.minimum_distance_m == to_compare.minimum_distance_m) and \
                (self.maximum_distance_m == to_compare.maximum_distance_m) and \
                (self.current_distance_m == to_compare.current_distance_m)

        except AttributeError:
            return False

    def __str__(self):
        """ DistanceSensor in string representation """
        struct_repr = ", ".join([
                "minimum_distance_m: " + str(self.minimum_distance_m),
                "maximum_distance_m: " + str(self.maximum_distance_m),
                "current_distance_m: " + str(self.current_distance_m)
                ])

        return f"DistanceSensor: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcDistanceSensor):
        """ Translates a gRPC struct to the SDK equivalent """
        return DistanceSensor(
                
                rpcDistanceSensor.minimum_distance_m,
                
                
                rpcDistanceSensor.maximum_distance_m,
                
                
                rpcDistanceSensor.current_distance_m
                )

    def translate_to_rpc(self, rpcDistanceSensor):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcDistanceSensor.minimum_distance_m = self.minimum_distance_m
            
        
        
        
            
        rpcDistanceSensor.maximum_distance_m = self.maximum_distance_m
            
        
        
        
            
        rpcDistanceSensor.current_distance_m = self.current_distance_m
            
        
        


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
            
        
        


class TelemetryServerResult:
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
            if self == TelemetryServerResult.Result.UNKNOWN:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_UNKNOWN
            if self == TelemetryServerResult.Result.SUCCESS:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_SUCCESS
            if self == TelemetryServerResult.Result.NO_SYSTEM:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_NO_SYSTEM
            if self == TelemetryServerResult.Result.CONNECTION_ERROR:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_CONNECTION_ERROR
            if self == TelemetryServerResult.Result.BUSY:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_BUSY
            if self == TelemetryServerResult.Result.COMMAND_DENIED:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_COMMAND_DENIED
            if self == TelemetryServerResult.Result.TIMEOUT:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_TIMEOUT
            if self == TelemetryServerResult.Result.UNSUPPORTED:
                return telemetry_server_pb2.TelemetryServerResult.RESULT_UNSUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_UNKNOWN:
                return TelemetryServerResult.Result.UNKNOWN
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_SUCCESS:
                return TelemetryServerResult.Result.SUCCESS
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_NO_SYSTEM:
                return TelemetryServerResult.Result.NO_SYSTEM
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_CONNECTION_ERROR:
                return TelemetryServerResult.Result.CONNECTION_ERROR
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_BUSY:
                return TelemetryServerResult.Result.BUSY
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_COMMAND_DENIED:
                return TelemetryServerResult.Result.COMMAND_DENIED
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_TIMEOUT:
                return TelemetryServerResult.Result.TIMEOUT
            if rpc_enum_value == telemetry_server_pb2.TelemetryServerResult.RESULT_UNSUPPORTED:
                return TelemetryServerResult.Result.UNSUPPORTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TelemetryServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TelemetryServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TelemetryServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TelemetryServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TelemetryServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTelemetryServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TelemetryServerResult(
                
                TelemetryServerResult.Result.translate_from_rpc(rpcTelemetryServerResult.result),
                
                
                rpcTelemetryServerResult.result_str
                )

    def translate_to_rpc(self, rpcTelemetryServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTelemetryServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTelemetryServerResult.result_str = self.result_str
            
        
        



class TelemetryServerError(Exception):
    """ Raised when a TelemetryServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class TelemetryServer(AsyncBase):
    """
     Allow users to provide vehicle telemetry and state information
     (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.

     Generated by dcsdkgen - MAVSDK TelemetryServer API
    """

    # Plugin name
    name = "TelemetryServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = telemetry_server_pb2_grpc.TelemetryServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return TelemetryServerResult.translate_from_rpc(response.telemetry_server_result)
    

    async def publish_position(self, position, velocity_ned, heading):
        """
         Publish to 'position' updates.

         Parameters
         ----------
         position : Position
              The next position

         velocity_ned : VelocityNed
              The next velocity (NED)

         heading : Heading
              Heading (yaw) in degrees

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishPositionRequest()
        
        position.translate_to_rpc(request.position)
                
            
        
        velocity_ned.translate_to_rpc(request.velocity_ned)
                
            
        
        heading.translate_to_rpc(request.heading)
                
            
        response = await self._stub.PublishPosition(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_position()", position, velocity_ned, heading)
        

    async def publish_home(self, home):
        """
         Publish to 'home position' updates.

         Parameters
         ----------
         home : Position
              The next home position

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishHomeRequest()
        
        home.translate_to_rpc(request.home)
                
            
        response = await self._stub.PublishHome(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_home()", home)
        

    async def publish_sys_status(self, battery, rc_receiver_status, gyro_status, accel_status, mag_status, gps_status):
        """
         Publish 'sys status' updates.

         Parameters
         ----------
         battery : Battery
              The next 'battery' state

         rc_receiver_status : bool
              rc receiver status

         gyro_status : bool
             
         accel_status : bool
             
         mag_status : bool
             
         gps_status : bool
             
         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishSysStatusRequest()
        
        battery.translate_to_rpc(request.battery)
                
            
        request.rc_receiver_status = rc_receiver_status
        request.gyro_status = gyro_status
        request.accel_status = accel_status
        request.mag_status = mag_status
        request.gps_status = gps_status
        response = await self._stub.PublishSysStatus(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_sys_status()", battery, rc_receiver_status, gyro_status, accel_status, mag_status, gps_status)
        

    async def publish_extended_sys_state(self, vtol_state, landed_state):
        """
         Publish 'extended sys state' updates.

         Parameters
         ----------
         vtol_state : VtolState
             
         landed_state : LandedState
             
         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishExtendedSysStateRequest()
        
        request.vtol_state = vtol_state.translate_to_rpc()
                
            
        
        request.landed_state = landed_state.translate_to_rpc()
                
            
        response = await self._stub.PublishExtendedSysState(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_extended_sys_state()", vtol_state, landed_state)
        

    async def publish_raw_gps(self, raw_gps, gps_info):
        """
         Publish to 'Raw GPS' updates.

         Parameters
         ----------
         raw_gps : RawGps
              The next 'Raw GPS' state. Warning: this is an advanced feature, use `Position` updates to get the location of the drone!

         gps_info : GpsInfo
              The next 'GPS info' state

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishRawGpsRequest()
        
        raw_gps.translate_to_rpc(request.raw_gps)
                
            
        
        gps_info.translate_to_rpc(request.gps_info)
                
            
        response = await self._stub.PublishRawGps(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_raw_gps()", raw_gps, gps_info)
        

    async def publish_battery(self, battery):
        """
         Publish to 'battery' updates.

         Parameters
         ----------
         battery : Battery
              The next 'battery' state

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishBatteryRequest()
        
        battery.translate_to_rpc(request.battery)
                
            
        response = await self._stub.PublishBattery(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_battery()", battery)
        

    async def publish_status_text(self, status_text):
        """
         Publish to 'status text' updates.

         Parameters
         ----------
         status_text : StatusText
              The next 'status text'

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishStatusTextRequest()
        
        status_text.translate_to_rpc(request.status_text)
                
            
        response = await self._stub.PublishStatusText(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_status_text()", status_text)
        

    async def publish_odometry(self, odometry):
        """
         Publish to 'odometry' updates.

         Parameters
         ----------
         odometry : Odometry
              The next odometry status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishOdometryRequest()
        
        odometry.translate_to_rpc(request.odometry)
                
            
        response = await self._stub.PublishOdometry(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_odometry()", odometry)
        

    async def publish_position_velocity_ned(self, position_velocity_ned):
        """
         Publish to 'position velocity' updates.

         Parameters
         ----------
         position_velocity_ned : PositionVelocityNed
              The next position and velocity status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishPositionVelocityNedRequest()
        
        position_velocity_ned.translate_to_rpc(request.position_velocity_ned)
                
            
        response = await self._stub.PublishPositionVelocityNed(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_position_velocity_ned()", position_velocity_ned)
        

    async def publish_ground_truth(self, ground_truth):
        """
         Publish to 'ground truth' updates.

         Parameters
         ----------
         ground_truth : GroundTruth
              Ground truth position information available in simulation

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishGroundTruthRequest()
        
        ground_truth.translate_to_rpc(request.ground_truth)
                
            
        response = await self._stub.PublishGroundTruth(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_ground_truth()", ground_truth)
        

    async def publish_imu(self, imu):
        """
         Publish to 'IMU' updates (in SI units in NED body frame).

         Parameters
         ----------
         imu : Imu
              The next IMU status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishImuRequest()
        
        imu.translate_to_rpc(request.imu)
                
            
        response = await self._stub.PublishImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_imu()", imu)
        

    async def publish_scaled_imu(self, imu):
        """
         Publish to 'Scaled IMU' updates.

         Parameters
         ----------
         imu : Imu
              The next scaled IMU status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishScaledImuRequest()
        
        imu.translate_to_rpc(request.imu)
                
            
        response = await self._stub.PublishScaledImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_scaled_imu()", imu)
        

    async def publish_raw_imu(self, imu):
        """
         Publish to 'Raw IMU' updates.

         Parameters
         ----------
         imu : Imu
              The next raw IMU status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishRawImuRequest()
        
        imu.translate_to_rpc(request.imu)
                
            
        response = await self._stub.PublishRawImu(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_raw_imu()", imu)
        

    async def publish_unix_epoch_time(self, time_us):
        """
         Publish to 'unix epoch time' updates.

         Parameters
         ----------
         time_us : uint64_t
              The next 'unix epoch time' status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishUnixEpochTimeRequest()
        request.time_us = time_us
        response = await self._stub.PublishUnixEpochTime(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_unix_epoch_time()", time_us)
        

    async def publish_distance_sensor(self, distance_sensor):
        """
         Publish to "distance sensor" updates.

         Parameters
         ----------
         distance_sensor : DistanceSensor
              The next 'Distance Sensor' status

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishDistanceSensorRequest()
        
        distance_sensor.translate_to_rpc(request.distance_sensor)
                
            
        response = await self._stub.PublishDistanceSensor(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_distance_sensor()", distance_sensor)
        

    async def publish_attitude(self, angle, angular_velocity):
        """
         Publish to "attitude" updates.

         Parameters
         ----------
         angle : EulerAngle
              roll/pitch/yaw body angles

         angular_velocity : AngularVelocityBody
              roll/pitch/yaw angular velocities

         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishAttitudeRequest()
        
        angle.translate_to_rpc(request.angle)
                
            
        
        angular_velocity.translate_to_rpc(request.angular_velocity)
                
            
        response = await self._stub.PublishAttitude(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_attitude()", angle, angular_velocity)
        

    async def publish_visual_flight_rules_hud(self, fixed_wing_metrics):
        """
         Publish to "Visual Flight Rules HUD" updates.

         Parameters
         ----------
         fixed_wing_metrics : FixedwingMetrics
             
         Raises
         ------
         TelemetryServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = telemetry_server_pb2.PublishVisualFlightRulesHudRequest()
        
        fixed_wing_metrics.translate_to_rpc(request.fixed_wing_metrics)
                
            
        response = await self._stub.PublishVisualFlightRulesHud(request)

        
        result = self._extract_result(response)

        if result.result != TelemetryServerResult.Result.SUCCESS:
            raise TelemetryServerError(result, "publish_visual_flight_rules_hud()", fixed_wing_metrics)
        