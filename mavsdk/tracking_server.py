# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import tracking_server_pb2, tracking_server_pb2_grpc
from enum import Enum


class CommandAnswer(Enum):
    """
     Answer to respond to an incoming command

     Values
     ------
     ACCEPTED
          Command accepted

     TEMPORARILY_REJECTED
          Command temporarily rejected

     DENIED
          Command denied

     UNSUPPORTED
          Command unsupported

     FAILED
          Command failed

     """

    
    ACCEPTED = 0
    TEMPORARILY_REJECTED = 1
    DENIED = 2
    UNSUPPORTED = 3
    FAILED = 4

    def translate_to_rpc(self):
        if self == CommandAnswer.ACCEPTED:
            return tracking_server_pb2.COMMAND_ANSWER_ACCEPTED
        if self == CommandAnswer.TEMPORARILY_REJECTED:
            return tracking_server_pb2.COMMAND_ANSWER_TEMPORARILY_REJECTED
        if self == CommandAnswer.DENIED:
            return tracking_server_pb2.COMMAND_ANSWER_DENIED
        if self == CommandAnswer.UNSUPPORTED:
            return tracking_server_pb2.COMMAND_ANSWER_UNSUPPORTED
        if self == CommandAnswer.FAILED:
            return tracking_server_pb2.COMMAND_ANSWER_FAILED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == tracking_server_pb2.COMMAND_ANSWER_ACCEPTED:
            return CommandAnswer.ACCEPTED
        if rpc_enum_value == tracking_server_pb2.COMMAND_ANSWER_TEMPORARILY_REJECTED:
            return CommandAnswer.TEMPORARILY_REJECTED
        if rpc_enum_value == tracking_server_pb2.COMMAND_ANSWER_DENIED:
            return CommandAnswer.DENIED
        if rpc_enum_value == tracking_server_pb2.COMMAND_ANSWER_UNSUPPORTED:
            return CommandAnswer.UNSUPPORTED
        if rpc_enum_value == tracking_server_pb2.COMMAND_ANSWER_FAILED:
            return CommandAnswer.FAILED

    def __str__(self):
        return self.name


class TrackPoint:
    """
     Point description type

     Parameters
     ----------
     point_x : float
          Point to track x value (normalized 0..1, 0 is left, 1 is right).

     point_y : float
          Point to track y value (normalized 0..1, 0 is top, 1 is bottom).

     radius : float
          Point to track y value (normalized 0..1, 0 is top, 1 is bottom).

     """

    

    def __init__(
            self,
            point_x,
            point_y,
            radius):
        """ Initializes the TrackPoint object """
        self.point_x = point_x
        self.point_y = point_y
        self.radius = radius

    def __eq__(self, to_compare):
        """ Checks if two TrackPoint are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TrackPoint object
            return \
                (self.point_x == to_compare.point_x) and \
                (self.point_y == to_compare.point_y) and \
                (self.radius == to_compare.radius)

        except AttributeError:
            return False

    def __str__(self):
        """ TrackPoint in string representation """
        struct_repr = ", ".join([
                "point_x: " + str(self.point_x),
                "point_y: " + str(self.point_y),
                "radius: " + str(self.radius)
                ])

        return f"TrackPoint: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTrackPoint):
        """ Translates a gRPC struct to the SDK equivalent """
        return TrackPoint(
                
                rpcTrackPoint.point_x,
                
                
                rpcTrackPoint.point_y,
                
                
                rpcTrackPoint.radius
                )

    def translate_to_rpc(self, rpcTrackPoint):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTrackPoint.point_x = self.point_x
            
        
        
        
            
        rpcTrackPoint.point_y = self.point_y
            
        
        
        
            
        rpcTrackPoint.radius = self.radius
            
        
        


class TrackRectangle:
    """
     Rectangle description type

     Parameters
     ----------
     top_left_corner_x : float
          Top left corner of rectangle x value (normalized 0..1, 0 is left, 1 is right).

     top_left_corner_y : float
          Top left corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom).

     bottom_right_corner_x : float
          Bottom right corner of rectangle x value (normalized 0..1, 0 is left, 1 is right).

     bottom_right_corner_y : float
          Bottom right corner of rectangle y value (normalized 0..1, 0 is top, 1 is bottom).

     """

    

    def __init__(
            self,
            top_left_corner_x,
            top_left_corner_y,
            bottom_right_corner_x,
            bottom_right_corner_y):
        """ Initializes the TrackRectangle object """
        self.top_left_corner_x = top_left_corner_x
        self.top_left_corner_y = top_left_corner_y
        self.bottom_right_corner_x = bottom_right_corner_x
        self.bottom_right_corner_y = bottom_right_corner_y

    def __eq__(self, to_compare):
        """ Checks if two TrackRectangle are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TrackRectangle object
            return \
                (self.top_left_corner_x == to_compare.top_left_corner_x) and \
                (self.top_left_corner_y == to_compare.top_left_corner_y) and \
                (self.bottom_right_corner_x == to_compare.bottom_right_corner_x) and \
                (self.bottom_right_corner_y == to_compare.bottom_right_corner_y)

        except AttributeError:
            return False

    def __str__(self):
        """ TrackRectangle in string representation """
        struct_repr = ", ".join([
                "top_left_corner_x: " + str(self.top_left_corner_x),
                "top_left_corner_y: " + str(self.top_left_corner_y),
                "bottom_right_corner_x: " + str(self.bottom_right_corner_x),
                "bottom_right_corner_y: " + str(self.bottom_right_corner_y)
                ])

        return f"TrackRectangle: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTrackRectangle):
        """ Translates a gRPC struct to the SDK equivalent """
        return TrackRectangle(
                
                rpcTrackRectangle.top_left_corner_x,
                
                
                rpcTrackRectangle.top_left_corner_y,
                
                
                rpcTrackRectangle.bottom_right_corner_x,
                
                
                rpcTrackRectangle.bottom_right_corner_y
                )

    def translate_to_rpc(self, rpcTrackRectangle):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTrackRectangle.top_left_corner_x = self.top_left_corner_x
            
        
        
        
            
        rpcTrackRectangle.top_left_corner_y = self.top_left_corner_y
            
        
        
        
            
        rpcTrackRectangle.bottom_right_corner_x = self.bottom_right_corner_x
            
        
        
        
            
        rpcTrackRectangle.bottom_right_corner_y = self.bottom_right_corner_y
            
        
        


