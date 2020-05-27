# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import mocap_pb2, mocap_pb2_grpc
from enum import Enum


class PositionBody:
    """
     Body position type

     Parameters
     ----------
     x_m : float
          X position in metres.

     y_m : float
          Y position in metres.

     z_m : float
          Z position in metres.

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
            
        
        


class AngleBody:
    """
     Body angle type

     Parameters
     ----------
     roll_rad : float
          Roll angle in radians.

     pitch_rad : float
          Pitch angle in radians.

     yaw_rad : float
          Yaw angle in radians.

     """

    

    def __init__(
            self,
            roll_rad,
            pitch_rad,
            yaw_rad):
        """ Initializes the AngleBody object """
        self.roll_rad = roll_rad
        self.pitch_rad = pitch_rad
        self.yaw_rad = yaw_rad

    def __equals__(self, to_compare):
        """ Checks if two AngleBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AngleBody object
            return \
                (self.roll_rad == to_compare.roll_rad) and \
                (self.pitch_rad == to_compare.pitch_rad) and \
                (self.yaw_rad == to_compare.yaw_rad)

        except AttributeError:
            return False

    def __str__(self):
        """ AngleBody in string representation """
        struct_repr = ", ".join([
                "roll_rad: " + str(self.roll_rad),
                "pitch_rad: " + str(self.pitch_rad),
                "yaw_rad: " + str(self.yaw_rad)
                ])

        return f"AngleBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAngleBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return AngleBody(
                
                rpcAngleBody.roll_rad,
                
                
                rpcAngleBody.pitch_rad,
                
                
                rpcAngleBody.yaw_rad
                )

    def translate_to_rpc(self, rpcAngleBody):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAngleBody.roll_rad = self.roll_rad
            
        
        
        
            
        rpcAngleBody.pitch_rad = self.pitch_rad
            
        
        
        
            
        rpcAngleBody.yaw_rad = self.yaw_rad
            
        
        


class SpeedBody:
    """
     Speed type, represented in the Body (X Y Z) frame and in metres/second.

     Parameters
     ----------
     x_m_s : float
          Velocity in X in metres/second.

     y_m_s : float
          Velocity in Y in metres/second.

     z_m_s : float
          Velocity in Z in metres/second.

     """

    

    def __init__(
            self,
            x_m_s,
            y_m_s,
            z_m_s):
        """ Initializes the SpeedBody object """
        self.x_m_s = x_m_s
        self.y_m_s = y_m_s
        self.z_m_s = z_m_s

    def __equals__(self, to_compare):
        """ Checks if two SpeedBody are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SpeedBody object
            return \
                (self.x_m_s == to_compare.x_m_s) and \
                (self.y_m_s == to_compare.y_m_s) and \
                (self.z_m_s == to_compare.z_m_s)

        except AttributeError:
            return False

    def __str__(self):
        """ SpeedBody in string representation """
        struct_repr = ", ".join([
                "x_m_s: " + str(self.x_m_s),
                "y_m_s: " + str(self.y_m_s),
                "z_m_s: " + str(self.z_m_s)
                ])

        return f"SpeedBody: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcSpeedBody):
        """ Translates a gRPC struct to the SDK equivalent """
        return SpeedBody(
                
                rpcSpeedBody.x_m_s,
                
                
                rpcSpeedBody.y_m_s,
                
                
                rpcSpeedBody.z_m_s
                )

    def translate_to_rpc(self, rpcSpeedBody):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcSpeedBody.x_m_s = self.x_m_s
            
        
        
        
            
        rpcSpeedBody.y_m_s = self.y_m_s
            
        
        
        
            
        rpcSpeedBody.z_m_s = self.z_m_s
            
        
        


class AngularVelocityBody:
    """
     Angular velocity type

     Parameters
     ----------
     roll_rad_s : float
          Roll angular velocity in radians/second.

     pitch_rad_s : float
          Pitch angular velocity in radians/second.

     yaw_rad_s : float
          Yaw angular velocity in radians/second.

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
            
        
        


