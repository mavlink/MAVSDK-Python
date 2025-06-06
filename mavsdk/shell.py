# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import shell_pb2, shell_pb2_grpc
from enum import Enum


class ShellResult:
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
         Possible results returned for shell requests

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

         NO_RESPONSE
              Response was not received

         BUSY
              Shell busy (transfer in progress)

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        NO_RESPONSE = 4
        BUSY = 5

        def translate_to_rpc(self):
            if self == ShellResult.Result.UNKNOWN:
                return shell_pb2.ShellResult.RESULT_UNKNOWN
            if self == ShellResult.Result.SUCCESS:
                return shell_pb2.ShellResult.RESULT_SUCCESS
            if self == ShellResult.Result.NO_SYSTEM:
                return shell_pb2.ShellResult.RESULT_NO_SYSTEM
            if self == ShellResult.Result.CONNECTION_ERROR:
                return shell_pb2.ShellResult.RESULT_CONNECTION_ERROR
            if self == ShellResult.Result.NO_RESPONSE:
                return shell_pb2.ShellResult.RESULT_NO_RESPONSE
            if self == ShellResult.Result.BUSY:
                return shell_pb2.ShellResult.RESULT_BUSY

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_UNKNOWN:
                return ShellResult.Result.UNKNOWN
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_SUCCESS:
                return ShellResult.Result.SUCCESS
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_NO_SYSTEM:
                return ShellResult.Result.NO_SYSTEM
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_CONNECTION_ERROR:
                return ShellResult.Result.CONNECTION_ERROR
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_NO_RESPONSE:
                return ShellResult.Result.NO_RESPONSE
            if rpc_enum_value == shell_pb2.ShellResult.RESULT_BUSY:
                return ShellResult.Result.BUSY

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ShellResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ShellResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ShellResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ShellResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ShellResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcShellResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ShellResult(
                
                ShellResult.Result.translate_from_rpc(rpcShellResult.result),
                
                
                rpcShellResult.result_str
                )

    def translate_to_rpc(self, rpcShellResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcShellResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcShellResult.result_str = self.result_str
            
        
        



class ShellError(Exception):
    """ Raised when a ShellResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Shell(AsyncBase):
    """
     Allow to communicate with the vehicle's system shell.

     Generated by dcsdkgen - MAVSDK Shell API
    """

    # Plugin name
    name = "Shell"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = shell_pb2_grpc.ShellServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ShellResult.translate_from_rpc(response.shell_result)
    

    async def send(self, command):
        """
         Send a command line.

         Parameters
         ----------
         command : std::string
              The command line to send

         Raises
         ------
         ShellError
             If the request fails. The error contains the reason for the failure.
        """

        request = shell_pb2.SendRequest()
        request.command = command
        response = await self._stub.Send(request)

        
        result = self._extract_result(response)

        if result.result != ShellResult.Result.SUCCESS:
            raise ShellError(result, "send()", command)
        

    async def receive(self):
        """
         Receive feedback from a sent command line.

         This subscription needs to be made before a command line is sent, otherwise, no response will be sent.

         Yields
         -------
         data : std::string
              Received data.

         
        """

        request = shell_pb2.SubscribeReceiveRequest()
        receive_stream = self._stub.SubscribeReceive(request)

        try:
            async for response in receive_stream:
                

            
                yield response.data
        finally:
            receive_stream.cancel()