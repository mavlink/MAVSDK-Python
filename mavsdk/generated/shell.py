# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import shell_pb2, shell_pb2_grpc
from enum import Enum


class ShellMessage:
    """
 

     Parameters
     ----------
     need_response : bool
          Set if the sender wants the receiver to send a response.

     timeout_ms : uint32_t
          Timeout (ms).

     data : std::string
          Serial data.

     """

    

    def __init__(
            self,
            need_response,
            timeout_ms,
            data):
        """ Initializes the ShellMessage object """
        self.need_response = need_response
        self.timeout_ms = timeout_ms
        self.data = data

    def __equals__(self, to_compare):
        """ Checks if two ShellMessage are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ShellMessage object
            return \
                (self.need_response == to_compare.need_response) and \
                (self.timeout_ms == to_compare.timeout_ms) and \
                (self.data == to_compare.data)

        except AttributeError:
            return False

    def __str__(self):
        """ ShellMessage in string representation """
        struct_repr = ", ".join([
                "need_response: " + str(self.need_response),
                "timeout_ms: " + str(self.timeout_ms),
                "data: " + str(self.data)
                ])

        return f"ShellMessage: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcShellMessage):
        """ Translates a gRPC struct to the SDK equivalent """
        return ShellMessage(
                
                rpcShellMessage.need_response,
                
                
                rpcShellMessage.timeout_ms,
                
                
                rpcShellMessage.data
                )

    def translate_to_rpc(self, rpcShellMessage):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcShellMessage.need_response = self.need_response
            
        
        
        
            
        rpcShellMessage.timeout_ms = self.timeout_ms
            
        
        
        
            
        rpcShellMessage.data = self.data
            
        
        


class ShellResult:
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
         Possible results returned for shell requests

         Values
         ------
         UNKNOWN
              Unknown error

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

        def translate_to_rpc(self, rpcResult):
            return {
                    0: shell_pb2.ShellResult.UNKNOWN,
                    1: shell_pb2.ShellResult.SUCCESS,
                    2: shell_pb2.ShellResult.NO_SYSTEM,
                    3: shell_pb2.ShellResult.CONNECTION_ERROR,
                    4: shell_pb2.ShellResult.NO_RESPONSE,
                    5: shell_pb2.ShellResult.BUSY
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: ShellResult.Result.UNKNOWN,
                    1: ShellResult.Result.SUCCESS,
                    2: ShellResult.Result.NO_SYSTEM,
                    3: ShellResult.Result.CONNECTION_ERROR,
                    4: ShellResult.Result.NO_RESPONSE,
                    5: ShellResult.Result.BUSY,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ShellResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
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

        
        
            
        self.result.translate_to_rpc(rpcShellResult.result)
            
        
        
        
            
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
     *
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
    

    async def send(self, shell_message):
        """
         Communicate with a vehicle's Shell.

         Parameters
         ----------
         shell_message : ShellMessage
             
         Returns
         -------
         response_message_data : std::string
              Response message data (if available)

         Raises
         ------
         ShellError
             If the request fails. The error contains the reason for the failure.
        """

        request = shell_pb2.SendRequest()
        
            
                
        shell_message.translate_to_rpc(request.shell_message)
                
            
        response = await self._stub.Send(request)

        
        result = self._extract_result(response)

        if result.result is not ShellResult.Result.SUCCESS:
            raise ShellError(result, "send()", shell_message)
        

        return response.response_message_data
        