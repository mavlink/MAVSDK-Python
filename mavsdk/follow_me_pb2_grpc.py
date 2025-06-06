# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import follow_me_pb2 as follow__me_dot_follow__me__pb2

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
        + f' but the generated code in follow_me/follow_me_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FollowMeServiceStub(object):
    """
    Allow users to command the vehicle to follow a specific target.
    The target is provided as a GPS coordinate and altitude.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConfig = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/GetConfig',
                request_serializer=follow__me_dot_follow__me__pb2.GetConfigRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.GetConfigResponse.FromString,
                _registered_method=True)
        self.SetConfig = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/SetConfig',
                request_serializer=follow__me_dot_follow__me__pb2.SetConfigRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.SetConfigResponse.FromString,
                _registered_method=True)
        self.IsActive = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/IsActive',
                request_serializer=follow__me_dot_follow__me__pb2.IsActiveRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.IsActiveResponse.FromString,
                _registered_method=True)
        self.SetTargetLocation = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/SetTargetLocation',
                request_serializer=follow__me_dot_follow__me__pb2.SetTargetLocationRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.SetTargetLocationResponse.FromString,
                _registered_method=True)
        self.GetLastLocation = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/GetLastLocation',
                request_serializer=follow__me_dot_follow__me__pb2.GetLastLocationRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.GetLastLocationResponse.FromString,
                _registered_method=True)
        self.Start = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/Start',
                request_serializer=follow__me_dot_follow__me__pb2.StartRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.StartResponse.FromString,
                _registered_method=True)
        self.Stop = channel.unary_unary(
                '/mavsdk.rpc.follow_me.FollowMeService/Stop',
                request_serializer=follow__me_dot_follow__me__pb2.StopRequest.SerializeToString,
                response_deserializer=follow__me_dot_follow__me__pb2.StopResponse.FromString,
                _registered_method=True)


class FollowMeServiceServicer(object):
    """
    Allow users to command the vehicle to follow a specific target.
    The target is provided as a GPS coordinate and altitude.
    """

    def GetConfig(self, request, context):
        """Get current configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetConfig(self, request, context):
        """Apply configuration by sending it to the system.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IsActive(self, request, context):
        """Check if FollowMe is active.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTargetLocation(self, request, context):
        """Set location of the moving target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastLocation(self, request, context):
        """Get the last location of the target.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Start(self, request, context):
        """Start FollowMe mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Stop(self, request, context):
        """Stop FollowMe mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FollowMeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.GetConfig,
                    request_deserializer=follow__me_dot_follow__me__pb2.GetConfigRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.GetConfigResponse.SerializeToString,
            ),
            'SetConfig': grpc.unary_unary_rpc_method_handler(
                    servicer.SetConfig,
                    request_deserializer=follow__me_dot_follow__me__pb2.SetConfigRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.SetConfigResponse.SerializeToString,
            ),
            'IsActive': grpc.unary_unary_rpc_method_handler(
                    servicer.IsActive,
                    request_deserializer=follow__me_dot_follow__me__pb2.IsActiveRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.IsActiveResponse.SerializeToString,
            ),
            'SetTargetLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTargetLocation,
                    request_deserializer=follow__me_dot_follow__me__pb2.SetTargetLocationRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.SetTargetLocationResponse.SerializeToString,
            ),
            'GetLastLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastLocation,
                    request_deserializer=follow__me_dot_follow__me__pb2.GetLastLocationRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.GetLastLocationResponse.SerializeToString,
            ),
            'Start': grpc.unary_unary_rpc_method_handler(
                    servicer.Start,
                    request_deserializer=follow__me_dot_follow__me__pb2.StartRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.StartResponse.SerializeToString,
            ),
            'Stop': grpc.unary_unary_rpc_method_handler(
                    servicer.Stop,
                    request_deserializer=follow__me_dot_follow__me__pb2.StopRequest.FromString,
                    response_serializer=follow__me_dot_follow__me__pb2.StopResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.follow_me.FollowMeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.follow_me.FollowMeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class FollowMeService(object):
    """
    Allow users to command the vehicle to follow a specific target.
    The target is provided as a GPS coordinate and altitude.
    """

    @staticmethod
    def GetConfig(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/GetConfig',
            follow__me_dot_follow__me__pb2.GetConfigRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.GetConfigResponse.FromString,
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
    def SetConfig(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/SetConfig',
            follow__me_dot_follow__me__pb2.SetConfigRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.SetConfigResponse.FromString,
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
    def IsActive(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/IsActive',
            follow__me_dot_follow__me__pb2.IsActiveRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.IsActiveResponse.FromString,
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
    def SetTargetLocation(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/SetTargetLocation',
            follow__me_dot_follow__me__pb2.SetTargetLocationRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.SetTargetLocationResponse.FromString,
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
    def GetLastLocation(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/GetLastLocation',
            follow__me_dot_follow__me__pb2.GetLastLocationRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.GetLastLocationResponse.FromString,
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
    def Start(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/Start',
            follow__me_dot_follow__me__pb2.StartRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.StartResponse.FromString,
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
    def Stop(request,
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
            '/mavsdk.rpc.follow_me.FollowMeService/Stop',
            follow__me_dot_follow__me__pb2.StopRequest.SerializeToString,
            follow__me_dot_follow__me__pb2.StopResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
