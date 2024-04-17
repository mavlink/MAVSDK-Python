# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import info_pb2, info_pb2_grpc
from enum import Enum


class FlightInfo:
    """
     System flight information.

     Parameters
     ----------
     time_boot_ms : uint32_t
          Time since system boot

     flight_uid : uint64_t
          Flight counter. Starts from zero, is incremented at every disarm and is never reset (even after reboot)

     duration_since_arming_ms : uint32_t
          Duration since arming in milliseconds

     duration_since_takeoff_ms : uint32_t
          Duration since takeoff in milliseconds

     """

    

    def __init__(
            self,
            time_boot_ms,
            flight_uid,
            duration_since_arming_ms,
            duration_since_takeoff_ms):
        """ Initializes the FlightInfo object """
        self.time_boot_ms = time_boot_ms
        self.flight_uid = flight_uid
        self.duration_since_arming_ms = duration_since_arming_ms
        self.duration_since_takeoff_ms = duration_since_takeoff_ms

    def __eq__(self, to_compare):
        """ Checks if two FlightInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FlightInfo object
            return \
                (self.time_boot_ms == to_compare.time_boot_ms) and \
                (self.flight_uid == to_compare.flight_uid) and \
                (self.duration_since_arming_ms == to_compare.duration_since_arming_ms) and \
                (self.duration_since_takeoff_ms == to_compare.duration_since_takeoff_ms)

        except AttributeError:
            return False

    def __str__(self):
        """ FlightInfo in string representation """
        struct_repr = ", ".join([
                "time_boot_ms: " + str(self.time_boot_ms),
                "flight_uid: " + str(self.flight_uid),
                "duration_since_arming_ms: " + str(self.duration_since_arming_ms),
                "duration_since_takeoff_ms: " + str(self.duration_since_takeoff_ms)
                ])

        return f"FlightInfo: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFlightInfo):
        """ Translates a gRPC struct to the SDK equivalent """
        return FlightInfo(
                
                rpcFlightInfo.time_boot_ms,
                
                
                rpcFlightInfo.flight_uid,
                
                
                rpcFlightInfo.duration_since_arming_ms,
                
                
                rpcFlightInfo.duration_since_takeoff_ms
                )

    def translate_to_rpc(self, rpcFlightInfo):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFlightInfo.time_boot_ms = self.time_boot_ms
            
        
        
        
            
        rpcFlightInfo.flight_uid = self.flight_uid
            
        
        
        
            
        rpcFlightInfo.duration_since_arming_ms = self.duration_since_arming_ms
            
        
        
        
            
        rpcFlightInfo.duration_since_takeoff_ms = self.duration_since_takeoff_ms
            
        
        


class Identification:
    """
     System identification.

     Parameters
     ----------
     hardware_uid : std::string
          UID of the hardware. This refers to uid2 of MAVLink. If the system does not support uid2 yet, this is all zeros.

     legacy_uid : uint64_t
          Legacy UID of the hardware, referred to as uid in MAVLink (formerly exposed during system discovery as UUID).

     """

    

    def __init__(
            self,
            hardware_uid,
            legacy_uid):
        """ Initializes the Identification object """
        self.hardware_uid = hardware_uid
        self.legacy_uid = legacy_uid

    def __eq__(self, to_compare):
        """ Checks if two Identification are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Identification object
            return \
                (self.hardware_uid == to_compare.hardware_uid) and \
                (self.legacy_uid == to_compare.legacy_uid)

        except AttributeError:
            return False

    def __str__(self):
        """ Identification in string representation """
        struct_repr = ", ".join([
                "hardware_uid: " + str(self.hardware_uid),
                "legacy_uid: " + str(self.legacy_uid)
                ])

        return f"Identification: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcIdentification):
        """ Translates a gRPC struct to the SDK equivalent """
        return Identification(
                
                rpcIdentification.hardware_uid,
                
                
                rpcIdentification.legacy_uid
                )

    def translate_to_rpc(self, rpcIdentification):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcIdentification.hardware_uid = self.hardware_uid
            
        
        
        
            
        rpcIdentification.legacy_uid = self.legacy_uid
            
        
        


