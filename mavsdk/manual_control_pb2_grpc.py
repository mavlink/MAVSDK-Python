# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import manual_control_pb2 as manual__control_dot_manual__control__pb2

GRPC_GENERATED_VERSION = '1.63.0'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.65.0'
SCHEDULED_RELEASE_DATE = 'June 25, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in manual_control/manual_control_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class ManualControlServiceStub(object):
    """Enable manual control using e.g. a joystick or gamepad.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartPositionControl = channel.unary_unary(
                '/mavsdk.rpc.manual_control.ManualControlService/StartPositionControl',
                request_serializer=manual__control_dot_manual__control__pb2.StartPositionControlRequest.SerializeToString,
                response_deserializer=manual__control_dot_manual__control__pb2.StartPositionControlResponse.FromString,
                _registered_method=True)
        self.StartAltitudeControl = channel.unary_unary(
                '/mavsdk.rpc.manual_control.ManualControlService/StartAltitudeControl',
                request_serializer=manual__control_dot_manual__control__pb2.StartAltitudeControlRequest.SerializeToString,
                response_deserializer=manual__control_dot_manual__control__pb2.StartAltitudeControlResponse.FromString,
                _registered_method=True)
        self.SetManualControlInput = channel.unary_unary(
                '/mavsdk.rpc.manual_control.ManualControlService/SetManualControlInput',
                request_serializer=manual__control_dot_manual__control__pb2.SetManualControlInputRequest.SerializeToString,
                response_deserializer=manual__control_dot_manual__control__pb2.SetManualControlInputResponse.FromString,
                _registered_method=True)


class ManualControlServiceServicer(object):
    """Enable manual control using e.g. a joystick or gamepad.
    """

    def StartPositionControl(self, request, context):
        """
        Start position control using e.g. joystick input.

        Requires manual control input to be sent regularly already.
        Requires a valid position using e.g. GPS, external vision, or optical flow.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def StartAltitudeControl(self, request, context):
        """
        Start altitude control

        Requires manual control input to be sent regularly already.
        Does not require a  valid position e.g. GPS.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetManualControlInput(self, request, context):
        """
        Set manual control input

        The manual control input needs to be sent at a rate high enough to prevent
        triggering of RC loss, a good minimum rate is 10 Hz.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ManualControlServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartPositionControl': grpc.unary_unary_rpc_method_handler(
                    servicer.StartPositionControl,
                    request_deserializer=manual__control_dot_manual__control__pb2.StartPositionControlRequest.FromString,
                    response_serializer=manual__control_dot_manual__control__pb2.StartPositionControlResponse.SerializeToString,
            ),
            'StartAltitudeControl': grpc.unary_unary_rpc_method_handler(
                    servicer.StartAltitudeControl,
                    request_deserializer=manual__control_dot_manual__control__pb2.StartAltitudeControlRequest.FromString,
                    response_serializer=manual__control_dot_manual__control__pb2.StartAltitudeControlResponse.SerializeToString,
            ),
            'SetManualControlInput': grpc.unary_unary_rpc_method_handler(
                    servicer.SetManualControlInput,
                    request_deserializer=manual__control_dot_manual__control__pb2.SetManualControlInputRequest.FromString,
                    response_serializer=manual__control_dot_manual__control__pb2.SetManualControlInputResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.manual_control.ManualControlService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ManualControlService(object):
    """Enable manual control using e.g. a joystick or gamepad.
    """

    @staticmethod
    def StartPositionControl(request,
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
            '/mavsdk.rpc.manual_control.ManualControlService/StartPositionControl',
            manual__control_dot_manual__control__pb2.StartPositionControlRequest.SerializeToString,
            manual__control_dot_manual__control__pb2.StartPositionControlResponse.FromString,
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
    def StartAltitudeControl(request,
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
            '/mavsdk.rpc.manual_control.ManualControlService/StartAltitudeControl',
            manual__control_dot_manual__control__pb2.StartAltitudeControlRequest.SerializeToString,
            manual__control_dot_manual__control__pb2.StartAltitudeControlResponse.FromString,
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
    def SetManualControlInput(request,
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
            '/mavsdk.rpc.manual_control.ManualControlService/SetManualControlInput',
            manual__control_dot_manual__control__pb2.SetManualControlInputRequest.SerializeToString,
            manual__control_dot_manual__control__pb2.SetManualControlInputResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
