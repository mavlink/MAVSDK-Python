# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import param_pb2, param_pb2_grpc
from enum import Enum


class IntParam:
    """
     Type for integer parameters.

     Parameters
     ----------
     name : std::string
          Name of the parameter

     value : int32_t
          Value of the parameter

     """

    

    def __init__(
            self,
            name,
            value):
        """ Initializes the IntParam object """
        self.name = name
        self.value = value

    def __eq__(self, to_compare):
        """ Checks if two IntParam are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # IntParam object
            return \
                (self.name == to_compare.name) and \
                (self.value == to_compare.value)

        except AttributeError:
            return False

    def __str__(self):
        """ IntParam in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "value: " + str(self.value)
                ])

        return f"IntParam: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcIntParam):
        """ Translates a gRPC struct to the SDK equivalent """
        return IntParam(
                
                rpcIntParam.name,
                
                
                rpcIntParam.value
                )

    def translate_to_rpc(self, rpcIntParam):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcIntParam.name = self.name
            
        
        
        
            
        rpcIntParam.value = self.value
            
        
        


class FloatParam:
    """
     Type for float parameters.

     Parameters
     ----------
     name : std::string
          Name of the parameter

     value : float
          Value of the parameter

     """

    

    def __init__(
            self,
            name,
            value):
        """ Initializes the FloatParam object """
        self.name = name
        self.value = value

    def __eq__(self, to_compare):
        """ Checks if two FloatParam are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FloatParam object
            return \
                (self.name == to_compare.name) and \
                (self.value == to_compare.value)

        except AttributeError:
            return False

    def __str__(self):
        """ FloatParam in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "value: " + str(self.value)
                ])

        return f"FloatParam: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFloatParam):
        """ Translates a gRPC struct to the SDK equivalent """
        return FloatParam(
                
                rpcFloatParam.name,
                
                
                rpcFloatParam.value
                )

    def translate_to_rpc(self, rpcFloatParam):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFloatParam.name = self.name
            
        
        
        
            
        rpcFloatParam.value = self.value
            
        
        


class CustomParam:
    """
     Type for custom parameters

     Parameters
     ----------
     name : std::string
          Name of the parameter

     value : std::string
          Value of the parameter (max len 128 bytes)

     """

    

    def __init__(
            self,
            name,
            value):
        """ Initializes the CustomParam object """
        self.name = name
        self.value = value

    def __eq__(self, to_compare):
        """ Checks if two CustomParam are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CustomParam object
            return \
                (self.name == to_compare.name) and \
                (self.value == to_compare.value)

        except AttributeError:
            return False

    def __str__(self):
        """ CustomParam in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "value: " + str(self.value)
                ])

        return f"CustomParam: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCustomParam):
        """ Translates a gRPC struct to the SDK equivalent """
        return CustomParam(
                
                rpcCustomParam.name,
                
                
                rpcCustomParam.value
                )

    def translate_to_rpc(self, rpcCustomParam):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCustomParam.name = self.name
            
        
        
        
            
        rpcCustomParam.value = self.value
            
        
        


