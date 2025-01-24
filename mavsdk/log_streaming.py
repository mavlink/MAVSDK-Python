# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import log_streaming_pb2, log_streaming_pb2_grpc
from enum import Enum


class LogStreamingRaw:
    """
     Raw logging data type

     Parameters
     ----------
     data_base64 : std::string
          Ulog file stream data encoded as base64

     """

    

    def __init__(
            self,
            data_base64):
        """ Initializes the LogStreamingRaw object """
        self.data_base64 = data_base64

    def __eq__(self, to_compare):
        """ Checks if two LogStreamingRaw are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LogStreamingRaw object
            return \
                (self.data_base64 == to_compare.data_base64)

        except AttributeError:
            return False

    def __str__(self):
        """ LogStreamingRaw in string representation """
        struct_repr = ", ".join([
                "data_base64: " + str(self.data_base64)
                ])

        return f"LogStreamingRaw: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLogStreamingRaw):
        """ Translates a gRPC struct to the SDK equivalent """
        return LogStreamingRaw(
                
                rpcLogStreamingRaw.data_base64
                )

    def translate_to_rpc(self, rpcLogStreamingRaw):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcLogStreamingRaw.data_base64 = self.data_base64
            
        
        


class LogStreamingResult:
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
         Possible results returned for logging requests

         Values
         ------
         SUCCESS
              Request succeeded

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         BUSY
              System busy

         COMMAND_DENIED
              Command denied

         TIMEOUT
              Timeout

         UNSUPPORTED
              Unsupported

         UNKNOWN
              Unknown error

         """

        
        SUCCESS = 0
        NO_SYSTEM = 1
        CONNECTION_ERROR = 2
        BUSY = 3
        COMMAND_DENIED = 4
        TIMEOUT = 5
        UNSUPPORTED = 6
        UNKNOWN = 7

        def translate_to_rpc(self):
            if self == LogStreamingResult.Result.SUCCESS:
                return log_streaming_pb2.LogStreamingResult.RESULT_SUCCESS
            if self == LogStreamingResult.Result.NO_SYSTEM:
                return log_streaming_pb2.LogStreamingResult.RESULT_NO_SYSTEM
            if self == LogStreamingResult.Result.CONNECTION_ERROR:
                return log_streaming_pb2.LogStreamingResult.RESULT_CONNECTION_ERROR
            if self == LogStreamingResult.Result.BUSY:
                return log_streaming_pb2.LogStreamingResult.RESULT_BUSY
            if self == LogStreamingResult.Result.COMMAND_DENIED:
                return log_streaming_pb2.LogStreamingResult.RESULT_COMMAND_DENIED
            if self == LogStreamingResult.Result.TIMEOUT:
                return log_streaming_pb2.LogStreamingResult.RESULT_TIMEOUT
            if self == LogStreamingResult.Result.UNSUPPORTED:
                return log_streaming_pb2.LogStreamingResult.RESULT_UNSUPPORTED
            if self == LogStreamingResult.Result.UNKNOWN:
                return log_streaming_pb2.LogStreamingResult.RESULT_UNKNOWN

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_SUCCESS:
                return LogStreamingResult.Result.SUCCESS
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_NO_SYSTEM:
                return LogStreamingResult.Result.NO_SYSTEM
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_CONNECTION_ERROR:
                return LogStreamingResult.Result.CONNECTION_ERROR
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_BUSY:
                return LogStreamingResult.Result.BUSY
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_COMMAND_DENIED:
                return LogStreamingResult.Result.COMMAND_DENIED
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_TIMEOUT:
                return LogStreamingResult.Result.TIMEOUT
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_UNSUPPORTED:
                return LogStreamingResult.Result.UNSUPPORTED
            if rpc_enum_value == log_streaming_pb2.LogStreamingResult.RESULT_UNKNOWN:
                return LogStreamingResult.Result.UNKNOWN

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the LogStreamingResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two LogStreamingResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LogStreamingResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ LogStreamingResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"LogStreamingResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLogStreamingResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return LogStreamingResult(
                
                LogStreamingResult.Result.translate_from_rpc(rpcLogStreamingResult.result),
                
                
                rpcLogStreamingResult.result_str
                )

    def translate_to_rpc(self, rpcLogStreamingResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcLogStreamingResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcLogStreamingResult.result_str = self.result_str
            
        
        



class LogStreamingError(Exception):
    """ Raised when a LogStreamingResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class LogStreaming(AsyncBase):
    """
     Provide log streaming data.

     Generated by dcsdkgen - MAVSDK LogStreaming API
    """

    # Plugin name
    name = "LogStreaming"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = log_streaming_pb2_grpc.LogStreamingServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return LogStreamingResult.translate_from_rpc(response.log_streaming_result)
    

    async def start_log_streaming(self):
        """
         Start streaming logging data.

         Raises
         ------
         LogStreamingError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_streaming_pb2.StartLogStreamingRequest()
        response = await self._stub.StartLogStreaming(request)

        
        result = self._extract_result(response)

        if result.result != LogStreamingResult.Result.SUCCESS:
            raise LogStreamingError(result, "start_log_streaming()")
        

    async def stop_log_streaming(self):
        """
         Stop streaming logging data.

         Raises
         ------
         LogStreamingError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_streaming_pb2.StopLogStreamingRequest()
        response = await self._stub.StopLogStreaming(request)

        
        result = self._extract_result(response)

        if result.result != LogStreamingResult.Result.SUCCESS:
            raise LogStreamingError(result, "stop_log_streaming()")
        

    async def log_streaming_raw(self):
        """
         Subscribe to logging messages

         Yields
         -------
         logging_raw : LogStreamingRaw
              A message containing logged data

         
        """

        request = log_streaming_pb2.SubscribeLogStreamingRawRequest()
        log_streaming_raw_stream = self._stub.SubscribeLogStreamingRaw(request)

        try:
            async for response in log_streaming_raw_stream:
                

            
                yield LogStreamingRaw.translate_from_rpc(response.logging_raw)
        finally:
            log_streaming_raw_stream.cancel()