class TrackingServerResult:
    """
     Result type

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for tracking_server requests.

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

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3

        def translate_to_rpc(self):
            if self == TrackingServerResult.Result.UNKNOWN:
                return tracking_server_pb2.TrackingServerResult.RESULT_UNKNOWN
            if self == TrackingServerResult.Result.SUCCESS:
                return tracking_server_pb2.TrackingServerResult.RESULT_SUCCESS
            if self == TrackingServerResult.Result.NO_SYSTEM:
                return tracking_server_pb2.TrackingServerResult.RESULT_NO_SYSTEM
            if self == TrackingServerResult.Result.CONNECTION_ERROR:
                return tracking_server_pb2.TrackingServerResult.RESULT_CONNECTION_ERROR

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == tracking_server_pb2.TrackingServerResult.RESULT_UNKNOWN:
                return TrackingServerResult.Result.UNKNOWN
            if rpc_enum_value == tracking_server_pb2.TrackingServerResult.RESULT_SUCCESS:
                return TrackingServerResult.Result.SUCCESS
            if rpc_enum_value == tracking_server_pb2.TrackingServerResult.RESULT_NO_SYSTEM:
                return TrackingServerResult.Result.NO_SYSTEM
            if rpc_enum_value == tracking_server_pb2.TrackingServerResult.RESULT_CONNECTION_ERROR:
                return TrackingServerResult.Result.CONNECTION_ERROR

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TrackingServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TrackingServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TrackingServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TrackingServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TrackingServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTrackingServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TrackingServerResult(
                
                TrackingServerResult.Result.translate_from_rpc(rpcTrackingServerResult.result),
                
                
                rpcTrackingServerResult.result_str
                )

    def translate_to_rpc(self, rpcTrackingServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTrackingServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTrackingServerResult.result_str = self.result_str
            
        
        



class TrackingServerError(Exception):
    """ Raised when a TrackingServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class TrackingServer(AsyncBase):
    """
     API for an onboard image tracking software.

     Generated by dcsdkgen - MAVSDK TrackingServer API
    """

    # Plugin name
    name = "TrackingServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = tracking_server_pb2_grpc.TrackingServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return TrackingServerResult.translate_from_rpc(response.tracking_server_result)
    

    async def set_tracking_point_status(self, tracked_point):
        """
         Set/update the current point tracking status.

         Parameters
         ----------
         tracked_point : TrackPoint
              The tracked point

         
        """

        request = tracking_server_pb2.SetTrackingPointStatusRequest()
        
        tracked_point.translate_to_rpc(request.tracked_point)
                
            
        response = await self._stub.SetTrackingPointStatus(request)

        

    async def set_tracking_rectangle_status(self, tracked_rectangle):
        """
         Set/update the current rectangle tracking status.

         Parameters
         ----------
         tracked_rectangle : TrackRectangle
              The tracked rectangle

         
        """

        request = tracking_server_pb2.SetTrackingRectangleStatusRequest()
        
        tracked_rectangle.translate_to_rpc(request.tracked_rectangle)
                
            
        response = await self._stub.SetTrackingRectangleStatus(request)

        

    async def set_tracking_off_status(self):
        """
         Set the current tracking status to off.

         
        """

        request = tracking_server_pb2.SetTrackingOffStatusRequest()
        response = await self._stub.SetTrackingOffStatus(request)

        

    async def tracking_point_command(self):
        """
         Subscribe to incoming tracking point command.

         Yields
         -------
         track_point : TrackPoint
              The point to track if a point is to be tracked

         
        """

        request = tracking_server_pb2.SubscribeTrackingPointCommandRequest()
        tracking_point_command_stream = self._stub.SubscribeTrackingPointCommand(request)

        try:
            async for response in tracking_point_command_stream:
                

            
                yield TrackPoint.translate_from_rpc(response.track_point)
        finally:
            tracking_point_command_stream.cancel()

    async def tracking_rectangle_command(self):
        """
         Subscribe to incoming tracking rectangle command.

         Yields
         -------
         track_rectangle : TrackRectangle
              The point to track if a point is to be tracked

         
        """

        request = tracking_server_pb2.SubscribeTrackingRectangleCommandRequest()
        tracking_rectangle_command_stream = self._stub.SubscribeTrackingRectangleCommand(request)

        try:
            async for response in tracking_rectangle_command_stream:
                

            
                yield TrackRectangle.translate_from_rpc(response.track_rectangle)
        finally:
            tracking_rectangle_command_stream.cancel()

    async def tracking_off_command(self):
        """
         Subscribe to incoming tracking off command.

         Yields
         -------
         dummy : int32_t
              Unused

         
        """

        request = tracking_server_pb2.SubscribeTrackingOffCommandRequest()
        tracking_off_command_stream = self._stub.SubscribeTrackingOffCommand(request)

        try:
            async for response in tracking_off_command_stream:
                

            
                yield response.dummy
        finally:
            tracking_off_command_stream.cancel()

    async def respond_tracking_point_command(self, command_answer):
        """
         Respond to an incoming tracking point command.

         Parameters
         ----------
         command_answer : CommandAnswer
              The ack to answer to the incoming command

         Raises
         ------
         TrackingServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = tracking_server_pb2.RespondTrackingPointCommandRequest()
        
        request.command_answer = command_answer.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingPointCommand(request)

        
        result = self._extract_result(response)

        if result.result != TrackingServerResult.Result.SUCCESS:
            raise TrackingServerError(result, "respond_tracking_point_command()", command_answer)
        

    async def respond_tracking_rectangle_command(self, command_answer):
        """
         Respond to an incoming tracking rectangle command.

         Parameters
         ----------
         command_answer : CommandAnswer
              The ack to answer to the incoming command

         Raises
         ------
         TrackingServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = tracking_server_pb2.RespondTrackingRectangleCommandRequest()
        
        request.command_answer = command_answer.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingRectangleCommand(request)

        
        result = self._extract_result(response)

        if result.result != TrackingServerResult.Result.SUCCESS:
            raise TrackingServerError(result, "respond_tracking_rectangle_command()", command_answer)
        

    async def respond_tracking_off_command(self, command_answer):
        """
         Respond to an incoming tracking off command.

         Parameters
         ----------
         command_answer : CommandAnswer
              The ack to answer to the incoming command

         Raises
         ------
         TrackingServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = tracking_server_pb2.RespondTrackingOffCommandRequest()
        
        request.command_answer = command_answer.translate_to_rpc()
                
            
        response = await self._stub.RespondTrackingOffCommand(request)

        
        result = self._extract_result(response)

        if result.result != TrackingServerResult.Result.SUCCESS:
            raise TrackingServerError(result, "respond_tracking_off_command()", command_answer)
        