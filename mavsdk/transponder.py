# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import transponder_pb2, transponder_pb2_grpc
from enum import Enum


class AdsbEmitterType(Enum):
    """
     ADSB classification for the type of vehicle emitting the transponder signal.

     Values
     ------
     NO_INFO
          No emitter info.

     LIGHT
          Light emitter.

     SMALL
          Small emitter.

     LARGE
          Large emitter.

     HIGH_VORTEX_LARGE
          High vortex emitter.

     HEAVY
          Heavy emitter.

     HIGHLY_MANUV
          Highly maneuverable emitter.

     ROTOCRAFT
          Rotorcraft emitter.

     UNASSIGNED
          Unassigned emitter.

     GLIDER
          Glider emitter.

     LIGHTER_AIR
          Lighter air emitter.

     PARACHUTE
          Parachute emitter.

     ULTRA_LIGHT
          Ultra light emitter.

     UNASSIGNED2
          Unassigned2 emitter.

     UAV
          UAV emitter.

     SPACE
          Space emitter.

     UNASSGINED3
          Unassigned3 emitter.

     EMERGENCY_SURFACE
          Emergency emitter.

     SERVICE_SURFACE
          Service surface emitter.

     POINT_OBSTACLE
          Point obstacle emitter.

     """

    
    NO_INFO = 0
    LIGHT = 1
    SMALL = 2
    LARGE = 3
    HIGH_VORTEX_LARGE = 4
    HEAVY = 5
    HIGHLY_MANUV = 6
    ROTOCRAFT = 7
    UNASSIGNED = 8
    GLIDER = 9
    LIGHTER_AIR = 10
    PARACHUTE = 11
    ULTRA_LIGHT = 12
    UNASSIGNED2 = 13
    UAV = 14
    SPACE = 15
    UNASSGINED3 = 16
    EMERGENCY_SURFACE = 17
    SERVICE_SURFACE = 18
    POINT_OBSTACLE = 19

    def translate_to_rpc(self):
        if self == AdsbEmitterType.NO_INFO:
            return transponder_pb2.ADSB_EMITTER_TYPE_NO_INFO
        if self == AdsbEmitterType.LIGHT:
            return transponder_pb2.ADSB_EMITTER_TYPE_LIGHT
        if self == AdsbEmitterType.SMALL:
            return transponder_pb2.ADSB_EMITTER_TYPE_SMALL
        if self == AdsbEmitterType.LARGE:
            return transponder_pb2.ADSB_EMITTER_TYPE_LARGE
        if self == AdsbEmitterType.HIGH_VORTEX_LARGE:
            return transponder_pb2.ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE
        if self == AdsbEmitterType.HEAVY:
            return transponder_pb2.ADSB_EMITTER_TYPE_HEAVY
        if self == AdsbEmitterType.HIGHLY_MANUV:
            return transponder_pb2.ADSB_EMITTER_TYPE_HIGHLY_MANUV
        if self == AdsbEmitterType.ROTOCRAFT:
            return transponder_pb2.ADSB_EMITTER_TYPE_ROTOCRAFT
        if self == AdsbEmitterType.UNASSIGNED:
            return transponder_pb2.ADSB_EMITTER_TYPE_UNASSIGNED
        if self == AdsbEmitterType.GLIDER:
            return transponder_pb2.ADSB_EMITTER_TYPE_GLIDER
        if self == AdsbEmitterType.LIGHTER_AIR:
            return transponder_pb2.ADSB_EMITTER_TYPE_LIGHTER_AIR
        if self == AdsbEmitterType.PARACHUTE:
            return transponder_pb2.ADSB_EMITTER_TYPE_PARACHUTE
        if self == AdsbEmitterType.ULTRA_LIGHT:
            return transponder_pb2.ADSB_EMITTER_TYPE_ULTRA_LIGHT
        if self == AdsbEmitterType.UNASSIGNED2:
            return transponder_pb2.ADSB_EMITTER_TYPE_UNASSIGNED2
        if self == AdsbEmitterType.UAV:
            return transponder_pb2.ADSB_EMITTER_TYPE_UAV
        if self == AdsbEmitterType.SPACE:
            return transponder_pb2.ADSB_EMITTER_TYPE_SPACE
        if self == AdsbEmitterType.UNASSGINED3:
            return transponder_pb2.ADSB_EMITTER_TYPE_UNASSGINED3
        if self == AdsbEmitterType.EMERGENCY_SURFACE:
            return transponder_pb2.ADSB_EMITTER_TYPE_EMERGENCY_SURFACE
        if self == AdsbEmitterType.SERVICE_SURFACE:
            return transponder_pb2.ADSB_EMITTER_TYPE_SERVICE_SURFACE
        if self == AdsbEmitterType.POINT_OBSTACLE:
            return transponder_pb2.ADSB_EMITTER_TYPE_POINT_OBSTACLE

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_NO_INFO:
            return AdsbEmitterType.NO_INFO
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_LIGHT:
            return AdsbEmitterType.LIGHT
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_SMALL:
            return AdsbEmitterType.SMALL
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_LARGE:
            return AdsbEmitterType.LARGE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_HIGH_VORTEX_LARGE:
            return AdsbEmitterType.HIGH_VORTEX_LARGE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_HEAVY:
            return AdsbEmitterType.HEAVY
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_HIGHLY_MANUV:
            return AdsbEmitterType.HIGHLY_MANUV
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_ROTOCRAFT:
            return AdsbEmitterType.ROTOCRAFT
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_UNASSIGNED:
            return AdsbEmitterType.UNASSIGNED
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_GLIDER:
            return AdsbEmitterType.GLIDER
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_LIGHTER_AIR:
            return AdsbEmitterType.LIGHTER_AIR
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_PARACHUTE:
            return AdsbEmitterType.PARACHUTE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_ULTRA_LIGHT:
            return AdsbEmitterType.ULTRA_LIGHT
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_UNASSIGNED2:
            return AdsbEmitterType.UNASSIGNED2
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_UAV:
            return AdsbEmitterType.UAV
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_SPACE:
            return AdsbEmitterType.SPACE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_UNASSGINED3:
            return AdsbEmitterType.UNASSGINED3
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_EMERGENCY_SURFACE:
            return AdsbEmitterType.EMERGENCY_SURFACE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_SERVICE_SURFACE:
            return AdsbEmitterType.SERVICE_SURFACE
        if rpc_enum_value == transponder_pb2.ADSB_EMITTER_TYPE_POINT_OBSTACLE:
            return AdsbEmitterType.POINT_OBSTACLE

    def __str__(self):
        return self.name


