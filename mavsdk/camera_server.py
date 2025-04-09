# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import camera_server_pb2, camera_server_pb2_grpc
from enum import Enum


class CameraFeedback(Enum):
    """
     Possible feedback results for camera respond command.

     Values
     ------
     UNKNOWN
          Unknown

     OK
          Ok

     BUSY
          Busy

     FAILED
          Failed

     """

    
    UNKNOWN = 0
    OK = 1
    BUSY = 2
    FAILED = 3

    def translate_to_rpc(self):
        if self == CameraFeedback.UNKNOWN:
            return camera_server_pb2.CAMERA_FEEDBACK_UNKNOWN
        if self == CameraFeedback.OK:
            return camera_server_pb2.CAMERA_FEEDBACK_OK
        if self == CameraFeedback.BUSY:
            return camera_server_pb2.CAMERA_FEEDBACK_BUSY
        if self == CameraFeedback.FAILED:
            return camera_server_pb2.CAMERA_FEEDBACK_FAILED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == camera_server_pb2.CAMERA_FEEDBACK_UNKNOWN:
            return CameraFeedback.UNKNOWN
        if rpc_enum_value == camera_server_pb2.CAMERA_FEEDBACK_OK:
            return CameraFeedback.OK
        if rpc_enum_value == camera_server_pb2.CAMERA_FEEDBACK_BUSY:
            return CameraFeedback.BUSY
        if rpc_enum_value == camera_server_pb2.CAMERA_FEEDBACK_FAILED:
            return CameraFeedback.FAILED

    def __str__(self):
        return self.name


class Mode(Enum):
    """
     Camera mode type.

     Values
     ------
     UNKNOWN
          Unknown mode

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
            return camera_server_pb2.MODE_UNKNOWN
        if self == Mode.PHOTO:
            return camera_server_pb2.MODE_PHOTO
        if self == Mode.VIDEO:
            return camera_server_pb2.MODE_VIDEO

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == camera_server_pb2.MODE_UNKNOWN:
            return Mode.UNKNOWN
        if rpc_enum_value == camera_server_pb2.MODE_PHOTO:
            return Mode.PHOTO
        if rpc_enum_value == camera_server_pb2.MODE_VIDEO:
            return Mode.VIDEO

    def __str__(self):
        return self.name


class Information:
    """
     Type to represent a camera information.

     Parameters
     ----------
     vendor_name : std::string
          Name of the camera vendor

     model_name : std::string
          Name of the camera model

     firmware_version : std::string
          Camera firmware version in major[.minor[.patch[.dev]]] format

     focal_length_mm : float
          Focal length

     horizontal_sensor_size_mm : float
          Horizontal sensor size

     vertical_sensor_size_mm : float
          Vertical sensor size

     horizontal_resolution_px : uint32_t
          Horizontal image resolution in pixels

     vertical_resolution_px : uint32_t
          Vertical image resolution in pixels

     lens_id : uint32_t
          Lens ID

     definition_file_version : uint32_t
          Camera definition file version (iteration)

     definition_file_uri : std::string
          Camera definition URI (http or mavlink ftp)

     image_in_video_mode_supported : bool
          Camera supports taking images while in video mode

     video_in_image_mode_supported : bool
          Camera supports recording video while in image mode

     """

    

    def __init__(
            self,
            vendor_name,
            model_name,
            firmware_version,
            focal_length_mm,
            horizontal_sensor_size_mm,
            vertical_sensor_size_mm,
            horizontal_resolution_px,
            vertical_resolution_px,
            lens_id,
            definition_file_version,
            definition_file_uri,
            image_in_video_mode_supported,
            video_in_image_mode_supported):
        """ Initializes the Information object """
        self.vendor_name = vendor_name
        self.model_name = model_name
        self.firmware_version = firmware_version
        self.focal_length_mm = focal_length_mm
        self.horizontal_sensor_size_mm = horizontal_sensor_size_mm
        self.vertical_sensor_size_mm = vertical_sensor_size_mm
        self.horizontal_resolution_px = horizontal_resolution_px
        self.vertical_resolution_px = vertical_resolution_px
        self.lens_id = lens_id
        self.definition_file_version = definition_file_version
        self.definition_file_uri = definition_file_uri
        self.image_in_video_mode_supported = image_in_video_mode_supported
        self.video_in_image_mode_supported = video_in_image_mode_supported

    def __eq__(self, to_compare):
        """ Checks if two Information are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Information object
            return \
                (self.vendor_name == to_compare.vendor_name) and \
                (self.model_name == to_compare.model_name) and \
                (self.firmware_version == to_compare.firmware_version) and \
                (self.focal_length_mm == to_compare.focal_length_mm) and \
                (self.horizontal_sensor_size_mm == to_compare.horizontal_sensor_size_mm) and \
                (self.vertical_sensor_size_mm == to_compare.vertical_sensor_size_mm) and \
                (self.horizontal_resolution_px == to_compare.horizontal_resolution_px) and \
                (self.vertical_resolution_px == to_compare.vertical_resolution_px) and \
                (self.lens_id == to_compare.lens_id) and \
                (self.definition_file_version == to_compare.definition_file_version) and \
                (self.definition_file_uri == to_compare.definition_file_uri) and \
                (self.image_in_video_mode_supported == to_compare.image_in_video_mode_supported) and \
                (self.video_in_image_mode_supported == to_compare.video_in_image_mode_supported)

        except AttributeError:
            return False

    def __str__(self):
        """ Information in string representation """
        struct_repr = ", ".join([
                "vendor_name: " + str(self.vendor_name),
                "model_name: " + str(self.model_name),
                "firmware_version: " + str(self.firmware_version),
                "focal_length_mm: " + str(self.focal_length_mm),
                "horizontal_sensor_size_mm: " + str(self.horizontal_sensor_size_mm),
                "vertical_sensor_size_mm: " + str(self.vertical_sensor_size_mm),
                "horizontal_resolution_px: " + str(self.horizontal_resolution_px),
                "vertical_resolution_px: " + str(self.vertical_resolution_px),
                "lens_id: " + str(self.lens_id),
                "definition_file_version: " + str(self.definition_file_version),
                "definition_file_uri: " + str(self.definition_file_uri),
                "image_in_video_mode_supported: " + str(self.image_in_video_mode_supported),
                "video_in_image_mode_supported: " + str(self.video_in_image_mode_supported)
                ])

        return f"Information: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcInformation):
        """ Translates a gRPC struct to the SDK equivalent """
        return Information(
                
                rpcInformation.vendor_name,
                
                
                rpcInformation.model_name,
                
                
                rpcInformation.firmware_version,
                
                
                rpcInformation.focal_length_mm,
                
                
                rpcInformation.horizontal_sensor_size_mm,
                
                
                rpcInformation.vertical_sensor_size_mm,
                
                
                rpcInformation.horizontal_resolution_px,
                
                
                rpcInformation.vertical_resolution_px,
                
                
                rpcInformation.lens_id,
                
                
                rpcInformation.definition_file_version,
                
                
                rpcInformation.definition_file_uri,
                
                
                rpcInformation.image_in_video_mode_supported,
                
                
                rpcInformation.video_in_image_mode_supported
                )

    def translate_to_rpc(self, rpcInformation):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcInformation.vendor_name = self.vendor_name
            
        
        
        
            
        rpcInformation.model_name = self.model_name
            
        
        
        
            
        rpcInformation.firmware_version = self.firmware_version
            
        
        
        
            
        rpcInformation.focal_length_mm = self.focal_length_mm
            
        
        
        
            
        rpcInformation.horizontal_sensor_size_mm = self.horizontal_sensor_size_mm
            
        
        
        
            
        rpcInformation.vertical_sensor_size_mm = self.vertical_sensor_size_mm
            
        
        
        
            
        rpcInformation.horizontal_resolution_px = self.horizontal_resolution_px
            
        
        
        
            
        rpcInformation.vertical_resolution_px = self.vertical_resolution_px
            
        
        
        
            
        rpcInformation.lens_id = self.lens_id
            
        
        
        
            
        rpcInformation.definition_file_version = self.definition_file_version
            
        
        
        
            
        rpcInformation.definition_file_uri = self.definition_file_uri
            
        
        
        
            
        rpcInformation.image_in_video_mode_supported = self.image_in_video_mode_supported
            
        
        
        
            
        rpcInformation.video_in_image_mode_supported = self.video_in_image_mode_supported
            
        
        


