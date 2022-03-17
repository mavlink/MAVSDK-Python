# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import mission_pb2, mission_pb2_grpc
from enum import Enum


class MissionItem:
    """
     Type representing a mission item.

     A MissionItem can contain a position and/or actions.
     Mission items are building blocks to assemble a mission,
     which can be sent to (or received from) a system.
     They cannot be used independently.

     Parameters
     ----------
     latitude_deg : double
          Latitude in degrees (range: -90 to +90)

     longitude_deg : double
          Longitude in degrees (range: -180 to +180)

     relative_altitude_m : float
          Altitude relative to takeoff altitude in metres

     speed_m_s : float
          Speed to use after this mission item (in metres/second)

     is_fly_through : bool
          True will make the drone fly through without stopping, while false will make the drone stop on the waypoint

     gimbal_pitch_deg : float
          Gimbal pitch (in degrees)

     gimbal_yaw_deg : float
          Gimbal yaw (in degrees)

     camera_action : CameraAction
          Camera action to trigger at this mission item

     loiter_time_s : float
          Loiter time (in seconds)

     camera_photo_interval_s : double
          Camera photo interval to use after this mission item (in seconds)

     acceptance_radius_m : float
          Radius for completing a mission item (in metres)

     yaw_deg : float
          Absolute yaw angle (in degrees)

     camera_photo_distance_m : float
          Camera photo distance to use after this mission item (in meters)

     """

    
    
    class CameraAction(Enum):
        """
         Possible camera actions at a mission item.

         Values
         ------
         NONE
              No action

         TAKE_PHOTO
              Take a single photo

         START_PHOTO_INTERVAL
              Start capturing photos at regular intervals

         STOP_PHOTO_INTERVAL
              Stop capturing photos at regular intervals

         START_VIDEO
              Start capturing video

         STOP_VIDEO
              Stop capturing video

         START_PHOTO_DISTANCE
              Start capturing photos at regular distance

         STOP_PHOTO_DISTANCE
              Stop capturing photos at regular distance

         """

        
        NONE = 0
        TAKE_PHOTO = 1
        START_PHOTO_INTERVAL = 2
        STOP_PHOTO_INTERVAL = 3
        START_VIDEO = 4
        STOP_VIDEO = 5
        START_PHOTO_DISTANCE = 6
        STOP_PHOTO_DISTANCE = 7

        def translate_to_rpc(self):
            if self == MissionItem.CameraAction.NONE:
                return mission_pb2.MissionItem.CAMERA_ACTION_NONE
            if self == MissionItem.CameraAction.TAKE_PHOTO:
                return mission_pb2.MissionItem.CAMERA_ACTION_TAKE_PHOTO
            if self == MissionItem.CameraAction.START_PHOTO_INTERVAL:
                return mission_pb2.MissionItem.CAMERA_ACTION_START_PHOTO_INTERVAL
            if self == MissionItem.CameraAction.STOP_PHOTO_INTERVAL:
                return mission_pb2.MissionItem.CAMERA_ACTION_STOP_PHOTO_INTERVAL
            if self == MissionItem.CameraAction.START_VIDEO:
                return mission_pb2.MissionItem.CAMERA_ACTION_START_VIDEO
            if self == MissionItem.CameraAction.STOP_VIDEO:
                return mission_pb2.MissionItem.CAMERA_ACTION_STOP_VIDEO
            if self == MissionItem.CameraAction.START_PHOTO_DISTANCE:
                return mission_pb2.MissionItem.CAMERA_ACTION_START_PHOTO_DISTANCE
            if self == MissionItem.CameraAction.STOP_PHOTO_DISTANCE:
                return mission_pb2.MissionItem.CAMERA_ACTION_STOP_PHOTO_DISTANCE

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_NONE:
                return MissionItem.CameraAction.NONE
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_TAKE_PHOTO:
                return MissionItem.CameraAction.TAKE_PHOTO
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_START_PHOTO_INTERVAL:
                return MissionItem.CameraAction.START_PHOTO_INTERVAL
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_STOP_PHOTO_INTERVAL:
                return MissionItem.CameraAction.STOP_PHOTO_INTERVAL
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_START_VIDEO:
                return MissionItem.CameraAction.START_VIDEO
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_STOP_VIDEO:
                return MissionItem.CameraAction.STOP_VIDEO
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_START_PHOTO_DISTANCE:
                return MissionItem.CameraAction.START_PHOTO_DISTANCE
            if rpc_enum_value == mission_pb2.MissionItem.CAMERA_ACTION_STOP_PHOTO_DISTANCE:
                return MissionItem.CameraAction.STOP_PHOTO_DISTANCE

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            latitude_deg,
            longitude_deg,
            relative_altitude_m,
            speed_m_s,
            is_fly_through,
            gimbal_pitch_deg,
            gimbal_yaw_deg,
            camera_action,
            loiter_time_s,
            camera_photo_interval_s,
            acceptance_radius_m,
            yaw_deg,
            camera_photo_distance_m):
        """ Initializes the MissionItem object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.relative_altitude_m = relative_altitude_m
        self.speed_m_s = speed_m_s
        self.is_fly_through = is_fly_through
        self.gimbal_pitch_deg = gimbal_pitch_deg
        self.gimbal_yaw_deg = gimbal_yaw_deg
        self.camera_action = camera_action
        self.loiter_time_s = loiter_time_s
        self.camera_photo_interval_s = camera_photo_interval_s
        self.acceptance_radius_m = acceptance_radius_m
        self.yaw_deg = yaw_deg
        self.camera_photo_distance_m = camera_photo_distance_m

    def __eq__(self, to_compare):
        """ Checks if two MissionItem are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionItem object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.relative_altitude_m == to_compare.relative_altitude_m) and \
                (self.speed_m_s == to_compare.speed_m_s) and \
                (self.is_fly_through == to_compare.is_fly_through) and \
                (self.gimbal_pitch_deg == to_compare.gimbal_pitch_deg) and \
                (self.gimbal_yaw_deg == to_compare.gimbal_yaw_deg) and \
                (self.camera_action == to_compare.camera_action) and \
                (self.loiter_time_s == to_compare.loiter_time_s) and \
                (self.camera_photo_interval_s == to_compare.camera_photo_interval_s) and \
                (self.acceptance_radius_m == to_compare.acceptance_radius_m) and \
                (self.yaw_deg == to_compare.yaw_deg) and \
                (self.camera_photo_distance_m == to_compare.camera_photo_distance_m)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionItem in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "relative_altitude_m: " + str(self.relative_altitude_m),
                "speed_m_s: " + str(self.speed_m_s),
                "is_fly_through: " + str(self.is_fly_through),
                "gimbal_pitch_deg: " + str(self.gimbal_pitch_deg),
                "gimbal_yaw_deg: " + str(self.gimbal_yaw_deg),
                "camera_action: " + str(self.camera_action),
                "loiter_time_s: " + str(self.loiter_time_s),
                "camera_photo_interval_s: " + str(self.camera_photo_interval_s),
                "acceptance_radius_m: " + str(self.acceptance_radius_m),
                "yaw_deg: " + str(self.yaw_deg),
                "camera_photo_distance_m: " + str(self.camera_photo_distance_m)
                ])

        return f"MissionItem: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionItem):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionItem(
                
                rpcMissionItem.latitude_deg,
                
                
                rpcMissionItem.longitude_deg,
                
                
                rpcMissionItem.relative_altitude_m,
                
                
                rpcMissionItem.speed_m_s,
                
                
                rpcMissionItem.is_fly_through,
                
                
                rpcMissionItem.gimbal_pitch_deg,
                
                
                rpcMissionItem.gimbal_yaw_deg,
                
                
                MissionItem.CameraAction.translate_from_rpc(rpcMissionItem.camera_action),
                
                
                rpcMissionItem.loiter_time_s,
                
                
                rpcMissionItem.camera_photo_interval_s,
                
                
                rpcMissionItem.acceptance_radius_m,
                
                
                rpcMissionItem.yaw_deg,
                
                
                rpcMissionItem.camera_photo_distance_m
                )

    def translate_to_rpc(self, rpcMissionItem):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionItem.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcMissionItem.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcMissionItem.relative_altitude_m = self.relative_altitude_m
            
        
        
        
            
        rpcMissionItem.speed_m_s = self.speed_m_s
            
        
        
        
            
        rpcMissionItem.is_fly_through = self.is_fly_through
            
        
        
        
            
        rpcMissionItem.gimbal_pitch_deg = self.gimbal_pitch_deg
            
        
        
        
            
        rpcMissionItem.gimbal_yaw_deg = self.gimbal_yaw_deg
            
        
        
        
            
        rpcMissionItem.camera_action = self.camera_action.translate_to_rpc()
            
        
        
        
            
        rpcMissionItem.loiter_time_s = self.loiter_time_s
            
        
        
        
            
        rpcMissionItem.camera_photo_interval_s = self.camera_photo_interval_s
            
        
        
        
            
        rpcMissionItem.acceptance_radius_m = self.acceptance_radius_m
            
        
        
        
            
        rpcMissionItem.yaw_deg = self.yaw_deg
            
        
        
        
            
        rpcMissionItem.camera_photo_distance_m = self.camera_photo_distance_m
            
        
        