class Product:
    """
     System product information.

     Parameters
     ----------
     vendor_id : int32_t
          ID of the board vendor

     vendor_name : std::string
          Name of the vendor

     product_id : int32_t
          ID of the product

     product_name : std::string
          Name of the product

     """

    

    def __init__(
            self,
            vendor_id,
            vendor_name,
            product_id,
            product_name):
        """ Initializes the Product object """
        self.vendor_id = vendor_id
        self.vendor_name = vendor_name
        self.product_id = product_id
        self.product_name = product_name

    def __eq__(self, to_compare):
        """ Checks if two Product are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Product object
            return \
                (self.vendor_id == to_compare.vendor_id) and \
                (self.vendor_name == to_compare.vendor_name) and \
                (self.product_id == to_compare.product_id) and \
                (self.product_name == to_compare.product_name)

        except AttributeError:
            return False

    def __str__(self):
        """ Product in string representation """
        struct_repr = ", ".join([
                "vendor_id: " + str(self.vendor_id),
                "vendor_name: " + str(self.vendor_name),
                "product_id: " + str(self.product_id),
                "product_name: " + str(self.product_name)
                ])

        return f"Product: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProduct):
        """ Translates a gRPC struct to the SDK equivalent """
        return Product(
                
                rpcProduct.vendor_id,
                
                
                rpcProduct.vendor_name,
                
                
                rpcProduct.product_id,
                
                
                rpcProduct.product_name
                )

    def translate_to_rpc(self, rpcProduct):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProduct.vendor_id = self.vendor_id
            
        
        
        
            
        rpcProduct.vendor_name = self.vendor_name
            
        
        
        
            
        rpcProduct.product_id = self.product_id
            
        
        
        
            
        rpcProduct.product_name = self.product_name
            
        
        


class Version:
    """
     System version information.

     Parameters
     ----------
     flight_sw_major : int32_t
          Flight software major version

     flight_sw_minor : int32_t
          Flight software minor version

     flight_sw_patch : int32_t
          Flight software patch version

     flight_sw_vendor_major : int32_t
          Flight software vendor major version

     flight_sw_vendor_minor : int32_t
          Flight software vendor minor version

     flight_sw_vendor_patch : int32_t
          Flight software vendor patch version

     os_sw_major : int32_t
          Operating system software major version

     os_sw_minor : int32_t
          Operating system software minor version

     os_sw_patch : int32_t
          Operating system software patch version

     flight_sw_git_hash : std::string
          Flight software git hash

     os_sw_git_hash : std::string
          Operating system software git hash

     flight_sw_version_type : FlightSoftwareVersionType
          Flight software version type

     """

    
    
    class FlightSoftwareVersionType(Enum):
        """
         These values define the type of firmware/flight software release

         Values
         ------
         UNKNOWN
              Unknown type

         DEV
              Development release

         ALPHA
              Alpha release

         BETA
              Beta release

         RC
              Release candidate

         RELEASE
              Official stable release

         """

        
        UNKNOWN = 0
        DEV = 1
        ALPHA = 2
        BETA = 3
        RC = 4
        RELEASE = 5

        def translate_to_rpc(self):
            if self == Version.FlightSoftwareVersionType.UNKNOWN:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_UNKNOWN
            if self == Version.FlightSoftwareVersionType.DEV:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_DEV
            if self == Version.FlightSoftwareVersionType.ALPHA:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_ALPHA
            if self == Version.FlightSoftwareVersionType.BETA:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_BETA
            if self == Version.FlightSoftwareVersionType.RC:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_RC
            if self == Version.FlightSoftwareVersionType.RELEASE:
                return info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_RELEASE

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_UNKNOWN:
                return Version.FlightSoftwareVersionType.UNKNOWN
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_DEV:
                return Version.FlightSoftwareVersionType.DEV
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_ALPHA:
                return Version.FlightSoftwareVersionType.ALPHA
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_BETA:
                return Version.FlightSoftwareVersionType.BETA
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_RC:
                return Version.FlightSoftwareVersionType.RC
            if rpc_enum_value == info_pb2.Version.FLIGHT_SOFTWARE_VERSION_TYPE_RELEASE:
                return Version.FlightSoftwareVersionType.RELEASE

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            flight_sw_major,
            flight_sw_minor,
            flight_sw_patch,
            flight_sw_vendor_major,
            flight_sw_vendor_minor,
            flight_sw_vendor_patch,
            os_sw_major,
            os_sw_minor,
            os_sw_patch,
            flight_sw_git_hash,
            os_sw_git_hash,
            flight_sw_version_type):
        """ Initializes the Version object """
        self.flight_sw_major = flight_sw_major
        self.flight_sw_minor = flight_sw_minor
        self.flight_sw_patch = flight_sw_patch
        self.flight_sw_vendor_major = flight_sw_vendor_major
        self.flight_sw_vendor_minor = flight_sw_vendor_minor
        self.flight_sw_vendor_patch = flight_sw_vendor_patch
        self.os_sw_major = os_sw_major
        self.os_sw_minor = os_sw_minor
        self.os_sw_patch = os_sw_patch
        self.flight_sw_git_hash = flight_sw_git_hash
        self.os_sw_git_hash = os_sw_git_hash
        self.flight_sw_version_type = flight_sw_version_type

    def __eq__(self, to_compare):
        """ Checks if two Version are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Version object
            return \
                (self.flight_sw_major == to_compare.flight_sw_major) and \
                (self.flight_sw_minor == to_compare.flight_sw_minor) and \
                (self.flight_sw_patch == to_compare.flight_sw_patch) and \
                (self.flight_sw_vendor_major == to_compare.flight_sw_vendor_major) and \
                (self.flight_sw_vendor_minor == to_compare.flight_sw_vendor_minor) and \
                (self.flight_sw_vendor_patch == to_compare.flight_sw_vendor_patch) and \
                (self.os_sw_major == to_compare.os_sw_major) and \
                (self.os_sw_minor == to_compare.os_sw_minor) and \
                (self.os_sw_patch == to_compare.os_sw_patch) and \
                (self.flight_sw_git_hash == to_compare.flight_sw_git_hash) and \
                (self.os_sw_git_hash == to_compare.os_sw_git_hash) and \
                (self.flight_sw_version_type == to_compare.flight_sw_version_type)

        except AttributeError:
            return False

    def __str__(self):
        """ Version in string representation """
        struct_repr = ", ".join([
                "flight_sw_major: " + str(self.flight_sw_major),
                "flight_sw_minor: " + str(self.flight_sw_minor),
                "flight_sw_patch: " + str(self.flight_sw_patch),
                "flight_sw_vendor_major: " + str(self.flight_sw_vendor_major),
                "flight_sw_vendor_minor: " + str(self.flight_sw_vendor_minor),
                "flight_sw_vendor_patch: " + str(self.flight_sw_vendor_patch),
                "os_sw_major: " + str(self.os_sw_major),
                "os_sw_minor: " + str(self.os_sw_minor),
                "os_sw_patch: " + str(self.os_sw_patch),
                "flight_sw_git_hash: " + str(self.flight_sw_git_hash),
                "os_sw_git_hash: " + str(self.os_sw_git_hash),
                "flight_sw_version_type: " + str(self.flight_sw_version_type)
                ])

        return f"Version: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcVersion):
        """ Translates a gRPC struct to the SDK equivalent """
        return Version(
                
                rpcVersion.flight_sw_major,
                
                
                rpcVersion.flight_sw_minor,
                
                
                rpcVersion.flight_sw_patch,
                
                
                rpcVersion.flight_sw_vendor_major,
                
                
                rpcVersion.flight_sw_vendor_minor,
                
                
                rpcVersion.flight_sw_vendor_patch,
                
                
                rpcVersion.os_sw_major,
                
                
                rpcVersion.os_sw_minor,
                
                
                rpcVersion.os_sw_patch,
                
                
                rpcVersion.flight_sw_git_hash,
                
                
                rpcVersion.os_sw_git_hash,
                
                
                Version.FlightSoftwareVersionType.translate_from_rpc(rpcVersion.flight_sw_version_type)
                )

    def translate_to_rpc(self, rpcVersion):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcVersion.flight_sw_major = self.flight_sw_major
            
        
        
        
            
        rpcVersion.flight_sw_minor = self.flight_sw_minor
            
        
        
        
            
        rpcVersion.flight_sw_patch = self.flight_sw_patch
            
        
        
        
            
        rpcVersion.flight_sw_vendor_major = self.flight_sw_vendor_major
            
        
        
        
            
        rpcVersion.flight_sw_vendor_minor = self.flight_sw_vendor_minor
            
        
        
        
            
        rpcVersion.flight_sw_vendor_patch = self.flight_sw_vendor_patch
            
        
        
        
            
        rpcVersion.os_sw_major = self.os_sw_major
            
        
        
        
            
        rpcVersion.os_sw_minor = self.os_sw_minor
            
        
        
        
            
        rpcVersion.os_sw_patch = self.os_sw_patch
            
        
        
        
            
        rpcVersion.flight_sw_git_hash = self.flight_sw_git_hash
            
        
        
        
            
        rpcVersion.os_sw_git_hash = self.os_sw_git_hash
            
        
        
        
            
        rpcVersion.flight_sw_version_type = self.flight_sw_version_type.translate_to_rpc()
            
        
        


