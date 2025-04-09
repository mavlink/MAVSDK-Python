# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import camera_pb2, camera_pb2_grpc
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


class PhotosRange(Enum):
    """
     Photos range type.

     Values
     ------
     ALL
          All the photos present on the camera

     SINCE_CONNECTION
          Photos taken since MAVSDK got connected

     """

    
    ALL = 0
    SINCE_CONNECTION = 1

    def translate_to_rpc(self):
        if self == PhotosRange.ALL:
            return camera_pb2.PHOTOS_RANGE_ALL
        if self == PhotosRange.SINCE_CONNECTION:
            return camera_pb2.PHOTOS_RANGE_SINCE_CONNECTION

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == camera_pb2.PHOTOS_RANGE_ALL:
            return PhotosRange.ALL
        if rpc_enum_value == camera_pb2.PHOTOS_RANGE_SINCE_CONNECTION:
            return PhotosRange.SINCE_CONNECTION

    def __str__(self):
        return self.name


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

    def __eq__(self, to_compare):
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

    def __eq__(self, to_compare):
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
     component_id : int32_t
          Component ID

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
            component_id,
            setting_id,
            setting_description,
            options,
            is_range):
        """ Initializes the SettingOptions object """
        self.component_id = component_id
        self.setting_id = setting_id
        self.setting_description = setting_description
        self.options = options
        self.is_range = is_range

    def __eq__(self, to_compare):
        """ Checks if two SettingOptions are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SettingOptions object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.setting_id == to_compare.setting_id) and \
                (self.setting_description == to_compare.setting_description) and \
                (self.options == to_compare.options) and \
                (self.is_range == to_compare.is_range)

        except AttributeError:
            return False

    def __str__(self):
        """ SettingOptions in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
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
                
                rpcSettingOptions.component_id,
                
                
                rpcSettingOptions.setting_id,
                
                
                rpcSettingOptions.setting_description,
                
                
                list(map(lambda elem: Option.translate_from_rpc(elem), rpcSettingOptions.options)),
                
                
                rpcSettingOptions.is_range
                )

    def translate_to_rpc(self, rpcSettingOptions):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcSettingOptions.component_id = self.component_id
            
        
        
        
            
        rpcSettingOptions.setting_id = self.setting_id
            
        
        
        
            
        rpcSettingOptions.setting_description = self.setting_description
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.options:
                
            rpc_elem = camera_pb2.Option()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcSettingOptions.options.extend(rpc_elems_list)
            
        
        
        
            
        rpcSettingOptions.is_range = self.is_range
            
        
        


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

     horizontal_fov_deg : float
          Horizontal fov in degrees

     """

    

    def __init__(
            self,
            frame_rate_hz,
            horizontal_resolution_pix,
            vertical_resolution_pix,
            bit_rate_b_s,
            rotation_deg,
            uri,
            horizontal_fov_deg):
        """ Initializes the VideoStreamSettings object """
        self.frame_rate_hz = frame_rate_hz
        self.horizontal_resolution_pix = horizontal_resolution_pix
        self.vertical_resolution_pix = vertical_resolution_pix
        self.bit_rate_b_s = bit_rate_b_s
        self.rotation_deg = rotation_deg
        self.uri = uri
        self.horizontal_fov_deg = horizontal_fov_deg

    def __eq__(self, to_compare):
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
                (self.uri == to_compare.uri) and \
                (self.horizontal_fov_deg == to_compare.horizontal_fov_deg)

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
                "uri: " + str(self.uri),
                "horizontal_fov_deg: " + str(self.horizontal_fov_deg)
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
                
                
                rpcVideoStreamSettings.uri,
                
                
                rpcVideoStreamSettings.horizontal_fov_deg
                )

    def translate_to_rpc(self, rpcVideoStreamSettings):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVideoStreamSettings.frame_rate_hz = self.frame_rate_hz
            
        
        
        
            
        rpcVideoStreamSettings.horizontal_resolution_pix = self.horizontal_resolution_pix
            
        
        
        
            
        rpcVideoStreamSettings.vertical_resolution_pix = self.vertical_resolution_pix
            
        
        
        
            
        rpcVideoStreamSettings.bit_rate_b_s = self.bit_rate_b_s
            
        
        
        
            
        rpcVideoStreamSettings.rotation_deg = self.rotation_deg
            
        
        
        
            
        rpcVideoStreamSettings.uri = self.uri
            
        
        
        
            
        rpcVideoStreamSettings.horizontal_fov_deg = self.horizontal_fov_deg
            
        
        


class VideoStreamInfo:
    """
     Information about the video stream.

     Parameters
     ----------
     stream_id : int32_t
          Stream ID

     settings : VideoStreamSettings
          Video stream settings

     status : VideoStreamStatus
          Current status of video streaming

     spectrum : VideoStreamSpectrum
          Light-spectrum of the video stream

     """

    
    
    class VideoStreamStatus(Enum):
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
            if self == VideoStreamInfo.VideoStreamStatus.NOT_RUNNING:
                return camera_pb2.VideoStreamInfo.VIDEO_STREAM_STATUS_NOT_RUNNING
            if self == VideoStreamInfo.VideoStreamStatus.IN_PROGRESS:
                return camera_pb2.VideoStreamInfo.VIDEO_STREAM_STATUS_IN_PROGRESS

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.VideoStreamInfo.VIDEO_STREAM_STATUS_NOT_RUNNING:
                return VideoStreamInfo.VideoStreamStatus.NOT_RUNNING
            if rpc_enum_value == camera_pb2.VideoStreamInfo.VIDEO_STREAM_STATUS_IN_PROGRESS:
                return VideoStreamInfo.VideoStreamStatus.IN_PROGRESS

        def __str__(self):
            return self.name
    
    
    class VideoStreamSpectrum(Enum):
        """
         Video stream light spectrum type

         Values
         ------
         UNKNOWN
              Unknown

         VISIBLE_LIGHT
              Visible light

         INFRARED
              Infrared

         """

        
        UNKNOWN = 0
        VISIBLE_LIGHT = 1
        INFRARED = 2

        def translate_to_rpc(self):
            if self == VideoStreamInfo.VideoStreamSpectrum.UNKNOWN:
                return camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_UNKNOWN
            if self == VideoStreamInfo.VideoStreamSpectrum.VISIBLE_LIGHT:
                return camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_VISIBLE_LIGHT
            if self == VideoStreamInfo.VideoStreamSpectrum.INFRARED:
                return camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_INFRARED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_UNKNOWN:
                return VideoStreamInfo.VideoStreamSpectrum.UNKNOWN
            if rpc_enum_value == camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_VISIBLE_LIGHT:
                return VideoStreamInfo.VideoStreamSpectrum.VISIBLE_LIGHT
            if rpc_enum_value == camera_pb2.VideoStreamInfo.VIDEO_STREAM_SPECTRUM_INFRARED:
                return VideoStreamInfo.VideoStreamSpectrum.INFRARED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            stream_id,
            settings,
            status,
            spectrum):
        """ Initializes the VideoStreamInfo object """
        self.stream_id = stream_id
        self.settings = settings
        self.status = status
        self.spectrum = spectrum

    def __eq__(self, to_compare):
        """ Checks if two VideoStreamInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VideoStreamInfo object
            return \
                (self.stream_id == to_compare.stream_id) and \
                (self.settings == to_compare.settings) and \
                (self.status == to_compare.status) and \
                (self.spectrum == to_compare.spectrum)

        except AttributeError:
            return False

    def __str__(self):
        """ VideoStreamInfo in string representation """
        struct_repr = ", ".join([
                "stream_id: " + str(self.stream_id),
                "settings: " + str(self.settings),
                "status: " + str(self.status),
                "spectrum: " + str(self.spectrum)
                ])

        return f"VideoStreamInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVideoStreamInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return VideoStreamInfo(
                
                rpcVideoStreamInfo.stream_id,
                
                
                VideoStreamSettings.translate_from_rpc(rpcVideoStreamInfo.settings),
                
                
                VideoStreamInfo.VideoStreamStatus.translate_from_rpc(rpcVideoStreamInfo.status),
                
                
                VideoStreamInfo.VideoStreamSpectrum.translate_from_rpc(rpcVideoStreamInfo.spectrum)
                )

    def translate_to_rpc(self, rpcVideoStreamInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVideoStreamInfo.stream_id = self.stream_id
            
        
        
        
            
        self.settings.translate_to_rpc(rpcVideoStreamInfo.settings)
            
        
        
        
            
        rpcVideoStreamInfo.status = self.status.translate_to_rpc()
            
        
        
        
            
        rpcVideoStreamInfo.spectrum = self.spectrum.translate_to_rpc()
            
        
        


class ModeUpdate:
    """
     An update about the current mode

     Parameters
     ----------
     component_id : int32_t
          Component ID

     mode : Mode
          Camera mode

     """

    

    def __init__(
            self,
            component_id,
            mode):
        """ Initializes the ModeUpdate object """
        self.component_id = component_id
        self.mode = mode

    def __eq__(self, to_compare):
        """ Checks if two ModeUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ModeUpdate object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.mode == to_compare.mode)

        except AttributeError:
            return False

    def __str__(self):
        """ ModeUpdate in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "mode: " + str(self.mode)
                ])

        return f"ModeUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcModeUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return ModeUpdate(
                
                rpcModeUpdate.component_id,
                
                
                Mode.translate_from_rpc(rpcModeUpdate.mode)
                )

    def translate_to_rpc(self, rpcModeUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcModeUpdate.component_id = self.component_id
            
        
        
        
            
        rpcModeUpdate.mode = self.mode.translate_to_rpc()
            
        
        


class VideoStreamUpdate:
    """
     An update about a video stream

     Parameters
     ----------
     component_id : int32_t
          Component ID

     video_stream_info : VideoStreamInfo
          Video stream info

     """

    

    def __init__(
            self,
            component_id,
            video_stream_info):
        """ Initializes the VideoStreamUpdate object """
        self.component_id = component_id
        self.video_stream_info = video_stream_info

    def __eq__(self, to_compare):
        """ Checks if two VideoStreamUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # VideoStreamUpdate object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.video_stream_info == to_compare.video_stream_info)

        except AttributeError:
            return False

    def __str__(self):
        """ VideoStreamUpdate in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "video_stream_info: " + str(self.video_stream_info)
                ])

        return f"VideoStreamUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVideoStreamUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return VideoStreamUpdate(
                
                rpcVideoStreamUpdate.component_id,
                
                
                VideoStreamInfo.translate_from_rpc(rpcVideoStreamUpdate.video_stream_info)
                )

    def translate_to_rpc(self, rpcVideoStreamUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVideoStreamUpdate.component_id = self.component_id
            
        
        
        
            
        self.video_stream_info.translate_to_rpc(rpcVideoStreamUpdate.video_stream_info)
            
        
        


class Storage:
    """
     Information about the camera's storage status.

     Parameters
     ----------
     component_id : int32_t
          Component ID

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

     storage_id : uint32_t
          Storage ID starting at 1

     storage_type : StorageType
          Storage type

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

         NOT_SUPPORTED
              Storage status is not supported

         """

        
        NOT_AVAILABLE = 0
        UNFORMATTED = 1
        FORMATTED = 2
        NOT_SUPPORTED = 3

        def translate_to_rpc(self):
            if self == Storage.StorageStatus.NOT_AVAILABLE:
                return camera_pb2.Storage.STORAGE_STATUS_NOT_AVAILABLE
            if self == Storage.StorageStatus.UNFORMATTED:
                return camera_pb2.Storage.STORAGE_STATUS_UNFORMATTED
            if self == Storage.StorageStatus.FORMATTED:
                return camera_pb2.Storage.STORAGE_STATUS_FORMATTED
            if self == Storage.StorageStatus.NOT_SUPPORTED:
                return camera_pb2.Storage.STORAGE_STATUS_NOT_SUPPORTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.Storage.STORAGE_STATUS_NOT_AVAILABLE:
                return Storage.StorageStatus.NOT_AVAILABLE
            if rpc_enum_value == camera_pb2.Storage.STORAGE_STATUS_UNFORMATTED:
                return Storage.StorageStatus.UNFORMATTED
            if rpc_enum_value == camera_pb2.Storage.STORAGE_STATUS_FORMATTED:
                return Storage.StorageStatus.FORMATTED
            if rpc_enum_value == camera_pb2.Storage.STORAGE_STATUS_NOT_SUPPORTED:
                return Storage.StorageStatus.NOT_SUPPORTED

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
            if self == Storage.StorageType.UNKNOWN:
                return camera_pb2.Storage.STORAGE_TYPE_UNKNOWN
            if self == Storage.StorageType.USB_STICK:
                return camera_pb2.Storage.STORAGE_TYPE_USB_STICK
            if self == Storage.StorageType.SD:
                return camera_pb2.Storage.STORAGE_TYPE_SD
            if self == Storage.StorageType.MICROSD:
                return camera_pb2.Storage.STORAGE_TYPE_MICROSD
            if self == Storage.StorageType.HD:
                return camera_pb2.Storage.STORAGE_TYPE_HD
            if self == Storage.StorageType.OTHER:
                return camera_pb2.Storage.STORAGE_TYPE_OTHER

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_UNKNOWN:
                return Storage.StorageType.UNKNOWN
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_USB_STICK:
                return Storage.StorageType.USB_STICK
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_SD:
                return Storage.StorageType.SD
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_MICROSD:
                return Storage.StorageType.MICROSD
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_HD:
                return Storage.StorageType.HD
            if rpc_enum_value == camera_pb2.Storage.STORAGE_TYPE_OTHER:
                return Storage.StorageType.OTHER

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            component_id,
            video_on,
            photo_interval_on,
            used_storage_mib,
            available_storage_mib,
            total_storage_mib,
            recording_time_s,
            media_folder_name,
            storage_status,
            storage_id,
            storage_type):
        """ Initializes the Storage object """
        self.component_id = component_id
        self.video_on = video_on
        self.photo_interval_on = photo_interval_on
        self.used_storage_mib = used_storage_mib
        self.available_storage_mib = available_storage_mib
        self.total_storage_mib = total_storage_mib
        self.recording_time_s = recording_time_s
        self.media_folder_name = media_folder_name
        self.storage_status = storage_status
        self.storage_id = storage_id
        self.storage_type = storage_type

    def __eq__(self, to_compare):
        """ Checks if two Storage are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Storage object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.video_on == to_compare.video_on) and \
                (self.photo_interval_on == to_compare.photo_interval_on) and \
                (self.used_storage_mib == to_compare.used_storage_mib) and \
                (self.available_storage_mib == to_compare.available_storage_mib) and \
                (self.total_storage_mib == to_compare.total_storage_mib) and \
                (self.recording_time_s == to_compare.recording_time_s) and \
                (self.media_folder_name == to_compare.media_folder_name) and \
                (self.storage_status == to_compare.storage_status) and \
                (self.storage_id == to_compare.storage_id) and \
                (self.storage_type == to_compare.storage_type)

        except AttributeError:
            return False

    def __str__(self):
        """ Storage in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "video_on: " + str(self.video_on),
                "photo_interval_on: " + str(self.photo_interval_on),
                "used_storage_mib: " + str(self.used_storage_mib),
                "available_storage_mib: " + str(self.available_storage_mib),
                "total_storage_mib: " + str(self.total_storage_mib),
                "recording_time_s: " + str(self.recording_time_s),
                "media_folder_name: " + str(self.media_folder_name),
                "storage_status: " + str(self.storage_status),
                "storage_id: " + str(self.storage_id),
                "storage_type: " + str(self.storage_type)
                ])

        return f"Storage: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStorage):
        """ Translates a gRPC struct to the SDK equivalent """
        return Storage(
                
                rpcStorage.component_id,
                
                
                rpcStorage.video_on,
                
                
                rpcStorage.photo_interval_on,
                
                
                rpcStorage.used_storage_mib,
                
                
                rpcStorage.available_storage_mib,
                
                
                rpcStorage.total_storage_mib,
                
                
                rpcStorage.recording_time_s,
                
                
                rpcStorage.media_folder_name,
                
                
                Storage.StorageStatus.translate_from_rpc(rpcStorage.storage_status),
                
                
                rpcStorage.storage_id,
                
                
                Storage.StorageType.translate_from_rpc(rpcStorage.storage_type)
                )

    def translate_to_rpc(self, rpcStorage):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStorage.component_id = self.component_id
            
        
        
        
            
        rpcStorage.video_on = self.video_on
            
        
        
        
            
        rpcStorage.photo_interval_on = self.photo_interval_on
            
        
        
        
            
        rpcStorage.used_storage_mib = self.used_storage_mib
            
        
        
        
            
        rpcStorage.available_storage_mib = self.available_storage_mib
            
        
        
        
            
        rpcStorage.total_storage_mib = self.total_storage_mib
            
        
        
        
            
        rpcStorage.recording_time_s = self.recording_time_s
            
        
        
        
            
        rpcStorage.media_folder_name = self.media_folder_name
            
        
        
        
            
        rpcStorage.storage_status = self.storage_status.translate_to_rpc()
            
        
        
        
            
        rpcStorage.storage_id = self.storage_id
            
        
        
        
            
        rpcStorage.storage_type = self.storage_type.translate_to_rpc()
            
        
        


