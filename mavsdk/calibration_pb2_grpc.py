# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import calibration_pb2 as calibration_dot_calibration__pb2

GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in calibration/calibration_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CalibrationServiceStub(object):
    """Enable to calibrate sensors of a drone such as gyro, accelerometer, and magnetometer.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeCalibrateGyro = channel.unary_stream(
                '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateGyro',
                request_serializer=calibration_dot_calibration__pb2.SubscribeCalibrateGyroRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CalibrateGyroResponse.FromString,
                _registered_method=True)
        self.SubscribeCalibrateAccelerometer = channel.unary_stream(
                '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateAccelerometer',
                request_serializer=calibration_dot_calibration__pb2.SubscribeCalibrateAccelerometerRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CalibrateAccelerometerResponse.FromString,
                _registered_method=True)
        self.SubscribeCalibrateMagnetometer = channel.unary_stream(
                '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateMagnetometer',
                request_serializer=calibration_dot_calibration__pb2.SubscribeCalibrateMagnetometerRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CalibrateMagnetometerResponse.FromString,
                _registered_method=True)
        self.SubscribeCalibrateLevelHorizon = channel.unary_stream(
                '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateLevelHorizon',
                request_serializer=calibration_dot_calibration__pb2.SubscribeCalibrateLevelHorizonRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CalibrateLevelHorizonResponse.FromString,
                _registered_method=True)
        self.SubscribeCalibrateGimbalAccelerometer = channel.unary_stream(
                '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateGimbalAccelerometer',
                request_serializer=calibration_dot_calibration__pb2.SubscribeCalibrateGimbalAccelerometerRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CalibrateGimbalAccelerometerResponse.FromString,
                _registered_method=True)
        self.Cancel = channel.unary_unary(
                '/mavsdk.rpc.calibration.CalibrationService/Cancel',
                request_serializer=calibration_dot_calibration__pb2.CancelRequest.SerializeToString,
                response_deserializer=calibration_dot_calibration__pb2.CancelResponse.FromString,
                _registered_method=True)


class CalibrationServiceServicer(object):
    """Enable to calibrate sensors of a drone such as gyro, accelerometer, and magnetometer.
    """

    def SubscribeCalibrateGyro(self, request, context):
        """Perform gyro calibration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCalibrateAccelerometer(self, request, context):
        """Perform accelerometer calibration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCalibrateMagnetometer(self, request, context):
        """Perform magnetometer calibration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCalibrateLevelHorizon(self, request, context):
        """Perform board level horizon calibration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeCalibrateGimbalAccelerometer(self, request, context):
        """Perform gimbal accelerometer calibration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Cancel(self, request, context):
        """Cancel ongoing calibration process.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalibrationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeCalibrateGyro': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCalibrateGyro,
                    request_deserializer=calibration_dot_calibration__pb2.SubscribeCalibrateGyroRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CalibrateGyroResponse.SerializeToString,
            ),
            'SubscribeCalibrateAccelerometer': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCalibrateAccelerometer,
                    request_deserializer=calibration_dot_calibration__pb2.SubscribeCalibrateAccelerometerRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CalibrateAccelerometerResponse.SerializeToString,
            ),
            'SubscribeCalibrateMagnetometer': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCalibrateMagnetometer,
                    request_deserializer=calibration_dot_calibration__pb2.SubscribeCalibrateMagnetometerRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CalibrateMagnetometerResponse.SerializeToString,
            ),
            'SubscribeCalibrateLevelHorizon': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCalibrateLevelHorizon,
                    request_deserializer=calibration_dot_calibration__pb2.SubscribeCalibrateLevelHorizonRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CalibrateLevelHorizonResponse.SerializeToString,
            ),
            'SubscribeCalibrateGimbalAccelerometer': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeCalibrateGimbalAccelerometer,
                    request_deserializer=calibration_dot_calibration__pb2.SubscribeCalibrateGimbalAccelerometerRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CalibrateGimbalAccelerometerResponse.SerializeToString,
            ),
            'Cancel': grpc.unary_unary_rpc_method_handler(
                    servicer.Cancel,
                    request_deserializer=calibration_dot_calibration__pb2.CancelRequest.FromString,
                    response_serializer=calibration_dot_calibration__pb2.CancelResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.calibration.CalibrationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.calibration.CalibrationService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CalibrationService(object):
    """Enable to calibrate sensors of a drone such as gyro, accelerometer, and magnetometer.
    """

    @staticmethod
    def SubscribeCalibrateGyro(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateGyro',
            calibration_dot_calibration__pb2.SubscribeCalibrateGyroRequest.SerializeToString,
            calibration_dot_calibration__pb2.CalibrateGyroResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeCalibrateAccelerometer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateAccelerometer',
            calibration_dot_calibration__pb2.SubscribeCalibrateAccelerometerRequest.SerializeToString,
            calibration_dot_calibration__pb2.CalibrateAccelerometerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeCalibrateMagnetometer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateMagnetometer',
            calibration_dot_calibration__pb2.SubscribeCalibrateMagnetometerRequest.SerializeToString,
            calibration_dot_calibration__pb2.CalibrateMagnetometerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeCalibrateLevelHorizon(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateLevelHorizon',
            calibration_dot_calibration__pb2.SubscribeCalibrateLevelHorizonRequest.SerializeToString,
            calibration_dot_calibration__pb2.CalibrateLevelHorizonResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeCalibrateGimbalAccelerometer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/SubscribeCalibrateGimbalAccelerometer',
            calibration_dot_calibration__pb2.SubscribeCalibrateGimbalAccelerometerRequest.SerializeToString,
            calibration_dot_calibration__pb2.CalibrateGimbalAccelerometerResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Cancel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mavsdk.rpc.calibration.CalibrationService/Cancel',
            calibration_dot_calibration__pb2.CancelRequest.SerializeToString,
            calibration_dot_calibration__pb2.CancelResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
