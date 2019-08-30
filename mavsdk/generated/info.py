# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import info_pb2, info_pb2_grpc
from enum import Enum


class Version:
    """
     System version information.

     Parameters
     ----------
     flight_sw_major : int32_t
          Flight software major version

     flight_sw_minor : int32_t
          Flight software minor version

     flight_sw_patch : int32_t
          Flight software patch version

     flight_sw_vendor_major : int32_t
          Flight software vendor major version

     flight_sw_vendor_minor : int32_t
          Flight software vendor minor version

     flight_sw_vendor_patch : int32_t
          Flight software vendor patch version

     os_sw_major : int32_t
          Operating system software major version

     os_sw_minor : int32_t
          Operating system software minor version

     os_sw_patch : int32_t
          Operating system software patch version

     """

    

    def __init__(
            self,
            flight_sw_major,
            flight_sw_minor,
            flight_sw_patch,
            flight_sw_vendor_major,
            flight_sw_vendor_minor,
            flight_sw_vendor_patch,
            os_sw_major,
            os_sw_minor,
            os_sw_patch):
        """ Initializes the Version object """
        self.flight_sw_major = flight_sw_major
        self.flight_sw_minor = flight_sw_minor
        self.flight_sw_patch = flight_sw_patch
        self.flight_sw_vendor_major = flight_sw_vendor_major
        self.flight_sw_vendor_minor = flight_sw_vendor_minor
        self.flight_sw_vendor_patch = flight_sw_vendor_patch
        self.os_sw_major = os_sw_major
        self.os_sw_minor = os_sw_minor
        self.os_sw_patch = os_sw_patch

    def __equals__(self, to_compare):
        """ Checks if two Version are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Version object
            return \
                (self.flight_sw_major == to_compare.flight_sw_major) and \
                (self.flight_sw_minor == to_compare.flight_sw_minor) and \
                (self.flight_sw_patch == to_compare.flight_sw_patch) and \
                (self.flight_sw_vendor_major == to_compare.flight_sw_vendor_major) and \
                (self.flight_sw_vendor_minor == to_compare.flight_sw_vendor_minor) and \
                (self.flight_sw_vendor_patch == to_compare.flight_sw_vendor_patch) and \
                (self.os_sw_major == to_compare.os_sw_major) and \
                (self.os_sw_minor == to_compare.os_sw_minor) and \
                (self.os_sw_patch == to_compare.os_sw_patch)

        except AttributeError:
            return False

    def __str__(self):
        """ Version in string representation """
        struct_repr = ", ".join([
                "flight_sw_major: " + str(self.flight_sw_major),
                "flight_sw_minor: " + str(self.flight_sw_minor),
                "flight_sw_patch: " + str(self.flight_sw_patch),
                "flight_sw_vendor_major: " + str(self.flight_sw_vendor_major),
                "flight_sw_vendor_minor: " + str(self.flight_sw_vendor_minor),
                "flight_sw_vendor_patch: " + str(self.flight_sw_vendor_patch),
                "os_sw_major: " + str(self.os_sw_major),
                "os_sw_minor: " + str(self.os_sw_minor),
                "os_sw_patch: " + str(self.os_sw_patch)
                ])

        return f"Version: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVersion):
        """ Translates a gRPC struct to the SDK equivalent """
        return Version(
                
                rpcVersion.flight_sw_major,
                
                
                rpcVersion.flight_sw_minor,
                
                
                rpcVersion.flight_sw_patch,
                
                
                rpcVersion.flight_sw_vendor_major,
                
                
                rpcVersion.flight_sw_vendor_minor,
                
                
                rpcVersion.flight_sw_vendor_patch,
                
                
                rpcVersion.os_sw_major,
                
                
                rpcVersion.os_sw_minor,
                
                
                rpcVersion.os_sw_patch
                )

    def translate_to_rpc(self, rpcVersion):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVersion.flight_sw_major = self.flight_sw_major
            
        
        
        
            
        rpcVersion.flight_sw_minor = self.flight_sw_minor
            
        
        
        
            
        rpcVersion.flight_sw_patch = self.flight_sw_patch
            
        
        
        
            
        rpcVersion.flight_sw_vendor_major = self.flight_sw_vendor_major
            
        
        
        
            
        rpcVersion.flight_sw_vendor_minor = self.flight_sw_vendor_minor
            
        
        
        
            
        rpcVersion.flight_sw_vendor_patch = self.flight_sw_vendor_patch
            
        
        
        
            
        rpcVersion.os_sw_major = self.os_sw_major
            
        
        
        
            
        rpcVersion.os_sw_minor = self.os_sw_minor
            
        
        
        
            
        rpcVersion.os_sw_patch = self.os_sw_patch
            
        
        


class InfoResult:
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
         Possible results returned for info requests.

         Values
         ------
         UNKNOWN
              Unknown error

         SUCCESS
              Request succeeded

         INFORMATION_NOT_RECEIVED_YET
              Information has not been received yet

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        INFORMATION_NOT_RECEIVED_YET = 2

        def translate_to_rpc(self, rpcResult):
            return {
                    0: info_pb2.InfoResult.UNKNOWN,
                    1: info_pb2.InfoResult.SUCCESS,
                    2: info_pb2.InfoResult.INFORMATION_NOT_RECEIVED_YET
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: InfoResult.Result.UNKNOWN,
                    1: InfoResult.Result.SUCCESS,
                    2: InfoResult.Result.INFORMATION_NOT_RECEIVED_YET,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the InfoResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two InfoResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # InfoResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ InfoResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"InfoResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcInfoResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return InfoResult(
                
                InfoResult.Result.translate_from_rpc(rpcInfoResult.result),
                
                
                rpcInfoResult.result_str
                )

    def translate_to_rpc(self, rpcInfoResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.result.translate_to_rpc(rpcInfoResult.result)
            
        
        
        
            
        rpcInfoResult.result_str = self.result_str
            
        
        



class InfoError(Exception):
    """ Raised when a InfoResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Info(AsyncBase):
    """
     Provide infomation about the hardware and/or software of a system.

     Generated by dcsdkgen - MAVSDK Info API
    """

    # Plugin name
    name = "Info"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = info_pb2_grpc.InfoServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return InfoResult.translate_from_rpc(response.info_result)
    

    async def get_version(self):
        """
         Get the system version information.

         Returns
         -------
         version : Version
              Version information about the system

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetVersionRequest()
        response = await self._stub.GetVersion(request)

        
        result = self._extract_result(response)

        if result.result is not InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_version()")
        

        return Version.translate_from_rpc(response.version)
        