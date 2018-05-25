from .._base import Base
from ..generated import telemetry_pb2, telemetry_pb2_grpc


class Telemetry(Base):
    """
    Dronecore Telemetry API
    """

    # Plugin name
    name = "Telemetry"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create observables
        self._create_armed_observable()

    def _setup_stub(self, channel):
        """
        Setup the telemetry stub
        """
        self._stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

    def _create_armed_observable(self):
        """
        Creats the inair observable
        """
        def f(observable):
            stream = self._stub.SubscribeArmed(
                telemetry_pb2.SubscribeArmedRequest()
            )

            try:
                while True:
                    # @TODO
                    # observable.on_next(
                    #     stream.receive().is_in_air
                    # )
                    pass
            except Exception as e:
                observable.on_error(e)

            observable.on_completed()

        self._armed_observable = self._create_stream_observable(f)

    @property
    def armed(self):
        """
        published arm observable
        """
        return self._armed_observable
