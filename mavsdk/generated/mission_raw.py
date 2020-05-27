# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import mission_raw_pb2, mission_raw_pb2_grpc
from enum import Enum


class MissionProgress:
    """
     Mission progress type.

     Parameters
     ----------
     current : int32_t
          Current mission item index (0-based)

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

    def __equals__(self, to_compare):
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
            
        
        


class MissionItem:
    """
     Mission item exactly identical to MAVLink MISSION_ITEM_INT.

     Parameters
     ----------
     seq : uint32_t
          Sequence (uint16_t)

     frame : uint32_t
          The coordinate system of the waypoint (actually uint8_t)

     command : uint32_t
          The scheduled action for the waypoint (actually uint16_t)

     current : uint32_t
          false:0, true:1 (actually uint8_t)

     autocontinue : uint32_t
          Autocontinue to next waypoint (actually uint8_t)

     param1 : float
          PARAM1, see MAV_CMD enum

     param2 : float
          PARAM2, see MAV_CMD enum

     param3 : float
          PARAM3, see MAV_CMD enum

     param4 : float
          PARAM4, see MAV_CMD enum

     x : int32_t
          PARAM5 / local: x position in meters * 1e4, global: latitude in degrees * 10^7

     y : int32_t
          PARAM6 / y position: local: x position in meters * 1e4, global: longitude in degrees *10^7

     z : float
          PARAM7 / local: Z coordinate, global: altitude (relative or absolute, depending on frame)

     mission_type : uint32_t
          @brief Mission type (actually uint8_t)

     """

    

    def __init__(
            self,
            seq,
            frame,
            command,
            current,
            autocontinue,
            param1,
            param2,
            param3,
            param4,
            x,
            y,
            z,
            mission_type):
        """ Initializes the MissionItem object """
        self.seq = seq
        self.frame = frame
        self.command = command
        self.current = current
        self.autocontinue = autocontinue
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        self.param4 = param4
        self.x = x
        self.y = y
        self.z = z
        self.mission_type = mission_type

    def __equals__(self, to_compare):
        """ Checks if two MissionItem are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionItem object
            return \
                (self.seq == to_compare.seq) and \
                (self.frame == to_compare.frame) and \
                (self.command == to_compare.command) and \
                (self.current == to_compare.current) and \
                (self.autocontinue == to_compare.autocontinue) and \
                (self.param1 == to_compare.param1) and \
                (self.param2 == to_compare.param2) and \
                (self.param3 == to_compare.param3) and \
                (self.param4 == to_compare.param4) and \
                (self.x == to_compare.x) and \
                (self.y == to_compare.y) and \
                (self.z == to_compare.z) and \
                (self.mission_type == to_compare.mission_type)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionItem in string representation """
        struct_repr = ", ".join([
                "seq: " + str(self.seq),
                "frame: " + str(self.frame),
                "command: " + str(self.command),
                "current: " + str(self.current),
                "autocontinue: " + str(self.autocontinue),
                "param1: " + str(self.param1),
                "param2: " + str(self.param2),
                "param3: " + str(self.param3),
                "param4: " + str(self.param4),
                "x: " + str(self.x),
                "y: " + str(self.y),
                "z: " + str(self.z),
                "mission_type: " + str(self.mission_type)
                ])

        return f"MissionItem: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionItem):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionItem(
                
                rpcMissionItem.seq,
                
                
                rpcMissionItem.frame,
                
                
                rpcMissionItem.command,
                
                
                rpcMissionItem.current,
                
                
                rpcMissionItem.autocontinue,
                
                
                rpcMissionItem.param1,
                
                
                rpcMissionItem.param2,
                
                
                rpcMissionItem.param3,
                
                
                rpcMissionItem.param4,
                
                
                rpcMissionItem.x,
                
                
                rpcMissionItem.y,
                
                
                rpcMissionItem.z,
                
                
                rpcMissionItem.mission_type
                )

    def translate_to_rpc(self, rpcMissionItem):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionItem.seq = self.seq
            
        
        
        
            
        rpcMissionItem.frame = self.frame
            
        
        
        
            
        rpcMissionItem.command = self.command
            
        
        
        
            
        rpcMissionItem.current = self.current
            
        
        
        
            
        rpcMissionItem.autocontinue = self.autocontinue
            
        
        
        
            
        rpcMissionItem.param1 = self.param1
            
        
        
        
            
        rpcMissionItem.param2 = self.param2
            
        
        
        
            
        rpcMissionItem.param3 = self.param3
            
        
        
        
            
        rpcMissionItem.param4 = self.param4
            
        
        
        
            
        rpcMissionItem.x = self.x
            
        
        
        
            
        rpcMissionItem.y = self.y
            
        
        
        
            
        rpcMissionItem.z = self.z
            
        
        
        
            
        rpcMissionItem.mission_type = self.mission_type
            
        
        


class MissionRawResult:
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
        TRANSFER_CANCELLED = 9

        def translate_to_rpc(self):
            if self == MissionRawResult.Result.UNKNOWN:
                return mission_raw_pb2.MissionRawResult.RESULT_UNKNOWN
            if self == MissionRawResult.Result.SUCCESS:
                return mission_raw_pb2.MissionRawResult.RESULT_SUCCESS
            if self == MissionRawResult.Result.ERROR:
                return mission_raw_pb2.MissionRawResult.RESULT_ERROR
            if self == MissionRawResult.Result.TOO_MANY_MISSION_ITEMS:
                return mission_raw_pb2.MissionRawResult.RESULT_TOO_MANY_MISSION_ITEMS
            if self == MissionRawResult.Result.BUSY:
                return mission_raw_pb2.MissionRawResult.RESULT_BUSY
            if self == MissionRawResult.Result.TIMEOUT:
                return mission_raw_pb2.MissionRawResult.RESULT_TIMEOUT
            if self == MissionRawResult.Result.INVALID_ARGUMENT:
                return mission_raw_pb2.MissionRawResult.RESULT_INVALID_ARGUMENT
            if self == MissionRawResult.Result.UNSUPPORTED:
                return mission_raw_pb2.MissionRawResult.RESULT_UNSUPPORTED
            if self == MissionRawResult.Result.NO_MISSION_AVAILABLE:
                return mission_raw_pb2.MissionRawResult.RESULT_NO_MISSION_AVAILABLE
            if self == MissionRawResult.Result.TRANSFER_CANCELLED:
                return mission_raw_pb2.MissionRawResult.RESULT_TRANSFER_CANCELLED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_UNKNOWN:
                return MissionRawResult.Result.UNKNOWN
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_SUCCESS:
                return MissionRawResult.Result.SUCCESS
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_ERROR:
                return MissionRawResult.Result.ERROR
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_TOO_MANY_MISSION_ITEMS:
                return MissionRawResult.Result.TOO_MANY_MISSION_ITEMS
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_BUSY:
                return MissionRawResult.Result.BUSY
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_TIMEOUT:
                return MissionRawResult.Result.TIMEOUT
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_INVALID_ARGUMENT:
                return MissionRawResult.Result.INVALID_ARGUMENT
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_UNSUPPORTED:
                return MissionRawResult.Result.UNSUPPORTED
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_NO_MISSION_AVAILABLE:
                return MissionRawResult.Result.NO_MISSION_AVAILABLE
            if rpc_enum_value == mission_raw_pb2.MissionRawResult.RESULT_TRANSFER_CANCELLED:
                return MissionRawResult.Result.TRANSFER_CANCELLED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MissionRawResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two MissionRawResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionRawResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionRawResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"MissionRawResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionRawResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionRawResult(
                
                MissionRawResult.Result.translate_from_rpc(rpcMissionRawResult.result),
                
                
                rpcMissionRawResult.result_str
                )

    def translate_to_rpc(self, rpcMissionRawResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionRawResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcMissionRawResult.result_str = self.result_str
            
        
        



class MissionRawError(Exception):
    """ Raised when a MissionRawResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class MissionRaw(AsyncBase):
    """
     Enable raw missions as exposed by MAVLink.

     Generated by dcsdkgen - MAVSDK MissionRaw API
    """

    # Plugin name
    name = "MissionRaw"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = mission_raw_pb2_grpc.MissionRawServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return MissionRawResult.translate_from_rpc(response.mission_raw_result)
    

    async def upload_mission(self, mission_items):
        """
         Upload a list of raw mission items to the system.

         The raw mission items are uploaded to a drone. Once uploaded the mission
         can be started and executed even if the connection is lost.

         Parameters
         ----------
         mission_items : [MissionItem]
              The mission items

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.UploadMissionRequest()
        
        rpc_elems_list = []
        for elem in mission_items:
            rpc_elem = mission_raw_pb2.MissionItem()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        request.mission_items.extend(rpc_elems_list)
                
            
        response = await self._stub.UploadMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "upload_mission()", mission_items)
        

    async def cancel_mission_upload(self):
        """
         Cancel an ongoing mission upload.

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.CancelMissionUploadRequest()
        response = await self._stub.CancelMissionUpload(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "cancel_mission_upload()")
        

    async def download_mission(self):
        """
         Download a list of raw mission items from the system (asynchronous).

         Returns
         -------
         mission_items : [MissionItem]
              The mission items

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.DownloadMissionRequest()
        response = await self._stub.DownloadMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "download_mission()")
        

        mission_items = []
        for mission_items_rpc in response.mission_items:
            mission_items.append(MissionItem.translate_from_rpc(mission_items_rpc))

        return mission_items
            

    async def cancel_mission_download(self):
        """
         Cancel an ongoing mission download.

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.CancelMissionDownloadRequest()
        response = await self._stub.CancelMissionDownload(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "cancel_mission_download()")
        

    async def start_mission(self):
        """
         Start the mission.

         A mission must be uploaded to the vehicle before this can be called.

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.StartMissionRequest()
        response = await self._stub.StartMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "start_mission()")
        

    async def pause_mission(self):
        """
         Pause the mission.

         Pausing the mission puts the vehicle into
         [HOLD mode](https://docs.px4.io/en/flight_modes/hold.html).
         A multicopter should just hover at the spot while a fixedwing vehicle should loiter
         around the location where it paused.

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.PauseMissionRequest()
        response = await self._stub.PauseMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "pause_mission()")
        

    async def clear_mission(self):
        """
         Clear the mission saved on the vehicle.

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.ClearMissionRequest()
        response = await self._stub.ClearMission(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "clear_mission()")
        

    async def set_current_mission_item(self, index):
        """
         Sets the raw mission item index to go to.

         By setting the current index to 0, the mission is restarted from the beginning. If it is set
         to a specific index of a raw mission item, the mission will be set to this item.

         Parameters
         ----------
         index : int32_t
              Index of the mission item to be set as the next one (0-based)

         Raises
         ------
         MissionRawError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_pb2.SetCurrentMissionItemRequest()
        request.index = index
        response = await self._stub.SetCurrentMissionItem(request)

        
        result = self._extract_result(response)

        if result.result is not MissionRawResult.Result.SUCCESS:
            raise MissionRawError(result, "set_current_mission_item()", index)
        

    async def mission_progress(self):
        """
         Subscribe to mission progress updates.

         Yields
         -------
         mission_progress : MissionProgress
              Mission progress

         
        """

        request = missionRaw_pb2.SubscribeMissionProgressRequest()
        mission_progress_stream = self._stub.SubscribeMissionProgress(request)

        try:
            async for response in mission_progress_stream:
                

            
                yield MissionProgress.translate_from_rpc(response.mission_progress)
        finally:
            mission_progress_stream.cancel()

    async def mission_changed(self):
        """
         *
         Subscribes to mission changed.

         This notification can be used to be informed if a ground station has
         been uploaded or changed by a ground station or companion computer.

         @param callback Callback to notify about change.

         Yields
         -------
         mission_changed : bool
              Mission has changed

         
        """

        request = missionRaw_pb2.SubscribeMissionChangedRequest()
        mission_changed_stream = self._stub.SubscribeMissionChanged(request)

        try:
            async for response in mission_changed_stream:
                

            
                yield response.mission_changed
        finally:
            mission_changed_stream.cancel()