class VideoStreaming:
    """
     Type to represent video streaming settings

     Parameters
     ----------
     has_rtsp_server : bool
          True if the capture was successful

     rtsp_uri : std::string
          RTSP URI (e.g. rtsp://192.168.1.42:8554/live)

     """

    

    def __init__(
            self,
            has_rtsp_server,
            rtsp_uri):
        """ Initializes the VideoStreaming object """
        self.has_rtsp_server = has_rtsp_server
        self.rtsp_uri = rtsp_uri

    def __eq__(self, to_compare):
        """ Checks if two VideoStreaming are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VideoStreaming object
            return \
                (self.has_rtsp_server == to_compare.has_rtsp_server) and \
                (self.rtsp_uri == to_compare.rtsp_uri)

        except AttributeError:
            return False

    def __str__(self):
        """ VideoStreaming in string representation """
        struct_repr = ", ".join([
                "has_rtsp_server: " + str(self.has_rtsp_server),
                "rtsp_uri: " + str(self.rtsp_uri)
                ])

        return f"VideoStreaming: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVideoStreaming):
        """ Translates a gRPC struct to the SDK equivalent """
        return VideoStreaming(
                
                rpcVideoStreaming.has_rtsp_server,
                
                
                rpcVideoStreaming.rtsp_uri
                )

    def translate_to_rpc(self, rpcVideoStreaming):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVideoStreaming.has_rtsp_server = self.has_rtsp_server
            
        
        
        
            
        rpcVideoStreaming.rtsp_uri = self.rtsp_uri
            
        
        


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

    def __eq__(self, to_compare):
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
            
        
        


class CaptureInfo:
    """
     Information about a picture just captured.

     Parameters
     ----------
     position : Position
          Location where the picture was taken

     attitude_quaternion : Quaternion
          Attitude of the camera when the picture was taken (quaternion)

     time_utc_us : uint64_t
          Timestamp in UTC (since UNIX epoch) in microseconds

     is_success : bool
          True if the capture was successful

     index : int32_t
          Index from TakePhotoResponse

     file_url : std::string
          Download URL of this image

     """

    

    def __init__(
            self,
            position,
            attitude_quaternion,
            time_utc_us,
            is_success,
            index,
            file_url):
        """ Initializes the CaptureInfo object """
        self.position = position
        self.attitude_quaternion = attitude_quaternion
        self.time_utc_us = time_utc_us
        self.is_success = is_success
        self.index = index
        self.file_url = file_url

    def __eq__(self, to_compare):
        """ Checks if two CaptureInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CaptureInfo object
            return \
                (self.position == to_compare.position) and \
                (self.attitude_quaternion == to_compare.attitude_quaternion) and \
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
                
                
                rpcCaptureInfo.time_utc_us,
                
                
                rpcCaptureInfo.is_success,
                
                
                rpcCaptureInfo.index,
                
                
                rpcCaptureInfo.file_url
                )

    def translate_to_rpc(self, rpcCaptureInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.position.translate_to_rpc(rpcCaptureInfo.position)
            
        
        
        
            
        self.attitude_quaternion.translate_to_rpc(rpcCaptureInfo.attitude_quaternion)
            
        
        
        
            
        rpcCaptureInfo.time_utc_us = self.time_utc_us
            
        
        
        
            
        rpcCaptureInfo.is_success = self.is_success
            
        
        
        
            
        rpcCaptureInfo.index = self.index
            
        
        
        
            
        rpcCaptureInfo.file_url = self.file_url
            
        
        


class CameraServerResult:
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
              Command executed successfully

         IN_PROGRESS
              Command in progress

         BUSY
              Camera is busy and rejected command

         DENIED
              Camera denied the command

         ERROR
              An error has occurred while executing the command

         TIMEOUT
              Command timed out

         WRONG_ARGUMENT
              Command has wrong argument(s)

         NO_SYSTEM
              No system connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        IN_PROGRESS = 2
        BUSY = 3
        DENIED = 4
        ERROR = 5
        TIMEOUT = 6
        WRONG_ARGUMENT = 7
        NO_SYSTEM = 8

        def translate_to_rpc(self):
            if self == CameraServerResult.Result.UNKNOWN:
                return camera_server_pb2.CameraServerResult.RESULT_UNKNOWN
            if self == CameraServerResult.Result.SUCCESS:
                return camera_server_pb2.CameraServerResult.RESULT_SUCCESS
            if self == CameraServerResult.Result.IN_PROGRESS:
                return camera_server_pb2.CameraServerResult.RESULT_IN_PROGRESS
            if self == CameraServerResult.Result.BUSY:
                return camera_server_pb2.CameraServerResult.RESULT_BUSY
            if self == CameraServerResult.Result.DENIED:
                return camera_server_pb2.CameraServerResult.RESULT_DENIED
            if self == CameraServerResult.Result.ERROR:
                return camera_server_pb2.CameraServerResult.RESULT_ERROR
            if self == CameraServerResult.Result.TIMEOUT:
                return camera_server_pb2.CameraServerResult.RESULT_TIMEOUT
            if self == CameraServerResult.Result.WRONG_ARGUMENT:
                return camera_server_pb2.CameraServerResult.RESULT_WRONG_ARGUMENT
            if self == CameraServerResult.Result.NO_SYSTEM:
                return camera_server_pb2.CameraServerResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_UNKNOWN:
                return CameraServerResult.Result.UNKNOWN
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_SUCCESS:
                return CameraServerResult.Result.SUCCESS
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_IN_PROGRESS:
                return CameraServerResult.Result.IN_PROGRESS
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_BUSY:
                return CameraServerResult.Result.BUSY
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_DENIED:
                return CameraServerResult.Result.DENIED
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_ERROR:
                return CameraServerResult.Result.ERROR
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_TIMEOUT:
                return CameraServerResult.Result.TIMEOUT
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_WRONG_ARGUMENT:
                return CameraServerResult.Result.WRONG_ARGUMENT
            if rpc_enum_value == camera_server_pb2.CameraServerResult.RESULT_NO_SYSTEM:
                return CameraServerResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the CameraServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two CameraServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CameraServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ CameraServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"CameraServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCameraServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return CameraServerResult(
                
                CameraServerResult.Result.translate_from_rpc(rpcCameraServerResult.result),
                
                
                rpcCameraServerResult.result_str
                )

    def translate_to_rpc(self, rpcCameraServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCameraServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcCameraServerResult.result_str = self.result_str
            
        
        


class StorageInformation:
    """
     Information about the camera storage.

     Parameters
     ----------
     used_storage_mib : float
          Used storage (in MiB)

     available_storage_mib : float
          Available storage (in MiB)

     total_storage_mib : float
          Total storage (in MiB)

     storage_status : StorageStatus
          Storage status

     storage_id : uint32_t
          Storage ID starting at 1

     storage_type : StorageType
          Storage type

     read_speed_mib_s : float
          Read speed [MiB/s]

     write_speed_mib_s : float
          Write speed [MiB/s]

     """

    
    
    class StorageStatus(Enum):
        """
         Storage status type.

         Values
         ------
         NOT_AVAILABLE
              Storage not available

         UNFORMATTED
              Storage is not formatted (i.e. has no recognized file system)

         FORMATTED
              Storage is formatted (i.e. has recognized a file system)

         NOT_SUPPORTED
              Storage status is not supported

         """

        
        NOT_AVAILABLE = 0
        UNFORMATTED = 1
        FORMATTED = 2
        NOT_SUPPORTED = 3

        def translate_to_rpc(self):
            if self == StorageInformation.StorageStatus.NOT_AVAILABLE:
                return camera_server_pb2.StorageInformation.STORAGE_STATUS_NOT_AVAILABLE
            if self == StorageInformation.StorageStatus.UNFORMATTED:
                return camera_server_pb2.StorageInformation.STORAGE_STATUS_UNFORMATTED
            if self == StorageInformation.StorageStatus.FORMATTED:
                return camera_server_pb2.StorageInformation.STORAGE_STATUS_FORMATTED
            if self == StorageInformation.StorageStatus.NOT_SUPPORTED:
                return camera_server_pb2.StorageInformation.STORAGE_STATUS_NOT_SUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_STATUS_NOT_AVAILABLE:
                return StorageInformation.StorageStatus.NOT_AVAILABLE
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_STATUS_UNFORMATTED:
                return StorageInformation.StorageStatus.UNFORMATTED
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_STATUS_FORMATTED:
                return StorageInformation.StorageStatus.FORMATTED
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_STATUS_NOT_SUPPORTED:
                return StorageInformation.StorageStatus.NOT_SUPPORTED

        def __str__(self):
            return self.name
    
    
    class StorageType(Enum):
        """
         Storage type.

         Values
         ------
         UNKNOWN
              Storage type unknown

         USB_STICK
              Storage type USB stick

         SD
              Storage type SD card

         MICROSD
              Storage type MicroSD card

         HD
              Storage type HD mass storage

         OTHER
              Storage type other, not listed

         """

        
        UNKNOWN = 0
        USB_STICK = 1
        SD = 2
        MICROSD = 3
        HD = 4
        OTHER = 5

        def translate_to_rpc(self):
            if self == StorageInformation.StorageType.UNKNOWN:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_UNKNOWN
            if self == StorageInformation.StorageType.USB_STICK:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_USB_STICK
            if self == StorageInformation.StorageType.SD:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_SD
            if self == StorageInformation.StorageType.MICROSD:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_MICROSD
            if self == StorageInformation.StorageType.HD:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_HD
            if self == StorageInformation.StorageType.OTHER:
                return camera_server_pb2.StorageInformation.STORAGE_TYPE_OTHER

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_UNKNOWN:
                return StorageInformation.StorageType.UNKNOWN
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_USB_STICK:
                return StorageInformation.StorageType.USB_STICK
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_SD:
                return StorageInformation.StorageType.SD
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_MICROSD:
                return StorageInformation.StorageType.MICROSD
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_HD:
                return StorageInformation.StorageType.HD
            if rpc_enum_value == camera_server_pb2.StorageInformation.STORAGE_TYPE_OTHER:
                return StorageInformation.StorageType.OTHER

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            used_storage_mib,
            available_storage_mib,
            total_storage_mib,
            storage_status,
            storage_id,
            storage_type,
            read_speed_mib_s,
            write_speed_mib_s):
        """ Initializes the StorageInformation object """
        self.used_storage_mib = used_storage_mib
        self.available_storage_mib = available_storage_mib
        self.total_storage_mib = total_storage_mib
        self.storage_status = storage_status
        self.storage_id = storage_id
        self.storage_type = storage_type
        self.read_speed_mib_s = read_speed_mib_s
        self.write_speed_mib_s = write_speed_mib_s

    def __eq__(self, to_compare):
        """ Checks if two StorageInformation are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # StorageInformation object
            return \
                (self.used_storage_mib == to_compare.used_storage_mib) and \
                (self.available_storage_mib == to_compare.available_storage_mib) and \
                (self.total_storage_mib == to_compare.total_storage_mib) and \
                (self.storage_status == to_compare.storage_status) and \
                (self.storage_id == to_compare.storage_id) and \
                (self.storage_type == to_compare.storage_type) and \
                (self.read_speed_mib_s == to_compare.read_speed_mib_s) and \
                (self.write_speed_mib_s == to_compare.write_speed_mib_s)

        except AttributeError:
            return False

    def __str__(self):
        """ StorageInformation in string representation """
        struct_repr = ", ".join([
                "used_storage_mib: " + str(self.used_storage_mib),
                "available_storage_mib: " + str(self.available_storage_mib),
                "total_storage_mib: " + str(self.total_storage_mib),
                "storage_status: " + str(self.storage_status),
                "storage_id: " + str(self.storage_id),
                "storage_type: " + str(self.storage_type),
                "read_speed_mib_s: " + str(self.read_speed_mib_s),
                "write_speed_mib_s: " + str(self.write_speed_mib_s)
                ])

        return f"StorageInformation: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStorageInformation):
        """ Translates a gRPC struct to the SDK equivalent """
        return StorageInformation(
                
                rpcStorageInformation.used_storage_mib,
                
                
                rpcStorageInformation.available_storage_mib,
                
                
                rpcStorageInformation.total_storage_mib,
                
                
                StorageInformation.StorageStatus.translate_from_rpc(rpcStorageInformation.storage_status),
                
                
                rpcStorageInformation.storage_id,
                
                
                StorageInformation.StorageType.translate_from_rpc(rpcStorageInformation.storage_type),
                
                
                rpcStorageInformation.read_speed_mib_s,
                
                
                rpcStorageInformation.write_speed_mib_s
                )

    def translate_to_rpc(self, rpcStorageInformation):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStorageInformation.used_storage_mib = self.used_storage_mib
            
        
        
        
            
        rpcStorageInformation.available_storage_mib = self.available_storage_mib
            
        
        
        
            
        rpcStorageInformation.total_storage_mib = self.total_storage_mib
            
        
        
        
            
        rpcStorageInformation.storage_status = self.storage_status.translate_to_rpc()
            
        
        
        
            
        rpcStorageInformation.storage_id = self.storage_id
            
        
        
        
            
        rpcStorageInformation.storage_type = self.storage_type.translate_to_rpc()
            
        
        
        
            
        rpcStorageInformation.read_speed_mib_s = self.read_speed_mib_s
            
        
        
        
            
        rpcStorageInformation.write_speed_mib_s = self.write_speed_mib_s
            
        
        


class CaptureStatus:
    """
     Capture status

     Parameters
     ----------
     image_interval_s : float
          Image capture interval (in s)

     recording_time_s : float
          Elapsed time since recording started (in s)

     available_capacity_mib : float
          Available storage capacity. (in MiB)

     image_status : ImageStatus
          Current status of image capturing

     video_status : VideoStatus
          Current status of video capturing

     image_count : int32_t
          Total number of images captured ('forever', or until reset using MAV_CMD_STORAGE_FORMAT)

     """

    
    
    class ImageStatus(Enum):
        """
         The image status

         Values
         ------
         IDLE
              idle

         CAPTURE_IN_PROGRESS
              capture in progress

         INTERVAL_IDLE
              interval set but idle

         INTERVAL_IN_PROGRESS
              interval set and capture in progress)

         """

        
        IDLE = 0
        CAPTURE_IN_PROGRESS = 1
        INTERVAL_IDLE = 2
        INTERVAL_IN_PROGRESS = 3

        def translate_to_rpc(self):
            if self == CaptureStatus.ImageStatus.IDLE:
                return camera_server_pb2.CaptureStatus.IMAGE_STATUS_IDLE
            if self == CaptureStatus.ImageStatus.CAPTURE_IN_PROGRESS:
                return camera_server_pb2.CaptureStatus.IMAGE_STATUS_CAPTURE_IN_PROGRESS
            if self == CaptureStatus.ImageStatus.INTERVAL_IDLE:
                return camera_server_pb2.CaptureStatus.IMAGE_STATUS_INTERVAL_IDLE
            if self == CaptureStatus.ImageStatus.INTERVAL_IN_PROGRESS:
                return camera_server_pb2.CaptureStatus.IMAGE_STATUS_INTERVAL_IN_PROGRESS

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_server_pb2.CaptureStatus.IMAGE_STATUS_IDLE:
                return CaptureStatus.ImageStatus.IDLE
            if rpc_enum_value == camera_server_pb2.CaptureStatus.IMAGE_STATUS_CAPTURE_IN_PROGRESS:
                return CaptureStatus.ImageStatus.CAPTURE_IN_PROGRESS
            if rpc_enum_value == camera_server_pb2.CaptureStatus.IMAGE_STATUS_INTERVAL_IDLE:
                return CaptureStatus.ImageStatus.INTERVAL_IDLE
            if rpc_enum_value == camera_server_pb2.CaptureStatus.IMAGE_STATUS_INTERVAL_IN_PROGRESS:
                return CaptureStatus.ImageStatus.INTERVAL_IN_PROGRESS

        def __str__(self):
            return self.name
    
    
    class VideoStatus(Enum):
        """
         The video status

         Values
         ------
         IDLE
              idle

         CAPTURE_IN_PROGRESS
              capture in progress

         """

        
        IDLE = 0
        CAPTURE_IN_PROGRESS = 1

        def translate_to_rpc(self):
            if self == CaptureStatus.VideoStatus.IDLE:
                return camera_server_pb2.CaptureStatus.VIDEO_STATUS_IDLE
            if self == CaptureStatus.VideoStatus.CAPTURE_IN_PROGRESS:
                return camera_server_pb2.CaptureStatus.VIDEO_STATUS_CAPTURE_IN_PROGRESS

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_server_pb2.CaptureStatus.VIDEO_STATUS_IDLE:
                return CaptureStatus.VideoStatus.IDLE
            if rpc_enum_value == camera_server_pb2.CaptureStatus.VIDEO_STATUS_CAPTURE_IN_PROGRESS:
                return CaptureStatus.VideoStatus.CAPTURE_IN_PROGRESS

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            image_interval_s,
            recording_time_s,
            available_capacity_mib,
            image_status,
            video_status,
            image_count):
        """ Initializes the CaptureStatus object """
        self.image_interval_s = image_interval_s
        self.recording_time_s = recording_time_s
        self.available_capacity_mib = available_capacity_mib
        self.image_status = image_status
        self.video_status = video_status
        self.image_count = image_count

    def __eq__(self, to_compare):
        """ Checks if two CaptureStatus are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CaptureStatus object
            return \
                (self.image_interval_s == to_compare.image_interval_s) and \
                (self.recording_time_s == to_compare.recording_time_s) and \
                (self.available_capacity_mib == to_compare.available_capacity_mib) and \
                (self.image_status == to_compare.image_status) and \
                (self.video_status == to_compare.video_status) and \
                (self.image_count == to_compare.image_count)

        except AttributeError:
            return False

    def __str__(self):
        """ CaptureStatus in string representation """
        struct_repr = ", ".join([
                "image_interval_s: " + str(self.image_interval_s),
                "recording_time_s: " + str(self.recording_time_s),
                "available_capacity_mib: " + str(self.available_capacity_mib),
                "image_status: " + str(self.image_status),
                "video_status: " + str(self.video_status),
                "image_count: " + str(self.image_count)
                ])

        return f"CaptureStatus: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCaptureStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return CaptureStatus(
                
                rpcCaptureStatus.image_interval_s,
                
                
                rpcCaptureStatus.recording_time_s,
                
                
                rpcCaptureStatus.available_capacity_mib,
                
                
                CaptureStatus.ImageStatus.translate_from_rpc(rpcCaptureStatus.image_status),
                
                
                CaptureStatus.VideoStatus.translate_from_rpc(rpcCaptureStatus.video_status),
                
                
                rpcCaptureStatus.image_count
                )

    def translate_to_rpc(self, rpcCaptureStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCaptureStatus.image_interval_s = self.image_interval_s
            
        
        
        
            
        rpcCaptureStatus.recording_time_s = self.recording_time_s
            
        
        
        
            
        rpcCaptureStatus.available_capacity_mib = self.available_capacity_mib
            
        
        
        
            
        rpcCaptureStatus.image_status = self.image_status.translate_to_rpc()
            
        
        
        
            
        rpcCaptureStatus.video_status = self.video_status.translate_to_rpc()
            
        
        
        
            
        rpcCaptureStatus.image_count = self.image_count
            
        
        


class TrackPoint:
    """
     Point description type

     Parameters
     ----------
     point_x : float
          Point to track x value (normalized 0..1, 0 is left, 1 is right).

     point_y : float
          Point to track y value (normalized 0..1, 0 is top, 1 is bottom).

     radius : float
          Point to track y value (normalized 0..1, 0 is top, 1 is bottom).

     """

    

    def __init__(
            self,
            point_x,
            point_y,
            radius):
        """ Initializes the TrackPoint object """
        self.point_x = point_x
        self.point_y = point_y
        self.radius = radius

    def __eq__(self, to_compare):
        """ Checks if two TrackPoint are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TrackPoint object
            return \
                (self.point_x == to_compare.point_x) and \
                (self.point_y == to_compare.point_y) and \
                (self.radius == to_compare.radius)

        except AttributeError:
            return False

    def __str__(self):
        """ TrackPoint in string representation """
        struct_repr = ", ".join([
                "point_x: " + str(self.point_x),
                "point_y: " + str(self.point_y),
                "radius: " + str(self.radius)
                ])

        return f"TrackPoint: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTrackPoint):
        """ Translates a gRPC struct to the SDK equivalent """
        return TrackPoint(
                
                rpcTrackPoint.point_x,
                
                
                rpcTrackPoint.point_y,
                
                
                rpcTrackPoint.radius
                )

    def translate_to_rpc(self, rpcTrackPoint):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTrackPoint.point_x = self.point_x
            
        
        
        
            
        rpcTrackPoint.point_y = self.point_y
            
        
        
        
            
        rpcTrackPoint.radius = self.radius
            
        
        


class TrackRectangle:
    """
     Rectangle description type

     Parameters
     ----------
     top_left_corner_x : float
          Top left corner of rectangle x value (normalized 0..1, 0 is left, 1 is right).

     top_left_corner_y : float
          Top left corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom).

     bottom_right_corner_x : float
          Bottom right corner of rectangle x value (normalized 0..1, 0 is left, 1 is right).

     bottom_right_corner_y : float
          Bottom right corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom).

     """

    

    def __init__(
            self,
            top_left_corner_x,
            top_left_corner_y,
            bottom_right_corner_x,
            bottom_right_corner_y):
        """ Initializes the TrackRectangle object """
        self.top_left_corner_x = top_left_corner_x
        self.top_left_corner_y = top_left_corner_y
        self.bottom_right_corner_x = bottom_right_corner_x
        self.bottom_right_corner_y = bottom_right_corner_y

    def __eq__(self, to_compare):
        """ Checks if two TrackRectangle are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TrackRectangle object
            return \
                (self.top_left_corner_x == to_compare.top_left_corner_x) and \
                (self.top_left_corner_y == to_compare.top_left_corner_y) and \
                (self.bottom_right_corner_x == to_compare.bottom_right_corner_x) and \
                (self.bottom_right_corner_y == to_compare.bottom_right_corner_y)

        except AttributeError:
            return False

    def __str__(self):
        """ TrackRectangle in string representation """
        struct_repr = ", ".join([
                "top_left_corner_x: " + str(self.top_left_corner_x),
                "top_left_corner_y: " + str(self.top_left_corner_y),
                "bottom_right_corner_x: " + str(self.bottom_right_corner_x),
                "bottom_right_corner_y: " + str(self.bottom_right_corner_y)
                ])

        return f"TrackRectangle: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTrackRectangle):
        """ Translates a gRPC struct to the SDK equivalent """
        return TrackRectangle(
                
                rpcTrackRectangle.top_left_corner_x,
                
                
                rpcTrackRectangle.top_left_corner_y,
                
                
                rpcTrackRectangle.bottom_right_corner_x,
                
                
                rpcTrackRectangle.bottom_right_corner_y
                )

    def translate_to_rpc(self, rpcTrackRectangle):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTrackRectangle.top_left_corner_x = self.top_left_corner_x
            
        
        
        
            
        rpcTrackRectangle.top_left_corner_y = self.top_left_corner_y
            
        
        
        
            
        rpcTrackRectangle.bottom_right_corner_x = self.bottom_right_corner_x
            
        
        
        
            
        rpcTrackRectangle.bottom_right_corner_y = self.bottom_right_corner_y
            
        
        



