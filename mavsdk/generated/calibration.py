# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import calibration_pb2, calibration_pb2_grpc
from enum import Enum


class CalibrationResult:
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
         Possible results returned for calibration commands

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              The calibration succeeded

         NEXT
              Intermediate message showing progress or instructions on the next steps

         FAILED
              Calibration failed

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         TIMEOUT
              Command timed out

         CANCELLED
              Calibration process was cancelled

         FAILED_ARMED
              Calibration process failed since the vehicle is armed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NEXT = 2
        FAILED = 3
        NO_SYSTEM = 4
        CONNECTION_ERROR = 5
        BUSY = 6
        COMMAND_DENIED = 7
        TIMEOUT = 8
        CANCELLED = 9
        FAILED_ARMED = 10

        def translate_to_rpc(self):
            if self == CalibrationResult.Result.UNKNOWN:
                return calibration_pb2.CalibrationResult.RESULT_UNKNOWN
            if self == CalibrationResult.Result.SUCCESS:
                return calibration_pb2.CalibrationResult.RESULT_SUCCESS
            if self == CalibrationResult.Result.NEXT:
                return calibration_pb2.CalibrationResult.RESULT_NEXT
            if self == CalibrationResult.Result.FAILED:
                return calibration_pb2.CalibrationResult.RESULT_FAILED
            if self == CalibrationResult.Result.NO_SYSTEM:
                return calibration_pb2.CalibrationResult.RESULT_NO_SYSTEM
            if self == CalibrationResult.Result.CONNECTION_ERROR:
                return calibration_pb2.CalibrationResult.RESULT_CONNECTION_ERROR
            if self == CalibrationResult.Result.BUSY:
                return calibration_pb2.CalibrationResult.RESULT_BUSY
            if self == CalibrationResult.Result.COMMAND_DENIED:
                return calibration_pb2.CalibrationResult.RESULT_COMMAND_DENIED
            if self == CalibrationResult.Result.TIMEOUT:
                return calibration_pb2.CalibrationResult.RESULT_TIMEOUT
            if self == CalibrationResult.Result.CANCELLED:
                return calibration_pb2.CalibrationResult.RESULT_CANCELLED
            if self == CalibrationResult.Result.FAILED_ARMED:
                return calibration_pb2.CalibrationResult.RESULT_FAILED_ARMED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_UNKNOWN:
                return CalibrationResult.Result.UNKNOWN
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_SUCCESS:
                return CalibrationResult.Result.SUCCESS
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_NEXT:
                return CalibrationResult.Result.NEXT
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_FAILED:
                return CalibrationResult.Result.FAILED
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_NO_SYSTEM:
                return CalibrationResult.Result.NO_SYSTEM
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_CONNECTION_ERROR:
                return CalibrationResult.Result.CONNECTION_ERROR
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_BUSY:
                return CalibrationResult.Result.BUSY
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_COMMAND_DENIED:
                return CalibrationResult.Result.COMMAND_DENIED
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_TIMEOUT:
                return CalibrationResult.Result.TIMEOUT
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_CANCELLED:
                return CalibrationResult.Result.CANCELLED
            if rpc_enum_value == calibration_pb2.CalibrationResult.RESULT_FAILED_ARMED:
                return CalibrationResult.Result.FAILED_ARMED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the CalibrationResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two CalibrationResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CalibrationResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ CalibrationResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"CalibrationResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcCalibrationResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return CalibrationResult(
                
                CalibrationResult.Result.translate_from_rpc(rpcCalibrationResult.result),
                
                
                rpcCalibrationResult.result_str
                )

    def translate_to_rpc(self, rpcCalibrationResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcCalibrationResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcCalibrationResult.result_str = self.result_str
            
        
        


class ProgressData:
    """
     Progress data coming from calibration.

     Can be a progress percentage, or an instruction text.

     Parameters
     ----------
     has_progress : bool
          Whether this ProgressData contains a 'progress' status or not

     progress : float
          Progress (percentage)

     has_status_text : bool
          Whether this ProgressData contains a 'status_text' or not

     status_text : std::string
          Instruction text

     """

    

    def __init__(
            self,
            has_progress,
            progress,
            has_status_text,
            status_text):
        """ Initializes the ProgressData object """
        self.has_progress = has_progress
        self.progress = progress
        self.has_status_text = has_status_text
        self.status_text = status_text

    def __equals__(self, to_compare):
        """ Checks if two ProgressData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressData object
            return \
                (self.has_progress == to_compare.has_progress) and \
                (self.progress == to_compare.progress) and \
                (self.has_status_text == to_compare.has_status_text) and \
                (self.status_text == to_compare.status_text)

        except AttributeError:
            return False

    def __str__(self):
        """ ProgressData in string representation """
        struct_repr = ", ".join([
                "has_progress: " + str(self.has_progress),
                "progress: " + str(self.progress),
                "has_status_text: " + str(self.has_status_text),
                "status_text: " + str(self.status_text)
                ])

        return f"ProgressData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProgressData):
        """ Translates a gRPC struct to the SDK equivalent """
        return ProgressData(
                
                rpcProgressData.has_progress,
                
                
                rpcProgressData.progress,
                
                
                rpcProgressData.has_status_text,
                
                
                rpcProgressData.status_text
                )

    def translate_to_rpc(self, rpcProgressData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProgressData.has_progress = self.has_progress
            
        
        
        
            
        rpcProgressData.progress = self.progress
            
        
        
        
            
        rpcProgressData.has_status_text = self.has_status_text
            
        
        
        
            
        rpcProgressData.status_text = self.status_text
            
        
        



class CalibrationError(Exception):
    """ Raised when a CalibrationResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Calibration(AsyncBase):
    """
     Enable to calibrate sensors of a drone such as gyro, accelerometer, and magnetometer.

     Generated by dcsdkgen - MAVSDK Calibration API
    """

    # Plugin name
    name = "Calibration"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = calibration_pb2_grpc.CalibrationServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return CalibrationResult.translate_from_rpc(response.calibration_result)
    

    async def calibrate_gyro(self):
        """
         Perform gyro calibration.

         Yields
         -------
         progress_data : ProgressData
              Progress data

         Raises
         ------
         CalibrationError
             If the request fails. The error contains the reason for the failure.
        """

        request = calibration_pb2.SubscribeCalibrateGyroRequest()
        calibrate_gyro_stream = self._stub.SubscribeCalibrateGyro(request)

        try:
            async for response in calibrate_gyro_stream:
                
                result = self._extract_result(response)

                success_codes = [CalibrationResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in CalibrationResult.Result]:
                    success_codes.append(CalibrationResult.Result.NEXT)

                if result.result not in success_codes:
                    raise CalibrationError(result, "calibrate_gyro()")

                if result.result is CalibrationResult.Result.SUCCESS:
                    calibrate_gyro_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            calibrate_gyro_stream.cancel()

    async def calibrate_accelerometer(self):
        """
         Perform accelerometer calibration.

         Yields
         -------
         progress_data : ProgressData
              Progress data

         Raises
         ------
         CalibrationError
             If the request fails. The error contains the reason for the failure.
        """

        request = calibration_pb2.SubscribeCalibrateAccelerometerRequest()
        calibrate_accelerometer_stream = self._stub.SubscribeCalibrateAccelerometer(request)

        try:
            async for response in calibrate_accelerometer_stream:
                
                result = self._extract_result(response)

                success_codes = [CalibrationResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in CalibrationResult.Result]:
                    success_codes.append(CalibrationResult.Result.NEXT)

                if result.result not in success_codes:
                    raise CalibrationError(result, "calibrate_accelerometer()")

                if result.result is CalibrationResult.Result.SUCCESS:
                    calibrate_accelerometer_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            calibrate_accelerometer_stream.cancel()

    async def calibrate_magnetometer(self):
        """
         Perform magnetometer calibration.

         Yields
         -------
         progress_data : ProgressData
              Progress data

         Raises
         ------
         CalibrationError
             If the request fails. The error contains the reason for the failure.
        """

        request = calibration_pb2.SubscribeCalibrateMagnetometerRequest()
        calibrate_magnetometer_stream = self._stub.SubscribeCalibrateMagnetometer(request)

        try:
            async for response in calibrate_magnetometer_stream:
                
                result = self._extract_result(response)

                success_codes = [CalibrationResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in CalibrationResult.Result]:
                    success_codes.append(CalibrationResult.Result.NEXT)

                if result.result not in success_codes:
                    raise CalibrationError(result, "calibrate_magnetometer()")

                if result.result is CalibrationResult.Result.SUCCESS:
                    calibrate_magnetometer_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            calibrate_magnetometer_stream.cancel()

    async def calibrate_level_horizon(self):
        """
         Perform board level horizon calibration.

         Yields
         -------
         progress_data : ProgressData
              Progress data

         Raises
         ------
         CalibrationError
             If the request fails. The error contains the reason for the failure.
        """

        request = calibration_pb2.SubscribeCalibrateLevelHorizonRequest()
        calibrate_level_horizon_stream = self._stub.SubscribeCalibrateLevelHorizon(request)

        try:
            async for response in calibrate_level_horizon_stream:
                
                result = self._extract_result(response)

                success_codes = [CalibrationResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in CalibrationResult.Result]:
                    success_codes.append(CalibrationResult.Result.NEXT)

                if result.result not in success_codes:
                    raise CalibrationError(result, "calibrate_level_horizon()")

                if result.result is CalibrationResult.Result.SUCCESS:
                    calibrate_level_horizon_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            calibrate_level_horizon_stream.cancel()

    async def calibrate_gimbal_accelerometer(self):
        """
         Perform gimbal accelerometer calibration.

         Yields
         -------
         progress_data : ProgressData
              Progress data

         Raises
         ------
         CalibrationError
             If the request fails. The error contains the reason for the failure.
        """

        request = calibration_pb2.SubscribeCalibrateGimbalAccelerometerRequest()
        calibrate_gimbal_accelerometer_stream = self._stub.SubscribeCalibrateGimbalAccelerometer(request)

        try:
            async for response in calibrate_gimbal_accelerometer_stream:
                
                result = self._extract_result(response)

                success_codes = [CalibrationResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in CalibrationResult.Result]:
                    success_codes.append(CalibrationResult.Result.NEXT)

                if result.result not in success_codes:
                    raise CalibrationError(result, "calibrate_gimbal_accelerometer()")

                if result.result is CalibrationResult.Result.SUCCESS:
                    calibrate_gimbal_accelerometer_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            calibrate_gimbal_accelerometer_stream.cancel()

    async def cancel(self):
        """
         Cancel ongoing calibration process.

         
        """

        request = calibration_pb2.CancelRequest()
        response = await self._stub.Cancel(request)

        