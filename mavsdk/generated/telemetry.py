# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import telemetry_pb2, telemetry_pb2_grpc
from enum import Enum


class FixType(Enum):
    """
     Fix type.

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

    def translate_to_rpc(self, rpcFixType):
        return {
                0: telemetry_pb2.NO_GPS,
                1: telemetry_pb2.NO_FIX,
                2: telemetry_pb2.FIX_2D,
                3: telemetry_pb2.FIX_3D,
                4: telemetry_pb2.FIX_DGPS,
                5: telemetry_pb2.RTK_FLOAT,
                6: telemetry_pb2.RTK_FIXED
            }.get(self.value, None)

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        return {
                0: FixType.NO_GPS,
                1: FixType.NO_FIX,
                2: FixType.FIX_2D,
                3: FixType.FIX_3D,
                4: FixType.FIX_DGPS,
                5: FixType.RTK_FLOAT,
                6: FixType.RTK_FIXED,
            }.get(rpc_enum_value, None)

    def __str__(self):
        return self.name


class FlightMode(Enum):
    """
     Flight modes.

     For more information about flight modes, check out
     https://docs.px4.io/en/config/flight_mode.html.

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

    def translate_to_rpc(self, rpcFlightMode):
        return {
                0: telemetry_pb2.UNKNOWN,
                1: telemetry_pb2.READY,
                2: telemetry_pb2.TAKEOFF,
                3: telemetry_pb2.HOLD,
                4: telemetry_pb2.MISSION,
                5: telemetry_pb2.RETURN_TO_LAUNCH,
                6: telemetry_pb2.LAND,
                7: telemetry_pb2.OFFBOARD,
                8: telemetry_pb2.FOLLOW_ME
            }.get(self.value, None)

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        return {
                0: FlightMode.UNKNOWN,
                1: FlightMode.READY,
                2: FlightMode.TAKEOFF,
                3: FlightMode.HOLD,
                4: FlightMode.MISSION,
                5: FlightMode.RETURN_TO_LAUNCH,
                6: FlightMode.LAND,
                7: FlightMode.OFFBOARD,
                8: FlightMode.FOLLOW_ME,
            }.get(rpc_enum_value, None)

    def __str__(self):
        return self.name