class AdsbAltitudeType(Enum):
    """
     Altitude type used in AdsbVehicle message

     Values
     ------
     PRESSURE_QNH
          Altitude reported from a Baro source using QNH reference

     GEOMETRIC
          Altitude reported from a GNSS source

     """

    
    PRESSURE_QNH = 0
    GEOMETRIC = 1

    def translate_to_rpc(self):
        if self == AdsbAltitudeType.PRESSURE_QNH:
            return transponder_pb2.ADSB_ALTITUDE_TYPE_PRESSURE_QNH
        if self == AdsbAltitudeType.GEOMETRIC:
            return transponder_pb2.ADSB_ALTITUDE_TYPE_GEOMETRIC

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == transponder_pb2.ADSB_ALTITUDE_TYPE_PRESSURE_QNH:
            return AdsbAltitudeType.PRESSURE_QNH
        if rpc_enum_value == transponder_pb2.ADSB_ALTITUDE_TYPE_GEOMETRIC:
            return AdsbAltitudeType.GEOMETRIC

    def __str__(self):
        return self.name


class AdsbVehicle:
    """
     ADSB Vehicle type.

     Parameters
     ----------
     icao_address : uint32_t
          ICAO (International Civil Aviation Organization) unique worldwide identifier

     latitude_deg : double
          Latitude in degrees (range: -90 to +90)

     longitude_deg : double
          Longitude in degrees (range: -180 to +180).

     altitude_type : AdsbAltitudeType
          ADSB altitude type.

     absolute_altitude_m : float
          Altitude in metres according to altitude_type 

     heading_deg : float
          Course over ground, in degrees

     horizontal_velocity_m_s : float
          The horizontal velocity in metres/second

     vertical_velocity_m_s : float
          The vertical velocity in metres/second. Positive is up.

     callsign : std::string
          The callsign

     emitter_type : AdsbEmitterType
          ADSB emitter type.

     squawk : uint32_t
          Squawk code.

     tslc_s : uint32_t
          Time Since Last Communication in seconds.

     """

    

    def __init__(
            self,
            icao_address,
            latitude_deg,
            longitude_deg,
            altitude_type,
            absolute_altitude_m,
            heading_deg,
            horizontal_velocity_m_s,
            vertical_velocity_m_s,
            callsign,
            emitter_type,
            squawk,
            tslc_s):
        """ Initializes the AdsbVehicle object """
        self.icao_address = icao_address
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg
        self.altitude_type = altitude_type
        self.absolute_altitude_m = absolute_altitude_m
        self.heading_deg = heading_deg
        self.horizontal_velocity_m_s = horizontal_velocity_m_s
        self.vertical_velocity_m_s = vertical_velocity_m_s
        self.callsign = callsign
        self.emitter_type = emitter_type
        self.squawk = squawk
        self.tslc_s = tslc_s

    def __eq__(self, to_compare):
        """ Checks if two AdsbVehicle are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AdsbVehicle object
            return \
                (self.icao_address == to_compare.icao_address) and \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg) and \
                (self.altitude_type == to_compare.altitude_type) and \
                (self.absolute_altitude_m == to_compare.absolute_altitude_m) and \
                (self.heading_deg == to_compare.heading_deg) and \
                (self.horizontal_velocity_m_s == to_compare.horizontal_velocity_m_s) and \
                (self.vertical_velocity_m_s == to_compare.vertical_velocity_m_s) and \
                (self.callsign == to_compare.callsign) and \
                (self.emitter_type == to_compare.emitter_type) and \
                (self.squawk == to_compare.squawk) and \
                (self.tslc_s == to_compare.tslc_s)

        except AttributeError:
            return False

    def __str__(self):
        """ AdsbVehicle in string representation """
        struct_repr = ", ".join([
                "icao_address: " + str(self.icao_address),
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg),
                "altitude_type: " + str(self.altitude_type),
                "absolute_altitude_m: " + str(self.absolute_altitude_m),
                "heading_deg: " + str(self.heading_deg),
                "horizontal_velocity_m_s: " + str(self.horizontal_velocity_m_s),
                "vertical_velocity_m_s: " + str(self.vertical_velocity_m_s),
                "callsign: " + str(self.callsign),
                "emitter_type: " + str(self.emitter_type),
                "squawk: " + str(self.squawk),
                "tslc_s: " + str(self.tslc_s)
                ])

        return f"AdsbVehicle: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAdsbVehicle):
        """ Translates a gRPC struct to the SDK equivalent """
        return AdsbVehicle(
                
                rpcAdsbVehicle.icao_address,
                
                
                rpcAdsbVehicle.latitude_deg,
                
                
                rpcAdsbVehicle.longitude_deg,
                
                
                AdsbAltitudeType.translate_from_rpc(rpcAdsbVehicle.altitude_type),
                
                
                rpcAdsbVehicle.absolute_altitude_m,
                
                
                rpcAdsbVehicle.heading_deg,
                
                
                rpcAdsbVehicle.horizontal_velocity_m_s,
                
                
                rpcAdsbVehicle.vertical_velocity_m_s,
                
                
                rpcAdsbVehicle.callsign,
                
                
                AdsbEmitterType.translate_from_rpc(rpcAdsbVehicle.emitter_type),
                
                
                rpcAdsbVehicle.squawk,
                
                
                rpcAdsbVehicle.tslc_s
                )

    def translate_to_rpc(self, rpcAdsbVehicle):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAdsbVehicle.icao_address = self.icao_address
            
        
        
        
            
        rpcAdsbVehicle.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcAdsbVehicle.longitude_deg = self.longitude_deg
            
        
        
        
            
        rpcAdsbVehicle.altitude_type = self.altitude_type.translate_to_rpc()
            
        
        
        
            
        rpcAdsbVehicle.absolute_altitude_m = self.absolute_altitude_m
            
        
        
        
            
        rpcAdsbVehicle.heading_deg = self.heading_deg
            
        
        
        
            
        rpcAdsbVehicle.horizontal_velocity_m_s = self.horizontal_velocity_m_s
            
        
        
        
            
        rpcAdsbVehicle.vertical_velocity_m_s = self.vertical_velocity_m_s
            
        
        
        
            
        rpcAdsbVehicle.callsign = self.callsign
            
        
        
        
            
        rpcAdsbVehicle.emitter_type = self.emitter_type.translate_to_rpc()
            
        
        
        
            
        rpcAdsbVehicle.squawk = self.squawk
            
        
        
        
            
        rpcAdsbVehicle.tslc_s = self.tslc_s
            
        
        


class TransponderResult:
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
         Possible results returned for transponder requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Success: the transponder command was accepted by the vehicle

         NO_SYSTEM
              No system connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         TIMEOUT
              Request timed out

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        TIMEOUT = 6

        def translate_to_rpc(self):
            if self == TransponderResult.Result.UNKNOWN:
                return transponder_pb2.TransponderResult.RESULT_UNKNOWN
            if self == TransponderResult.Result.SUCCESS:
                return transponder_pb2.TransponderResult.RESULT_SUCCESS
            if self == TransponderResult.Result.NO_SYSTEM:
                return transponder_pb2.TransponderResult.RESULT_NO_SYSTEM
            if self == TransponderResult.Result.CONNECTION_ERROR:
                return transponder_pb2.TransponderResult.RESULT_CONNECTION_ERROR
            if self == TransponderResult.Result.BUSY:
                return transponder_pb2.TransponderResult.RESULT_BUSY
            if self == TransponderResult.Result.COMMAND_DENIED:
                return transponder_pb2.TransponderResult.RESULT_COMMAND_DENIED
            if self == TransponderResult.Result.TIMEOUT:
                return transponder_pb2.TransponderResult.RESULT_TIMEOUT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_UNKNOWN:
                return TransponderResult.Result.UNKNOWN
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_SUCCESS:
                return TransponderResult.Result.SUCCESS
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_NO_SYSTEM:
                return TransponderResult.Result.NO_SYSTEM
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_CONNECTION_ERROR:
                return TransponderResult.Result.CONNECTION_ERROR
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_BUSY:
                return TransponderResult.Result.BUSY
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_COMMAND_DENIED:
                return TransponderResult.Result.COMMAND_DENIED
            if rpc_enum_value == transponder_pb2.TransponderResult.RESULT_TIMEOUT:
                return TransponderResult.Result.TIMEOUT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TransponderResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TransponderResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TransponderResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TransponderResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TransponderResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTransponderResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TransponderResult(
                
                TransponderResult.Result.translate_from_rpc(rpcTransponderResult.result),
                
                
                rpcTransponderResult.result_str
                )

    def translate_to_rpc(self, rpcTransponderResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTransponderResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTransponderResult.result_str = self.result_str
            
        
        



class TransponderError(Exception):
    """ Raised when a TransponderResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Transponder(AsyncBase):
    """
     Allow users to get ADS-B information
     and set ADS-B update rates.

     Generated by dcsdkgen - MAVSDK Transponder API
    """

    # Plugin name
    name = "Transponder"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = transponder_pb2_grpc.TransponderServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return TransponderResult.translate_from_rpc(response.transponder_result)
    

    async def transponder(self):
        """
         Subscribe to 'transponder' updates.

         Yields
         -------
         transponder : AdsbVehicle
              The next detection

         
        """

        request = transponder_pb2.SubscribeTransponderRequest()
        transponder_stream = self._stub.SubscribeTransponder(request)

        try:
            async for response in transponder_stream:
                

            
                yield AdsbVehicle.translate_from_rpc(response.transponder)
        finally:
            transponder_stream.cancel()

    async def set_rate_transponder(self, rate_hz):
        """
         Set rate to 'transponder' updates.

         Parameters
         ----------
         rate_hz : double
              The requested rate (in Hertz)

         Raises
         ------
         TransponderError
             If the request fails. The error contains the reason for the failure.
        """

        request = transponder_pb2.SetRateTransponderRequest()
        request.rate_hz = rate_hz
        response = await self._stub.SetRateTransponder(request)

        
        result = self._extract_result(response)

        if result.result != TransponderResult.Result.SUCCESS:
            raise TransponderError(result, "set_rate_transponder()", rate_hz)
        