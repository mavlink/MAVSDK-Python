from rx import Observable
from .base import Base
from .generated import action_pb2, action_pb2_grpc


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

        def arm_request(observable):
            response = self._stub.Arm(action_pb2.ArmRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return Observable.create(arm_request)

    def disarm(self):
        """
        Disarms the vehicle

        :returns: Observable
        """

        def disarm_request(observable):
            response = self._stub.Disarm(action_pb2.DisarmRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return Observable.create(disarm_request)

    def takeoff(self):
        """
        Takeoff

        :returns Observable
        """

        def takeoff_request(observable):
            response = self._stub.Takeoff(action_pb2.TakeoffRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return Observable.create(takeoff_request)

    def set_takeoff_height(self, height):
        """
        Takeoff

        :returns: Observable
        """

        def set_takeoff_height_request(observable):

            response = self._stub.SetTakeoffAltitude(
                action_pb2.SetTakeoffAltitudeRequest(altitude_m=height)
            )

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return Observable.create(set_takeoff_height_request)

    def get_takeoff_height(self):
        """
        Takeoff

        :returns: Ovservable
        """

        def get_takeoff_height_request(observable):

            response = self._stub.GetTakeoffAltitude(
                action_pb2.GetTakeoffAltitudeRequest()
            )

            if self._response_success(response):
                observable.on_completed(response.altitude_m)
            else:
                observable.on_error(response)

        return Observable.create(get_takeoff_height_request)

    def land(self):
        """
        Land

        :returns: Observable
        """
        def land_request(observable):

            response = self._stub.Land(action_pb2.LandRequest())

            if self._response_success(response):
                observable.on_completed()
            else:
                observable.on_error(response)

        return Observable.create(land_request)