class MissionPlan:
    """
     Mission plan type

     Parameters
     ----------
     mission_items : [MissionItem]
          The mission items

     """

    

    def __init__(
            self,
            mission_items):
        """ Initializes the MissionPlan object """
        self.mission_items = mission_items

    def __eq__(self, to_compare):
        """ Checks if two MissionPlan are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionPlan object
            return \
                (self.mission_items == to_compare.mission_items)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionPlan in string representation """
        struct_repr = ", ".join([
                "mission_items: " + str(self.mission_items)
                ])

        return f"MissionPlan: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionPlan):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionPlan(
                
                list(map(lambda elem: MissionItem.translate_from_rpc(elem), rpcMissionPlan.mission_items))
                )

    def translate_to_rpc(self, rpcMissionPlan):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.mission_items:
                
            rpc_elem = mission_pb2.MissionItem()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcMissionPlan.mission_items.extend(rpc_elems_list)
            
        
        


class MissionProgress:
    """
     Mission progress type.

     Parameters
     ----------
     current : int32_t
          Current mission item index (0-based), if equal to total, the mission is finished

     total : int32_t
          Total number of mission items

     """

    

    def __init__(
            self,
            current,
            total):
        """ Initializes the MissionProgress object """
        self.current = current
        self.total = total

    def __eq__(self, to_compare):
        """ Checks if two MissionProgress are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionProgress object
            return \
                (self.current == to_compare.current) and \
                (self.total == to_compare.total)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionProgress in string representation """
        struct_repr = ", ".join([
                "current: " + str(self.current),
                "total: " + str(self.total)
                ])

        return f"MissionProgress: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionProgress):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionProgress(
                
                rpcMissionProgress.current,
                
                
                rpcMissionProgress.total
                )

    def translate_to_rpc(self, rpcMissionProgress):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionProgress.current = self.current
            
        
        
        
            
        rpcMissionProgress.total = self.total
            
        
        


