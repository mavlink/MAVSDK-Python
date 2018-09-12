# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ...generated import telemetry_pb2, telemetry_pb2_grpc


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
            # Health object
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
            # Battery object
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


class Telemetry(AsyncBase):
    """
    Dronecore Telemetry API
    """

    # Plugin name
    name = "Telemetry"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _setup_stub(self, channel):
        """
        Setup the telemetry stub
        """
        self._stub = telemetry_pb2_grpc.TelemetryServiceStub(channel)

    async def in_air_watcher(self):
        """
        Async generator for the inair status
        """
        async for response in self._stub.SubscribeInAir(
                telemetry_pb2.SubscribeInAirRequest()):

            yield response.is_in_air

    async def armed_watcher(self):
        """
        Creats the inair observable
        """
        async for response in self._stub.SubscribeArmed(
                telemetry_pb2.SubscribeArmedRequest()):

            yield response.is_armed


    async def position_watcher(self):
        """
        Create the position observable
        """
        async for response in self._stub.SubscribePosition(
                telemetry_pb2.SubscribePositionRequest()):

            yield Position.parse_response(response)

    async def health_watcher(self):
        """
        Create the health observable
        """
        async for response in self._stub.SubscribeHealth(
                telemetry_pb2.SubscribeHealthRequest()):

            yield Health.parse_response(response)

    async def battery_watcher(self):
        """
        Create the battery observable
        """
        async for response in self._stub.SubscribeBattery(
                telemetry_pb2.SubscribeBatteryRequest()):

            yield Battery.parse_response(response)