class AllParams:
    """
     Type collecting all integer, float, and custom parameters.

     Parameters
     ----------
     int_params : [IntParam]
          Collection of all parameter names and values of type int

     float_params : [FloatParam]
          Collection of all parameter names and values of type float

     custom_params : [CustomParam]
          Collection of all parameter names and values of type custom

     """

    

    def __init__(
            self,
            int_params,
            float_params,
            custom_params):
        """ Initializes the AllParams object """
        self.int_params = int_params
        self.float_params = float_params
        self.custom_params = custom_params

    def __eq__(self, to_compare):
        """ Checks if two AllParams are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AllParams object
            return \
                (self.int_params == to_compare.int_params) and \
                (self.float_params == to_compare.float_params) and \
                (self.custom_params == to_compare.custom_params)

        except AttributeError:
            return False

    def __str__(self):
        """ AllParams in string representation """
        struct_repr = ", ".join([
                "int_params: " + str(self.int_params),
                "float_params: " + str(self.float_params),
                "custom_params: " + str(self.custom_params)
                ])

        return f"AllParams: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAllParams):
        """ Translates a gRPC struct to the SDK equivalent """
        return AllParams(
                
                list(map(lambda elem: IntParam.translate_from_rpc(elem), rpcAllParams.int_params)),
                
                
                list(map(lambda elem: FloatParam.translate_from_rpc(elem), rpcAllParams.float_params)),
                
                
                list(map(lambda elem: CustomParam.translate_from_rpc(elem), rpcAllParams.custom_params))
                )

    def translate_to_rpc(self, rpcAllParams):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.int_params:
                
            rpc_elem = param_pb2.IntParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.int_params.extend(rpc_elems_list)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.float_params:
                
            rpc_elem = param_pb2.FloatParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.float_params.extend(rpc_elems_list)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.custom_params:
                
            rpc_elem = param_pb2.CustomParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.custom_params.extend(rpc_elems_list)
            
        
        


class ParamResult:
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
         Possible results returned for param requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         TIMEOUT
              Request timed out

         CONNECTION_ERROR
              Connection error

         WRONG_TYPE
              Wrong type

         PARAM_NAME_TOO_LONG
              Parameter name too long (> 16)

         NO_SYSTEM
              No system connected

         PARAM_VALUE_TOO_LONG
              Param value too long (> 128)

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        TIMEOUT = 2
        CONNECTION_ERROR = 3
        WRONG_TYPE = 4
        PARAM_NAME_TOO_LONG = 5
        NO_SYSTEM = 6
        PARAM_VALUE_TOO_LONG = 7

        def translate_to_rpc(self):
            if self == ParamResult.Result.UNKNOWN:
                return param_pb2.ParamResult.RESULT_UNKNOWN
            if self == ParamResult.Result.SUCCESS:
                return param_pb2.ParamResult.RESULT_SUCCESS
            if self == ParamResult.Result.TIMEOUT:
                return param_pb2.ParamResult.RESULT_TIMEOUT
            if self == ParamResult.Result.CONNECTION_ERROR:
                return param_pb2.ParamResult.RESULT_CONNECTION_ERROR
            if self == ParamResult.Result.WRONG_TYPE:
                return param_pb2.ParamResult.RESULT_WRONG_TYPE
            if self == ParamResult.Result.PARAM_NAME_TOO_LONG:
                return param_pb2.ParamResult.RESULT_PARAM_NAME_TOO_LONG
            if self == ParamResult.Result.NO_SYSTEM:
                return param_pb2.ParamResult.RESULT_NO_SYSTEM
            if self == ParamResult.Result.PARAM_VALUE_TOO_LONG:
                return param_pb2.ParamResult.RESULT_PARAM_VALUE_TOO_LONG

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == param_pb2.ParamResult.RESULT_UNKNOWN:
                return ParamResult.Result.UNKNOWN
            if rpc_enum_value == param_pb2.ParamResult.RESULT_SUCCESS:
                return ParamResult.Result.SUCCESS
            if rpc_enum_value == param_pb2.ParamResult.RESULT_TIMEOUT:
                return ParamResult.Result.TIMEOUT
            if rpc_enum_value == param_pb2.ParamResult.RESULT_CONNECTION_ERROR:
                return ParamResult.Result.CONNECTION_ERROR
            if rpc_enum_value == param_pb2.ParamResult.RESULT_WRONG_TYPE:
                return ParamResult.Result.WRONG_TYPE
            if rpc_enum_value == param_pb2.ParamResult.RESULT_PARAM_NAME_TOO_LONG:
                return ParamResult.Result.PARAM_NAME_TOO_LONG
            if rpc_enum_value == param_pb2.ParamResult.RESULT_NO_SYSTEM:
                return ParamResult.Result.NO_SYSTEM
            if rpc_enum_value == param_pb2.ParamResult.RESULT_PARAM_VALUE_TOO_LONG:
                return ParamResult.Result.PARAM_VALUE_TOO_LONG

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ParamResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ParamResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ParamResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ParamResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ParamResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcParamResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ParamResult(
                
                ParamResult.Result.translate_from_rpc(rpcParamResult.result),
                
                
                rpcParamResult.result_str
                )

    def translate_to_rpc(self, rpcParamResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcParamResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcParamResult.result_str = self.result_str
            
        
        



class ParamError(Exception):
    """ Raised when a ParamResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Param(AsyncBase):
    """
     Provide raw access to get and set parameters.

     Generated by dcsdkgen - MAVSDK Param API
    """

    # Plugin name
    name = "Param"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = param_pb2_grpc.ParamServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ParamResult.translate_from_rpc(response.param_result)
    

    async def get_param_int(self, name):
        """
         Get an int parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter

         Returns
         -------
         value : int32_t
              Value of the requested parameter

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.GetParamIntRequest()
        
            
        request.name = name
            
        response = await self._stub.GetParamInt(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "get_param_int()", name)
        

        return response.value
        

    async def set_param_int(self, name, value):
        """
         Set an int parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to set

         value : int32_t
              Value the parameter should be set to

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.SetParamIntRequest()
        request.name = name
        request.value = value
        response = await self._stub.SetParamInt(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "set_param_int()", name, value)
        

    async def get_param_float(self, name):
        """
         Get a float parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter

         Returns
         -------
         value : float
              Value of the requested parameter

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.GetParamFloatRequest()
        
            
        request.name = name
            
        response = await self._stub.GetParamFloat(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "get_param_float()", name)
        

        return response.value
        

    async def set_param_float(self, name, value):
        """
         Set a float parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to set

         value : float
              Value the parameter should be set to

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.SetParamFloatRequest()
        request.name = name
        request.value = value
        response = await self._stub.SetParamFloat(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "set_param_float()", name, value)
        

    async def get_param_custom(self, name):
        """
         Get a custom parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter

         Returns
         -------
         value : std::string
              Value of the requested parameter

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.GetParamCustomRequest()
        
            
        request.name = name
            
        response = await self._stub.GetParamCustom(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "get_param_custom()", name)
        

        return response.value
        

    async def set_param_custom(self, name, value):
        """
         Set a custom parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to set

         value : std::string
              Value the parameter should be set to

         Raises
         ------
         ParamError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_pb2.SetParamCustomRequest()
        request.name = name
        request.value = value
        response = await self._stub.SetParamCustom(request)

        
        result = self._extract_result(response)

        if result.result != ParamResult.Result.SUCCESS:
            raise ParamError(result, "set_param_custom()", name, value)
        

    async def get_all_params(self):
        """
         Get all parameters.

         Returns
         -------
         params : AllParams
              Collection of all parameters

         
        """

        request = param_pb2.GetAllParamsRequest()
        response = await self._stub.GetAllParams(request)

        

        return AllParams.translate_from_rpc(response.params)
            