class Covariance:
    """
     Covariance type.
     Row-major representation of a 6x6 cross-covariance matrix upper
     right triangle.
     Needs to be 21 entries or 1 entry with NaN if unknown.

     Parameters
     ----------
     covariance_matrix : [float]
          The covariance matrix

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
            
        
        


class VisionPositionEstimate:
    """
     Global position/attitude estimate from a vision source.

     Parameters
     ----------
     time_usec : uint64_t
          PositionBody frame timestamp UNIX Epoch time (0 to use Backend timestamp)

     position_body : PositionBody
          Global position (m)

     angle_body : AngleBody
          Body angle (rad).

     pose_covariance : Covariance
          Pose cross-covariance matrix.

     """

    

    def __init__(
            self,
            time_usec,
            position_body,
            angle_body,
            pose_covariance):
        """ Initializes the VisionPositionEstimate object """
        self.time_usec = time_usec
        self.position_body = position_body
        self.angle_body = angle_body
        self.pose_covariance = pose_covariance

    def __equals__(self, to_compare):
        """ Checks if two VisionPositionEstimate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VisionPositionEstimate object
            return \
                (self.time_usec == to_compare.time_usec) and \
                (self.position_body == to_compare.position_body) and \
                (self.angle_body == to_compare.angle_body) and \
                (self.pose_covariance == to_compare.pose_covariance)

        except AttributeError:
            return False

    def __str__(self):
        """ VisionPositionEstimate in string representation """
        struct_repr = ", ".join([
                "time_usec: " + str(self.time_usec),
                "position_body: " + str(self.position_body),
                "angle_body: " + str(self.angle_body),
                "pose_covariance: " + str(self.pose_covariance)
                ])

        return f"VisionPositionEstimate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVisionPositionEstimate):
        """ Translates a gRPC struct to the SDK equivalent """
        return VisionPositionEstimate(
                
                rpcVisionPositionEstimate.time_usec,
                
                
                PositionBody.translate_from_rpc(rpcVisionPositionEstimate.position_body),
                
                
                AngleBody.translate_from_rpc(rpcVisionPositionEstimate.angle_body),
                
                
                Covariance.translate_from_rpc(rpcVisionPositionEstimate.pose_covariance)
                )

    def translate_to_rpc(self, rpcVisionPositionEstimate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVisionPositionEstimate.time_usec = self.time_usec
            
        
        
        
            
        self.position_body.translate_to_rpc(rpcVisionPositionEstimate.position_body)
            
        
        
        
            
        self.angle_body.translate_to_rpc(rpcVisionPositionEstimate.angle_body)
            
        
        
        
            
        self.pose_covariance.translate_to_rpc(rpcVisionPositionEstimate.pose_covariance)
            
        
        


class AttitudePositionMocap:
    """
     Motion capture attitude and position

     Parameters
     ----------
     time_usec : uint64_t
          PositionBody frame timestamp UNIX Epoch time (0 to use Backend timestamp)

     q : Quaternion
          Attitude quaternion (w, x, y, z order, zero-rotation is 1, 0, 0, 0)

     position_body : PositionBody
          Body Position (NED)

     pose_covariance : Covariance
          Pose cross-covariance matrix.

     """

    

    def __init__(
            self,
            time_usec,
            q,
            position_body,
            pose_covariance):
        """ Initializes the AttitudePositionMocap object """
        self.time_usec = time_usec
        self.q = q
        self.position_body = position_body
        self.pose_covariance = pose_covariance

    def __equals__(self, to_compare):
        """ Checks if two AttitudePositionMocap are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AttitudePositionMocap object
            return \
                (self.time_usec == to_compare.time_usec) and \
                (self.q == to_compare.q) and \
                (self.position_body == to_compare.position_body) and \
                (self.pose_covariance == to_compare.pose_covariance)

        except AttributeError:
            return False

    def __str__(self):
        """ AttitudePositionMocap in string representation """
        struct_repr = ", ".join([
                "time_usec: " + str(self.time_usec),
                "q: " + str(self.q),
                "position_body: " + str(self.position_body),
                "pose_covariance: " + str(self.pose_covariance)
                ])

        return f"AttitudePositionMocap: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAttitudePositionMocap):
        """ Translates a gRPC struct to the SDK equivalent """
        return AttitudePositionMocap(
                
                rpcAttitudePositionMocap.time_usec,
                
                
                Quaternion.translate_from_rpc(rpcAttitudePositionMocap.q),
                
                
                PositionBody.translate_from_rpc(rpcAttitudePositionMocap.position_body),
                
                
                Covariance.translate_from_rpc(rpcAttitudePositionMocap.pose_covariance)
                )

    def translate_to_rpc(self, rpcAttitudePositionMocap):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAttitudePositionMocap.time_usec = self.time_usec
            
        
        
        
            
        self.q.translate_to_rpc(rpcAttitudePositionMocap.q)
            
        
        
        
            
        self.position_body.translate_to_rpc(rpcAttitudePositionMocap.position_body)
            
        
        
        
            
        self.pose_covariance.translate_to_rpc(rpcAttitudePositionMocap.pose_covariance)
            
        
        


class Odometry:
    """
     Odometry message to communicate odometry information with an external interface.

     Parameters
     ----------
     time_usec : uint64_t
          Timestamp (0 to use Backend timestamp).

     frame_id : MavFrame
          Coordinate frame of reference for the pose data.

     position_body : PositionBody
          Body Position.

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
         MOCAP_NED
              MAVLink number: 14. Odometry local coordinate frame of data given by a motion capture system, Z-down (x: north, y: east, z: down).

         LOCAL_FRD
              MAVLink number: 20. Forward, Right, Down coordinate frame. This is a local frame with Z-down and arbitrary F/R alignment (i.e. not aligned with NED/earth frame). Replacement for MAV_FRAME_MOCAP_NED, MAV_FRAME_VISION_NED, MAV_FRAME_ESTIM_NED.

         """

        
        MOCAP_NED = 0
        LOCAL_FRD = 1

        def translate_to_rpc(self):
            if self == Odometry.MavFrame.MOCAP_NED:
                return mocap_pb2.Odometry.MAV_FRAME_MOCAP_NED
            if self == Odometry.MavFrame.LOCAL_FRD:
                return mocap_pb2.Odometry.MAV_FRAME_LOCAL_FRD

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mocap_pb2.Odometry.MAV_FRAME_MOCAP_NED:
                return Odometry.MavFrame.MOCAP_NED
            if rpc_enum_value == mocap_pb2.Odometry.MAV_FRAME_LOCAL_FRD:
                return Odometry.MavFrame.LOCAL_FRD

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            time_usec,
            frame_id,
            position_body,
            q,
            speed_body,
            angular_velocity_body,
            pose_covariance,
            velocity_covariance):
        """ Initializes the Odometry object """
        self.time_usec = time_usec
        self.frame_id = frame_id
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
            
        
        
        
            
        rpcOdometry.frame_id = self.frame_id.translate_to_rpc()
            
        
        
        
            
        self.position_body.translate_to_rpc(rpcOdometry.position_body)
            
        
        
        
            
        self.q.translate_to_rpc(rpcOdometry.q)
            
        
        
        
            
        self.speed_body.translate_to_rpc(rpcOdometry.speed_body)
            
        
        
        
            
        self.angular_velocity_body.translate_to_rpc(rpcOdometry.angular_velocity_body)
            
        
        
        
            
        self.pose_covariance.translate_to_rpc(rpcOdometry.pose_covariance)
            
        
        
        
            
        self.velocity_covariance.translate_to_rpc(rpcOdometry.velocity_covariance)
            
        
        


class MocapResult:
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
         Possible results returned for mocap requests

         Values
         ------
         UNKNOWN
              Unknown error

         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         INVALID_REQUEST_DATA
              Invalid request data

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        INVALID_REQUEST_DATA = 4

        def translate_to_rpc(self):
            if self == MocapResult.Result.UNKNOWN:
                return mocap_pb2.MocapResult.RESULT_UNKNOWN
            if self == MocapResult.Result.SUCCESS:
                return mocap_pb2.MocapResult.RESULT_SUCCESS
            if self == MocapResult.Result.NO_SYSTEM:
                return mocap_pb2.MocapResult.RESULT_NO_SYSTEM
            if self == MocapResult.Result.CONNECTION_ERROR:
                return mocap_pb2.MocapResult.RESULT_CONNECTION_ERROR
            if self == MocapResult.Result.INVALID_REQUEST_DATA:
                return mocap_pb2.MocapResult.RESULT_INVALID_REQUEST_DATA

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mocap_pb2.MocapResult.RESULT_UNKNOWN:
                return MocapResult.Result.UNKNOWN
            if rpc_enum_value == mocap_pb2.MocapResult.RESULT_SUCCESS:
                return MocapResult.Result.SUCCESS
            if rpc_enum_value == mocap_pb2.MocapResult.RESULT_NO_SYSTEM:
                return MocapResult.Result.NO_SYSTEM
            if rpc_enum_value == mocap_pb2.MocapResult.RESULT_CONNECTION_ERROR:
                return MocapResult.Result.CONNECTION_ERROR
            if rpc_enum_value == mocap_pb2.MocapResult.RESULT_INVALID_REQUEST_DATA:
                return MocapResult.Result.INVALID_REQUEST_DATA

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MocapResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two MocapResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MocapResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ MocapResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"MocapResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMocapResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return MocapResult(
                
                MocapResult.Result.translate_from_rpc(rpcMocapResult.result),
                
                
                rpcMocapResult.result_str
                )

    def translate_to_rpc(self, rpcMocapResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMocapResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcMocapResult.result_str = self.result_str
            
        
        



class MocapError(Exception):
    """ Raised when a MocapResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Mocap(AsyncBase):
    """
     *
     Allows interfacing a vehicle with a motion capture system in
     order to allow navigation without global positioning sources available
     (e.g. indoors, or when flying under a bridge. etc.).

     Generated by dcsdkgen - MAVSDK Mocap API
    """

    # Plugin name
    name = "Mocap"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = mocap_pb2_grpc.MocapServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return MocapResult.translate_from_rpc(response.mocap_result)
    

    async def set_vision_position_estimate(self, vision_position_estimate):
        """
         Send Global position/attitude estimate from a vision source.

         Parameters
         ----------
         vision_position_estimate : VisionPositionEstimate
              The vision position estimate

         Raises
         ------
         MocapError
             If the request fails. The error contains the reason for the failure.
        """

        request = mocap_pb2.SetVisionPositionEstimateRequest()
        
        vision_position_estimate.translate_to_rpc(request.vision_position_estimate)
                
            
        response = await self._stub.SetVisionPositionEstimate(request)

        
        result = self._extract_result(response)

        if result.result is not MocapResult.Result.SUCCESS:
            raise MocapError(result, "set_vision_position_estimate()", vision_position_estimate)
        

    async def set_attitude_position_mocap(self, attitude_position_mocap):
        """
         Send motion capture attitude and position.

         Parameters
         ----------
         attitude_position_mocap : AttitudePositionMocap
              The attitude and position data

         Raises
         ------
         MocapError
             If the request fails. The error contains the reason for the failure.
        """

        request = mocap_pb2.SetAttitudePositionMocapRequest()
        
        attitude_position_mocap.translate_to_rpc(request.attitude_position_mocap)
                
            
        response = await self._stub.SetAttitudePositionMocap(request)

        
        result = self._extract_result(response)

        if result.result is not MocapResult.Result.SUCCESS:
            raise MocapError(result, "set_attitude_position_mocap()", attitude_position_mocap)
        

    async def set_odometry(self, odometry):
        """
         Send odometry information with an external interface.

         Parameters
         ----------
         odometry : Odometry
              The odometry data

         Raises
         ------
         MocapError
             If the request fails. The error contains the reason for the failure.
        """

        request = mocap_pb2.SetOdometryRequest()
        
        odometry.translate_to_rpc(request.odometry)
                
            
        response = await self._stub.SetOdometry(request)

        
        result = self._extract_result(response)

        if result.result is not MocapResult.Result.SUCCESS:
            raise MocapError(result, "set_odometry()", odometry)
        