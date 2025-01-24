# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import param_server_pb2, param_server_pb2_grpc
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
     Type for float parameters.

     Parameters
     ----------
     name : std::string
          Name of the parameter

     value : std::string
          Value of the parameter

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
                
            rpc_elem = param_server_pb2.IntParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.int_params.extend(rpc_elems_list)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.float_params:
                
            rpc_elem = param_server_pb2.FloatParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.float_params.extend(rpc_elems_list)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.custom_params:
                
            rpc_elem = param_server_pb2.CustomParam()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcAllParams.custom_params.extend(rpc_elems_list)
            
        
        


class ParamServerResult:
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

         NOT_FOUND
              Not Found

         WRONG_TYPE
              Wrong type

         PARAM_NAME_TOO_LONG
              Parameter name too long (> 16)

         NO_SYSTEM
              No system available

         PARAM_VALUE_TOO_LONG
              Parameter name too long (> 128)

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NOT_FOUND = 2
        WRONG_TYPE = 3
        PARAM_NAME_TOO_LONG = 4
        NO_SYSTEM = 5
        PARAM_VALUE_TOO_LONG = 6

        def translate_to_rpc(self):
            if self == ParamServerResult.Result.UNKNOWN:
                return param_server_pb2.ParamServerResult.RESULT_UNKNOWN
            if self == ParamServerResult.Result.SUCCESS:
                return param_server_pb2.ParamServerResult.RESULT_SUCCESS
            if self == ParamServerResult.Result.NOT_FOUND:
                return param_server_pb2.ParamServerResult.RESULT_NOT_FOUND
            if self == ParamServerResult.Result.WRONG_TYPE:
                return param_server_pb2.ParamServerResult.RESULT_WRONG_TYPE
            if self == ParamServerResult.Result.PARAM_NAME_TOO_LONG:
                return param_server_pb2.ParamServerResult.RESULT_PARAM_NAME_TOO_LONG
            if self == ParamServerResult.Result.NO_SYSTEM:
                return param_server_pb2.ParamServerResult.RESULT_NO_SYSTEM
            if self == ParamServerResult.Result.PARAM_VALUE_TOO_LONG:
                return param_server_pb2.ParamServerResult.RESULT_PARAM_VALUE_TOO_LONG

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_UNKNOWN:
                return ParamServerResult.Result.UNKNOWN
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_SUCCESS:
                return ParamServerResult.Result.SUCCESS
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_NOT_FOUND:
                return ParamServerResult.Result.NOT_FOUND
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_WRONG_TYPE:
                return ParamServerResult.Result.WRONG_TYPE
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_PARAM_NAME_TOO_LONG:
                return ParamServerResult.Result.PARAM_NAME_TOO_LONG
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_NO_SYSTEM:
                return ParamServerResult.Result.NO_SYSTEM
            if rpc_enum_value == param_server_pb2.ParamServerResult.RESULT_PARAM_VALUE_TOO_LONG:
                return ParamServerResult.Result.PARAM_VALUE_TOO_LONG

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ParamServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ParamServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ParamServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ParamServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ParamServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcParamServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ParamServerResult(
                
                ParamServerResult.Result.translate_from_rpc(rpcParamServerResult.result),
                
                
                rpcParamServerResult.result_str
                )

    def translate_to_rpc(self, rpcParamServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcParamServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcParamServerResult.result_str = self.result_str
            
        
        



class ParamServerError(Exception):
    """ Raised when a ParamServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ParamServer(AsyncBase):
    """
     Provide raw access to retrieve and provide server parameters.

     Generated by dcsdkgen - MAVSDK ParamServer API
    """

    # Plugin name
    name = "ParamServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = param_server_pb2_grpc.ParamServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ParamServerResult.translate_from_rpc(response.param_server_result)
    

    async def set_protocol(self, extended_protocol):
        """
         Set param protocol.

         The extended param protocol is used by default. This allows to use the previous/normal one.

         Note that camera definition files are meant to implement/use the extended protocol.

         Parameters
         ----------
         extended_protocol : bool
              Use extended protocol

         Raises
         ------
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.SetProtocolRequest()
        request.extended_protocol = extended_protocol
        response = await self._stub.SetProtocol(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "set_protocol()", extended_protocol)
        

    async def retrieve_param_int(self, name):
        """
         Retrieve an int parameter.

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
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.RetrieveParamIntRequest()
        
            
        request.name = name
            
        response = await self._stub.RetrieveParamInt(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "retrieve_param_int()", name)
        

        return response.value
        

    async def provide_param_int(self, name, value):
        """
         Provide an int parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to provide

         value : int32_t
              Value the parameter should be set to

         Raises
         ------
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.ProvideParamIntRequest()
        request.name = name
        request.value = value
        response = await self._stub.ProvideParamInt(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "provide_param_int()", name, value)
        

    async def retrieve_param_float(self, name):
        """
         Retrieve a float parameter.

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
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.RetrieveParamFloatRequest()
        
            
        request.name = name
            
        response = await self._stub.RetrieveParamFloat(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "retrieve_param_float()", name)
        

        return response.value
        

    async def provide_param_float(self, name, value):
        """
         Provide a float parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to provide

         value : float
              Value the parameter should be set to

         Raises
         ------
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.ProvideParamFloatRequest()
        request.name = name
        request.value = value
        response = await self._stub.ProvideParamFloat(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "provide_param_float()", name, value)
        

    async def retrieve_param_custom(self, name):
        """
         Retrieve a custom parameter.

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
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.RetrieveParamCustomRequest()
        
            
        request.name = name
            
        response = await self._stub.RetrieveParamCustom(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "retrieve_param_custom()", name)
        

        return response.value
        

    async def provide_param_custom(self, name, value):
        """
         Provide a custom parameter.

         If the type is wrong, the result will be `WRONG_TYPE`.

         Parameters
         ----------
         name : std::string
              Name of the parameter to provide

         value : std::string
              Value the parameter should be set to

         Raises
         ------
         ParamServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = param_server_pb2.ProvideParamCustomRequest()
        request.name = name
        request.value = value
        response = await self._stub.ProvideParamCustom(request)

        
        result = self._extract_result(response)

        if result.result != ParamServerResult.Result.SUCCESS:
            raise ParamServerError(result, "provide_param_custom()", name, value)
        

    async def retrieve_all_params(self):
        """
         Retrieve all parameters.

         Returns
         -------
         params : AllParams
              Collection of all parameters

         
        """

        request = param_server_pb2.RetrieveAllParamsRequest()
        response = await self._stub.RetrieveAllParams(request)

        

        return AllParams.translate_from_rpc(response.params)
            

    async def changed_param_int(self):
        """
         Subscribe to changed int param.

         Yields
         -------
         param : IntParam
              Param that changed

         
        """

        request = param_server_pb2.SubscribeChangedParamIntRequest()
        changed_param_int_stream = self._stub.SubscribeChangedParamInt(request)

        try:
            async for response in changed_param_int_stream:
                

            
                yield IntParam.translate_from_rpc(response.param)
        finally:
            changed_param_int_stream.cancel()

    async def changed_param_float(self):
        """
         Subscribe to changed float param.

         Yields
         -------
         param : FloatParam
              Param that changed

         
        """

        request = param_server_pb2.SubscribeChangedParamFloatRequest()
        changed_param_float_stream = self._stub.SubscribeChangedParamFloat(request)

        try:
            async for response in changed_param_float_stream:
                

            
                yield FloatParam.translate_from_rpc(response.param)
        finally:
            changed_param_float_stream.cancel()

    async def changed_param_custom(self):
        """
         Subscribe to changed custom param.

         Yields
         -------
         param : CustomParam
              Param that changed

         
        """

        request = param_server_pb2.SubscribeChangedParamCustomRequest()
        changed_param_custom_stream = self._stub.SubscribeChangedParamCustom(request)

        try:
            async for response in changed_param_custom_stream:
                

            
                yield CustomParam.translate_from_rpc(response.param)
        finally:
            changed_param_custom_stream.cancel()