# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import mavlink_direct_pb2, mavlink_direct_pb2_grpc
from enum import Enum


class MavlinkMessage:
    """
     A complete MAVLink message with all header information and fields

     Parameters
     ----------
     message_name : std::string
          MAVLink message name (e.g., "HEARTBEAT", "GLOBAL_POSITION_INT")

     system_id : uint32_t
          System ID of the sender (for received messages)

     component_id : uint32_t
          Component ID of the sender (for received messages)

     target_system : uint32_t
          Target system ID (for sending, 0 for broadcast)

     target_component : uint32_t
          Target component ID (for sending, 0 for broadcast)

     fields_json : std::string
          All message fields as single JSON object

     """

    

    def __init__(
            self,
            message_name,
            system_id,
            component_id,
            target_system,
            target_component,
            fields_json):
        """ Initializes the MavlinkMessage object """
        self.message_name = message_name
        self.system_id = system_id
        self.component_id = component_id
        self.target_system = target_system
        self.target_component = target_component
        self.fields_json = fields_json

    def __eq__(self, to_compare):
        """ Checks if two MavlinkMessage are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MavlinkMessage object
            return \
                (self.message_name == to_compare.message_name) and \
                (self.system_id == to_compare.system_id) and \
                (self.component_id == to_compare.component_id) and \
                (self.target_system == to_compare.target_system) and \
                (self.target_component == to_compare.target_component) and \
                (self.fields_json == to_compare.fields_json)

        except AttributeError:
            return False

    def __str__(self):
        """ MavlinkMessage in string representation """
        struct_repr = ", ".join([
                "message_name: " + str(self.message_name),
                "system_id: " + str(self.system_id),
                "component_id: " + str(self.component_id),
                "target_system: " + str(self.target_system),
                "target_component: " + str(self.target_component),
                "fields_json: " + str(self.fields_json)
                ])

        return f"MavlinkMessage: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMavlinkMessage):
        """ Translates a gRPC struct to the SDK equivalent """
        return MavlinkMessage(
                
                rpcMavlinkMessage.message_name,
                
                
                rpcMavlinkMessage.system_id,
                
                
                rpcMavlinkMessage.component_id,
                
                
                rpcMavlinkMessage.target_system,
                
                
                rpcMavlinkMessage.target_component,
                
                
                rpcMavlinkMessage.fields_json
                )

    def translate_to_rpc(self, rpcMavlinkMessage):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMavlinkMessage.message_name = self.message_name
            
        
        
        
            
        rpcMavlinkMessage.system_id = self.system_id
            
        
        
        
            
        rpcMavlinkMessage.component_id = self.component_id
            
        
        
        
            
        rpcMavlinkMessage.target_system = self.target_system
            
        
        
        
            
        rpcMavlinkMessage.target_component = self.target_component
            
        
        
        
            
        rpcMavlinkMessage.fields_json = self.fields_json
            
        
        


class MavlinkDirectResult:
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

         INVALID_MESSAGE
              Invalid MAVLink message

         INVALID_FIELD
              Invalid field name or value

         CONNECTION_ERROR
              Connection error

         NO_SYSTEM
              No system connected

         TIMEOUT
              Request timed out

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        ERROR = 2
        INVALID_MESSAGE = 3
        INVALID_FIELD = 4
        CONNECTION_ERROR = 5
        NO_SYSTEM = 6
        TIMEOUT = 7

        def translate_to_rpc(self):
            if self == MavlinkDirectResult.Result.UNKNOWN:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_UNKNOWN
            if self == MavlinkDirectResult.Result.SUCCESS:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_SUCCESS
            if self == MavlinkDirectResult.Result.ERROR:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_ERROR
            if self == MavlinkDirectResult.Result.INVALID_MESSAGE:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_INVALID_MESSAGE
            if self == MavlinkDirectResult.Result.INVALID_FIELD:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_INVALID_FIELD
            if self == MavlinkDirectResult.Result.CONNECTION_ERROR:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_CONNECTION_ERROR
            if self == MavlinkDirectResult.Result.NO_SYSTEM:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_NO_SYSTEM
            if self == MavlinkDirectResult.Result.TIMEOUT:
                return mavlink_direct_pb2.MavlinkDirectResult.RESULT_TIMEOUT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_UNKNOWN:
                return MavlinkDirectResult.Result.UNKNOWN
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_SUCCESS:
                return MavlinkDirectResult.Result.SUCCESS
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_ERROR:
                return MavlinkDirectResult.Result.ERROR
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_INVALID_MESSAGE:
                return MavlinkDirectResult.Result.INVALID_MESSAGE
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_INVALID_FIELD:
                return MavlinkDirectResult.Result.INVALID_FIELD
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_CONNECTION_ERROR:
                return MavlinkDirectResult.Result.CONNECTION_ERROR
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_NO_SYSTEM:
                return MavlinkDirectResult.Result.NO_SYSTEM
            if rpc_enum_value == mavlink_direct_pb2.MavlinkDirectResult.RESULT_TIMEOUT:
                return MavlinkDirectResult.Result.TIMEOUT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the MavlinkDirectResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two MavlinkDirectResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MavlinkDirectResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ MavlinkDirectResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"MavlinkDirectResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMavlinkDirectResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return MavlinkDirectResult(
                
                MavlinkDirectResult.Result.translate_from_rpc(rpcMavlinkDirectResult.result),
                
                
                rpcMavlinkDirectResult.result_str
                )

    def translate_to_rpc(self, rpcMavlinkDirectResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMavlinkDirectResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcMavlinkDirectResult.result_str = self.result_str
            
        
        



class MavlinkDirectError(Exception):
    """ Raised when a MavlinkDirectResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class MavlinkDirect(AsyncBase):
    """
     Enable direct MAVLink communication using libmav.

     Generated by dcsdkgen - MAVSDK MavlinkDirect API
    """

    # Plugin name
    name = "MavlinkDirect"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = mavlink_direct_pb2_grpc.MavlinkDirectServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return MavlinkDirectResult.translate_from_rpc(response.mavlink_direct_result)
    

    async def send_message(self, message):
        """
         Send a MAVLink message directly to the system.

         This allows sending any MAVLink message with full control over the message content.

         Parameters
         ----------
         message : MavlinkMessage
              The MAVLink message to send

         Raises
         ------
         MavlinkDirectError
             If the request fails. The error contains the reason for the failure.
        """

        request = mavlink_direct_pb2.SendMessageRequest()
        
        message.translate_to_rpc(request.message)
                
            
        response = await self._stub.SendMessage(request)

        
        result = self._extract_result(response)

        if result.result != MavlinkDirectResult.Result.SUCCESS:
            raise MavlinkDirectError(result, "send_message()", message)
        

    async def message(self, message_name):
        """
         Subscribe to incoming MAVLink messages.

         This provides direct access to incoming MAVLink messages. Use an empty string
         in message_name to subscribe to all messages, or specify a message name
         (e.g., "HEARTBEAT") to filter for specific message types.

         Parameters
         ----------
         message_name : std::string
              MAVLink message name to filter for (e.g., "HEARTBEAT"), empty string = all messages

         Yields
         -------
         message : MavlinkMessage
              The received MAVLink message

         
        """

        request = mavlink_direct_pb2.SubscribeMessageRequest()
        request.message_name = message_name
        message_stream = self._stub.SubscribeMessage(request)

        try:
            async for response in message_stream:
                

            
                yield MavlinkMessage.translate_from_rpc(response.message)
        finally:
            message_stream.cancel()

    async def load_custom_xml(self, xml_content):
        """
         Load custom MAVLink message definitions from XML.

         This allows loading custom MAVLink message definitions at runtime,
         extending the available message types beyond the built-in definitions.

         Parameters
         ----------
         xml_content : std::string
              The custom MAVLink XML definition content

         Raises
         ------
         MavlinkDirectError
             If the request fails. The error contains the reason for the failure.
        """

        request = mavlink_direct_pb2.LoadCustomXmlRequest()
        request.xml_content = xml_content
        response = await self._stub.LoadCustomXml(request)

        
        result = self._extract_result(response)

        if result.result != MavlinkDirectResult.Result.SUCCESS:
            raise MavlinkDirectError(result, "load_custom_xml()", xml_content)
        