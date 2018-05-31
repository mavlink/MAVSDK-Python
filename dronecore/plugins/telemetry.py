# -*- coding: utf-8 -*-
from .._base import Base
from ..generated import telemetry_pb2, telemetry_pb2_grpc


class Position(object):
    """ Position """

    def __init__(
            self, latitude, longitude, absolute_altitude, relative_altitude):
        """ Initialize the position object """

        # Set latitude and longitude
        self.latitude, self.longitude = latitude, longitude
        # Set absolute altitude
        self.absolute_altitude = absolute_altitude
        # Set relative altitude
        self.relative_altitude = relative_altitude

    def __equals__(self, to_compare):
        """ Checks if two positions are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Position object
            return \
                self.latitude == to_compare.latitude and \
                self.longitude == to_compare.longitude and \
                self.absolute_altitude == to_compare.absolute_altitude and \
                self.relative_altitude == to_compare.absolute_altotude

        except AttributeError:
            return False

    def __repr__(self):
        """ Position in string representation """
        return "Position: Lat: {}, Long: {}, Alt: {}".format(
                    self.latitude,
                    self.longitude,
                    self.absolute_altitude)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return Position(response.position.latitude_deg,
                        response.position.longitude_deg,
                        response.position.absolute_altitude_m,
                        response.position.relative_altitude_m)


class Health(object):
    """ Health """

    def __init__(
            self,
            is_gyrometer_calibration_ok,
            is_accelerometer_calibration_ok,
            is_level_calibration_ok,
            is_local_position_ok,
            is_global_position_ok,
            is_home_position_ok):
        """ Initializes the Health object """
        self.is_gyrometer_calibration_ok = is_gyrometer_calibration_ok
        self.is_accelerometer_calibration_ok = is_accelerometer_calibration_ok
        self.is_level_calibration_ok = is_level_calibration_ok
        self.is_local_position_ok = is_local_position_ok
        self.is_global_position_ok = is_global_position_ok
        self.is_home_position_ok = is_home_position_ok

    def __eq__(self, other):
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Position object
            return (
                (self.is_gyrometer_calibration_ok ==
                    other.is_gyrometer_calibration_ok) and
                (self.is_accelerometer_calibration_ok ==
                    other.is_accelerometer_calibration_ok) and
                (self.is_level_calibration_ok ==
                    other.is_level_calibration_ok) and
                (self.is_local_position_ok ==
                    other.is_local_position_ok) and
                (self.is_global_position_ok ==
                    other.is_global_position_ok) and
                (self.is_home_position_ok == other.is_home_position_ok))

        except AttributeError:
            return False

    def __repr__(self):
        """ String representation of the health state """
        if (self.is_gyrometer_calibration_ok and
                self.is_accelerometer_calibration_ok and
                self.is_level_calibration_ok and self.is_local_position_ok and
                self.is_global_position_ok and self.is_home_position_ok):
            return "Health: OK"
        else:
            return "Health: WARNING"

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return Health(
            response.health.is_gyrometer_calibration_ok,
            response.health.is_accelerometer_calibration_ok,
            response.health.is_level_calibration_ok,
            response.health.is_local_position_ok,
            response.health.is_global_position_ok,
            response.health.is_home_position_ok)


class Battery(object):
    """ Battery """

    def __init__(self, remaining_percent, voltage):
        """ Initializes the Battery object """
        self.remaining_percent = remaining_percent
        self.voltage = voltage

    def __eq__(self, other):
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Position object
            return (self.remaining_percent == other.remaining_percet and
                    self.voltage == other.voltage)

        except AttributeError:
            return False

    def __repr__(self):
        """ String representation of the battery """
        return "Battery: {} Volt, {} left".format(
                    self.remaining_percent,
                    self.voltage)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return Battery(
                    response.battery.remaining_percent,
                    response.battery.voltage_v)


class Telemetry(Base):
    """
    Dronecore Telemetry API
    """

    # Plugin name
    name = "Telemetry"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create observables
        self._create_in_air_observable()
        self._create_armed_observable()
        self._create_position_observable()
        self._create_health_observable()
        self._create_battery_observable()

    def _setup_stub(self, channel):
        """
        Setup the telemetry stub
        """
        self._stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

    def _create_in_air_observable(self):
        """
        Creates inair observable
        """
        stream = self._stub.SubscribeInAir(
            telemetry_pb2.SubscribeInAirRequest())

        self._in_air_observable = self._create_stream_observable(
                response.is_in_air for response in stream)

    def _create_armed_observable(self):
        """
        Creats the inair observable
        """
        stream = self._stub.SubscribeArmed(
            telemetry_pb2.SubscribeArmedRequest())

        self._armed_observable = self._create_stream_observable(
                response.is_armed for response in stream)

    def _create_position_observable(self):
        """
        Create the position observable
        """
        stream = self._stub.SubscribePosition(
                telemetry_pb2.SubscribePositionRequest())

        self._position_observable = self._create_stream_observable(
                Position.parse_response(response) for response in stream)

    def _create_health_observable(self):
        """
        Create the health observable
        """
        stream = self._stub.SubscribeHealth(
                telemetry_pb2.SubscribeHealthRequest())

        self._health_observable = self._create_stream_observable(
                Health.parse_response(response) for response in stream)

    def _create_battery_observable(self):
        """
        Create the battery observable
        """
        stream = self._stub.SubscribeBattery(
                telemetry_pb2.SubscribeBatteryRequest())

        self._battery_observable = self._create_stream_observable(
                Battery.parse_response(response) for response in stream)

    @property
    def in_air(self):
        """
        published arm observable
        """
        return self._in_air_observable

    @property
    def armed(self):
        """
        published arm observable
        """
        return self._armed_observable

    @property
    def position(self):
        """
        published position observable
        """
        return self._position_observable

    @property
    def health(self):
        """
        published health observable
        """
        return self._health_observable

    @property
    def battery(self):
        """
        published battery observable
        """
        return self._battery_observable
