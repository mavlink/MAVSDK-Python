# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import geofence_pb2, geofence_pb2_grpc
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

    def __eq__(self, to_compare):
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

     fence_type : FenceType
          Fence type

     """

    
    
    class FenceType(Enum):
        """
         Geofence polygon types.

         Values
         ------
         INCLUSION
              Type representing an inclusion fence

         EXCLUSION
              Type representing an exclusion fence

         """

        
        INCLUSION = 0
        EXCLUSION = 1

        def translate_to_rpc(self):
            if self == Polygon.FenceType.INCLUSION:
                return geofence_pb2.Polygon.FENCE_TYPE_INCLUSION
            if self == Polygon.FenceType.EXCLUSION:
                return geofence_pb2.Polygon.FENCE_TYPE_EXCLUSION

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == geofence_pb2.Polygon.FENCE_TYPE_INCLUSION:
                return Polygon.FenceType.INCLUSION
            if rpc_enum_value == geofence_pb2.Polygon.FENCE_TYPE_EXCLUSION:
                return Polygon.FenceType.EXCLUSION

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            points,
            fence_type):
        """ Initializes the Polygon object """
        self.points = points
        self.fence_type = fence_type

    def __eq__(self, to_compare):
        """ Checks if two Polygon are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Polygon object
            return \
                (self.points == to_compare.points) and \
                (self.fence_type == to_compare.fence_type)

        except AttributeError:
            return False

    def __str__(self):
        """ Polygon in string representation """
        struct_repr = ", ".join([
                "points: " + str(self.points),
                "fence_type: " + str(self.fence_type)
                ])

        return f"Polygon: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcPolygon):
        """ Translates a gRPC struct to the SDK equivalent """
        return Polygon(
                
                list(map(lambda elem: Point.translate_from_rpc(elem), rpcPolygon.points)),
                
                
                Polygon.FenceType.translate_from_rpc(rpcPolygon.fence_type)
                )

    def translate_to_rpc(self, rpcPolygon):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.points:
                
            rpc_elem = geofence_pb2.Point()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcPolygon.points.extend(rpc_elems_list)
            
        
        
        
            
        rpcPolygon.fence_type = self.fence_type.translate_to_rpc()
            
        
        


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
              Unknown result

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

         NO_SYSTEM
              No system connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        ERROR = 2
        TOO_MANY_GEOFENCE_ITEMS = 3
        BUSY = 4
        TIMEOUT = 5
        INVALID_ARGUMENT = 6
        NO_SYSTEM = 7

        def translate_to_rpc(self):
            if self == GeofenceResult.Result.UNKNOWN:
                return geofence_pb2.GeofenceResult.RESULT_UNKNOWN
            if self == GeofenceResult.Result.SUCCESS:
                return geofence_pb2.GeofenceResult.RESULT_SUCCESS
            if self == GeofenceResult.Result.ERROR:
                return geofence_pb2.GeofenceResult.RESULT_ERROR
            if self == GeofenceResult.Result.TOO_MANY_GEOFENCE_ITEMS:
                return geofence_pb2.GeofenceResult.RESULT_TOO_MANY_GEOFENCE_ITEMS
            if self == GeofenceResult.Result.BUSY:
                return geofence_pb2.GeofenceResult.RESULT_BUSY
            if self == GeofenceResult.Result.TIMEOUT:
                return geofence_pb2.GeofenceResult.RESULT_TIMEOUT
            if self == GeofenceResult.Result.INVALID_ARGUMENT:
                return geofence_pb2.GeofenceResult.RESULT_INVALID_ARGUMENT
            if self == GeofenceResult.Result.NO_SYSTEM:
                return geofence_pb2.GeofenceResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_UNKNOWN:
                return GeofenceResult.Result.UNKNOWN
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_SUCCESS:
                return GeofenceResult.Result.SUCCESS
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_ERROR:
                return GeofenceResult.Result.ERROR
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_TOO_MANY_GEOFENCE_ITEMS:
                return GeofenceResult.Result.TOO_MANY_GEOFENCE_ITEMS
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_BUSY:
                return GeofenceResult.Result.BUSY
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_TIMEOUT:
                return GeofenceResult.Result.TIMEOUT
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_INVALID_ARGUMENT:
                return GeofenceResult.Result.INVALID_ARGUMENT
            if rpc_enum_value == geofence_pb2.GeofenceResult.RESULT_NO_SYSTEM:
                return GeofenceResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the GeofenceResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
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

        
        
            
        rpcGeofenceResult.result = self.result.translate_to_rpc()
            
        
        
        
            
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

        if result.result != GeofenceResult.Result.SUCCESS:
            raise GeofenceError(result, "upload_geofence()", polygons)
        

    async def clear_geofence(self):
        """
         Clear all geofences saved on the vehicle.

         Raises
         ------
         GeofenceError
             If the request fails. The error contains the reason for the failure.
        """

        request = geofence_pb2.ClearGeofenceRequest()
        response = await self._stub.ClearGeofence(request)

        
        result = self._extract_result(response)

        if result.result != GeofenceResult.Result.SUCCESS:
            raise GeofenceError(result, "clear_geofence()")
        