# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import camera_pb2, camera_pb2_grpc
from enum import Enum


class Mode(Enum):
    """
     Camera mode type.

     Values
     ------
     UNKNOWN
          Unknown

     PHOTO
          Photo mode

     VIDEO
          Video mode

     """

    
    UNKNOWN = 0
    PHOTO = 1
    VIDEO = 2

    def translate_to_rpc(self):
        if self == Mode.UNKNOWN:
            return camera_pb2.MODE_UNKNOWN
        if self == Mode.PHOTO:
            return camera_pb2.MODE_PHOTO
        if self == Mode.VIDEO:
            return camera_pb2.MODE_VIDEO

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == camera_pb2.MODE_UNKNOWN:
            return Mode.UNKNOWN
        if rpc_enum_value == camera_pb2.MODE_PHOTO:
            return Mode.PHOTO
        if rpc_enum_value == camera_pb2.MODE_VIDEO:
            return Mode.VIDEO

    def __str__(self):
        return self.name


class CameraResult:
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
         Possible results returned for camera commands

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Command executed successfully

         IN_PROGRESS
              Command in progress

         BUSY
              Camera is busy and rejected command

         DENIED
              Camera denied the command

         ERROR
              An error has occured while executing the command

         TIMEOUT
              Command timed out

         WRONG_ARGUMENT
              Command has wrong argument(s)

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        IN_PROGRESS = 2
        BUSY = 3
        DENIED = 4
        ERROR = 5
        TIMEOUT = 6
        WRONG_ARGUMENT = 7

        def translate_to_rpc(self):
            if self == CameraResult.Result.UNKNOWN:
                return camera_pb2.CameraResult.RESULT_UNKNOWN
            if self == CameraResult.Result.SUCCESS:
                return camera_pb2.CameraResult.RESULT_SUCCESS
            if self == CameraResult.Result.IN_PROGRESS:
                return camera_pb2.CameraResult.RESULT_IN_PROGRESS
            if self == CameraResult.Result.BUSY:
                return camera_pb2.CameraResult.RESULT_BUSY
            if self == CameraResult.Result.DENIED:
                return camera_pb2.CameraResult.RESULT_DENIED
            if self == CameraResult.Result.ERROR:
                return camera_pb2.CameraResult.RESULT_ERROR
            if self == CameraResult.Result.TIMEOUT:
                return camera_pb2.CameraResult.RESULT_TIMEOUT
            if self == CameraResult.Result.WRONG_ARGUMENT:
                return camera_pb2.CameraResult.RESULT_WRONG_ARGUMENT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_UNKNOWN:
                return CameraResult.Result.UNKNOWN
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_SUCCESS:
                return CameraResult.Result.SUCCESS
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_IN_PROGRESS:
                return CameraResult.Result.IN_PROGRESS
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_BUSY:
                return CameraResult.Result.BUSY
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_DENIED:
                return CameraResult.Result.DENIED
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_ERROR:
                return CameraResult.Result.ERROR
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_TIMEOUT:
                return CameraResult.Result.TIMEOUT
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_WRONG_ARGUMENT:
                return CameraResult.Result.WRONG_ARGUMENT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the CameraResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two CameraResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CameraResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ CameraResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"CameraResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCameraResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return CameraResult(
                
                CameraResult.Result.translate_from_rpc(rpcCameraResult.result),
                
                
                rpcCameraResult.result_str
                )

    def translate_to_rpc(self, rpcCameraResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCameraResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcCameraResult.result_str = self.result_str
            
        
        


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
            
        
        


class CaptureInfo:
    """
     Information about a picture just captured.

     Parameters
     ----------
     position : Position
          Location where the picture was taken

     attitude_quaternion : Quaternion
          Attitude of the camera when the picture was taken (quaternion)

     attitude_euler_angle : EulerAngle
          Attitude of the camera when the picture was taken (euler angle)

     time_utc_us : uint64_t
          Timestamp in UTC (since UNIX epoch) in microseconds

     is_success : bool
          True if the capture was successful

     index : int32_t
          Zero-based index of this image since vehicle was armed

     file_url : std::string
          Download URL of this image

     """

    

    def __init__(
            self,
            position,
            attitude_quaternion,
            attitude_euler_angle,
            time_utc_us,
            is_success,
            index,
            file_url):
        """ Initializes the CaptureInfo object """
        self.position = position
        self.attitude_quaternion = attitude_quaternion
        self.attitude_euler_angle = attitude_euler_angle
        self.time_utc_us = time_utc_us
        self.is_success = is_success
        self.index = index
        self.file_url = file_url

    def __equals__(self, to_compare):
        """ Checks if two CaptureInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CaptureInfo object
            return \
                (self.position == to_compare.position) and \
                (self.attitude_quaternion == to_compare.attitude_quaternion) and \
                (self.attitude_euler_angle == to_compare.attitude_euler_angle) and \
                (self.time_utc_us == to_compare.time_utc_us) and \
                (self.is_success == to_compare.is_success) and \
                (self.index == to_compare.index) and \
                (self.file_url == to_compare.file_url)

        except AttributeError:
            return False

    def __str__(self):
        """ CaptureInfo in string representation """
        struct_repr = ", ".join([
                "position: " + str(self.position),
                "attitude_quaternion: " + str(self.attitude_quaternion),
                "attitude_euler_angle: " + str(self.attitude_euler_angle),
                "time_utc_us: " + str(self.time_utc_us),
                "is_success: " + str(self.is_success),
                "index: " + str(self.index),
                "file_url: " + str(self.file_url)
                ])

        return f"CaptureInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCaptureInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return CaptureInfo(
                
                Position.translate_from_rpc(rpcCaptureInfo.position),
                
                
                Quaternion.translate_from_rpc(rpcCaptureInfo.attitude_quaternion),
                
                
                EulerAngle.translate_from_rpc(rpcCaptureInfo.attitude_euler_angle),
                
                
                rpcCaptureInfo.time_utc_us,
                
                
                rpcCaptureInfo.is_success,
                
                
                rpcCaptureInfo.index,
                
                
                rpcCaptureInfo.file_url
                )

    def translate_to_rpc(self, rpcCaptureInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.position.translate_to_rpc(rpcCaptureInfo.position)
            
        
        
        
            
        self.attitude_quaternion.translate_to_rpc(rpcCaptureInfo.attitude_quaternion)
            
        
        
        
            
        self.attitude_euler_angle.translate_to_rpc(rpcCaptureInfo.attitude_euler_angle)
            
        
        
        
            
        rpcCaptureInfo.time_utc_us = self.time_utc_us
            
        
        
        
            
        rpcCaptureInfo.is_success = self.is_success
            
        
        
        
            
        rpcCaptureInfo.index = self.index
            
        
        
        
            
        rpcCaptureInfo.file_url = self.file_url
            
        
        


class VideoStreamSettings:
    """
     Type for video stream settings.

     Parameters
     ----------
     frame_rate_hz : float
          Frames per second

     horizontal_resolution_pix : uint32_t
          Horizontal resolution (in pixels)

     vertical_resolution_pix : uint32_t
          Vertical resolution (in pixels)

     bit_rate_b_s : uint32_t
          Bit rate (in bits per second)

     rotation_deg : uint32_t
          Video image rotation (clockwise, 0-359 degrees)

     uri : std::string
          Video stream URI

     """

    

    def __init__(
            self,
            frame_rate_hz,
            horizontal_resolution_pix,
            vertical_resolution_pix,
            bit_rate_b_s,
            rotation_deg,
            uri):
        """ Initializes the VideoStreamSettings object """
        self.frame_rate_hz = frame_rate_hz
        self.horizontal_resolution_pix = horizontal_resolution_pix
        self.vertical_resolution_pix = vertical_resolution_pix
        self.bit_rate_b_s = bit_rate_b_s
        self.rotation_deg = rotation_deg
        self.uri = uri

    def __equals__(self, to_compare):
        """ Checks if two VideoStreamSettings are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VideoStreamSettings object
            return \
                (self.frame_rate_hz == to_compare.frame_rate_hz) and \
                (self.horizontal_resolution_pix == to_compare.horizontal_resolution_pix) and \
                (self.vertical_resolution_pix == to_compare.vertical_resolution_pix) and \
                (self.bit_rate_b_s == to_compare.bit_rate_b_s) and \
                (self.rotation_deg == to_compare.rotation_deg) and \
                (self.uri == to_compare.uri)

        except AttributeError:
            return False

    def __str__(self):
        """ VideoStreamSettings in string representation """
        struct_repr = ", ".join([
                "frame_rate_hz: " + str(self.frame_rate_hz),
                "horizontal_resolution_pix: " + str(self.horizontal_resolution_pix),
                "vertical_resolution_pix: " + str(self.vertical_resolution_pix),
                "bit_rate_b_s: " + str(self.bit_rate_b_s),
                "rotation_deg: " + str(self.rotation_deg),
                "uri: " + str(self.uri)
                ])

        return f"VideoStreamSettings: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVideoStreamSettings):
        """ Translates a gRPC struct to the SDK equivalent """
        return VideoStreamSettings(
                
                rpcVideoStreamSettings.frame_rate_hz,
                
                
                rpcVideoStreamSettings.horizontal_resolution_pix,
                
                
                rpcVideoStreamSettings.vertical_resolution_pix,
                
                
                rpcVideoStreamSettings.bit_rate_b_s,
                
                
                rpcVideoStreamSettings.rotation_deg,
                
                
                rpcVideoStreamSettings.uri
                )

    def translate_to_rpc(self, rpcVideoStreamSettings):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVideoStreamSettings.frame_rate_hz = self.frame_rate_hz
            
        
        
        
            
        rpcVideoStreamSettings.horizontal_resolution_pix = self.horizontal_resolution_pix
            
        
        
        
            
        rpcVideoStreamSettings.vertical_resolution_pix = self.vertical_resolution_pix
            
        
        
        
            
        rpcVideoStreamSettings.bit_rate_b_s = self.bit_rate_b_s
            
        
        
        
            
        rpcVideoStreamSettings.rotation_deg = self.rotation_deg
            
        
        
        
            
        rpcVideoStreamSettings.uri = self.uri
            
        
        


class VideoStreamInfo:
    """
     Information about the video stream.

     Parameters
     ----------
     settings : VideoStreamSettings
          Video stream settings

     status : Status
          Current status of video streaming

     """

    
    
    class Status(Enum):
        """
         Video stream status type.

         Values
         ------
         NOT_RUNNING
              Video stream is not running

         IN_PROGRESS
              Video stream is running

         """

        
        NOT_RUNNING = 0
        IN_PROGRESS = 1

        def translate_to_rpc(self):
            if self == VideoStreamInfo.Status.NOT_RUNNING:
                return camera_pb2.VideoStreamInfo.STATUS_NOT_RUNNING
            if self == VideoStreamInfo.Status.IN_PROGRESS:
                return camera_pb2.VideoStreamInfo.STATUS_IN_PROGRESS

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.VideoStreamInfo.STATUS_NOT_RUNNING:
                return VideoStreamInfo.Status.NOT_RUNNING
            if rpc_enum_value == camera_pb2.VideoStreamInfo.STATUS_IN_PROGRESS:
                return VideoStreamInfo.Status.IN_PROGRESS

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            settings,
            status):
        """ Initializes the VideoStreamInfo object """
        self.settings = settings
        self.status = status

    def __equals__(self, to_compare):
        """ Checks if two VideoStreamInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VideoStreamInfo object
            return \
                (self.settings == to_compare.settings) and \
                (self.status == to_compare.status)

        except AttributeError:
            return False

    def __str__(self):
        """ VideoStreamInfo in string representation """
        struct_repr = ", ".join([
                "settings: " + str(self.settings),
                "status: " + str(self.status)
                ])

        return f"VideoStreamInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVideoStreamInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return VideoStreamInfo(
                
                VideoStreamSettings.translate_from_rpc(rpcVideoStreamInfo.settings),
                
                
                VideoStreamInfo.Status.translate_from_rpc(rpcVideoStreamInfo.status)
                )

    def translate_to_rpc(self, rpcVideoStreamInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.settings.translate_to_rpc(rpcVideoStreamInfo.settings)
            
        
        
        
            
        rpcVideoStreamInfo.status = self.status.translate_to_rpc()
            
        
        


class Status:
    """
     Information about the camera status.

     Parameters
     ----------
     video_on : bool
          Whether video recording is currently in process

     photo_interval_on : bool
          Whether a photo interval is currently in process

     used_storage_mib : float
          Used storage (in MiB)

     available_storage_mib : float
          Available storage (in MiB)

     total_storage_mib : float
          Total storage (in MiB)

     recording_time_s : float
          Elapsed time since starting the video recording (in seconds)

     media_folder_name : std::string
          Current folder name where media are saved

     storage_status : StorageStatus
          Storage status

     """

    
    
    class StorageStatus(Enum):
        """
         Storage status type.

         Values
         ------
         NOT_AVAILABLE
              Status not available

         UNFORMATTED
              Storage is not formatted (i.e. has no recognized file system)

         FORMATTED
              Storage is formatted (i.e. has recognized a file system)

         """

        
        NOT_AVAILABLE = 0
        UNFORMATTED = 1
        FORMATTED = 2

        def translate_to_rpc(self):
            if self == Status.StorageStatus.NOT_AVAILABLE:
                return camera_pb2.Status.STORAGE_STATUS_NOT_AVAILABLE
            if self == Status.StorageStatus.UNFORMATTED:
                return camera_pb2.Status.STORAGE_STATUS_UNFORMATTED
            if self == Status.StorageStatus.FORMATTED:
                return camera_pb2.Status.STORAGE_STATUS_FORMATTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.Status.STORAGE_STATUS_NOT_AVAILABLE:
                return Status.StorageStatus.NOT_AVAILABLE
            if rpc_enum_value == camera_pb2.Status.STORAGE_STATUS_UNFORMATTED:
                return Status.StorageStatus.UNFORMATTED
            if rpc_enum_value == camera_pb2.Status.STORAGE_STATUS_FORMATTED:
                return Status.StorageStatus.FORMATTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            video_on,
            photo_interval_on,
            used_storage_mib,
            available_storage_mib,
            total_storage_mib,
            recording_time_s,
            media_folder_name,
            storage_status):
        """ Initializes the Status object """
        self.video_on = video_on
        self.photo_interval_on = photo_interval_on
        self.used_storage_mib = used_storage_mib
        self.available_storage_mib = available_storage_mib
        self.total_storage_mib = total_storage_mib
        self.recording_time_s = recording_time_s
        self.media_folder_name = media_folder_name
        self.storage_status = storage_status

    def __equals__(self, to_compare):
        """ Checks if two Status are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Status object
            return \
                (self.video_on == to_compare.video_on) and \
                (self.photo_interval_on == to_compare.photo_interval_on) and \
                (self.used_storage_mib == to_compare.used_storage_mib) and \
                (self.available_storage_mib == to_compare.available_storage_mib) and \
                (self.total_storage_mib == to_compare.total_storage_mib) and \
                (self.recording_time_s == to_compare.recording_time_s) and \
                (self.media_folder_name == to_compare.media_folder_name) and \
                (self.storage_status == to_compare.storage_status)

        except AttributeError:
            return False

    def __str__(self):
        """ Status in string representation """
        struct_repr = ", ".join([
                "video_on: " + str(self.video_on),
                "photo_interval_on: " + str(self.photo_interval_on),
                "used_storage_mib: " + str(self.used_storage_mib),
                "available_storage_mib: " + str(self.available_storage_mib),
                "total_storage_mib: " + str(self.total_storage_mib),
                "recording_time_s: " + str(self.recording_time_s),
                "media_folder_name: " + str(self.media_folder_name),
                "storage_status: " + str(self.storage_status)
                ])

        return f"Status: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return Status(
                
                rpcStatus.video_on,
                
                
                rpcStatus.photo_interval_on,
                
                
                rpcStatus.used_storage_mib,
                
                
                rpcStatus.available_storage_mib,
                
                
                rpcStatus.total_storage_mib,
                
                
                rpcStatus.recording_time_s,
                
                
                rpcStatus.media_folder_name,
                
                
                Status.StorageStatus.translate_from_rpc(rpcStatus.storage_status)
                )

    def translate_to_rpc(self, rpcStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStatus.video_on = self.video_on
            
        
        
        
            
        rpcStatus.photo_interval_on = self.photo_interval_on
            
        
        
        
            
        rpcStatus.used_storage_mib = self.used_storage_mib
            
        
        
        
            
        rpcStatus.available_storage_mib = self.available_storage_mib
            
        
        
        
            
        rpcStatus.total_storage_mib = self.total_storage_mib
            
        
        
        
            
        rpcStatus.recording_time_s = self.recording_time_s
            
        
        
        
            
        rpcStatus.media_folder_name = self.media_folder_name
            
        
        
        
            
        rpcStatus.storage_status = self.storage_status.translate_to_rpc()
            
        
        


class Option:
    """
     Type to represent a setting option.

     Parameters
     ----------
     option_id : std::string
          Name of the option (machine readable)

     option_description : std::string
          Description of the option (human readable)

     """

    

    def __init__(
            self,
            option_id,
            option_description):
        """ Initializes the Option object """
        self.option_id = option_id
        self.option_description = option_description

    def __equals__(self, to_compare):
        """ Checks if two Option are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Option object
            return \
                (self.option_id == to_compare.option_id) and \
                (self.option_description == to_compare.option_description)

        except AttributeError:
            return False

    def __str__(self):
        """ Option in string representation """
        struct_repr = ", ".join([
                "option_id: " + str(self.option_id),
                "option_description: " + str(self.option_description)
                ])

        return f"Option: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcOption):
        """ Translates a gRPC struct to the SDK equivalent """
        return Option(
                
                rpcOption.option_id,
                
                
                rpcOption.option_description
                )

    def translate_to_rpc(self, rpcOption):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcOption.option_id = self.option_id
            
        
        
        
            
        rpcOption.option_description = self.option_description
            
        
        


class Setting:
    """
     Type to represent a setting with a selected option.

     Parameters
     ----------
     setting_id : std::string
          Name of a setting (machine readable)

     setting_description : std::string
          Description of the setting (human readable). This field is meant to be read from the drone, ignore it when setting.

     option : Option
          Selected option

     is_range : bool
          If option is given as a range. This field is meant to be read from the drone, ignore it when setting.

     """

    

    def __init__(
            self,
            setting_id,
            setting_description,
            option,
            is_range):
        """ Initializes the Setting object """
        self.setting_id = setting_id
        self.setting_description = setting_description
        self.option = option
        self.is_range = is_range

    def __equals__(self, to_compare):
        """ Checks if two Setting are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Setting object
            return \
                (self.setting_id == to_compare.setting_id) and \
                (self.setting_description == to_compare.setting_description) and \
                (self.option == to_compare.option) and \
                (self.is_range == to_compare.is_range)

        except AttributeError:
            return False

    def __str__(self):
        """ Setting in string representation """
        struct_repr = ", ".join([
                "setting_id: " + str(self.setting_id),
                "setting_description: " + str(self.setting_description),
                "option: " + str(self.option),
                "is_range: " + str(self.is_range)
                ])

        return f"Setting: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcSetting):
        """ Translates a gRPC struct to the SDK equivalent """
        return Setting(
                
                rpcSetting.setting_id,
                
                
                rpcSetting.setting_description,
                
                
                Option.translate_from_rpc(rpcSetting.option),
                
                
                rpcSetting.is_range
                )

    def translate_to_rpc(self, rpcSetting):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcSetting.setting_id = self.setting_id
            
        
        
        
            
        rpcSetting.setting_description = self.setting_description
            
        
        
        
            
        self.option.translate_to_rpc(rpcSetting.option)
            
        
        
        
            
        rpcSetting.is_range = self.is_range
            
        
        


class SettingOptions:
    """
     Type to represent a setting with a list of options to choose from.

     Parameters
     ----------
     setting_id : std::string
          Name of the setting (machine readable)

     setting_description : std::string
          Description of the setting (human readable)

     options : [Option]
          List of options or if range [min, max] or [min, max, interval]

     is_range : bool
          If option is given as a range

     """

    

    def __init__(
            self,
            setting_id,
            setting_description,
            options,
            is_range):
        """ Initializes the SettingOptions object """
        self.setting_id = setting_id
        self.setting_description = setting_description
        self.options = options
        self.is_range = is_range

    def __equals__(self, to_compare):
        """ Checks if two SettingOptions are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SettingOptions object
            return \
                (self.setting_id == to_compare.setting_id) and \
                (self.setting_description == to_compare.setting_description) and \
                (self.options == to_compare.options) and \
                (self.is_range == to_compare.is_range)

        except AttributeError:
            return False

    def __str__(self):
        """ SettingOptions in string representation """
        struct_repr = ", ".join([
                "setting_id: " + str(self.setting_id),
                "setting_description: " + str(self.setting_description),
                "options: " + str(self.options),
                "is_range: " + str(self.is_range)
                ])

        return f"SettingOptions: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcSettingOptions):
        """ Translates a gRPC struct to the SDK equivalent """
        return SettingOptions(
                
                rpcSettingOptions.setting_id,
                
                
                rpcSettingOptions.setting_description,
                
                
                Option.translate_from_rpc(rpcSettingOptions.options),
                
                
                rpcSettingOptions.is_range
                )

    def translate_to_rpc(self, rpcSettingOptions):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcSettingOptions.setting_id = self.setting_id
            
        
        
        
            
        rpcSettingOptions.setting_description = self.setting_description
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.options:
            rpc_elem = camera_pb2.Option()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        rpcSettingOptions.options.extend(rpc_elems_list)
            
        
        
        
            
        rpcSettingOptions.is_range = self.is_range
            
        
        


class Information:
    """
     Type to represent a camera information.

     Parameters
     ----------
     vendor_name : std::string
          Name of the camera vendor

     model_name : std::string
          Name of the camera model

     """

    

    def __init__(
            self,
            vendor_name,
            model_name):
        """ Initializes the Information object """
        self.vendor_name = vendor_name
        self.model_name = model_name

    def __equals__(self, to_compare):
        """ Checks if two Information are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Information object
            return \
                (self.vendor_name == to_compare.vendor_name) and \
                (self.model_name == to_compare.model_name)

        except AttributeError:
            return False

    def __str__(self):
        """ Information in string representation """
        struct_repr = ", ".join([
                "vendor_name: " + str(self.vendor_name),
                "model_name: " + str(self.model_name)
                ])

        return f"Information: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcInformation):
        """ Translates a gRPC struct to the SDK equivalent """
        return Information(
                
                rpcInformation.vendor_name,
                
                
                rpcInformation.model_name
                )

    def translate_to_rpc(self, rpcInformation):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcInformation.vendor_name = self.vendor_name
            
        
        
        
            
        rpcInformation.model_name = self.model_name
            
        
        



class CameraError(Exception):
    """ Raised when a CameraResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Camera(AsyncBase):
    """
     Can be used to manage cameras that implement the MAVLink
     Camera Protocol: https://mavlink.io/en/protocol/camera.html.

     Currently only a single camera is supported.
     When multiple cameras are supported the plugin will need to be
     instantiated separately for every camera and the camera selected using
     `select_camera`.

     Generated by dcsdkgen - MAVSDK Camera API
    """

    # Plugin name
    name = "Camera"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = camera_pb2_grpc.CameraServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return CameraResult.translate_from_rpc(response.camera_result)
    

    async def take_photo(self):
        """
         Take one photo.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.TakePhotoRequest()
        response = await self._stub.TakePhoto(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "take_photo()")
        

    async def start_photo_interval(self, interval_s):
        """
         Start photo timelapse with a given interval.

         Parameters
         ----------
         interval_s : float
              Interval between photos (in seconds)

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartPhotoIntervalRequest()
        request.interval_s = interval_s
        response = await self._stub.StartPhotoInterval(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_photo_interval()", interval_s)
        

    async def stop_photo_interval(self):
        """
         Stop a running photo timelapse.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopPhotoIntervalRequest()
        response = await self._stub.StopPhotoInterval(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_photo_interval()")
        

    async def start_video(self):
        """
         Start a video recording.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartVideoRequest()
        response = await self._stub.StartVideo(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_video()")
        

    async def stop_video(self):
        """
         Stop a running video recording.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopVideoRequest()
        response = await self._stub.StopVideo(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_video()")
        

    async def start_video_streaming(self):
        """
         Start video streaming.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartVideoStreamingRequest()
        response = await self._stub.StartVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_video_streaming()")
        

    async def stop_video_streaming(self):
        """
         Stop current video streaming.

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopVideoStreamingRequest()
        response = await self._stub.StopVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_video_streaming()")
        

    async def set_mode(self, mode):
        """
         Set camera mode.

         Parameters
         ----------
         mode : Mode
              Camera mode to set

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.SetModeRequest()
        
        mode.translate_to_rpc(request.mode)
                
            
        response = await self._stub.SetMode(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "set_mode()", mode)
        

    async def mode(self):
        """
         Subscribe to camera mode updates.

         Yields
         -------
         mode : Mode
              Camera mode

         
        """

        request = camera_pb2.SubscribeModeRequest()
        mode_stream = self._stub.SubscribeMode(request)

        try:
            async for response in mode_stream:
                

            
                yield Mode.translate_from_rpc(response.mode)
        finally:
            mode_stream.cancel()

    async def information(self):
        """
         Subscribe to camera information updates.

         Yields
         -------
         information : Information
              Camera information

         
        """

        request = camera_pb2.SubscribeInformationRequest()
        information_stream = self._stub.SubscribeInformation(request)

        try:
            async for response in information_stream:
                

            
                yield Information.translate_from_rpc(response.information)
        finally:
            information_stream.cancel()

    async def video_stream_info(self):
        """
         Subscribe to video stream info updates.

         Yields
         -------
         video_stream_info : VideoStreamInfo
              Video stream info

         
        """

        request = camera_pb2.SubscribeVideoStreamInfoRequest()
        video_stream_info_stream = self._stub.SubscribeVideoStreamInfo(request)

        try:
            async for response in video_stream_info_stream:
                

            
                yield VideoStreamInfo.translate_from_rpc(response.video_stream_info)
        finally:
            video_stream_info_stream.cancel()

    async def capture_info(self):
        """
         Subscribe to capture info updates.

         Yields
         -------
         capture_info : CaptureInfo
              Capture info

         
        """

        request = camera_pb2.SubscribeCaptureInfoRequest()
        capture_info_stream = self._stub.SubscribeCaptureInfo(request)

        try:
            async for response in capture_info_stream:
                

            
                yield CaptureInfo.translate_from_rpc(response.capture_info)
        finally:
            capture_info_stream.cancel()

    async def status(self):
        """
         Subscribe to camera status updates.

         Yields
         -------
         camera_status : Status
              Camera status

         
        """

        request = camera_pb2.SubscribeStatusRequest()
        status_stream = self._stub.SubscribeStatus(request)

        try:
            async for response in status_stream:
                

            
                yield Status.translate_from_rpc(response.camera_status)
        finally:
            status_stream.cancel()

    async def current_settings(self):
        """
         Get the list of current camera settings.

         Yields
         -------
         current_settings : [Setting]
              List of current settings

         
        """

        request = camera_pb2.SubscribeCurrentSettingsRequest()
        current_settings_stream = self._stub.SubscribeCurrentSettings(request)

        try:
            async for response in current_settings_stream:
                

            
                yield [Setting].translate_from_rpc(response.current_settings)
        finally:
            current_settings_stream.cancel()

    async def possible_setting_options(self):
        """
         Get the list of settings that can be changed.

         Yields
         -------
         setting_options : [SettingOptions]
              List of settings that can be changed

         
        """

        request = camera_pb2.SubscribePossibleSettingOptionsRequest()
        possible_setting_options_stream = self._stub.SubscribePossibleSettingOptions(request)

        try:
            async for response in possible_setting_options_stream:
                

            
                yield [SettingOptions].translate_from_rpc(response.setting_options)
        finally:
            possible_setting_options_stream.cancel()

    async def set_setting(self, setting):
        """
         Set a setting to some value.

         Only setting_id of setting and option_id of option needs to be set.

         Parameters
         ----------
         setting : Setting
              Desired setting

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.SetSettingRequest()
        
        setting.translate_to_rpc(request.setting)
                
            
        response = await self._stub.SetSetting(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "set_setting()", setting)
        

    async def get_setting(self, setting):
        """
         Get a setting.

         Only setting_id of setting needs to be set.

         Parameters
         ----------
         setting : Setting
              Requested setting

         Returns
         -------
         setting : Setting
              Setting

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetSettingRequest()
        
            
                
        setting.translate_to_rpc(request.setting)
                
            
        response = await self._stub.GetSetting(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_setting()", setting)
        

        return Setting.translate_from_rpc(response.setting)
            

    async def format_storage(self):
        """
         Format storage (e.g. SD card) in camera.

         This will delete all content of the camera storage!

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FormatStorageRequest()
        response = await self._stub.FormatStorage(request)

        
        result = self._extract_result(response)

        if result.result is not CameraResult.Result.SUCCESS:
            raise CameraError(result, "format_storage()")
        