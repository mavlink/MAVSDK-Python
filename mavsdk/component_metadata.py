# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import component_metadata_pb2, component_metadata_pb2_grpc
from enum import Enum


class MetadataType(Enum):
    """
     The metadata type

     Values
     ------
     ALL_COMPLETED
          This is set in the subscription callback when all metadata types completed for a given component ID

     PARAMETER
          Parameter metadata

     EVENTS
          Event definitions

     ACTUATORS
          Actuator definitions

     """

    
    ALL_COMPLETED = 0
    PARAMETER = 1
    EVENTS = 2
    ACTUATORS = 3

    def translate_to_rpc(self):
        if self == MetadataType.ALL_COMPLETED:
            return component_metadata_pb2.METADATA_TYPE_ALL_COMPLETED
        if self == MetadataType.PARAMETER:
            return component_metadata_pb2.METADATA_TYPE_PARAMETER
        if self == MetadataType.EVENTS:
            return component_metadata_pb2.METADATA_TYPE_EVENTS
        if self == MetadataType.ACTUATORS:
            return component_metadata_pb2.METADATA_TYPE_ACTUATORS

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == component_metadata_pb2.METADATA_TYPE_ALL_COMPLETED:
            return MetadataType.ALL_COMPLETED
        if rpc_enum_value == component_metadata_pb2.METADATA_TYPE_PARAMETER:
            return MetadataType.PARAMETER
        if rpc_enum_value == component_metadata_pb2.METADATA_TYPE_EVENTS:
            return MetadataType.EVENTS
        if rpc_enum_value == component_metadata_pb2.METADATA_TYPE_ACTUATORS:
            return MetadataType.ACTUATORS

    def __str__(self):
        return self.name


