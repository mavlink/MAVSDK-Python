# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import gimbal_pb2 as gimbal_dot_gimbal__pb2

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
        + f' but the generated code in gimbal/gimbal_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GimbalServiceStub(object):
    """Provide control over a gimbal.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetAngles = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetAngles',
                request_serializer=gimbal_dot_gimbal__pb2.SetAnglesRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetAnglesResponse.FromString,
                _registered_method=True)
        self.SetAngularRates = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetAngularRates',
                request_serializer=gimbal_dot_gimbal__pb2.SetAngularRatesRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetAngularRatesResponse.FromString,
                _registered_method=True)
        self.SetRoiLocation = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/SetRoiLocation',
                request_serializer=gimbal_dot_gimbal__pb2.SetRoiLocationRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.SetRoiLocationResponse.FromString,
                _registered_method=True)
        self.TakeControl = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/TakeControl',
                request_serializer=gimbal_dot_gimbal__pb2.TakeControlRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.TakeControlResponse.FromString,
                _registered_method=True)
        self.ReleaseControl = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/ReleaseControl',
                request_serializer=gimbal_dot_gimbal__pb2.ReleaseControlRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.ReleaseControlResponse.FromString,
                _registered_method=True)
        self.SubscribeGimbalList = channel.unary_stream(
                '/mavsdk.rpc.gimbal.GimbalService/SubscribeGimbalList',
                request_serializer=gimbal_dot_gimbal__pb2.SubscribeGimbalListRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.GimbalListResponse.FromString,
                _registered_method=True)
        self.SubscribeControlStatus = channel.unary_stream(
                '/mavsdk.rpc.gimbal.GimbalService/SubscribeControlStatus',
                request_serializer=gimbal_dot_gimbal__pb2.SubscribeControlStatusRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.ControlStatusResponse.FromString,
                _registered_method=True)
        self.GetControlStatus = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/GetControlStatus',
                request_serializer=gimbal_dot_gimbal__pb2.GetControlStatusRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.GetControlStatusResponse.FromString,
                _registered_method=True)
        self.SubscribeAttitude = channel.unary_stream(
                '/mavsdk.rpc.gimbal.GimbalService/SubscribeAttitude',
                request_serializer=gimbal_dot_gimbal__pb2.SubscribeAttitudeRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.AttitudeResponse.FromString,
                _registered_method=True)
        self.GetAttitude = channel.unary_unary(
                '/mavsdk.rpc.gimbal.GimbalService/GetAttitude',
                request_serializer=gimbal_dot_gimbal__pb2.GetAttitudeRequest.SerializeToString,
                response_deserializer=gimbal_dot_gimbal__pb2.GetAttitudeResponse.FromString,
                _registered_method=True)


class GimbalServiceServicer(object):
    """Provide control over a gimbal.
    """

    def SetAngles(self, request, context):
        """
        Set gimbal roll, pitch and yaw angles.

        This sets the desired roll, pitch and yaw angles of a gimbal.
        Will return when the command is accepted, however, it might
        take the gimbal longer to actually be set to the new angles.

        Note that the roll angle needs to be set to 0 when send_mode is Once.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetAngularRates(self, request, context):
        """
        Set gimbal angular rates.

        This sets the desired angular rates around roll, pitch and yaw axes of a gimbal.
        Will return when the command is accepted, however, it might
        take the gimbal longer to actually reach the angular rate.

        Note that the roll angle needs to be set to 0 when send_mode is Once.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetRoiLocation(self, request, context):
        """
        Set gimbal region of interest (ROI).

        This sets a region of interest that the gimbal will point to.
        The gimbal will continue to point to the specified region until it
        receives a new command.
        The function will return when the command is accepted, however, it might
        take the gimbal longer to actually rotate to the ROI.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TakeControl(self, request, context):
        """
        Take control.

        There can be only two components in control of a gimbal at any given time.
        One with "primary" control, and one with "secondary" control. The way the
        secondary control is implemented is not specified and hence depends on the
        vehicle.

        Components are expected to be cooperative, which means that they can
        override each other and should therefore do it carefully.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReleaseControl(self, request, context):
        """
        Release control.

        Release control, such that other components can control the gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeGimbalList(self, request, context):
        """
        Subscribe to list of gimbals.

        This allows to find out what gimbals are connected to the system.
        Based on the gimbal ID, we can then address a specific gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeControlStatus(self, request, context):
        """
        Subscribe to control status updates.

        This allows a component to know if it has primary, secondary or
        no control over the gimbal. Also, it gives the system and component ids
        of the other components in control (if any).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetControlStatus(self, request, context):
        """
        Get control status for specific gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeAttitude(self, request, context):
        """
        Subscribe to attitude updates.

        This gets you the gimbal's attitude and angular rate.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttitude(self, request, context):
        """
        Get attitude for specific gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GimbalServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SetAngles': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAngles,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetAnglesRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetAnglesResponse.SerializeToString,
            ),
            'SetAngularRates': grpc.unary_unary_rpc_method_handler(
                    servicer.SetAngularRates,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetAngularRatesRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetAngularRatesResponse.SerializeToString,
            ),
            'SetRoiLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetRoiLocation,
                    request_deserializer=gimbal_dot_gimbal__pb2.SetRoiLocationRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.SetRoiLocationResponse.SerializeToString,
            ),
            'TakeControl': grpc.unary_unary_rpc_method_handler(
                    servicer.TakeControl,
                    request_deserializer=gimbal_dot_gimbal__pb2.TakeControlRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.TakeControlResponse.SerializeToString,
            ),
            'ReleaseControl': grpc.unary_unary_rpc_method_handler(
                    servicer.ReleaseControl,
                    request_deserializer=gimbal_dot_gimbal__pb2.ReleaseControlRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.ReleaseControlResponse.SerializeToString,
            ),
            'SubscribeGimbalList': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeGimbalList,
                    request_deserializer=gimbal_dot_gimbal__pb2.SubscribeGimbalListRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.GimbalListResponse.SerializeToString,
            ),
            'SubscribeControlStatus': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeControlStatus,
                    request_deserializer=gimbal_dot_gimbal__pb2.SubscribeControlStatusRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.ControlStatusResponse.SerializeToString,
            ),
            'GetControlStatus': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControlStatus,
                    request_deserializer=gimbal_dot_gimbal__pb2.GetControlStatusRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.GetControlStatusResponse.SerializeToString,
            ),
            'SubscribeAttitude': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeAttitude,
                    request_deserializer=gimbal_dot_gimbal__pb2.SubscribeAttitudeRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.AttitudeResponse.SerializeToString,
            ),
            'GetAttitude': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAttitude,
                    request_deserializer=gimbal_dot_gimbal__pb2.GetAttitudeRequest.FromString,
                    response_serializer=gimbal_dot_gimbal__pb2.GetAttitudeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.gimbal.GimbalService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.gimbal.GimbalService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GimbalService(object):
    """Provide control over a gimbal.
    """

    @staticmethod
    def SetAngles(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SetAngles',
            gimbal_dot_gimbal__pb2.SetAnglesRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetAnglesResponse.FromString,
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
    def SetAngularRates(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SetAngularRates',
            gimbal_dot_gimbal__pb2.SetAngularRatesRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetAngularRatesResponse.FromString,
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
    def SetRoiLocation(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SetRoiLocation',
            gimbal_dot_gimbal__pb2.SetRoiLocationRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.SetRoiLocationResponse.FromString,
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
    def TakeControl(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/TakeControl',
            gimbal_dot_gimbal__pb2.TakeControlRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.TakeControlResponse.FromString,
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
    def ReleaseControl(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/ReleaseControl',
            gimbal_dot_gimbal__pb2.ReleaseControlRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.ReleaseControlResponse.FromString,
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
    def SubscribeGimbalList(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SubscribeGimbalList',
            gimbal_dot_gimbal__pb2.SubscribeGimbalListRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.GimbalListResponse.FromString,
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
    def SubscribeControlStatus(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SubscribeControlStatus',
            gimbal_dot_gimbal__pb2.SubscribeControlStatusRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.ControlStatusResponse.FromString,
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
    def GetControlStatus(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/GetControlStatus',
            gimbal_dot_gimbal__pb2.GetControlStatusRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.GetControlStatusResponse.FromString,
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
    def SubscribeAttitude(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/SubscribeAttitude',
            gimbal_dot_gimbal__pb2.SubscribeAttitudeRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.AttitudeResponse.FromString,
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
    def GetAttitude(request,
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
            '/mavsdk.rpc.gimbal.GimbalService/GetAttitude',
            gimbal_dot_gimbal__pb2.GetAttitudeRequest.SerializeToString,
            gimbal_dot_gimbal__pb2.GetAttitudeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
