# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import arm_authorizer_server_pb2, arm_authorizer_server_pb2_grpc
from enum import Enum


class RejectionReason(Enum):
    """
     The rejection reason

     Values
     ------
     GENERIC
          Not a specific reason

     NONE
          Authorizer will send the error as string to GCS

     INVALID_WAYPOINT
          At least one waypoint have a invalid value

     TIMEOUT
          Timeout in the authorizer process(in case it depends on network)

     AIRSPACE_IN_USE
          Airspace of the mission in use by another vehicle, second result parameter can have the waypoint id that caused it to be denied.

     BAD_WEATHER
          Weather is not good to fly

     """

    
    GENERIC = 0
    NONE = 1
    INVALID_WAYPOINT = 2
    TIMEOUT = 3
    AIRSPACE_IN_USE = 4
    BAD_WEATHER = 5

    def translate_to_rpc(self):
        if self == RejectionReason.GENERIC:
            return arm_authorizer_server_pb2.REJECTION_REASON_GENERIC
        if self == RejectionReason.NONE:
            return arm_authorizer_server_pb2.REJECTION_REASON_NONE
        if self == RejectionReason.INVALID_WAYPOINT:
            return arm_authorizer_server_pb2.REJECTION_REASON_INVALID_WAYPOINT
        if self == RejectionReason.TIMEOUT:
            return arm_authorizer_server_pb2.REJECTION_REASON_TIMEOUT
        if self == RejectionReason.AIRSPACE_IN_USE:
            return arm_authorizer_server_pb2.REJECTION_REASON_AIRSPACE_IN_USE
        if self == RejectionReason.BAD_WEATHER:
            return arm_authorizer_server_pb2.REJECTION_REASON_BAD_WEATHER

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_GENERIC:
            return RejectionReason.GENERIC
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_NONE:
            return RejectionReason.NONE
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_INVALID_WAYPOINT:
            return RejectionReason.INVALID_WAYPOINT
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_TIMEOUT:
            return RejectionReason.TIMEOUT
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_AIRSPACE_IN_USE:
            return RejectionReason.AIRSPACE_IN_USE
        if rpc_enum_value == arm_authorizer_server_pb2.REJECTION_REASON_BAD_WEATHER:
            return RejectionReason.BAD_WEATHER

    def __str__(self):
        return self.name


class ArmAuthorizerServerResult:
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
         The result

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Command accepted

         FAILED
              Command failed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        FAILED = 2

        def translate_to_rpc(self):
            if self == ArmAuthorizerServerResult.Result.UNKNOWN:
                return arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_UNKNOWN
            if self == ArmAuthorizerServerResult.Result.SUCCESS:
                return arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_SUCCESS
            if self == ArmAuthorizerServerResult.Result.FAILED:
                return arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_UNKNOWN:
                return ArmAuthorizerServerResult.Result.UNKNOWN
            if rpc_enum_value == arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_SUCCESS:
                return ArmAuthorizerServerResult.Result.SUCCESS
            if rpc_enum_value == arm_authorizer_server_pb2.ArmAuthorizerServerResult.RESULT_FAILED:
                return ArmAuthorizerServerResult.Result.FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ArmAuthorizerServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ArmAuthorizerServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ArmAuthorizerServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ArmAuthorizerServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ArmAuthorizerServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcArmAuthorizerServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ArmAuthorizerServerResult(
                
                ArmAuthorizerServerResult.Result.translate_from_rpc(rpcArmAuthorizerServerResult.result),
                
                
                rpcArmAuthorizerServerResult.result_str
                )

    def translate_to_rpc(self, rpcArmAuthorizerServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcArmAuthorizerServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcArmAuthorizerServerResult.result_str = self.result_str
            
        
        



class ArmAuthorizerServerError(Exception):
    """ Raised when a ArmAuthorizerServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ArmAuthorizerServer(AsyncBase):
    """
     Use arm authorization.

     Generated by dcsdkgen - MAVSDK ArmAuthorizerServer API
    """

    # Plugin name
    name = "ArmAuthorizerServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = arm_authorizer_server_pb2_grpc.ArmAuthorizerServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ArmAuthorizerServerResult.translate_from_rpc(response.arm_authorizer_server_result)
    

    async def arm_authorization(self):
        """
         Subscribe to arm authorization request messages. Each request received should respond to using RespondArmAuthorization

         Yields
         -------
         system_id : uint32_t
              vehicle system id

         
        """

        request = arm_authorizer_server_pb2.SubscribeArmAuthorizationRequest()
        arm_authorization_stream = self._stub.SubscribeArmAuthorization(request)

        try:
            async for response in arm_authorization_stream:
                

            
                yield response.system_id
        finally:
            arm_authorization_stream.cancel()

    async def accept_arm_authorization(self, valid_time_s):
        """
         Authorize arm for the specific time

         Parameters
         ----------
         valid_time_s : int32_t
              Time in seconds for which this authorization is valid

         Raises
         ------
         ArmAuthorizerServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = arm_authorizer_server_pb2.AcceptArmAuthorizationRequest()
        request.valid_time_s = valid_time_s
        response = await self._stub.AcceptArmAuthorization(request)

        
        result = self._extract_result(response)

        if result.result != ArmAuthorizerServerResult.Result.SUCCESS:
            raise ArmAuthorizerServerError(result, "accept_arm_authorization()", valid_time_s)
        

    async def reject_arm_authorization(self, temporarily, reason, extra_info):
        """
         Reject arm authorization request

         Parameters
         ----------
         temporarily : bool
              True if the answer should be TEMPORARILY_REJECTED, false for DENIED

         reason : RejectionReason
              Reason for the arm to be rejected

         extra_info : int32_t
              Extra information specific to the rejection reason (see https://mavlink.io/en/services/arm_authorization.html)

         Raises
         ------
         ArmAuthorizerServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = arm_authorizer_server_pb2.RejectArmAuthorizationRequest()
        request.temporarily = temporarily
        
        request.reason = reason.translate_to_rpc()
                
            
        request.extra_info = extra_info
        response = await self._stub.RejectArmAuthorization(request)

        
        result = self._extract_result(response)

        if result.result != ArmAuthorizerServerResult.Result.SUCCESS:
            raise ArmAuthorizerServerError(result, "reject_arm_authorization()", temporarily, reason, extra_info)
        