class MissionResult:
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
              Request succeeded

         ERROR
              Error

         TOO_MANY_MISSION_ITEMS
              Too many mission items in the mission

         BUSY
              Vehicle is busy

         TIMEOUT
              Request timed out

         INVALID_ARGUMENT
              Invalid argument

         UNSUPPORTED
              Mission downloaded from the system is not supported

         NO_MISSION_AVAILABLE
              No mission available on the system

         UNSUPPORTED_MISSION_CMD
              Unsupported mission command

         TRANSFER_CANCELLED
              Mission transfer (upload or download) has been cancelled

         NO_SYSTEM
              No system connected

         NEXT
              Intermediate message showing progress

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        ERROR = 2
        TOO_MANY_MISSION_ITEMS = 3
        BUSY = 4
        TIMEOUT = 5
        INVALID_ARGUMENT = 6
        UNSUPPORTED = 7
        NO_MISSION_AVAILABLE = 8
        UNSUPPORTED_MISSION_CMD = 9
        TRANSFER_CANCELLED = 10
        NO_SYSTEM = 11
        NEXT = 12

        def translate_to_rpc(self):
            if self == MissionResult.Result.UNKNOWN:
                return mission_pb2.MissionResult.RESULT_UNKNOWN
            if self == MissionResult.Result.SUCCESS:
                return mission_pb2.MissionResult.RESULT_SUCCESS
            if self == MissionResult.Result.ERROR:
                return mission_pb2.MissionResult.RESULT_ERROR
            if self == MissionResult.Result.TOO_MANY_MISSION_ITEMS:
                return mission_pb2.MissionResult.RESULT_TOO_MANY_MISSION_ITEMS
            if self == MissionResult.Result.BUSY:
                return mission_pb2.MissionResult.RESULT_BUSY
            if self == MissionResult.Result.TIMEOUT:
                return mission_pb2.MissionResult.RESULT_TIMEOUT
            if self == MissionResult.Result.INVALID_ARGUMENT:
                return mission_pb2.MissionResult.RESULT_INVALID_ARGUMENT
            if self == MissionResult.Result.UNSUPPORTED:
                return mission_pb2.MissionResult.RESULT_UNSUPPORTED
            if self == MissionResult.Result.NO_MISSION_AVAILABLE:
                return mission_pb2.MissionResult.RESULT_NO_MISSION_AVAILABLE
            if self == MissionResult.Result.UNSUPPORTED_MISSION_CMD:
                return mission_pb2.MissionResult.RESULT_UNSUPPORTED_MISSION_CMD
            if self == MissionResult.Result.TRANSFER_CANCELLED:
                return mission_pb2.MissionResult.RESULT_TRANSFER_CANCELLED
            if self == MissionResult.Result.NO_SYSTEM:
                return mission_pb2.MissionResult.RESULT_NO_SYSTEM
            if self == MissionResult.Result.NEXT:
                return mission_pb2.MissionResult.RESULT_NEXT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_UNKNOWN:
                return MissionResult.Result.UNKNOWN
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_SUCCESS:
                return MissionResult.Result.SUCCESS
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_ERROR:
                return MissionResult.Result.ERROR
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_TOO_MANY_MISSION_ITEMS:
                return MissionResult.Result.TOO_MANY_MISSION_ITEMS
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_BUSY:
                return MissionResult.Result.BUSY
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_TIMEOUT:
                return MissionResult.Result.TIMEOUT
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_INVALID_ARGUMENT:
                return MissionResult.Result.INVALID_ARGUMENT
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_UNSUPPORTED:
                return MissionResult.Result.UNSUPPORTED
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_NO_MISSION_AVAILABLE:
                return MissionResult.Result.NO_MISSION_AVAILABLE
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_UNSUPPORTED_MISSION_CMD:
                return MissionResult.Result.UNSUPPORTED_MISSION_CMD
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_TRANSFER_CANCELLED:
                return MissionResult.Result.TRANSFER_CANCELLED
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_NO_SYSTEM:
                return MissionResult.Result.NO_SYSTEM
            if rpc_enum_value == mission_pb2.MissionResult.RESULT_NEXT:
                return MissionResult.Result.NEXT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MissionResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two MissionResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"MissionResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionResult(
                
                MissionResult.Result.translate_from_rpc(rpcMissionResult.result),
                
                
                rpcMissionResult.result_str
                )

    def translate_to_rpc(self, rpcMissionResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcMissionResult.result_str = self.result_str
            
        
        


class ProgressData:
    """
     Progress data coming from mission upload.

     Parameters
     ----------
     progress : float
          Progress (0..1.0)

     """

    

    def __init__(
            self,
            progress):
        """ Initializes the ProgressData object """
        self.progress = progress

    def __eq__(self, to_compare):
        """ Checks if two ProgressData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressData object
            return \
                (self.progress == to_compare.progress)

        except AttributeError:
            return False

    def __str__(self):
        """ ProgressData in string representation """
        struct_repr = ", ".join([
                "progress: " + str(self.progress)
                ])

        return f"ProgressData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProgressData):
        """ Translates a gRPC struct to the SDK equivalent """
        return ProgressData(
                
                rpcProgressData.progress
                )

    def translate_to_rpc(self, rpcProgressData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProgressData.progress = self.progress
            
        
        


class ProgressDataOrMission:
    """
     Progress data coming from mission download, or the mission itself (if the transfer succeeds).

     Parameters
     ----------
     has_progress : bool
          Whether this ProgressData contains a 'progress' status or not

     progress : float
          Progress (0..1.0)

     has_mission : bool
          Whether this ProgressData contains a 'mission_plan' or not

     mission_plan : MissionPlan
          Mission plan

     """

    

    def __init__(
            self,
            has_progress,
            progress,
            has_mission,
            mission_plan):
        """ Initializes the ProgressDataOrMission object """
        self.has_progress = has_progress
        self.progress = progress
        self.has_mission = has_mission
        self.mission_plan = mission_plan

    def __eq__(self, to_compare):
        """ Checks if two ProgressDataOrMission are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressDataOrMission object
            return \
                (self.has_progress == to_compare.has_progress) and \
                (self.progress == to_compare.progress) and \
                (self.has_mission == to_compare.has_mission) and \
                (self.mission_plan == to_compare.mission_plan)

        except AttributeError:
            return False

    def __str__(self):
        """ ProgressDataOrMission in string representation """
        struct_repr = ", ".join([
                "has_progress: " + str(self.has_progress),
                "progress: " + str(self.progress),
                "has_mission: " + str(self.has_mission),
                "mission_plan: " + str(self.mission_plan)
                ])

        return f"ProgressDataOrMission: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProgressDataOrMission):
        """ Translates a gRPC struct to the SDK equivalent """
        return ProgressDataOrMission(
                
                rpcProgressDataOrMission.has_progress,
                
                
                rpcProgressDataOrMission.progress,
                
                
                rpcProgressDataOrMission.has_mission,
                
                
                MissionPlan.translate_from_rpc(rpcProgressDataOrMission.mission_plan)
                )

    def translate_to_rpc(self, rpcProgressDataOrMission):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProgressDataOrMission.has_progress = self.has_progress
            
        
        
        
            
        rpcProgressDataOrMission.progress = self.progress
            
        
        
        
            
        rpcProgressDataOrMission.has_mission = self.has_mission
            
        
        
        
            
        self.mission_plan.translate_to_rpc(rpcProgressDataOrMission.mission_plan)
            
        
        



class MissionError(Exception):
    """ Raised when a MissionResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Mission(AsyncBase):
    """
     Enable waypoint missions.

     Generated by dcsdkgen - MAVSDK Mission API
    """

    # Plugin name
    name = "Mission"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = mission_pb2_grpc.MissionServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return MissionResult.translate_from_rpc(response.mission_result)
    

    async def upload_mission(self, mission_plan):
        """
         Upload a list of mission items to the system.

         The mission items are uploaded to a drone. Once uploaded the mission can be started and
         executed even if the connection is lost.

         Parameters
         ----------
         mission_plan : MissionPlan
              The mission plan

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.UploadMissionRequest()
        
        mission_plan.translate_to_rpc(request.mission_plan)
                
            
        response = await self._stub.UploadMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "upload_mission()", mission_plan)
        

    async def upload_mission_with_progress(self, mission_plan):
        """
         Upload a list of mission items to the system and report upload progress.

         The mission items are uploaded to a drone. Once uploaded the mission can be started and
         executed even if the connection is lost.

         Parameters
         ----------
         mission_plan : MissionPlan
              The mission plan

         Yields
         -------
         progress_data : ProgressData
              The progress data

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.SubscribeUploadMissionWithProgressRequest()
        
        mission_plan.translate_to_rpc(request.mission_plan)
                
            
        upload_mission_with_progress_stream = self._stub.SubscribeUploadMissionWithProgress(request)

        try:
            async for response in upload_mission_with_progress_stream:
                
                result = self._extract_result(response)

                success_codes = [MissionResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in MissionResult.Result]:
                    success_codes.append(MissionResult.Result.NEXT)

                if result.result not in success_codes:
                    raise MissionError(result, "upload_mission_with_progress()", mission_plan)

                if result.result == MissionResult.Result.SUCCESS:
                    upload_mission_with_progress_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            upload_mission_with_progress_stream.cancel()

    async def cancel_mission_upload(self):
        """
         Cancel an ongoing mission upload.

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.CancelMissionUploadRequest()
        response = await self._stub.CancelMissionUpload(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "cancel_mission_upload()")
        

    async def download_mission(self):
        """
         Download a list of mission items from the system (asynchronous).

         Will fail if any of the downloaded mission items are not supported
         by the MAVSDK API.

         Returns
         -------
         mission_plan : MissionPlan
              The mission plan

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.DownloadMissionRequest()
        response = await self._stub.DownloadMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "download_mission()")
        

        return MissionPlan.translate_from_rpc(response.mission_plan)
            

    async def download_mission_with_progress(self):
        """
         Download a list of mission items from the system (asynchronous) and report progress.

         Will fail if any of the downloaded mission items are not supported
         by the MAVSDK API.

         Yields
         -------
         progress_data : ProgressDataOrMission
              The progress data, or the mission plan (when the download is finished)

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.SubscribeDownloadMissionWithProgressRequest()
        download_mission_with_progress_stream = self._stub.SubscribeDownloadMissionWithProgress(request)

        try:
            async for response in download_mission_with_progress_stream:
                
                result = self._extract_result(response)

                success_codes = [MissionResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in MissionResult.Result]:
                    success_codes.append(MissionResult.Result.NEXT)

                if result.result not in success_codes:
                    raise MissionError(result, "download_mission_with_progress()")

                if result.result == MissionResult.Result.SUCCESS:
                    download_mission_with_progress_stream.cancel();
                    return
                

            
                yield ProgressDataOrMission.translate_from_rpc(response.progress_data)
        finally:
            download_mission_with_progress_stream.cancel()

    async def cancel_mission_download(self):
        """
         Cancel an ongoing mission download.

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.CancelMissionDownloadRequest()
        response = await self._stub.CancelMissionDownload(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "cancel_mission_download()")
        

    async def start_mission(self):
        """
         Start the mission.

         A mission must be uploaded to the vehicle before this can be called.

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.StartMissionRequest()
        response = await self._stub.StartMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "start_mission()")
        

    async def pause_mission(self):
        """
         Pause the mission.

         Pausing the mission puts the vehicle into
         [HOLD mode](https://docs.px4.io/en/flight_modes/hold.html).
         A multicopter should just hover at the spot while a fixedwing vehicle should loiter
         around the location where it paused.

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.PauseMissionRequest()
        response = await self._stub.PauseMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "pause_mission()")
        

    async def clear_mission(self):
        """
         Clear the mission saved on the vehicle.

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.ClearMissionRequest()
        response = await self._stub.ClearMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "clear_mission()")
        

    async def set_current_mission_item(self, index):
        """
         Sets the mission item index to go to.

         By setting the current index to 0, the mission is restarted from the beginning. If it is set
         to a specific index of a mission item, the mission will be set to this item.

         Note that this is not necessarily true for general missions using MAVLink if loop counters
         are used.

         Parameters
         ----------
         index : int32_t
              Index of the mission item to be set as the next one (0-based)

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.SetCurrentMissionItemRequest()
        request.index = index
        response = await self._stub.SetCurrentMissionItem(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "set_current_mission_item()", index)
        

    async def is_mission_finished(self):
        """
         Check if the mission has been finished.

         Returns
         -------
         is_finished : bool
              True if the mission is finished and the last mission item has been reached

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.IsMissionFinishedRequest()
        response = await self._stub.IsMissionFinished(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "is_mission_finished()")
        

        return response.is_finished
        

    async def mission_progress(self):
        """
         Subscribe to mission progress updates.

         Yields
         -------
         mission_progress : MissionProgress
              Mission progress

         
        """

        request = mission_pb2.SubscribeMissionProgressRequest()
        mission_progress_stream = self._stub.SubscribeMissionProgress(request)

        try:
            async for response in mission_progress_stream:
                

            
                yield MissionProgress.translate_from_rpc(response.mission_progress)
        finally:
            mission_progress_stream.cancel()

    async def get_return_to_launch_after_mission(self):
        """
         Get whether to trigger Return-to-Launch (RTL) after mission is complete.

         Before getting this option, it needs to be set, or a mission
         needs to be downloaded.

         Returns
         -------
         enable : bool
              If true, trigger an RTL at the end of the mission

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.GetReturnToLaunchAfterMissionRequest()
        response = await self._stub.GetReturnToLaunchAfterMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "get_return_to_launch_after_mission()")
        

        return response.enable
        

    async def set_return_to_launch_after_mission(self, enable):
        """
         Set whether to trigger Return-to-Launch (RTL) after the mission is complete.

         This will only take effect for the next mission upload, meaning that
         the mission may have to be uploaded again.

         Parameters
         ----------
         enable : bool
              If true, trigger an RTL at the end of the mission

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.SetReturnToLaunchAfterMissionRequest()
        request.enable = enable
        response = await self._stub.SetReturnToLaunchAfterMission(request)

        
        result = self._extract_result(response)

        if result.result != MissionResult.Result.SUCCESS:
            raise MissionError(result, "set_return_to_launch_after_mission()", enable)
        