class StorageUpdate:
    """
     An update about storage

     Parameters
     ----------
     component_id : int32_t
          Component ID

     storage : Storage
          Storage

     """

    

    def __init__(
            self,
            component_id,
            storage):
        """ Initializes the StorageUpdate object """
        self.component_id = component_id
        self.storage = storage

    def __eq__(self, to_compare):
        """ Checks if two StorageUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # StorageUpdate object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.storage == to_compare.storage)

        except AttributeError:
            return False

    def __str__(self):
        """ StorageUpdate in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "storage: " + str(self.storage)
                ])

        return f"StorageUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStorageUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return StorageUpdate(
                
                rpcStorageUpdate.component_id,
                
                
                Storage.translate_from_rpc(rpcStorageUpdate.storage)
                )

    def translate_to_rpc(self, rpcStorageUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStorageUpdate.component_id = self.component_id
            
        
        
        
            
        self.storage.translate_to_rpc(rpcStorageUpdate.storage)
            
        
        


class CurrentSettingsUpdate:
    """
     An update about a current setting

     Parameters
     ----------
     component_id : int32_t
          Component ID

     current_settings : [Setting]
          List of current settings

     """

    

    def __init__(
            self,
            component_id,
            current_settings):
        """ Initializes the CurrentSettingsUpdate object """
        self.component_id = component_id
        self.current_settings = current_settings

    def __eq__(self, to_compare):
        """ Checks if two CurrentSettingsUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CurrentSettingsUpdate object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.current_settings == to_compare.current_settings)

        except AttributeError:
            return False

    def __str__(self):
        """ CurrentSettingsUpdate in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "current_settings: " + str(self.current_settings)
                ])

        return f"CurrentSettingsUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCurrentSettingsUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return CurrentSettingsUpdate(
                
                rpcCurrentSettingsUpdate.component_id,
                
                
                list(map(lambda elem: Setting.translate_from_rpc(elem), rpcCurrentSettingsUpdate.current_settings))
                )

    def translate_to_rpc(self, rpcCurrentSettingsUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCurrentSettingsUpdate.component_id = self.component_id
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.current_settings:
                
            rpc_elem = camera_pb2.Setting()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcCurrentSettingsUpdate.current_settings.extend(rpc_elems_list)
            
        
        


class PossibleSettingOptionsUpdate:
    """
     An update about possible setting options

     Parameters
     ----------
     component_id : int32_t
          Component ID

     setting_options : [SettingOptions]
          List of settings that can be changed

     """

    

    def __init__(
            self,
            component_id,
            setting_options):
        """ Initializes the PossibleSettingOptionsUpdate object """
        self.component_id = component_id
        self.setting_options = setting_options

    def __eq__(self, to_compare):
        """ Checks if two PossibleSettingOptionsUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PossibleSettingOptionsUpdate object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.setting_options == to_compare.setting_options)

        except AttributeError:
            return False

    def __str__(self):
        """ PossibleSettingOptionsUpdate in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "setting_options: " + str(self.setting_options)
                ])

        return f"PossibleSettingOptionsUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPossibleSettingOptionsUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return PossibleSettingOptionsUpdate(
                
                rpcPossibleSettingOptionsUpdate.component_id,
                
                
                list(map(lambda elem: SettingOptions.translate_from_rpc(elem), rpcPossibleSettingOptionsUpdate.setting_options))
                )

    def translate_to_rpc(self, rpcPossibleSettingOptionsUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPossibleSettingOptionsUpdate.component_id = self.component_id
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.setting_options:
                
            rpc_elem = camera_pb2.SettingOptions()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcPossibleSettingOptionsUpdate.setting_options.extend(rpc_elems_list)
            
        
        


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
              An error has occurred while executing the command

         TIMEOUT
              Command timed out

         WRONG_ARGUMENT
              Command has wrong argument(s)

         NO_SYSTEM
              No system connected

         PROTOCOL_UNSUPPORTED
              Definition file protocol not supported

         UNAVAILABLE
              Not available (yet)

         CAMERA_ID_INVALID
              Camera with camera ID not found

         ACTION_UNSUPPORTED
              Camera action not supported

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
        PROTOCOL_UNSUPPORTED = 9
        UNAVAILABLE = 10
        CAMERA_ID_INVALID = 11
        ACTION_UNSUPPORTED = 12

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
            if self == CameraResult.Result.NO_SYSTEM:
                return camera_pb2.CameraResult.RESULT_NO_SYSTEM
            if self == CameraResult.Result.PROTOCOL_UNSUPPORTED:
                return camera_pb2.CameraResult.RESULT_PROTOCOL_UNSUPPORTED
            if self == CameraResult.Result.UNAVAILABLE:
                return camera_pb2.CameraResult.RESULT_UNAVAILABLE
            if self == CameraResult.Result.CAMERA_ID_INVALID:
                return camera_pb2.CameraResult.RESULT_CAMERA_ID_INVALID
            if self == CameraResult.Result.ACTION_UNSUPPORTED:
                return camera_pb2.CameraResult.RESULT_ACTION_UNSUPPORTED

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
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_NO_SYSTEM:
                return CameraResult.Result.NO_SYSTEM
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_PROTOCOL_UNSUPPORTED:
                return CameraResult.Result.PROTOCOL_UNSUPPORTED
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_UNAVAILABLE:
                return CameraResult.Result.UNAVAILABLE
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_CAMERA_ID_INVALID:
                return CameraResult.Result.CAMERA_ID_INVALID
            if rpc_enum_value == camera_pb2.CameraResult.RESULT_ACTION_UNSUPPORTED:
                return CameraResult.Result.ACTION_UNSUPPORTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the CameraResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
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

    def __eq__(self, to_compare):
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
     component_id : int32_t
          Component ID

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
            component_id,
            position,
            attitude_quaternion,
            attitude_euler_angle,
            time_utc_us,
            is_success,
            index,
            file_url):
        """ Initializes the CaptureInfo object """
        self.component_id = component_id
        self.position = position
        self.attitude_quaternion = attitude_quaternion
        self.attitude_euler_angle = attitude_euler_angle
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
                (self.component_id == to_compare.component_id) and \
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
                "component_id: " + str(self.component_id),
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
                
                rpcCaptureInfo.component_id,
                
                
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

        
        
            
        rpcCaptureInfo.component_id = self.component_id
            
        
        
        
            
        self.position.translate_to_rpc(rpcCaptureInfo.position)
            
        
        
        
            
        self.attitude_quaternion.translate_to_rpc(rpcCaptureInfo.attitude_quaternion)
            
        
        
        
            
        self.attitude_euler_angle.translate_to_rpc(rpcCaptureInfo.attitude_euler_angle)
            
        
        
        
            
        rpcCaptureInfo.time_utc_us = self.time_utc_us
            
        
        
        
            
        rpcCaptureInfo.is_success = self.is_success
            
        
        
        
            
        rpcCaptureInfo.index = self.index
            
        
        
        
            
        rpcCaptureInfo.file_url = self.file_url
            
        
        


