# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import mission_pb2, mission_pb2_grpc
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

         """

        
        NONE = 0
        TAKE_PHOTO = 1
        START_PHOTO_INTERVAL = 2
        STOP_PHOTO_INTERVAL = 3
        START_VIDEO = 4
        STOP_VIDEO = 5

        def translate_to_rpc(self, rpcCameraAction):
            return {
                    0: mission_pb2.MissionItem.NONE,
                    1: mission_pb2.MissionItem.TAKE_PHOTO,
                    2: mission_pb2.MissionItem.START_PHOTO_INTERVAL,
                    3: mission_pb2.MissionItem.STOP_PHOTO_INTERVAL,
                    4: mission_pb2.MissionItem.START_VIDEO,
                    5: mission_pb2.MissionItem.STOP_VIDEO
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: MissionItem.CameraAction.NONE,
                    1: MissionItem.CameraAction.TAKE_PHOTO,
                    2: MissionItem.CameraAction.START_PHOTO_INTERVAL,
                    3: MissionItem.CameraAction.STOP_PHOTO_INTERVAL,
                    4: MissionItem.CameraAction.START_VIDEO,
                    5: MissionItem.CameraAction.STOP_VIDEO,
                }.get(rpc_enum_value, None)

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
            camera_photo_interval_s):
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

    def __equals__(self, to_compare):
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
                (self.camera_photo_interval_s == to_compare.camera_photo_interval_s)

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
                "camera_photo_interval_s: " + str(self.camera_photo_interval_s)
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
                
                
                rpcMissionItem.camera_photo_interval_s
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
            
        
        
        
            
        self.camera_action.translate_to_rpc(rpcMissionItem.camera_action)
            
        
        
        
            
        rpcMissionItem.loiter_time_s = self.loiter_time_s
            
        
        
        
            
        rpcMissionItem.camera_photo_interval_s = self.camera_photo_interval_s
            
        
        


class MissionProgress:
    """
     Mission progress type.

     Parameters
     ----------
     current_item_index : int32_t
          Current mission item index (0-based)

     mission_count : int32_t
          Total number of mission items

     """

    

    def __init__(
            self,
            current_item_index,
            mission_count):
        """ Initializes the MissionProgress object """
        self.current_item_index = current_item_index
        self.mission_count = mission_count

    def __equals__(self, to_compare):
        """ Checks if two MissionProgress are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionProgress object
            return \
                (self.current_item_index == to_compare.current_item_index) and \
                (self.mission_count == to_compare.mission_count)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionProgress in string representation """
        struct_repr = ", ".join([
                "current_item_index: " + str(self.current_item_index),
                "mission_count: " + str(self.mission_count)
                ])

        return f"MissionProgress: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionProgress):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionProgress(
                
                rpcMissionProgress.current_item_index,
                
                
                rpcMissionProgress.mission_count
                )

    def translate_to_rpc(self, rpcMissionProgress):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionProgress.current_item_index = self.current_item_index
            
        
        
        
            
        rpcMissionProgress.mission_count = self.mission_count
            
        
        


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
              Unknown error

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

         FAILED_TO_OPEN_QGC_PLAN
              Failed to open the QGroundControl plan

         FAILED_TO_PARSE_QGC_PLAN
              Failed to parse the QGroundControl plan

         UNSUPPORTED_MISSION_CMD
              Unsupported mission command

         TRANSFER_CANCELLED
              Mission transfer (upload or download) has been cancelled

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
        FAILED_TO_OPEN_QGC_PLAN = 9
        FAILED_TO_PARSE_QGC_PLAN = 10
        UNSUPPORTED_MISSION_CMD = 11
        TRANSFER_CANCELLED = 12

        def translate_to_rpc(self, rpcResult):
            return {
                    0: mission_pb2.MissionResult.UNKNOWN,
                    1: mission_pb2.MissionResult.SUCCESS,
                    2: mission_pb2.MissionResult.ERROR,
                    3: mission_pb2.MissionResult.TOO_MANY_MISSION_ITEMS,
                    4: mission_pb2.MissionResult.BUSY,
                    5: mission_pb2.MissionResult.TIMEOUT,
                    6: mission_pb2.MissionResult.INVALID_ARGUMENT,
                    7: mission_pb2.MissionResult.UNSUPPORTED,
                    8: mission_pb2.MissionResult.NO_MISSION_AVAILABLE,
                    9: mission_pb2.MissionResult.FAILED_TO_OPEN_QGC_PLAN,
                    10: mission_pb2.MissionResult.FAILED_TO_PARSE_QGC_PLAN,
                    11: mission_pb2.MissionResult.UNSUPPORTED_MISSION_CMD,
                    12: mission_pb2.MissionResult.TRANSFER_CANCELLED
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: MissionResult.Result.UNKNOWN,
                    1: MissionResult.Result.SUCCESS,
                    2: MissionResult.Result.ERROR,
                    3: MissionResult.Result.TOO_MANY_MISSION_ITEMS,
                    4: MissionResult.Result.BUSY,
                    5: MissionResult.Result.TIMEOUT,
                    6: MissionResult.Result.INVALID_ARGUMENT,
                    7: MissionResult.Result.UNSUPPORTED,
                    8: MissionResult.Result.NO_MISSION_AVAILABLE,
                    9: MissionResult.Result.FAILED_TO_OPEN_QGC_PLAN,
                    10: MissionResult.Result.FAILED_TO_PARSE_QGC_PLAN,
                    11: MissionResult.Result.UNSUPPORTED_MISSION_CMD,
                    12: MissionResult.Result.TRANSFER_CANCELLED,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MissionResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
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

        
        
            
        self.result.translate_to_rpc(rpcMissionResult.result)
            
        
        
        
            
        rpcMissionResult.result_str = self.result_str
            
        
        



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
    

    async def upload_mission(self, mission_items):
        """
         Upload a list of mission items to the system.

         The mission items are uploaded to a drone. Once uploaded the mission can be started and
         executed even if the connection is lost.

         Parameters
         ----------
         mission_items : [MissionItem]
              List of mission items

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.UploadMissionRequest()
        
        rpc_elems_list = []
        for elem in mission_items:
            rpc_elem = mission_pb2.MissionItem()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        request.mission_items.extend(rpc_elems_list)
                
            
        response = await self._stub.UploadMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionResult.Result.SUCCESS:
            raise MissionError(result, "upload_mission()", mission_items)
        

    async def cancel_mission_upload(self):
        """
         Cancel an ongoing mission upload.

         
        """

        request = mission_pb2.CancelMissionUploadRequest()
        response = await self._stub.CancelMissionUpload(request)

        

    async def download_mission(self):
        """
         Download a list of mission items from the system (asynchronous).

         Will fail if any of the downloaded mission items are not supported
         by the MAVSDK API.

         Returns
         -------
         mission_items : [MissionItem]
              List of downloaded mission items

         Raises
         ------
         MissionError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_pb2.DownloadMissionRequest()
        response = await self._stub.DownloadMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionResult.Result.SUCCESS:
            raise MissionError(result, "download_mission()")
        

        mission_items = []
        for mission_items_rpc in response.mission_items:
            mission_items.append(MissionItem.translate_from_rpc(mission_items_rpc))

        return mission_items
            

    async def cancel_mission_download(self):
        """
         Cancel an ongoing mission download.

         
        """

        request = mission_pb2.CancelMissionDownloadRequest()
        response = await self._stub.CancelMissionDownload(request)

        

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

        if result.result is not MissionResult.Result.SUCCESS:
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

        if result.result is not MissionResult.Result.SUCCESS:
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

        if result.result is not MissionResult.Result.SUCCESS:
            raise MissionError(result, "clear_mission()")
        

    async def set_current_mission_item_index(self, index):
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

        request = mission_pb2.SetCurrentMissionItemIndexRequest()
        request.index = index
        response = await self._stub.SetCurrentMissionItemIndex(request)

        
        result = self._extract_result(response)

        if result.result is not MissionResult.Result.SUCCESS:
            raise MissionError(result, "set_current_mission_item_index()", index)
        

    async def is_mission_finished(self):
        """
         Check if the mission has been finished.

         Returns
         -------
         is_finished : bool
              True if the mission is finished and the last mission item has been reached

         
        """

        request = mission_pb2.IsMissionFinishedRequest()
        response = await self._stub.IsMissionFinished(request)

        

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

         
        """

        request = mission_pb2.GetReturnToLaunchAfterMissionRequest()
        response = await self._stub.GetReturnToLaunchAfterMission(request)

        

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

         
        """

        request = mission_pb2.SetReturnToLaunchAfterMissionRequest()
        request.enable = enable
        response = await self._stub.SetReturnToLaunchAfterMission(request)

        