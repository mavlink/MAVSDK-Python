# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import rtk_pb2, rtk_pb2_grpc
from enum import Enum


class RtcmData:
    """
     RTCM data type

     Parameters
     ----------
     data_base64 : std::string
          The data encoded as a base64 string

     """

    

    def __init__(
            self,
            data_base64):
        """ Initializes the RtcmData object """
        self.data_base64 = data_base64

    def __eq__(self, to_compare):
        """ Checks if two RtcmData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # RtcmData object
            return \
                (self.data_base64 == to_compare.data_base64)

        except AttributeError:
            return False

    def __str__(self):
        """ RtcmData in string representation """
        struct_repr = ", ".join([
                "data_base64: " + str(self.data_base64)
                ])

        return f"RtcmData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcRtcmData):
        """ Translates a gRPC struct to the SDK equivalent """
        return RtcmData(
                
                rpcRtcmData.data_base64
                )

    def translate_to_rpc(self, rpcRtcmData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcRtcmData.data_base64 = self.data_base64
            
        
        


class RtkResult:
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
         Possible results returned for rtk requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         TOO_LONG
              Passed data is too long

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        TOO_LONG = 2
        NO_SYSTEM = 3
        CONNECTION_ERROR = 4

        def translate_to_rpc(self):
            if self == RtkResult.Result.UNKNOWN:
                return rtk_pb2.RtkResult.RESULT_UNKNOWN
            if self == RtkResult.Result.SUCCESS:
                return rtk_pb2.RtkResult.RESULT_SUCCESS
            if self == RtkResult.Result.TOO_LONG:
                return rtk_pb2.RtkResult.RESULT_TOO_LONG
            if self == RtkResult.Result.NO_SYSTEM:
                return rtk_pb2.RtkResult.RESULT_NO_SYSTEM
            if self == RtkResult.Result.CONNECTION_ERROR:
                return rtk_pb2.RtkResult.RESULT_CONNECTION_ERROR

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == rtk_pb2.RtkResult.RESULT_UNKNOWN:
                return RtkResult.Result.UNKNOWN
            if rpc_enum_value == rtk_pb2.RtkResult.RESULT_SUCCESS:
                return RtkResult.Result.SUCCESS
            if rpc_enum_value == rtk_pb2.RtkResult.RESULT_TOO_LONG:
                return RtkResult.Result.TOO_LONG
            if rpc_enum_value == rtk_pb2.RtkResult.RESULT_NO_SYSTEM:
                return RtkResult.Result.NO_SYSTEM
            if rpc_enum_value == rtk_pb2.RtkResult.RESULT_CONNECTION_ERROR:
                return RtkResult.Result.CONNECTION_ERROR

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the RtkResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two RtkResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # RtkResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ RtkResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"RtkResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcRtkResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return RtkResult(
                
                RtkResult.Result.translate_from_rpc(rpcRtkResult.result),
                
                
                rpcRtkResult.result_str
                )

    def translate_to_rpc(self, rpcRtkResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcRtkResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcRtkResult.result_str = self.result_str
            
        
        



class RtkError(Exception):
    """ Raised when a RtkResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Rtk(AsyncBase):
    """
     Service to send RTK corrections to the vehicle.

     Generated by dcsdkgen - MAVSDK Rtk API
    """

    # Plugin name
    name = "Rtk"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = rtk_pb2_grpc.RtkServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return RtkResult.translate_from_rpc(response.rtk_result)
    

    async def send_rtcm_data(self, rtcm_data):
        """
         Send RTCM data.

         Parameters
         ----------
         rtcm_data : RtcmData
              The data

         Raises
         ------
         RtkError
             If the request fails. The error contains the reason for the failure.
        """

        request = rtk_pb2.SendRtcmDataRequest()
        
        rtcm_data.translate_to_rpc(request.rtcm_data)
                
            
        response = await self._stub.SendRtcmData(request)

        
        result = self._extract_result(response)

        if result.result != RtkResult.Result.SUCCESS:
            raise RtkError(result, "send_rtcm_data()", rtcm_data)
        