class InfoResult:
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
         Possible results returned for info requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         INFORMATION_NOT_RECEIVED_YET
              Information has not been received yet

         NO_SYSTEM
              No system is connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        INFORMATION_NOT_RECEIVED_YET = 2
        NO_SYSTEM = 3

        def translate_to_rpc(self):
            if self == InfoResult.Result.UNKNOWN:
                return info_pb2.InfoResult.RESULT_UNKNOWN
            if self == InfoResult.Result.SUCCESS:
                return info_pb2.InfoResult.RESULT_SUCCESS
            if self == InfoResult.Result.INFORMATION_NOT_RECEIVED_YET:
                return info_pb2.InfoResult.RESULT_INFORMATION_NOT_RECEIVED_YET
            if self == InfoResult.Result.NO_SYSTEM:
                return info_pb2.InfoResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == info_pb2.InfoResult.RESULT_UNKNOWN:
                return InfoResult.Result.UNKNOWN
            if rpc_enum_value == info_pb2.InfoResult.RESULT_SUCCESS:
                return InfoResult.Result.SUCCESS
            if rpc_enum_value == info_pb2.InfoResult.RESULT_INFORMATION_NOT_RECEIVED_YET:
                return InfoResult.Result.INFORMATION_NOT_RECEIVED_YET
            if rpc_enum_value == info_pb2.InfoResult.RESULT_NO_SYSTEM:
                return InfoResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the InfoResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two InfoResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # InfoResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ InfoResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"InfoResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcInfoResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return InfoResult(
                
                InfoResult.Result.translate_from_rpc(rpcInfoResult.result),
                
                
                rpcInfoResult.result_str
                )

    def translate_to_rpc(self, rpcInfoResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcInfoResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcInfoResult.result_str = self.result_str
            
        
        



class InfoError(Exception):
    """ Raised when a InfoResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Info(AsyncBase):
    """
     Provide information about the hardware and/or software of a system.

     Generated by dcsdkgen - MAVSDK Info API
    """

    # Plugin name
    name = "Info"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = info_pb2_grpc.InfoServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return InfoResult.translate_from_rpc(response.info_result)
    

    async def get_flight_information(self):
        """
         Get flight information of the system.

         Returns
         -------
         flight_info : FlightInfo
              Flight information of the system

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetFlightInformationRequest()
        response = await self._stub.GetFlightInformation(request)

        
        result = self._extract_result(response)

        if result.result != InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_flight_information()")
        

        return FlightInfo.translate_from_rpc(response.flight_info)
            

    async def get_identification(self):
        """
         Get the identification of the system.

         Returns
         -------
         identification : Identification
              Identification of the system

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetIdentificationRequest()
        response = await self._stub.GetIdentification(request)

        
        result = self._extract_result(response)

        if result.result != InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_identification()")
        

        return Identification.translate_from_rpc(response.identification)
            

    async def get_product(self):
        """
         Get product information of the system.

         Returns
         -------
         product : Product
              Product information of the system

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetProductRequest()
        response = await self._stub.GetProduct(request)

        
        result = self._extract_result(response)

        if result.result != InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_product()")
        

        return Product.translate_from_rpc(response.product)
            

    async def get_version(self):
        """
         Get the version information of the system.

         Returns
         -------
         version : Version
              Version information about the system

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetVersionRequest()
        response = await self._stub.GetVersion(request)

        
        result = self._extract_result(response)

        if result.result != InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_version()")
        

        return Version.translate_from_rpc(response.version)
            

    async def get_speed_factor(self):
        """
         Get the speed factor of a simulation (with lockstep a simulation can run faster or slower than realtime).

         Returns
         -------
         speed_factor : double
              Speed factor of simulation

         Raises
         ------
         InfoError
             If the request fails. The error contains the reason for the failure.
        """

        request = info_pb2.GetSpeedFactorRequest()
        response = await self._stub.GetSpeedFactor(request)

        
        result = self._extract_result(response)

        if result.result != InfoResult.Result.SUCCESS:
            raise InfoError(result, "get_speed_factor()")
        

        return response.speed_factor
        

    async def flight_information(self):
        """
         Subscribe to 'flight information' updates.

         Yields
         -------
         flight_info : FlightInfo
              The next flight information

         
        """

        request = info_pb2.SubscribeFlightInformationRequest()
        flight_information_stream = self._stub.SubscribeFlightInformation(request)

        try:
            async for response in flight_information_stream:
                

            
                yield FlightInfo.translate_from_rpc(response.flight_info)
        finally:
            flight_information_stream.cancel()