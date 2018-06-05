# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ...generated import action_pb2, action_pb2_grpc


class Action(AsyncBase):
    """
    Dronecore Action API
    """

    # Plugin name
    name = "Action"

    def _setup_stub(self, channel):
        """
        Setups the action stub
        """
        self._stub = action_pb2_grpc.ActionServiceStub(channel)

    def _response_success(self, response):
        """
        Checks if the request was successfull
        """
        return (response.action_result.result ==
                action_pb2.ActionResult.SUCCESS)

    async def arm(self):
        """
        Arms the vehicle

        :returns: (Success state, actual response)
        """

        # Request
        response = await self._stub.Arm(action_pb2.ArmRequest())
        return self._response_success(response), response

    async def disarm(self):
        """
        Disarms the vehicle

        :returns: (Success state, actual response)
        """
        response = await self._stub.Disarm(action_pb2.DisarmRequest())
        return self._response_success(response), response

    async def takeoff(self):
        """
        Takeoff

        :returns: (Success state, actual response)
        """
        response = await self._stub.Takeoff(action_pb2.TakeoffRequest())
        return self._response_success(response), response

    # @TODO seems to not be working, action_result is not available
    async def set_takeoff_altitude(self, altitude):
        """
        Takeoff

        :returns: (Success state, actual response)
        """
        response = await self._stub.SetTakeoffAltitude(
                action_pb2.SetTakeoffAltitudeRequest(altitude_m=altitude))
        # return self._response_success(response), response
        return True, response

    # @TODO seems to not be working, action_result is not available
    async def get_takeoff_altitude(self):
        """
        Takeoff

        :returns: (value, Success state, actual response)
        """

        response = await self._stub.GetTakeoffAltitude(
                action_pb2.GetTakeoffAltitudeRequest())
        return response.altitude_m, True, response #self._response_success(response), response

    async def land(self):
        """
        Land

        :returns: (Success state, actual response)
        """
        response = await self._stub.Land(action_pb2.LandRequest())
        return self._response_success(response), response
