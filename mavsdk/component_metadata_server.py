# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import component_metadata_server_pb2, component_metadata_server_pb2_grpc
from enum import Enum


class MetadataType(Enum):
    """
 

     Values
     ------
     PARAMETER
          Parameter metadata

     EVENTS
          Event definitions

     ACTUATORS
          Actuator definitions

     """

    
    PARAMETER = 0
    EVENTS = 1
    ACTUATORS = 2

    def translate_to_rpc(self):
        if self == MetadataType.PARAMETER:
            return component_metadata_server_pb2.METADATA_TYPE_PARAMETER
        if self == MetadataType.EVENTS:
            return component_metadata_server_pb2.METADATA_TYPE_EVENTS
        if self == MetadataType.ACTUATORS:
            return component_metadata_server_pb2.METADATA_TYPE_ACTUATORS

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == component_metadata_server_pb2.METADATA_TYPE_PARAMETER:
            return MetadataType.PARAMETER
        if rpc_enum_value == component_metadata_server_pb2.METADATA_TYPE_EVENTS:
            return MetadataType.EVENTS
        if rpc_enum_value == component_metadata_server_pb2.METADATA_TYPE_ACTUATORS:
            return MetadataType.ACTUATORS

    def __str__(self):
        return self.name


class Metadata:
    """
 

     Parameters
     ----------
     type : MetadataType
          The metadata type

     json_metadata : std::string
          The JSON metadata

     """

    

    def __init__(
            self,
            type,
            json_metadata):
        """ Initializes the Metadata object """
        self.type = type
        self.json_metadata = json_metadata

    def __eq__(self, to_compare):
        """ Checks if two Metadata are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Metadata object
            return \
                (self.type == to_compare.type) and \
                (self.json_metadata == to_compare.json_metadata)

        except AttributeError:
            return False

    def __str__(self):
        """ Metadata in string representation """
        struct_repr = ", ".join([
                "type: " + str(self.type),
                "json_metadata: " + str(self.json_metadata)
                ])

        return f"Metadata: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcMetadata):
        """ Translates a gRPC struct to the SDK equivalent """
        return Metadata(
                
                MetadataType.translate_from_rpc(rpcMetadata.type),
                
                
                rpcMetadata.json_metadata
                )

    def translate_to_rpc(self, rpcMetadata):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcMetadata.type = self.type.translate_to_rpc()
            
        
        
        
            
        rpcMetadata.json_metadata = self.json_metadata
            
        
        




class ComponentMetadataServer(AsyncBase):
    """
     Provide component metadata json definitions, such as parameters.

     Generated by dcsdkgen - MAVSDK ComponentMetadataServer API
    """

    # Plugin name
    name = "ComponentMetadataServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = component_metadata_server_pb2_grpc.ComponentMetadataServerServiceStub(channel)

    

    async def set_metadata(self, metadata):
        """
         Provide metadata (can only be called once)

         Parameters
         ----------
         metadata : [Metadata]
              List of metadata

         
        """

        request = component_metadata_server_pb2.SetMetadataRequest()
        
        rpc_elems_list = []
        for elem in metadata:
                    
            rpc_elem = component_metadata_server_pb2.Metadata()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                    
        request.metadata.extend(rpc_elems_list)
                
            
        response = await self._stub.SetMetadata(request)

        