from .._base import Base
from ..generated import action_pb2, action_pb2_grpc


class Action(Base):
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

    def arm(self):
        """
        Arms the vehicle

        :returns: Observable
        """

        def f(observable):
            response = self._stub.Arm(action_pb2.ArmRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)

    def disarm(self):
        """
        Disarms the vehicle

        :returns: Observable
        """

        def f(observable):
            response = self._stub.Disarm(action_pb2.DisarmRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)

    def takeoff(self):
        """
        Takeoff

        :returns Observable
        """

        def f(observable):
            response = self._stub.Takeoff(action_pb2.TakeoffRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)

#   @TODO seems to not be working, action_result is not available
    def set_takeoff_altitude(self, altitude):
        """
        Takeoff

        :returns: Observable
        """

        def f(observable):

            response = self._stub.SetTakeoffAltitude(
                action_pb2.SetTakeoffAltitudeRequest(altitude_m=altitude)
            )

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)

#   @TODO seems to not be working, action_result is not available
    def get_takeoff_altitude(self):
        """
        Takeoff

        :returns: Ovservable
        """

        def f(observable):

            response = self._stub.GetTakeoffAltitude(
                action_pb2.GetTakeoffAltitudeRequest()
            )

            if self._response_success(response):
                observable.on_next(response.altitude_m)
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)

    def land(self):
        """
        Land

        :returns: Observable
        """
        def f(observable):

            response = self._stub.Land(action_pb2.LandRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return self._create_call_observable(f)
