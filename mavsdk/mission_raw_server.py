# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import mission_raw_server_pb2, mission_raw_server_pb2_grpc
from enum import Enum


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
          Mission type (actually uint8_t)

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

    def __eq__(self, to_compare):
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
                
            rpc_elem = mission_raw_server_pb2.MissionItem()
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
            
        
        


class MissionRawServerResult:
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
              Intermediate message showing progress or instructions on the next steps

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
            if self == MissionRawServerResult.Result.UNKNOWN:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_UNKNOWN
            if self == MissionRawServerResult.Result.SUCCESS:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_SUCCESS
            if self == MissionRawServerResult.Result.ERROR:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_ERROR
            if self == MissionRawServerResult.Result.TOO_MANY_MISSION_ITEMS:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_TOO_MANY_MISSION_ITEMS
            if self == MissionRawServerResult.Result.BUSY:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_BUSY
            if self == MissionRawServerResult.Result.TIMEOUT:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_TIMEOUT
            if self == MissionRawServerResult.Result.INVALID_ARGUMENT:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_INVALID_ARGUMENT
            if self == MissionRawServerResult.Result.UNSUPPORTED:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_UNSUPPORTED
            if self == MissionRawServerResult.Result.NO_MISSION_AVAILABLE:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_NO_MISSION_AVAILABLE
            if self == MissionRawServerResult.Result.UNSUPPORTED_MISSION_CMD:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_UNSUPPORTED_MISSION_CMD
            if self == MissionRawServerResult.Result.TRANSFER_CANCELLED:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_TRANSFER_CANCELLED
            if self == MissionRawServerResult.Result.NO_SYSTEM:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_NO_SYSTEM
            if self == MissionRawServerResult.Result.NEXT:
                return mission_raw_server_pb2.MissionRawServerResult.RESULT_NEXT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_UNKNOWN:
                return MissionRawServerResult.Result.UNKNOWN
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_SUCCESS:
                return MissionRawServerResult.Result.SUCCESS
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_ERROR:
                return MissionRawServerResult.Result.ERROR
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_TOO_MANY_MISSION_ITEMS:
                return MissionRawServerResult.Result.TOO_MANY_MISSION_ITEMS
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_BUSY:
                return MissionRawServerResult.Result.BUSY
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_TIMEOUT:
                return MissionRawServerResult.Result.TIMEOUT
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_INVALID_ARGUMENT:
                return MissionRawServerResult.Result.INVALID_ARGUMENT
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_UNSUPPORTED:
                return MissionRawServerResult.Result.UNSUPPORTED
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_NO_MISSION_AVAILABLE:
                return MissionRawServerResult.Result.NO_MISSION_AVAILABLE
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_UNSUPPORTED_MISSION_CMD:
                return MissionRawServerResult.Result.UNSUPPORTED_MISSION_CMD
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_TRANSFER_CANCELLED:
                return MissionRawServerResult.Result.TRANSFER_CANCELLED
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_NO_SYSTEM:
                return MissionRawServerResult.Result.NO_SYSTEM
            if rpc_enum_value == mission_raw_server_pb2.MissionRawServerResult.RESULT_NEXT:
                return MissionRawServerResult.Result.NEXT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MissionRawServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two MissionRawServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MissionRawServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ MissionRawServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"MissionRawServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMissionRawServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return MissionRawServerResult(
                
                MissionRawServerResult.Result.translate_from_rpc(rpcMissionRawServerResult.result),
                
                
                rpcMissionRawServerResult.result_str
                )

    def translate_to_rpc(self, rpcMissionRawServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMissionRawServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcMissionRawServerResult.result_str = self.result_str
            
        
        



class MissionRawServerError(Exception):
    """ Raised when a MissionRawServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class MissionRawServer(AsyncBase):
    """
     Acts as a vehicle and receives incoming missions from GCS (in raw MAVLINK format). 
     Provides current mission item state, so the server can progress through missions.

     Generated by dcsdkgen - MAVSDK MissionRawServer API
    """

    # Plugin name
    name = "MissionRawServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = mission_raw_server_pb2_grpc.MissionRawServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return MissionRawServerResult.translate_from_rpc(response.mission_raw_server_result)
    

    async def incoming_mission(self):
        """
         Subscribe to when a new mission is uploaded (asynchronous).

         Yields
         -------
         mission_plan : MissionPlan
              The mission plan

         Raises
         ------
         MissionRawServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = mission_raw_server_pb2.SubscribeIncomingMissionRequest()
        incoming_mission_stream = self._stub.SubscribeIncomingMission(request)

        try:
            async for response in incoming_mission_stream:
                
                result = self._extract_result(response)

                success_codes = [MissionRawServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in MissionRawServerResult.Result]:
                    success_codes.append(MissionRawServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise MissionRawServerError(result, "incoming_mission()")

                if result.result == MissionRawServerResult.Result.SUCCESS:
                    incoming_mission_stream.cancel();
                    return
                

            
                yield MissionPlan.translate_from_rpc(response.mission_plan)
        finally:
            incoming_mission_stream.cancel()

    async def current_item_changed(self):
        """
         Subscribe to when a new current item is set

         Yields
         -------
         mission_item : MissionItem
             
         
        """

        request = mission_raw_server_pb2.SubscribeCurrentItemChangedRequest()
        current_item_changed_stream = self._stub.SubscribeCurrentItemChanged(request)

        try:
            async for response in current_item_changed_stream:
                

            
                yield MissionItem.translate_from_rpc(response.mission_item)
        finally:
            current_item_changed_stream.cancel()

    async def set_current_item_complete(self):
        """
         Set Current item as completed

         
        """

        request = mission_raw_server_pb2.SetCurrentItemCompleteRequest()
        response = await self._stub.SetCurrentItemComplete(request)

        

    async def clear_all(self):
        """
         Subscribe when a MISSION_CLEAR_ALL is received

         Yields
         -------
         clear_type : uint32_t
             
         
        """

        request = mission_raw_server_pb2.SubscribeClearAllRequest()
        clear_all_stream = self._stub.SubscribeClearAll(request)

        try:
            async for response in clear_all_stream:
                

            
                yield response.clear_type
        finally:
            clear_all_stream.cancel()