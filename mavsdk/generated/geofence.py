# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import geofence_pb2, geofence_pb2_grpc
from enum import Enum


class Point:
    """
     Point type.

     Parameters
     ----------
     latitude_deg : double
          Latitude in degrees (range: -90 to +90)

     longitude_deg : double
          Longitude in degrees (range: -180 to +180)

     """

    

    def __init__(
            self,
            latitude_deg,
            longitude_deg):
        """ Initializes the Point object """
        self.latitude_deg = latitude_deg
        self.longitude_deg = longitude_deg

    def __equals__(self, to_compare):
        """ Checks if two Point are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Point object
            return \
                (self.latitude_deg == to_compare.latitude_deg) and \
                (self.longitude_deg == to_compare.longitude_deg)

        except AttributeError:
            return False

    def __str__(self):
        """ Point in string representation """
        struct_repr = ", ".join([
                "latitude_deg: " + str(self.latitude_deg),
                "longitude_deg: " + str(self.longitude_deg)
                ])

        return f"Point: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPoint):
        """ Translates a gRPC struct to the SDK equivalent """
        return Point(
                
                rpcPoint.latitude_deg,
                
                
                rpcPoint.longitude_deg
                )

    def translate_to_rpc(self, rpcPoint):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcPoint.latitude_deg = self.latitude_deg
            
        
        
        
            
        rpcPoint.longitude_deg = self.longitude_deg
            
        
        


class Polygon:
    """
     Polygon type.

     Parameters
     ----------
     points : [Point]
          Points defining the polygon

     type : Type
          Fence type

     """

    
    
    class Type(Enum):
        """
     

         Values
         ------
         INCLUSION
              Type representing an inclusion fence

         EXCLUSION
              Type representing an exclusion fence

         """

        
        INCLUSION = 0
        EXCLUSION = 1

        def translate_to_rpc(self, rpcType):
            return {
                    0: geofence_pb2.Polygon.INCLUSION,
                    1: geofence_pb2.Polygon.EXCLUSION
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: Polygon.Type.INCLUSION,
                    1: Polygon.Type.EXCLUSION,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            points,
            type):
        """ Initializes the Polygon object """
        self.points = points
        self.type = type

    def __equals__(self, to_compare):
        """ Checks if two Polygon are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Polygon object
            return \
                (self.points == to_compare.points) and \
                (self.type == to_compare.type)

        except AttributeError:
            return False

    def __str__(self):
        """ Polygon in string representation """
        struct_repr = ", ".join([
                "points: " + str(self.points),
                "type: " + str(self.type)
                ])

        return f"Polygon: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPolygon):
        """ Translates a gRPC struct to the SDK equivalent """
        return Polygon(
                
                Point.translate_from_rpc(rpcPolygon.points),
                
                
                Polygon.Type.translate_from_rpc(rpcPolygon.type)
                )

    def translate_to_rpc(self, rpcPolygon):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.points:
            rpc_elem = geofence_pb2.Point()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        rpcPolygon.points.extend(rpc_elems_list)
            
        
        
        
            
        self.type.translate_to_rpc(rpcPolygon.type)
            
        
        


class GeofenceResult:
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
         Possible results returned for geofence requests.

         Values
         ------
         UNKNOWN
              Unknown error

         SUCCESS
              Request succeeded

         ERROR
              Error

         TOO_MANY_GEOFENCE_ITEMS
              Too many Polygon objects in the geofence

         BUSY
              Vehicle is busy

         TIMEOUT
              Request timed out

         INVALID_ARGUMENT
              Invalid argument

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        ERROR = 2
        TOO_MANY_GEOFENCE_ITEMS = 3
        BUSY = 4
        TIMEOUT = 5
        INVALID_ARGUMENT = 6

        def translate_to_rpc(self, rpcResult):
            return {
                    0: geofence_pb2.GeofenceResult.UNKNOWN,
                    1: geofence_pb2.GeofenceResult.SUCCESS,
                    2: geofence_pb2.GeofenceResult.ERROR,
                    3: geofence_pb2.GeofenceResult.TOO_MANY_GEOFENCE_ITEMS,
                    4: geofence_pb2.GeofenceResult.BUSY,
                    5: geofence_pb2.GeofenceResult.TIMEOUT,
                    6: geofence_pb2.GeofenceResult.INVALID_ARGUMENT
                }.get(self.value, None)

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            return {
                    0: GeofenceResult.Result.UNKNOWN,
                    1: GeofenceResult.Result.SUCCESS,
                    2: GeofenceResult.Result.ERROR,
                    3: GeofenceResult.Result.TOO_MANY_GEOFENCE_ITEMS,
                    4: GeofenceResult.Result.BUSY,
                    5: GeofenceResult.Result.TIMEOUT,
                    6: GeofenceResult.Result.INVALID_ARGUMENT,
                }.get(rpc_enum_value, None)

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the GeofenceResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two GeofenceResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # GeofenceResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ GeofenceResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"GeofenceResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcGeofenceResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return GeofenceResult(
                
                GeofenceResult.Result.translate_from_rpc(rpcGeofenceResult.result),
                
                
                rpcGeofenceResult.result_str
                )

    def translate_to_rpc(self, rpcGeofenceResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.result.translate_to_rpc(rpcGeofenceResult.result)
            
        
        
        
            
        rpcGeofenceResult.result_str = self.result_str
            
        
        



class GeofenceError(Exception):
    """ Raised when a GeofenceResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Geofence(AsyncBase):
    """
     Enable setting a geofence.

     Generated by dcsdkgen - MAVSDK Geofence API
    """

    # Plugin name
    name = "Geofence"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = geofence_pb2_grpc.GeofenceServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return GeofenceResult.translate_from_rpc(response.geofence_result)
    

    async def upload_geofence(self, polygons):
        """
         Upload a geofence.

         Polygons are uploaded to a drone. Once uploaded, the geofence will remain
         on the drone even if a connection is lost.

         Parameters
         ----------
         polygons : [Polygon]
              Polygon(s) representing the geofence(s)

         Raises
         ------
         GeofenceError
             If the request fails. The error contains the reason for the failure.
        """

        request = geofence_pb2.UploadGeofenceRequest()
        
        rpc_elems_list = []
        for elem in polygons:
            rpc_elem = geofence_pb2.Polygon()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
        request.polygons.extend(rpc_elems_list)
                
            
        response = await self._stub.UploadGeofence(request)

        
        result = self._extract_result(response)

        if result.result is not GeofenceResult.Result.SUCCESS:
            raise GeofenceError(result, "upload_geofence()", polygons)
        