class Information:
    """
     Type to represent a camera information.

     Parameters
     ----------
     component_id : int32_t
          Component ID

     vendor_name : std::string
          Name of the camera vendor

     model_name : std::string
          Name of the camera model

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

     """

    

    def __init__(
            self,
            component_id,
            vendor_name,
            model_name,
            focal_length_mm,
            horizontal_sensor_size_mm,
            vertical_sensor_size_mm,
            horizontal_resolution_px,
            vertical_resolution_px):
        """ Initializes the Information object """
        self.component_id = component_id
        self.vendor_name = vendor_name
        self.model_name = model_name
        self.focal_length_mm = focal_length_mm
        self.horizontal_sensor_size_mm = horizontal_sensor_size_mm
        self.vertical_sensor_size_mm = vertical_sensor_size_mm
        self.horizontal_resolution_px = horizontal_resolution_px
        self.vertical_resolution_px = vertical_resolution_px

    def __eq__(self, to_compare):
        """ Checks if two Information are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Information object
            return \
                (self.component_id == to_compare.component_id) and \
                (self.vendor_name == to_compare.vendor_name) and \
                (self.model_name == to_compare.model_name) and \
                (self.focal_length_mm == to_compare.focal_length_mm) and \
                (self.horizontal_sensor_size_mm == to_compare.horizontal_sensor_size_mm) and \
                (self.vertical_sensor_size_mm == to_compare.vertical_sensor_size_mm) and \
                (self.horizontal_resolution_px == to_compare.horizontal_resolution_px) and \
                (self.vertical_resolution_px == to_compare.vertical_resolution_px)

        except AttributeError:
            return False

    def __str__(self):
        """ Information in string representation """
        struct_repr = ", ".join([
                "component_id: " + str(self.component_id),
                "vendor_name: " + str(self.vendor_name),
                "model_name: " + str(self.model_name),
                "focal_length_mm: " + str(self.focal_length_mm),
                "horizontal_sensor_size_mm: " + str(self.horizontal_sensor_size_mm),
                "vertical_sensor_size_mm: " + str(self.vertical_sensor_size_mm),
                "horizontal_resolution_px: " + str(self.horizontal_resolution_px),
                "vertical_resolution_px: " + str(self.vertical_resolution_px)
                ])

        return f"Information: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcInformation):
        """ Translates a gRPC struct to the SDK equivalent """
        return Information(
                
                rpcInformation.component_id,
                
                
                rpcInformation.vendor_name,
                
                
                rpcInformation.model_name,
                
                
                rpcInformation.focal_length_mm,
                
                
                rpcInformation.horizontal_sensor_size_mm,
                
                
                rpcInformation.vertical_sensor_size_mm,
                
                
                rpcInformation.horizontal_resolution_px,
                
                
                rpcInformation.vertical_resolution_px
                )

    def translate_to_rpc(self, rpcInformation):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcInformation.component_id = self.component_id
            
        
        
        
            
        rpcInformation.vendor_name = self.vendor_name
            
        
        
        
            
        rpcInformation.model_name = self.model_name
            
        
        
        
            
        rpcInformation.focal_length_mm = self.focal_length_mm
            
        
        
        
            
        rpcInformation.horizontal_sensor_size_mm = self.horizontal_sensor_size_mm
            
        
        
        
            
        rpcInformation.vertical_sensor_size_mm = self.vertical_sensor_size_mm
            
        
        
        
            
        rpcInformation.horizontal_resolution_px = self.horizontal_resolution_px
            
        
        
        
            
        rpcInformation.vertical_resolution_px = self.vertical_resolution_px
            
        
        


class CameraList:
    """
     Camera list

     Parameters
     ----------
     cameras : [Information]
          Camera items.

     """

    

    def __init__(
            self,
            cameras):
        """ Initializes the CameraList object """
        self.cameras = cameras

    def __eq__(self, to_compare):
        """ Checks if two CameraList are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CameraList object
            return \
                (self.cameras == to_compare.cameras)

        except AttributeError:
            return False

    def __str__(self):
        """ CameraList in string representation """
        struct_repr = ", ".join([
                "cameras: " + str(self.cameras)
                ])

        return f"CameraList: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCameraList):
        """ Translates a gRPC struct to the SDK equivalent """
        return CameraList(
                
                list(map(lambda elem: Information.translate_from_rpc(elem), rpcCameraList.cameras))
                )

    def translate_to_rpc(self, rpcCameraList):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.cameras:
                
            rpc_elem = camera_pb2.Information()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcCameraList.cameras.extend(rpc_elems_list)
            
        
        



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
    

    async def take_photo(self, component_id):
        """
         Take one photo.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.TakePhotoRequest()
        request.component_id = component_id
        response = await self._stub.TakePhoto(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "take_photo()", component_id)
        

    async def start_photo_interval(self, component_id, interval_s):
        """
         Start photo timelapse with a given interval.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         interval_s : float
              Interval between photos (in seconds)

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartPhotoIntervalRequest()
        request.component_id = component_id
        request.interval_s = interval_s
        response = await self._stub.StartPhotoInterval(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_photo_interval()", component_id, interval_s)
        

    async def stop_photo_interval(self, component_id):
        """
         Stop a running photo timelapse.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopPhotoIntervalRequest()
        request.component_id = component_id
        response = await self._stub.StopPhotoInterval(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_photo_interval()", component_id)
        

    async def start_video(self, component_id):
        """
         Start a video recording.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartVideoRequest()
        request.component_id = component_id
        response = await self._stub.StartVideo(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_video()", component_id)
        

    async def stop_video(self, component_id):
        """
         Stop a running video recording.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopVideoRequest()
        request.component_id = component_id
        response = await self._stub.StopVideo(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_video()", component_id)
        

    async def start_video_streaming(self, component_id, stream_id):
        """
         Start video streaming.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         stream_id : int32_t
              video stream id

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StartVideoStreamingRequest()
        request.component_id = component_id
        request.stream_id = stream_id
        response = await self._stub.StartVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "start_video_streaming()", component_id, stream_id)
        

    async def stop_video_streaming(self, component_id, stream_id):
        """
         Stop current video streaming.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         stream_id : int32_t
              video stream id

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.StopVideoStreamingRequest()
        request.component_id = component_id
        request.stream_id = stream_id
        response = await self._stub.StopVideoStreaming(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "stop_video_streaming()", component_id, stream_id)
        

    async def set_mode(self, component_id, mode):
        """
         Set camera mode.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         mode : Mode
              Camera mode to set

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.SetModeRequest()
        request.component_id = component_id
        
        request.mode = mode.translate_to_rpc()
                
            
        response = await self._stub.SetMode(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "set_mode()", component_id, mode)
        

    async def list_photos(self, component_id, photos_range):
        """
         List photos available on the camera.

         Note that this might need to be called initially to set the PhotosRange accordingly.
         Once set to 'all' rather than 'since connection', it will try to request the previous
         images over time.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         photos_range : PhotosRange
              Which photos should be listed (all or since connection)

         Returns
         -------
         capture_infos : [CaptureInfo]
              List of capture infos (representing the photos)

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ListPhotosRequest()
        
            
        request.component_id = component_id
            
        
            
                
        request.photos_range = photos_range.translate_to_rpc()
                
            
        response = await self._stub.ListPhotos(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "list_photos()", component_id, photos_range)
        

        capture_infos = []
        for capture_infos_rpc in response.capture_infos:
            capture_infos.append(CaptureInfo.translate_from_rpc(capture_infos_rpc))

        return capture_infos
            

    async def camera_list(self):
        """
         Subscribe to list of cameras.

         This allows to find out what cameras are connected to the system.
         Based on the camera ID, we can then address a specific camera.

         Yields
         -------
         camera_list : CameraList
              Camera list

         
        """

        request = camera_pb2.SubscribeCameraListRequest()
        camera_list_stream = self._stub.SubscribeCameraList(request)

        try:
            async for response in camera_list_stream:
                

            
                yield CameraList.translate_from_rpc(response.camera_list)
        finally:
            camera_list_stream.cancel()

    async def mode(self):
        """
         Subscribe to camera mode updates.

         Yields
         -------
         update : ModeUpdate
              Mode update for camera

         
        """

        request = camera_pb2.SubscribeModeRequest()
        mode_stream = self._stub.SubscribeMode(request)

        try:
            async for response in mode_stream:
                

            
                yield ModeUpdate.translate_from_rpc(response.update)
        finally:
            mode_stream.cancel()

    async def get_mode(self, component_id):
        """
         Get camera mode.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Returns
         -------
         mode : Mode
              Mode

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetModeRequest()
        
            
        request.component_id = component_id
            
        response = await self._stub.GetMode(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_mode()", component_id)
        

        return Mode.translate_from_rpc(response.mode)
            

    async def video_stream_info(self):
        """
         Subscribe to video stream info updates.

         Yields
         -------
         update : VideoStreamUpdate
              Video stream update for camera

         
        """

        request = camera_pb2.SubscribeVideoStreamInfoRequest()
        video_stream_info_stream = self._stub.SubscribeVideoStreamInfo(request)

        try:
            async for response in video_stream_info_stream:
                

            
                yield VideoStreamUpdate.translate_from_rpc(response.update)
        finally:
            video_stream_info_stream.cancel()

    async def get_video_stream_info(self, component_id):
        """
         Get video stream info.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Returns
         -------
         video_stream_info : VideoStreamInfo
              Video stream info

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetVideoStreamInfoRequest()
        
            
        request.component_id = component_id
            
        response = await self._stub.GetVideoStreamInfo(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_video_stream_info()", component_id)
        

        return VideoStreamInfo.translate_from_rpc(response.video_stream_info)
            

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

    async def storage(self):
        """
         Subscribe to camera's storage status updates.

         Yields
         -------
         update : StorageUpdate
              Camera's storage status

         
        """

        request = camera_pb2.SubscribeStorageRequest()
        storage_stream = self._stub.SubscribeStorage(request)

        try:
            async for response in storage_stream:
                

            
                yield StorageUpdate.translate_from_rpc(response.update)
        finally:
            storage_stream.cancel()

    async def get_storage(self, component_id):
        """
         Get camera's storage status.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Returns
         -------
         storage : Storage
              Camera's storage status

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetStorageRequest()
        
            
        request.component_id = component_id
            
        response = await self._stub.GetStorage(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_storage()", component_id)
        

        return Storage.translate_from_rpc(response.storage)
            

    async def current_settings(self):
        """
         Get the list of current camera settings.

         Yields
         -------
         update : CurrentSettingsUpdate
              Current setting update per camera

         
        """

        request = camera_pb2.SubscribeCurrentSettingsRequest()
        current_settings_stream = self._stub.SubscribeCurrentSettings(request)

        try:
            async for response in current_settings_stream:
                

            
                yield CurrentSettingsUpdate.translate_from_rpc(response.update)
        finally:
            current_settings_stream.cancel()

    async def get_current_settings(self, component_id):
        """
         Get current settings.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Returns
         -------
         current_settings : [Setting]
              List of current settings

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetCurrentSettingsRequest()
        
            
        request.component_id = component_id
            
        response = await self._stub.GetCurrentSettings(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_current_settings()", component_id)
        

        current_settings = []
        for current_settings_rpc in response.current_settings:
            current_settings.append(Setting.translate_from_rpc(current_settings_rpc))

        return current_settings
            

    async def possible_setting_options(self):
        """
         Get the list of settings that can be changed.

         Yields
         -------
         update : PossibleSettingOptionsUpdate
              Possible setting update per camera

         
        """

        request = camera_pb2.SubscribePossibleSettingOptionsRequest()
        possible_setting_options_stream = self._stub.SubscribePossibleSettingOptions(request)

        try:
            async for response in possible_setting_options_stream:
                

            
                yield PossibleSettingOptionsUpdate.translate_from_rpc(response.update)
        finally:
            possible_setting_options_stream.cancel()

    async def get_possible_setting_options(self, component_id):
        """
         Get possible setting options.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Returns
         -------
         setting_options : [SettingOptions]
              List of settings that can be changed

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.GetPossibleSettingOptionsRequest()
        
            
        request.component_id = component_id
            
        response = await self._stub.GetPossibleSettingOptions(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_possible_setting_options()", component_id)
        

        setting_options = []
        for setting_options_rpc in response.setting_options:
            setting_options.append(SettingOptions.translate_from_rpc(setting_options_rpc))

        return setting_options
            

    async def set_setting(self, component_id, setting):
        """
         Set a setting to some value.

         Only setting_id of setting and option_id of option needs to be set.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         setting : Setting
              Desired setting

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.SetSettingRequest()
        request.component_id = component_id
        
        setting.translate_to_rpc(request.setting)
                
            
        response = await self._stub.SetSetting(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "set_setting()", component_id, setting)
        

    async def get_setting(self, component_id, setting):
        """
         Get a setting.

         Only setting_id of setting needs to be set.

         Parameters
         ----------
         component_id : int32_t
              Component ID (0/all not available)

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
        
            
        request.component_id = component_id
            
        
            
                
        setting.translate_to_rpc(request.setting)
                
            
        response = await self._stub.GetSetting(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "get_setting()", component_id, setting)
        

        return Setting.translate_from_rpc(response.setting)
            

    async def format_storage(self, component_id, storage_id):
        """
         Format storage (e.g. SD card) in camera.

         This will delete all content of the camera storage!

         Parameters
         ----------
         component_id : int32_t
              Component ID

         storage_id : int32_t
             Storage identify to be format

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FormatStorageRequest()
        request.component_id = component_id
        request.storage_id = storage_id
        response = await self._stub.FormatStorage(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "format_storage()", component_id, storage_id)
        

    async def reset_settings(self, component_id):
        """
         Reset all settings in camera.

         This will reset all camera settings to default value

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ResetSettingsRequest()
        request.component_id = component_id
        response = await self._stub.ResetSettings(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "reset_settings()", component_id)
        

    async def zoom_in_start(self, component_id):
        """
         Start zooming in.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ZoomInStartRequest()
        request.component_id = component_id
        response = await self._stub.ZoomInStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "zoom_in_start()", component_id)
        

    async def zoom_out_start(self, component_id):
        """
         Start zooming out.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ZoomOutStartRequest()
        request.component_id = component_id
        response = await self._stub.ZoomOutStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "zoom_out_start()", component_id)
        

    async def zoom_stop(self, component_id):
        """
         Stop zooming.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ZoomStopRequest()
        request.component_id = component_id
        response = await self._stub.ZoomStop(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "zoom_stop()", component_id)
        

    async def zoom_range(self, component_id, range):
        """
         Zoom to value as proportion of full camera range (percentage between 0.0 and 100.0).

         Parameters
         ----------
         component_id : int32_t
              Component ID

         range : float
              Range must be between 0.0 and 100.0

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.ZoomRangeRequest()
        request.component_id = component_id
        request.range = range
        response = await self._stub.ZoomRange(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "zoom_range()", component_id, range)
        

    async def track_point(self, component_id, point_x, point_y, radius):
        """
         Track point.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         point_x : float
              Point in X axis (0..1, 0 is left, 1 is right)

         point_y : float
              Point in Y axis (0..1, 0 is top, 1 is bottom)

         radius : float
              Radius (0 is one pixel, 1 is full image width)

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.TrackPointRequest()
        request.component_id = component_id
        request.point_x = point_x
        request.point_y = point_y
        request.radius = radius
        response = await self._stub.TrackPoint(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "track_point()", component_id, point_x, point_y, radius)
        

    async def track_rectangle(self, component_id, top_left_x, top_left_y, bottom_right_x, bottom_right_y):
        """
         Track rectangle.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         top_left_x : float
              Top left corner of rectangle x value (normalized 0..1, 0 is left, 1 is right)

         top_left_y : float
              Top left corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom)

         bottom_right_x : float
              Bottom right corner of rectangle x value (normalized 0..1, 0 is left, 1 is right)

         bottom_right_y : float
              Bottom right corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom)

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.TrackRectangleRequest()
        request.component_id = component_id
        request.top_left_x = top_left_x
        request.top_left_y = top_left_y
        request.bottom_right_x = bottom_right_x
        request.bottom_right_y = bottom_right_y
        response = await self._stub.TrackRectangle(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "track_rectangle()", component_id, top_left_x, top_left_y, bottom_right_x, bottom_right_y)
        

    async def track_stop(self, component_id):
        """
         Stop tracking.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.TrackStopRequest()
        request.component_id = component_id
        response = await self._stub.TrackStop(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "track_stop()", component_id)
        

    async def focus_in_start(self, component_id):
        """
         Start focusing in.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FocusInStartRequest()
        request.component_id = component_id
        response = await self._stub.FocusInStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "focus_in_start()", component_id)
        

    async def focus_out_start(self, component_id):
        """
         Start focusing out.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FocusOutStartRequest()
        request.component_id = component_id
        response = await self._stub.FocusOutStart(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "focus_out_start()", component_id)
        

    async def focus_stop(self, component_id):
        """
         Stop focus.

         Parameters
         ----------
         component_id : int32_t
              Component ID

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FocusStopRequest()
        request.component_id = component_id
        response = await self._stub.FocusStop(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "focus_stop()", component_id)
        

    async def focus_range(self, component_id, range):
        """
         Focus with range value of full range (value between 0.0 and 100.0).

         Parameters
         ----------
         component_id : int32_t
              Component ID

         range : float
              Range must be between 0.0 - 100.0

         Raises
         ------
         CameraError
             If the request fails. The error contains the reason for the failure.
        """

        request = camera_pb2.FocusRangeRequest()
        request.component_id = component_id
        request.range = range
        response = await self._stub.FocusRange(request)

        
        result = self._extract_result(response)

        if result.result != CameraResult.Result.SUCCESS:
            raise CameraError(result, "focus_range()", component_id, range)
        