class MetadataData:
    """
     Metadata response

     Parameters
     ----------
     json_metadata : std::string
          The JSON metadata

     """

    

    def __init__(
            self,
            json_metadata):
        """ Initializes the MetadataData object """
        self.json_metadata = json_metadata

    def __eq__(self, to_compare):
        """ Checks if two MetadataData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MetadataData object
            return \
                (self.json_metadata == to_compare.json_metadata)

        except AttributeError:
            return False

    def __str__(self):
        """ MetadataData in string representation """
        struct_repr = ", ".join([
                "json_metadata: " + str(self.json_metadata)
                ])

        return f"MetadataData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMetadataData):
        """ Translates a gRPC struct to the SDK equivalent """
        return MetadataData(
                
                rpcMetadataData.json_metadata
                )

    def translate_to_rpc(self, rpcMetadataData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMetadataData.json_metadata = self.json_metadata
            
        
        


class ComponentMetadataResult:
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
         Possible results returned

         Values
         ------
         SUCCESS
              Success

         NOT_AVAILABLE
              Not available

         CONNECTION_ERROR
              Connection error

         UNSUPPORTED
              Unsupported

         DENIED
              Denied

         FAILED
              Failed

         TIMEOUT
              Timeout

         NO_SYSTEM
              No system

         NOT_REQUESTED
              Not requested

         """

        
        SUCCESS = 0
        NOT_AVAILABLE = 1
        CONNECTION_ERROR = 2
        UNSUPPORTED = 3
        DENIED = 4
        FAILED = 5
        TIMEOUT = 6
        NO_SYSTEM = 7
        NOT_REQUESTED = 8

        def translate_to_rpc(self):
            if self == ComponentMetadataResult.Result.SUCCESS:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_SUCCESS
            if self == ComponentMetadataResult.Result.NOT_AVAILABLE:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_NOT_AVAILABLE
            if self == ComponentMetadataResult.Result.CONNECTION_ERROR:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_CONNECTION_ERROR
            if self == ComponentMetadataResult.Result.UNSUPPORTED:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_UNSUPPORTED
            if self == ComponentMetadataResult.Result.DENIED:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_DENIED
            if self == ComponentMetadataResult.Result.FAILED:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_FAILED
            if self == ComponentMetadataResult.Result.TIMEOUT:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_TIMEOUT
            if self == ComponentMetadataResult.Result.NO_SYSTEM:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_NO_SYSTEM
            if self == ComponentMetadataResult.Result.NOT_REQUESTED:
                return component_metadata_pb2.ComponentMetadataResult.RESULT_NOT_REQUESTED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_SUCCESS:
                return ComponentMetadataResult.Result.SUCCESS
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_NOT_AVAILABLE:
                return ComponentMetadataResult.Result.NOT_AVAILABLE
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_CONNECTION_ERROR:
                return ComponentMetadataResult.Result.CONNECTION_ERROR
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_UNSUPPORTED:
                return ComponentMetadataResult.Result.UNSUPPORTED
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_DENIED:
                return ComponentMetadataResult.Result.DENIED
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_FAILED:
                return ComponentMetadataResult.Result.FAILED
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_TIMEOUT:
                return ComponentMetadataResult.Result.TIMEOUT
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_NO_SYSTEM:
                return ComponentMetadataResult.Result.NO_SYSTEM
            if rpc_enum_value == component_metadata_pb2.ComponentMetadataResult.RESULT_NOT_REQUESTED:
                return ComponentMetadataResult.Result.NOT_REQUESTED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ComponentMetadataResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ComponentMetadataResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ComponentMetadataResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ComponentMetadataResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ComponentMetadataResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcComponentMetadataResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ComponentMetadataResult(
                
                ComponentMetadataResult.Result.translate_from_rpc(rpcComponentMetadataResult.result),
                
                
                rpcComponentMetadataResult.result_str
                )

    def translate_to_rpc(self, rpcComponentMetadataResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcComponentMetadataResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcComponentMetadataResult.result_str = self.result_str
            
        
        


class MetadataUpdate:
    """
     Metadata for a given component and type

     Parameters
     ----------
     compid : uint32_t
          The component ID

     type : MetadataType
          The metadata type

     json_metadata : std::string
          The JSON metadata

     """

    

    def __init__(
            self,
            compid,
            type,
            json_metadata):
        """ Initializes the MetadataUpdate object """
        self.compid = compid
        self.type = type
        self.json_metadata = json_metadata

    def __eq__(self, to_compare):
        """ Checks if two MetadataUpdate are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # MetadataUpdate object
            return \
                (self.compid == to_compare.compid) and \
                (self.type == to_compare.type) and \
                (self.json_metadata == to_compare.json_metadata)

        except AttributeError:
            return False

    def __str__(self):
        """ MetadataUpdate in string representation """
        struct_repr = ", ".join([
                "compid: " + str(self.compid),
                "type: " + str(self.type),
                "json_metadata: " + str(self.json_metadata)
                ])

        return f"MetadataUpdate: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMetadataUpdate):
        """ Translates a gRPC struct to the SDK equivalent """
        return MetadataUpdate(
                
                rpcMetadataUpdate.compid,
                
                
                MetadataType.translate_from_rpc(rpcMetadataUpdate.type),
                
                
                rpcMetadataUpdate.json_metadata
                )

    def translate_to_rpc(self, rpcMetadataUpdate):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMetadataUpdate.compid = self.compid
            
        
        
        
            
        rpcMetadataUpdate.type = self.type.translate_to_rpc()
            
        
        
        
            
        rpcMetadataUpdate.json_metadata = self.json_metadata
            
        
        



class ComponentMetadataError(Exception):
    """ Raised when a ComponentMetadataResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ComponentMetadata(AsyncBase):
    """
     Access component metadata json definitions, such as parameters.

     Generated by dcsdkgen - MAVSDK ComponentMetadata API
    """

    # Plugin name
    name = "ComponentMetadata"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = component_metadata_pb2_grpc.ComponentMetadataServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ComponentMetadataResult.translate_from_rpc(response.component_metadata_result)
    

    async def request_component(self, compid):
        """
         Request metadata from a specific component. This is used to start requesting metadata from a component.
         The metadata can later be accessed via subscription (see below) or GetMetadata.

         Parameters
         ----------
         compid : uint32_t
              The component ID to request

         
        """

        request = component_metadata_pb2.RequestComponentRequest()
        request.compid = compid
        response = await self._stub.RequestComponent(request)

        

    async def request_autopilot_component(self):
        """
         Request metadata from the autopilot component. This is used to start requesting metadata from the autopilot.
         The metadata can later be accessed via subscription (see below) or GetMetadata.

         
        """

        request = component_metadata_pb2.RequestAutopilotComponentRequest()
        response = await self._stub.RequestAutopilotComponent(request)

        

    async def metadata_available(self):
        """
         Register a callback that gets called when metadata is available

         Yields
         -------
         data : MetadataUpdate
              The metadata data

         
        """

        request = component_metadata_pb2.SubscribeMetadataAvailableRequest()
        metadata_available_stream = self._stub.SubscribeMetadataAvailable(request)

        try:
            async for response in metadata_available_stream:
                

            
                yield MetadataUpdate.translate_from_rpc(response.data)
        finally:
            metadata_available_stream.cancel()

    async def get_metadata(self, compid, metadata_type):
        """
         Access metadata. This can be used if you know the metadata is available already, otherwise use
         the subscription to get notified when it becomes available.

         Parameters
         ----------
         compid : uint32_t
              The component ID to request

         metadata_type : MetadataType
              The metadata type

         Returns
         -------
         response : MetadataData
              The response

         Raises
         ------
         ComponentMetadataError
             If the request fails. The error contains the reason for the failure.
        """

        request = component_metadata_pb2.GetMetadataRequest()
        
            
        request.compid = compid
            
        
            
                
        request.metadata_type = metadata_type.translate_to_rpc()
                
            
        response = await self._stub.GetMetadata(request)

        
        result = self._extract_result(response)

        if result.result != ComponentMetadataResult.Result.SUCCESS:
            raise ComponentMetadataError(result, "get_metadata()", compid, metadata_type)
        

        return MetadataData.translate_from_rpc(response.response)
            