class CameraServerError(Exception):
    """ Raised when a CameraServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class CameraServer(AsyncBase):
    """
     Provides handling of camera interface

     Generated by dcsdkgen - MAVSDK CameraServer API
    """

    # Plugin name
    name = "CameraServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = camera_server_pb2_grpc.CameraServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return CameraServerResult.translate_from_rpc(response.camera_server_result)
    

    async def set_information(self, information):
        """
         Sets the camera information. This must be called as soon as the camera server is created.

         Parameters
         ----------
         information : Information
              information about the camera

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.SetInformationRequest()
        
        information.translate_to_rpc(request.information)
                
            
        response = await self._stub.SetInformation(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "set_information()", information)
        

    async def set_video_streaming(self, video_streaming):
        """
         Sets video streaming settings.

         Parameters
         ----------
         video_streaming : VideoStreaming
              information about the video stream

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.SetVideoStreamingRequest()
        
        video_streaming.translate_to_rpc(request.video_streaming)
                
            
        response = await self._stub.SetVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "set_video_streaming()", video_streaming)
        

    async def set_in_progress(self, in_progress):
        """
         Sets image capture in progress status flags. This should be set to true when the camera is busy taking a photo and false when it is done.

         Parameters
         ----------
         in_progress : bool
              true if capture is in progress or false for idle.

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.SetInProgressRequest()
        request.in_progress = in_progress
        response = await self._stub.SetInProgress(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "set_in_progress()", in_progress)
        

    async def take_photo(self):
        """
         Subscribe to image capture requests. Each request received should respond to using RespondTakePhoto.

         Yields
         -------
         index : int32_t
             
         
        """

        request = camera_server_pb2.SubscribeTakePhotoRequest()
        take_photo_stream = self._stub.SubscribeTakePhoto(request)

        try:
            async for response in take_photo_stream:
                

            
                yield response.index
        finally:
            take_photo_stream.cancel()

    async def respond_take_photo(self, take_photo_feedback, capture_info):
        """
         Respond to an image capture request from SubscribeTakePhoto.

         Parameters
         ----------
         take_photo_feedback : CameraFeedback
              the feedback

         capture_info : CaptureInfo
              the capture information

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondTakePhotoRequest()
        
        request.take_photo_feedback = take_photo_feedback.translate_to_rpc()
                
            
        
        capture_info.translate_to_rpc(request.capture_info)
                
            
        response = await self._stub.RespondTakePhoto(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_take_photo()", take_photo_feedback, capture_info)
        

    async def start_video(self):
        """
         Subscribe to start video requests. Each request received should respond to using RespondStartVideo

         Yields
         -------
         stream_id : int32_t
              video stream id

         
        """

        request = camera_server_pb2.SubscribeStartVideoRequest()
        start_video_stream = self._stub.SubscribeStartVideo(request)

        try:
            async for response in start_video_stream:
                

            
                yield response.stream_id
        finally:
            start_video_stream.cancel()

    async def respond_start_video(self, start_video_feedback):
        """
         Subscribe to stop video requests. Each request received should respond using StopVideoResponse

         Parameters
         ----------
         start_video_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondStartVideoRequest()
        
        request.start_video_feedback = start_video_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondStartVideo(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_start_video()", start_video_feedback)
        

    async def stop_video(self):
        """
         Subscribe to stop video requests. Each request received should response to using RespondStopVideo

         Yields
         -------
         stream_id : int32_t
              video stream id

         
        """

        request = camera_server_pb2.SubscribeStopVideoRequest()
        stop_video_stream = self._stub.SubscribeStopVideo(request)

        try:
            async for response in stop_video_stream:
                

            
                yield response.stream_id
        finally:
            stop_video_stream.cancel()

    async def respond_stop_video(self, stop_video_feedback):
        """
         Respond to stop video request from SubscribeStopVideo.

         Parameters
         ----------
         stop_video_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondStopVideoRequest()
        
        request.stop_video_feedback = stop_video_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondStopVideo(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_stop_video()", stop_video_feedback)
        

    async def start_video_streaming(self):
        """
         Subscribe to start video streaming requests. Each request received should response to using RespondStartVideoStreaming

         Yields
         -------
         stream_id : int32_t
              video stream id

         
        """

        request = camera_server_pb2.SubscribeStartVideoStreamingRequest()
        start_video_streaming_stream = self._stub.SubscribeStartVideoStreaming(request)

        try:
            async for response in start_video_streaming_stream:
                

            
                yield response.stream_id
        finally:
            start_video_streaming_stream.cancel()

    async def respond_start_video_streaming(self, start_video_streaming_feedback):
        """
         Respond to start video streaming from SubscribeStartVideoStreaming.

         Parameters
         ----------
         start_video_streaming_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondStartVideoStreamingRequest()
        
        request.start_video_streaming_feedback = start_video_streaming_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondStartVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_start_video_streaming()", start_video_streaming_feedback)
        

    async def stop_video_streaming(self):
        """
         Subscribe to stop video streaming requests. Each request received should response to using RespondStopVideoStreaming

         Yields
         -------
         stream_id : int32_t
              video stream id

         
        """

        request = camera_server_pb2.SubscribeStopVideoStreamingRequest()
        stop_video_streaming_stream = self._stub.SubscribeStopVideoStreaming(request)

        try:
            async for response in stop_video_streaming_stream:
                

            
                yield response.stream_id
        finally:
            stop_video_streaming_stream.cancel()

    async def respond_stop_video_streaming(self, stop_video_streaming_feedback):
        """
         Respond to stop video streaming from SubscribeStopVideoStreaming.

         Parameters
         ----------
         stop_video_streaming_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondStopVideoStreamingRequest()
        
        request.stop_video_streaming_feedback = stop_video_streaming_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondStopVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_stop_video_streaming()", stop_video_streaming_feedback)
        

    async def set_mode(self):
        """
         Subscribe to set camera mode requests. Each request received should response to using RespondSetMode

         Yields
         -------
         mode : Mode
             
         
        """

        request = camera_server_pb2.SubscribeSetModeRequest()
        set_mode_stream = self._stub.SubscribeSetMode(request)

        try:
            async for response in set_mode_stream:
                

            
                yield Mode.translate_from_rpc(response.mode)
        finally:
            set_mode_stream.cancel()

    async def respond_set_mode(self, set_mode_feedback):
        """
         Respond to set camera mode from SubscribeSetMode.

         Parameters
         ----------
         set_mode_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondSetModeRequest()
        
        request.set_mode_feedback = set_mode_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondSetMode(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_set_mode()", set_mode_feedback)
        

    async def storage_information(self):
        """
         Subscribe to camera storage information requests. Each request received should response to using RespondStorageInformation

         Yields
         -------
         storage_id : int32_t
             
         
        """

        request = camera_server_pb2.SubscribeStorageInformationRequest()
        storage_information_stream = self._stub.SubscribeStorageInformation(request)

        try:
            async for response in storage_information_stream:
                

            
                yield response.storage_id
        finally:
            storage_information_stream.cancel()

    async def respond_storage_information(self, storage_information_feedback, storage_information):
        """
         Respond to camera storage information from SubscribeStorageInformation.

         Parameters
         ----------
         storage_information_feedback : CameraFeedback
              the feedback

         storage_information : StorageInformation
              the storage information

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondStorageInformationRequest()
        
        request.storage_information_feedback = storage_information_feedback.translate_to_rpc()
                
            
        
        storage_information.translate_to_rpc(request.storage_information)
                
            
        response = await self._stub.RespondStorageInformation(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_storage_information()", storage_information_feedback, storage_information)
        

    async def capture_status(self):
        """
         Subscribe to camera capture status requests. Each request received should response to using RespondCaptureStatus

         Yields
         -------
         reserved : int32_t
              reserved, just make protoc-gen-mavsdk working

         
        """

        request = camera_server_pb2.SubscribeCaptureStatusRequest()
        capture_status_stream = self._stub.SubscribeCaptureStatus(request)

        try:
            async for response in capture_status_stream:
                

            
                yield response.reserved
        finally:
            capture_status_stream.cancel()

    async def respond_capture_status(self, capture_status_feedback, capture_status):
        """
         Respond to camera capture status from SubscribeCaptureStatus.

         Parameters
         ----------
         capture_status_feedback : CameraFeedback
              the feedback

         capture_status : CaptureStatus
              the capture status

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondCaptureStatusRequest()
        
        request.capture_status_feedback = capture_status_feedback.translate_to_rpc()
                
            
        
        capture_status.translate_to_rpc(request.capture_status)
                
            
        response = await self._stub.RespondCaptureStatus(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_capture_status()", capture_status_feedback, capture_status)
        

    async def format_storage(self):
        """
         Subscribe to format storage requests. Each request received should response to using RespondFormatStorage

         Yields
         -------
         storage_id : int32_t
              the storage id to format

         
        """

        request = camera_server_pb2.SubscribeFormatStorageRequest()
        format_storage_stream = self._stub.SubscribeFormatStorage(request)

        try:
            async for response in format_storage_stream:
                

            
                yield response.storage_id
        finally:
            format_storage_stream.cancel()

    async def respond_format_storage(self, format_storage_feedback):
        """
         Respond to format storage from SubscribeFormatStorage.

         Parameters
         ----------
         format_storage_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondFormatStorageRequest()
        
        request.format_storage_feedback = format_storage_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondFormatStorage(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_format_storage()", format_storage_feedback)
        

    async def reset_settings(self):
        """
         Subscribe to reset settings requests. Each request received should response to using RespondResetSettings

         Yields
         -------
         reserved : int32_t
              reserved, just make protoc-gen-mavsdk working

         
        """

        request = camera_server_pb2.SubscribeResetSettingsRequest()
        reset_settings_stream = self._stub.SubscribeResetSettings(request)

        try:
            async for response in reset_settings_stream:
                

            
                yield response.reserved
        finally:
            reset_settings_stream.cancel()

    async def respond_reset_settings(self, reset_settings_feedback):
        """
         Respond to reset settings from SubscribeResetSettings.

         Parameters
         ----------
         reset_settings_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondResetSettingsRequest()
        
        request.reset_settings_feedback = reset_settings_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondResetSettings(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_reset_settings()", reset_settings_feedback)
        

    async def zoom_in_start(self):
        """
         Subscribe to zoom in start command

         Yields
         -------
         reserved : int32_t
              reserved, just make protoc-gen-mavsdk working

         
        """

        request = camera_server_pb2.SubscribeZoomInStartRequest()
        zoom_in_start_stream = self._stub.SubscribeZoomInStart(request)

        try:
            async for response in zoom_in_start_stream:
                

            
                yield response.reserved
        finally:
            zoom_in_start_stream.cancel()

    async def respond_zoom_in_start(self, zoom_in_start_feedback):
        """
         Respond to zoom in start.

         Parameters
         ----------
         zoom_in_start_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondZoomInStartRequest()
        
        request.zoom_in_start_feedback = zoom_in_start_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondZoomInStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_zoom_in_start()", zoom_in_start_feedback)
        

    async def zoom_out_start(self):
        """
         Subscribe to zoom out start command

         Yields
         -------
         reserved : int32_t
              reserved, just make protoc-gen-mavsdk working

         
        """

        request = camera_server_pb2.SubscribeZoomOutStartRequest()
        zoom_out_start_stream = self._stub.SubscribeZoomOutStart(request)

        try:
            async for response in zoom_out_start_stream:
                

            
                yield response.reserved
        finally:
            zoom_out_start_stream.cancel()

    async def respond_zoom_out_start(self, zoom_out_start_feedback):
        """
         Respond to zoom out start.

         Parameters
         ----------
         zoom_out_start_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondZoomOutStartRequest()
        
        request.zoom_out_start_feedback = zoom_out_start_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondZoomOutStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_zoom_out_start()", zoom_out_start_feedback)
        

    async def zoom_stop(self):
        """
         Subscribe to zoom stop command

         Yields
         -------
         reserved : int32_t
              reserved, just make protoc-gen-mavsdk working

         
        """

        request = camera_server_pb2.SubscribeZoomStopRequest()
        zoom_stop_stream = self._stub.SubscribeZoomStop(request)

        try:
            async for response in zoom_stop_stream:
                

            
                yield response.reserved
        finally:
            zoom_stop_stream.cancel()

    async def respond_zoom_stop(self, zoom_stop_feedback):
        """
         Respond to zoom stop.

         Parameters
         ----------
         zoom_stop_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondZoomStopRequest()
        
        request.zoom_stop_feedback = zoom_stop_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondZoomStop(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_zoom_stop()", zoom_stop_feedback)
        

    async def zoom_range(self):
        """
         Subscribe to zoom range command

         Yields
         -------
         factor : float
              The zoom factor, starting at 1x.

         
        """

        request = camera_server_pb2.SubscribeZoomRangeRequest()
        zoom_range_stream = self._stub.SubscribeZoomRange(request)

        try:
            async for response in zoom_range_stream:
                

            
                yield response.factor
        finally:
            zoom_range_stream.cancel()

    async def respond_zoom_range(self, zoom_range_feedback):
        """
         Respond to zoom range.

         Parameters
         ----------
         zoom_range_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondZoomRangeRequest()
        
        request.zoom_range_feedback = zoom_range_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondZoomRange(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_zoom_range()", zoom_range_feedback)
        

    async def set_tracking_rectangle_status(self, tracked_rectangle):
        """
         Set/update the current rectangle tracking status.

         Parameters
         ----------
         tracked_rectangle : TrackRectangle
              The tracked rectangle

         
        """

        request = camera_server_pb2.SetTrackingRectangleStatusRequest()
        
        tracked_rectangle.translate_to_rpc(request.tracked_rectangle)
                
            
        response = await self._stub.SetTrackingRectangleStatus(request)

        

    async def set_tracking_off_status(self):
        """
         Set the current tracking status to off.

         
        """

        request = camera_server_pb2.SetTrackingOffStatusRequest()
        response = await self._stub.SetTrackingOffStatus(request)

        

    async def tracking_point_command(self):
        """
         Subscribe to incoming tracking point command.

         Yields
         -------
         track_point : TrackPoint
              The point to track if a point is to be tracked

         
        """

        request = camera_server_pb2.SubscribeTrackingPointCommandRequest()
        tracking_point_command_stream = self._stub.SubscribeTrackingPointCommand(request)

        try:
            async for response in tracking_point_command_stream:
                

            
                yield TrackPoint.translate_from_rpc(response.track_point)
        finally:
            tracking_point_command_stream.cancel()

    async def tracking_rectangle_command(self):
        """
         Subscribe to incoming tracking rectangle command.

         Yields
         -------
         track_rectangle : TrackRectangle
              The point to track if a point is to be tracked

         
        """

        request = camera_server_pb2.SubscribeTrackingRectangleCommandRequest()
        tracking_rectangle_command_stream = self._stub.SubscribeTrackingRectangleCommand(request)

        try:
            async for response in tracking_rectangle_command_stream:
                

            
                yield TrackRectangle.translate_from_rpc(response.track_rectangle)
        finally:
            tracking_rectangle_command_stream.cancel()

    async def tracking_off_command(self):
        """
         Subscribe to incoming tracking off command.

         Yields
         -------
         dummy : int32_t
              Unused

         
        """

        request = camera_server_pb2.SubscribeTrackingOffCommandRequest()
        tracking_off_command_stream = self._stub.SubscribeTrackingOffCommand(request)

        try:
            async for response in tracking_off_command_stream:
                

            
                yield response.dummy
        finally:
            tracking_off_command_stream.cancel()

    async def respond_tracking_point_command(self, stop_video_feedback):
        """
         Respond to an incoming tracking point command.

         Parameters
         ----------
         stop_video_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondTrackingPointCommandRequest()
        
        request.stop_video_feedback = stop_video_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingPointCommand(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_tracking_point_command()", stop_video_feedback)
        

    async def respond_tracking_rectangle_command(self, stop_video_feedback):
        """
         Respond to an incoming tracking rectangle command.

         Parameters
         ----------
         stop_video_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondTrackingRectangleCommandRequest()
        
        request.stop_video_feedback = stop_video_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingRectangleCommand(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_tracking_rectangle_command()", stop_video_feedback)
        

    async def respond_tracking_off_command(self, stop_video_feedback):
        """
         Respond to an incoming tracking off command.

         Parameters
         ----------
         stop_video_feedback : CameraFeedback
              the feedback

         Raises
         ------
         CameraServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_server_pb2.RespondTrackingOffCommandRequest()
        
        request.stop_video_feedback = stop_video_feedback.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingOffCommand(request)

        
        result = self._extract_result(response)

        if result.result != CameraServerResult.Result.SUCCESS:
            raise CameraServerError(result, "respond_tracking_off_command()", stop_video_feedback)
        