# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import gripper_pb2, gripper_pb2_grpc
from enum import Enum


class GripperAction(Enum):
    """
     Gripper Actions.

     Available gripper actions are defined in mavlink under
     https://mavlink.io/en/messages/common.html#GRIPPER_ACTIONS

     Values
     ------
     RELEASE
          Open the gripper to release the cargo

     GRAB
          Close the gripper and grab onto cargo

     """

    
    RELEASE = 0
    GRAB = 1

    def translate_to_rpc(self):
        if self == GripperAction.RELEASE:
            return gripper_pb2.GRIPPER_ACTION_RELEASE
        if self == GripperAction.GRAB:
            return gripper_pb2.GRIPPER_ACTION_GRAB

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == gripper_pb2.GRIPPER_ACTION_RELEASE:
            return GripperAction.RELEASE
        if rpc_enum_value == gripper_pb2.GRIPPER_ACTION_GRAB:
            return GripperAction.GRAB

    def __str__(self):
        return self.name


class GripperResult:
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
         Possible results returned for gripper action requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request was successful

         NO_SYSTEM
              No system is connected

         BUSY
              Temporarily rejected

         TIMEOUT
              Request timed out

         UNSUPPORTED
              Action not supported

         FAILED
              Action failed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        BUSY = 3
        TIMEOUT = 4
        UNSUPPORTED = 5
        FAILED = 6

        def translate_to_rpc(self):
            if self == GripperResult.Result.UNKNOWN:
                return gripper_pb2.GripperResult.RESULT_UNKNOWN
            if self == GripperResult.Result.SUCCESS:
                return gripper_pb2.GripperResult.RESULT_SUCCESS
            if self == GripperResult.Result.NO_SYSTEM:
                return gripper_pb2.GripperResult.RESULT_NO_SYSTEM
            if self == GripperResult.Result.BUSY:
                return gripper_pb2.GripperResult.RESULT_BUSY
            if self == GripperResult.Result.TIMEOUT:
                return gripper_pb2.GripperResult.RESULT_TIMEOUT
            if self == GripperResult.Result.UNSUPPORTED:
                return gripper_pb2.GripperResult.RESULT_UNSUPPORTED
            if self == GripperResult.Result.FAILED:
                return gripper_pb2.GripperResult.RESULT_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_UNKNOWN:
                return GripperResult.Result.UNKNOWN
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_SUCCESS:
                return GripperResult.Result.SUCCESS
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_NO_SYSTEM:
                return GripperResult.Result.NO_SYSTEM
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_BUSY:
                return GripperResult.Result.BUSY
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_TIMEOUT:
                return GripperResult.Result.TIMEOUT
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_UNSUPPORTED:
                return GripperResult.Result.UNSUPPORTED
            if rpc_enum_value == gripper_pb2.GripperResult.RESULT_FAILED:
                return GripperResult.Result.FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the GripperResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two GripperResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GripperResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ GripperResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"GripperResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGripperResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return GripperResult(
                
                GripperResult.Result.translate_from_rpc(rpcGripperResult.result),
                
                
                rpcGripperResult.result_str
                )

    def translate_to_rpc(self, rpcGripperResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcGripperResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcGripperResult.result_str = self.result_str
            
        
        



class GripperError(Exception):
    """ Raised when a GripperResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Gripper(AsyncBase):
    """
     Allows users to send gripper actions.

     Generated by dcsdkgen - MAVSDK Gripper API
    """

    # Plugin name
    name = "Gripper"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = gripper_pb2_grpc.GripperServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return GripperResult.translate_from_rpc(response.gripper_result)
    

    async def grab(self, instance):
        """
         Gripper grab cargo.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         GripperError
             If the request fails. The error contains the reason for the failure.
        """

        request = gripper_pb2.GrabRequest()
        request.instance = instance
        response = await self._stub.Grab(request)

        
        result = self._extract_result(response)

        if result.result != GripperResult.Result.SUCCESS:
            raise GripperError(result, "grab()", instance)
        

    async def release(self, instance):
        """
         Gripper release cargo.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         GripperError
             If the request fails. The error contains the reason for the failure.
        """

        request = gripper_pb2.ReleaseRequest()
        request.instance = instance
        response = await self._stub.Release(request)

        
        result = self._extract_result(response)

        if result.result != GripperResult.Result.SUCCESS:
            raise GripperError(result, "release()", instance)
        