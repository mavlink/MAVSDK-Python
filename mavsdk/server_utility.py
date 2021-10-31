# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import server_utility_pb2, server_utility_pb2_grpc
from enum import Enum


class StatusTextType(Enum):
    """
     Status types.

     Values
     ------
     DEBUG
          Debug

     INFO
          Information

     NOTICE
          Notice

     WARNING
          Warning

     ERROR
          Error

     CRITICAL
          Critical

     ALERT
          Alert

     EMERGENCY
          Emergency

     """

    
    DEBUG = 0
    INFO = 1
    NOTICE = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5
    ALERT = 6
    EMERGENCY = 7

    def translate_to_rpc(self):
        if self == StatusTextType.DEBUG:
            return server_utility_pb2.STATUS_TEXT_TYPE_DEBUG
        if self == StatusTextType.INFO:
            return server_utility_pb2.STATUS_TEXT_TYPE_INFO
        if self == StatusTextType.NOTICE:
            return server_utility_pb2.STATUS_TEXT_TYPE_NOTICE
        if self == StatusTextType.WARNING:
            return server_utility_pb2.STATUS_TEXT_TYPE_WARNING
        if self == StatusTextType.ERROR:
            return server_utility_pb2.STATUS_TEXT_TYPE_ERROR
        if self == StatusTextType.CRITICAL:
            return server_utility_pb2.STATUS_TEXT_TYPE_CRITICAL
        if self == StatusTextType.ALERT:
            return server_utility_pb2.STATUS_TEXT_TYPE_ALERT
        if self == StatusTextType.EMERGENCY:
            return server_utility_pb2.STATUS_TEXT_TYPE_EMERGENCY

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_DEBUG:
            return StatusTextType.DEBUG
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_INFO:
            return StatusTextType.INFO
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_NOTICE:
            return StatusTextType.NOTICE
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_WARNING:
            return StatusTextType.WARNING
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_ERROR:
            return StatusTextType.ERROR
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_CRITICAL:
            return StatusTextType.CRITICAL
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_ALERT:
            return StatusTextType.ALERT
        if rpc_enum_value == server_utility_pb2.STATUS_TEXT_TYPE_EMERGENCY:
            return StatusTextType.EMERGENCY

    def __str__(self):
        return self.name


class ServerUtilityResult:
    """
 

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for server utility requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         INVALID_ARGUMENT
              Invalid argument

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        INVALID_ARGUMENT = 4

        def translate_to_rpc(self):
            if self == ServerUtilityResult.Result.UNKNOWN:
                return server_utility_pb2.ServerUtilityResult.RESULT_UNKNOWN
            if self == ServerUtilityResult.Result.SUCCESS:
                return server_utility_pb2.ServerUtilityResult.RESULT_SUCCESS
            if self == ServerUtilityResult.Result.NO_SYSTEM:
                return server_utility_pb2.ServerUtilityResult.RESULT_NO_SYSTEM
            if self == ServerUtilityResult.Result.CONNECTION_ERROR:
                return server_utility_pb2.ServerUtilityResult.RESULT_CONNECTION_ERROR
            if self == ServerUtilityResult.Result.INVALID_ARGUMENT:
                return server_utility_pb2.ServerUtilityResult.RESULT_INVALID_ARGUMENT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == server_utility_pb2.ServerUtilityResult.RESULT_UNKNOWN:
                return ServerUtilityResult.Result.UNKNOWN
            if rpc_enum_value == server_utility_pb2.ServerUtilityResult.RESULT_SUCCESS:
                return ServerUtilityResult.Result.SUCCESS
            if rpc_enum_value == server_utility_pb2.ServerUtilityResult.RESULT_NO_SYSTEM:
                return ServerUtilityResult.Result.NO_SYSTEM
            if rpc_enum_value == server_utility_pb2.ServerUtilityResult.RESULT_CONNECTION_ERROR:
                return ServerUtilityResult.Result.CONNECTION_ERROR
            if rpc_enum_value == server_utility_pb2.ServerUtilityResult.RESULT_INVALID_ARGUMENT:
                return ServerUtilityResult.Result.INVALID_ARGUMENT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ServerUtilityResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ServerUtilityResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ServerUtilityResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ServerUtilityResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ServerUtilityResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcServerUtilityResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ServerUtilityResult(
                
                ServerUtilityResult.Result.translate_from_rpc(rpcServerUtilityResult.result),
                
                
                rpcServerUtilityResult.result_str
                )

    def translate_to_rpc(self, rpcServerUtilityResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcServerUtilityResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcServerUtilityResult.result_str = self.result_str
            
        
        



class ServerUtilityError(Exception):
    """ Raised when a ServerUtilityResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ServerUtility(AsyncBase):
    """
     Utility for onboard MAVSDK instances for common "server" tasks.

     Generated by dcsdkgen - MAVSDK ServerUtility API
    """

    # Plugin name
    name = "ServerUtility"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = server_utility_pb2_grpc.ServerUtilityServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ServerUtilityResult.translate_from_rpc(response.server_utility_result)
    

    async def send_status_text(self, type, text):
        """
         Sends a statustext.

         Parameters
         ----------
         type : StatusTextType
              The text to send

         text : std::string
              Text message

         Raises
         ------
         ServerUtilityError
             If the request fails. The error contains the reason for the failure.
        """

        request = server_utility_pb2.SendStatusTextRequest()
        
        request.type = type.translate_to_rpc()
                
            
        request.text = text
        response = await self._stub.SendStatusText(request)

        
        result = self._extract_result(response)

        if result.result != ServerUtilityResult.Result.SUCCESS:
            raise ServerUtilityError(result, "send_status_text()", type, text)
        