class LandedState(Enum):
    """
     Landed State enumeration

     Values
     ------
     LANDED_STATE_UNKNOWN

     LANDED_STATE_ON_GROUND

     LANDED_STATE_IN_AIR

     LANDED_STATE_TAKING_OFF

     LANDED_STATE_LANDING

     """


    LANDED_STATE_UNKNOWN = 0
    LANDED_STATE_ON_GROUND = 1
    LANDED_STATE_IN_AIR = 2
    LANDED_STATE_TAKING_OFF = 3
    LANDED_STATE_LANDING = 4

    def translate_to_rpc(self, rpcLandedState):
        return {
                0: telemetry_pb2.LANDED_STATE_UNKNOWN,
                1: telemetry_pb2.LANDED_STATE_ON_GROUND,
                2: telemetry_pb2.LANDED_STATE_IN_AIR,
                3: telemetry_pb2.LANDED_STATE_TAKING_OFF,
                4: telemetry_pb2.LANDED_STATE_LANDING
            }.get(self.value, None)

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        return {
                0: LandedState.LANDED_STATE_UNKNOWN,
                1: LandedState.LANDED_STATE_ON_GROUND,
                2: LandedState.LANDED_STATE_IN_AIR,
                3: LandedState.LANDED_STATE_TAKING_OFF,
                4: LandedState.LANDED_STATE_LANDING,
            }.get(rpc_enum_value, None)

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

    def __equals__(self, to_compare):
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

     """



    def __init__(
            self,
            w,
            x,
            y,
            z):
        """ Initializes the Quaternion object """
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __equals__(self, to_compare):
        """ Checks if two Quaternion are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Quaternion object
            return \
                (self.w == to_compare.w) and \
                (self.x == to_compare.x) and \
                (self.y == to_compare.y) and \
                (self.z == to_compare.z)

        except AttributeError:
            return False

    def __str__(self):
        """ Quaternion in string representation """
        struct_repr = ", ".join([
                "w: " + str(self.w),
                "x: " + str(self.x),
                "y: " + str(self.y),
                "z: " + str(self.z)
                ])

        return f"Quaternion: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcQuaternion):
        """ Translates a gRPC struct to the SDK equivalent """
        return Quaternion(

                rpcQuaternion.w,


                rpcQuaternion.x,


                rpcQuaternion.y,


                rpcQuaternion.z
                )

    def translate_to_rpc(self, rpcQuaternion):
        """ Translates this SDK object into its gRPC equivalent """




        rpcQuaternion.w = self.w





        rpcQuaternion.x = self.x





        rpcQuaternion.y = self.y





        rpcQuaternion.z = self.z





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

     """



    def __init__(
            self,
            roll_deg,
            pitch_deg,
            yaw_deg):
        """ Initializes the EulerAngle object """
        self.roll_deg = roll_deg
        self.pitch_deg = pitch_deg
        self.yaw_deg = yaw_deg

    def __equals__(self, to_compare):
        """ Checks if two EulerAngle are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # EulerAngle object
            return \
                (self.roll_deg == to_compare.roll_deg) and \
                (self.pitch_deg == to_compare.pitch_deg) and \
                (self.yaw_deg == to_compare.yaw_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ EulerAngle in string representation """
        struct_repr = ", ".join([
                "roll_deg: " + str(self.roll_deg),
                "pitch_deg: " + str(self.pitch_deg),
                "yaw_deg: " + str(self.yaw_deg)
                ])

        return f"EulerAngle: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcEulerAngle):
        """ Translates a gRPC struct to the SDK equivalent """
        return EulerAngle(

                rpcEulerAngle.roll_deg,


                rpcEulerAngle.pitch_deg,


                rpcEulerAngle.yaw_deg
                )

    def translate_to_rpc(self, rpcEulerAngle):
        """ Translates this SDK object into its gRPC equivalent """




        rpcEulerAngle.roll_deg = self.roll_deg





        rpcEulerAngle.pitch_deg = self.pitch_deg





        rpcEulerAngle.yaw_deg = self.yaw_deg





class AngularVelocityBody:
    """
     Angular velocity type

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

    def __equals__(self, to_compare):
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





class SpeedNed:
    """
     Speed type, represented in the NED (North East Down) frame and in metres/second.

     Parameters
     ----------
     velocity_north_m_s : float
          Velocity in North direction in metres/second

     velocity_east_m_s : float
          Velocity in East direction in metres/second

     velocity_down_m_s : float
          Velocity in Down direction in metres/second

     """



    def __init__(
            self,
            velocity_north_m_s,
            velocity_east_m_s,
            velocity_down_m_s):
        """ Initializes the SpeedNed object """
        self.velocity_north_m_s = velocity_north_m_s
        self.velocity_east_m_s = velocity_east_m_s
        self.velocity_down_m_s = velocity_down_m_s

    def __equals__(self, to_compare):
        """ Checks if two SpeedNed are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SpeedNed object
            return \
                (self.velocity_north_m_s == to_compare.velocity_north_m_s) and \
                (self.velocity_east_m_s == to_compare.velocity_east_m_s) and \
                (self.velocity_down_m_s == to_compare.velocity_down_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ SpeedNed in string representation """
        struct_repr = ", ".join([
                "velocity_north_m_s: " + str(self.velocity_north_m_s),
                "velocity_east_m_s: " + str(self.velocity_east_m_s),
                "velocity_down_m_s: " + str(self.velocity_down_m_s)
                ])

        return f"SpeedNed: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcSpeedNed):
        """ Translates a gRPC struct to the SDK equivalent """
        return SpeedNed(

                rpcSpeedNed.velocity_north_m_s,


                rpcSpeedNed.velocity_east_m_s,


                rpcSpeedNed.velocity_down_m_s
                )

    def translate_to_rpc(self, rpcSpeedNed):
        """ Translates this SDK object into its gRPC equivalent """




        rpcSpeedNed.velocity_north_m_s = self.velocity_north_m_s





        rpcSpeedNed.velocity_east_m_s = self.velocity_east_m_s





        rpcSpeedNed.velocity_down_m_s = self.velocity_down_m_s





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

    def __equals__(self, to_compare):
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





        self.fix_type.translate_to_rpc(rpcGpsInfo.fix_type)





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

    def __equals__(self, to_compare):
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

     is_level_calibration_ok : bool
          True if the vehicle has a valid level calibration

     is_local_position_ok : bool
          True if the local position estimate is good enough to fly in 'position control' mode

     is_global_position_ok : bool
          True if the global position estimate is good enough to fly in 'position control' mode

     is_home_position_ok : bool
          True if the home position has been initialized properly

     """



    def __init__(
            self,
            is_gyrometer_calibration_ok,
            is_accelerometer_calibration_ok,
            is_magnetometer_calibration_ok,
            is_level_calibration_ok,
            is_local_position_ok,
            is_global_position_ok,
            is_home_position_ok):
        """ Initializes the Health object """
        self.is_gyrometer_calibration_ok = is_gyrometer_calibration_ok
        self.is_accelerometer_calibration_ok = is_accelerometer_calibration_ok
        self.is_magnetometer_calibration_ok = is_magnetometer_calibration_ok
        self.is_level_calibration_ok = is_level_calibration_ok
        self.is_local_position_ok = is_local_position_ok
        self.is_global_position_ok = is_global_position_ok
        self.is_home_position_ok = is_home_position_ok

    def __equals__(self, to_compare):
        """ Checks if two Health are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Health object
            return \
                (self.is_gyrometer_calibration_ok == to_compare.is_gyrometer_calibration_ok) and \
                (self.is_accelerometer_calibration_ok == to_compare.is_accelerometer_calibration_ok) and \
                (self.is_magnetometer_calibration_ok == to_compare.is_magnetometer_calibration_ok) and \
                (self.is_level_calibration_ok == to_compare.is_level_calibration_ok) and \
                (self.is_local_position_ok == to_compare.is_local_position_ok) and \
                (self.is_global_position_ok == to_compare.is_global_position_ok) and \
                (self.is_home_position_ok == to_compare.is_home_position_ok)

        except AttributeError:
            return False

    def __str__(self):
        """ Health in string representation """
        struct_repr = ", ".join([
                "is_gyrometer_calibration_ok: " + str(self.is_gyrometer_calibration_ok),
                "is_accelerometer_calibration_ok: " + str(self.is_accelerometer_calibration_ok),
                "is_magnetometer_calibration_ok: " + str(self.is_magnetometer_calibration_ok),
                "is_level_calibration_ok: " + str(self.is_level_calibration_ok),
                "is_local_position_ok: " + str(self.is_local_position_ok),
                "is_global_position_ok: " + str(self.is_global_position_ok),
                "is_home_position_ok: " + str(self.is_home_position_ok)
                ])

        return f"Health: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealth):
        """ Translates a gRPC struct to the SDK equivalent """
        return Health(

                rpcHealth.is_gyrometer_calibration_ok,


                rpcHealth.is_accelerometer_calibration_ok,


                rpcHealth.is_magnetometer_calibration_ok,


                rpcHealth.is_level_calibration_ok,


                rpcHealth.is_local_position_ok,


                rpcHealth.is_global_position_ok,


                rpcHealth.is_home_position_ok
                )

    def translate_to_rpc(self, rpcHealth):
        """ Translates this SDK object into its gRPC equivalent """




        rpcHealth.is_gyrometer_calibration_ok = self.is_gyrometer_calibration_ok





        rpcHealth.is_accelerometer_calibration_ok = self.is_accelerometer_calibration_ok





        rpcHealth.is_magnetometer_calibration_ok = self.is_magnetometer_calibration_ok





        rpcHealth.is_level_calibration_ok = self.is_level_calibration_ok





        rpcHealth.is_local_position_ok = self.is_local_position_ok





        rpcHealth.is_global_position_ok = self.is_global_position_ok





        rpcHealth.is_home_position_ok = self.is_home_position_ok





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
          Signal strength (range: 0 to 100)

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

    def __equals__(self, to_compare):
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
     type : StatusType
          Message type

     text : std::string
          MAVLink status message

     """



    class StatusType(Enum):
        """
         Status types.

         Values
         ------
         INFO
              Information or other

         WARNING
              Warning

         CRITICAL
              Critical

         """


        INFO = 0
        WARNING = 1
        CRITICAL = 2

        def translate_to_rpc(self, rpcStatusType):
            return {
                    0: telemetry_pb2.StatusText.INFO,
                    1: telemetry_pb2.StatusText.WARNING,
                    2: telemetry_pb2.StatusText.CRITICAL
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: StatusText.StatusType.INFO,
                    1: StatusText.StatusType.WARNING,
                    2: StatusText.StatusType.CRITICAL,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name


    def __init__(
            self,
            type,
            text):
        """ Initializes the StatusText object """
        self.type = type
        self.text = text

    def __equals__(self, to_compare):
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

                StatusText.StatusType.translate_from_rpc(rpcStatusText.type),


                rpcStatusText.text
                )

    def translate_to_rpc(self, rpcStatusText):
        """ Translates this SDK object into its gRPC equivalent """




        self.type.translate_to_rpc(rpcStatusText.type)





        rpcStatusText.text = self.text





class ActuatorControlTarget:
    """


     Parameters
     ----------
     group : int32_t

     controls : [float]

     """



    def __init__(
            self,
            group,
            controls):
        """ Initializes the ActuatorControlTarget object """
        self.group = group
        self.controls = controls

    def __equals__(self, to_compare):
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


     Parameters
     ----------
     active : uint32_t

     actuator : [float]

     """



    def __init__(
            self,
            active,
            actuator):
        """ Initializes the ActuatorOutputStatus object """
        self.active = active
        self.actuator = actuator

    def __equals__(self, to_compare):
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

     speed_body : SpeedBody
          Linear speed (m/s).

     angular_velocity_body : AngularVelocityBody
          Angular speed (rad/s).

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

         BODY_NED
              Setpoint in body NED frame. This makes sense if all position control is externalized - e.g. useful to command 2 m/s^2 acceleration to the right.

         VISION_NED
              Odometry local coordinate frame of data given by a vision estimation system, Z-down (x: north, y: east, z: down).

         ESTIM_NED
              Odometry local coordinate frame of data given by an estimator running onboard the vehicle, Z-down (x: north, y: east, z: down).

         """


        UNDEF = 0
        BODY_NED = 8
        VISION_NED = 16
        ESTIM_NED = 18

        def translate_to_rpc(self, rpcMavFrame):
            return {
                    0: telemetry_pb2.Odometry.UNDEF,
                    8: telemetry_pb2.Odometry.BODY_NED,
                    16: telemetry_pb2.Odometry.VISION_NED,
                    18: telemetry_pb2.Odometry.ESTIM_NED
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: Odometry.MavFrame.UNDEF,
                    8: Odometry.MavFrame.BODY_NED,
                    16: Odometry.MavFrame.VISION_NED,
                    18: Odometry.MavFrame.ESTIM_NED,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name


    def __init__(
            self,
            time_usec,
            frame_id,
            child_frame_id,
            position_body,
            q,
            speed_body,
            angular_velocity_body,
            pose_covariance,
            velocity_covariance):
        """ Initializes the Odometry object """
        self.time_usec = time_usec
        self.frame_id = frame_id
        self.child_frame_id = child_frame_id
        self.position_body = position_body
        self.q = q
        self.speed_body = speed_body
        self.angular_velocity_body = angular_velocity_body
        self.pose_covariance = pose_covariance
        self.velocity_covariance = velocity_covariance

    def __equals__(self, to_compare):
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
                (self.speed_body == to_compare.speed_body) and \
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
                "speed_body: " + str(self.speed_body),
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


                SpeedBody.translate_from_rpc(rpcOdometry.speed_body),


                AngularVelocityBody.translate_from_rpc(rpcOdometry.angular_velocity_body),


                Covariance.translate_from_rpc(rpcOdometry.pose_covariance),


                Covariance.translate_from_rpc(rpcOdometry.velocity_covariance)
                )

    def translate_to_rpc(self, rpcOdometry):
        """ Translates this SDK object into its gRPC equivalent """




        rpcOdometry.time_usec = self.time_usec





        self.frame_id.translate_to_rpc(rpcOdometry.frame_id)





        self.child_frame_id.translate_to_rpc(rpcOdometry.child_frame_id)





        self.position_body.translate_to_rpc(rpcOdometry.position_body)





        self.q.translate_to_rpc(rpcOdometry.q)





        self.speed_body.translate_to_rpc(rpcOdometry.speed_body)





        self.angular_velocity_body.translate_to_rpc(rpcOdometry.angular_velocity_body)





        self.pose_covariance.translate_to_rpc(rpcOdometry.pose_covariance)





        self.velocity_covariance.translate_to_rpc(rpcOdometry.velocity_covariance)





class Covariance:
    """
     Covariance type.
     Row-major representation of a 6x6 cross-covariance matrix
     upper right triangle.
     Set first to NaN if unknown.

     Parameters
     ----------
     covariance_matrix : [float]

     """



    def __init__(
            self,
            covariance_matrix):
        """ Initializes the Covariance object """
        self.covariance_matrix = covariance_matrix

    def __equals__(self, to_compare):
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





class SpeedBody:
    """
     Speed type, represented in the Body (X Y Z) frame and in metres/second.

     Parameters
     ----------
     velocity_x_m_s : float
          Velocity in X in metres/second

     velocity_y_m_s : float
          Velocity in Y in metres/second

     velocity_z_m_s : float
          Velocity in Z in metres/second

     """



    def __init__(
            self,
            velocity_x_m_s,
            velocity_y_m_s,
            velocity_z_m_s):
        """ Initializes the SpeedBody object """
        self.velocity_x_m_s = velocity_x_m_s
        self.velocity_y_m_s = velocity_y_m_s
        self.velocity_z_m_s = velocity_z_m_s

    def __equals__(self, to_compare):
        """ Checks if two SpeedBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SpeedBody object
            return \
                (self.velocity_x_m_s == to_compare.velocity_x_m_s) and \
                (self.velocity_y_m_s == to_compare.velocity_y_m_s) and \
                (self.velocity_z_m_s == to_compare.velocity_z_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ SpeedBody in string representation """
        struct_repr = ", ".join([
                "velocity_x_m_s: " + str(self.velocity_x_m_s),
                "velocity_y_m_s: " + str(self.velocity_y_m_s),
                "velocity_z_m_s: " + str(self.velocity_z_m_s)
                ])

        return f"SpeedBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcSpeedBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return SpeedBody(

                rpcSpeedBody.velocity_x_m_s,


                rpcSpeedBody.velocity_y_m_s,


                rpcSpeedBody.velocity_z_m_s
                )

    def translate_to_rpc(self, rpcSpeedBody):
        """ Translates this SDK object into its gRPC equivalent """




        rpcSpeedBody.velocity_x_m_s = self.velocity_x_m_s





        rpcSpeedBody.velocity_y_m_s = self.velocity_y_m_s





        rpcSpeedBody.velocity_z_m_s = self.velocity_z_m_s





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

    def __equals__(self, to_compare):
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
         Subscribe to 'attitude' updates (euler).

         Yields
         -------
         attitude_euler : EulerAngle
              The next attitude (euler)


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

    async def camera_attitude_quaternion(self):
        """
         Subscribe to 'camera attitude' updates (quaternion).

         Yields
         -------
         attitude_quaternion : Quaternion
              The next camera attitude (quaternion)


        """

        request = telemetry_pb2.SubscribeCameraAttitudeQuaternionRequest()
        camera_attitude_quaternion_stream = self._stub.SubscribeCameraAttitudeQuaternion(request)

        try:
            async for response in camera_attitude_quaternion_stream:



                yield Quaternion.translate_from_rpc(response.attitude_quaternion)
        finally:
            camera_attitude_quaternion_stream.cancel()

    async def camera_attitude_euler(self):
        """
         Subscribe to 'camera attitude' updates (euler).

         Yields
         -------
         attitude_euler : EulerAngle
              The next camera attitude (euler)


        """

        request = telemetry_pb2.SubscribeCameraAttitudeEulerRequest()
        camera_attitude_euler_stream = self._stub.SubscribeCameraAttitudeEuler(request)

        try:
            async for response in camera_attitude_euler_stream:



                yield EulerAngle.translate_from_rpc(response.attitude_euler)
        finally:
            camera_attitude_euler_stream.cancel()

    async def ground_speed_ned(self):
        """
         Subscribe to 'ground speed' updates (NED).

         Yields
         -------
         ground_speed_ned : SpeedNed
              The next ground speed (NED)


        """

        request = telemetry_pb2.SubscribeGroundSpeedNedRequest()
        ground_speed_ned_stream = self._stub.SubscribeGroundSpeedNed(request)

        try:
            async for response in ground_speed_ned_stream:



                yield SpeedNed.translate_from_rpc(response.ground_speed_ned)
        finally:
            ground_speed_ned_stream.cancel()

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
              Actuator control target


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
              Actuator output status


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
              Odometry


        """

        request = telemetry_pb2.SubscribeOdometryRequest()
        odometry_stream = self._stub.SubscribeOdometry(request)

        try:
            async for response in odometry_stream:



                yield Odometry.translate_from_rpc(response.odometry)
        finally:
            odometry_stream.cancel()
