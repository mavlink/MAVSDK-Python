# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import camera_server_pb2, camera_server_pb2_grpc
from enum import Enum


class TakePhotoFeedback(Enum):
    """
     Possible results when taking a photo.

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
        if self == TakePhotoFeedback.UNKNOWN:
            return camera_server_pb2.TAKE_PHOTO_FEEDBACK_UNKNOWN
        if self == TakePhotoFeedback.OK:
            return camera_server_pb2.TAKE_PHOTO_FEEDBACK_OK
        if self == TakePhotoFeedback.BUSY:
            return camera_server_pb2.TAKE_PHOTO_FEEDBACK_BUSY
        if self == TakePhotoFeedback.FAILED:
            return camera_server_pb2.TAKE_PHOTO_FEEDBACK_FAILED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == camera_server_pb2.TAKE_PHOTO_FEEDBACK_UNKNOWN:
            return TakePhotoFeedback.UNKNOWN
        if rpc_enum_value == camera_server_pb2.TAKE_PHOTO_FEEDBACK_OK:
            return TakePhotoFeedback.OK
        if rpc_enum_value == camera_server_pb2.TAKE_PHOTO_FEEDBACK_BUSY:
            return TakePhotoFeedback.BUSY
        if rpc_enum_value == camera_server_pb2.TAKE_PHOTO_FEEDBACK_FAILED:
            return TakePhotoFeedback.FAILED

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
            definition_file_uri):
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
                (self.definition_file_uri == to_compare.definition_file_uri)

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
                "definition_file_uri: " + str(self.definition_file_uri)
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
                
                
                rpcInformation.definition_file_uri
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
     Provides handling of camera trigger commands.

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
         take_photo_feedback : TakePhotoFeedback
              The feedback

         capture_info : CaptureInfo
              The capture information

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
        