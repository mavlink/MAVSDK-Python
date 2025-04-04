# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import arm_authorizer_server_pb2 as arm__authorizer__server_dot_arm__authorizer__server__pb2

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
        + f' but the generated code in arm_authorizer_server/arm_authorizer_server_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class ArmAuthorizerServerServiceStub(object):
    """Use arm authorization.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SubscribeArmAuthorization = channel.unary_stream(
                '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/SubscribeArmAuthorization',
                request_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.SubscribeArmAuthorizationRequest.SerializeToString,
                response_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.ArmAuthorizationResponse.FromString,
                _registered_method=True)
        self.AcceptArmAuthorization = channel.unary_unary(
                '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/AcceptArmAuthorization',
                request_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationRequest.SerializeToString,
                response_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationResponse.FromString,
                _registered_method=True)
        self.RejectArmAuthorization = channel.unary_unary(
                '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/RejectArmAuthorization',
                request_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationRequest.SerializeToString,
                response_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationResponse.FromString,
                _registered_method=True)


class ArmAuthorizerServerServiceServicer(object):
    """Use arm authorization.
    """

    def SubscribeArmAuthorization(self, request, context):
        """Subscribe to arm authorization request messages. Each request received should respond to using RespondArmAuthorization
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AcceptArmAuthorization(self, request, context):
        """Authorize arm for the specific time
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RejectArmAuthorization(self, request, context):
        """Reject arm authorization request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArmAuthorizerServerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SubscribeArmAuthorization': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeArmAuthorization,
                    request_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.SubscribeArmAuthorizationRequest.FromString,
                    response_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.ArmAuthorizationResponse.SerializeToString,
            ),
            'AcceptArmAuthorization': grpc.unary_unary_rpc_method_handler(
                    servicer.AcceptArmAuthorization,
                    request_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationRequest.FromString,
                    response_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationResponse.SerializeToString,
            ),
            'RejectArmAuthorization': grpc.unary_unary_rpc_method_handler(
                    servicer.RejectArmAuthorization,
                    request_deserializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationRequest.FromString,
                    response_serializer=arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class ArmAuthorizerServerService(object):
    """Use arm authorization.
    """

    @staticmethod
    def SubscribeArmAuthorization(request,
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
            '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/SubscribeArmAuthorization',
            arm__authorizer__server_dot_arm__authorizer__server__pb2.SubscribeArmAuthorizationRequest.SerializeToString,
            arm__authorizer__server_dot_arm__authorizer__server__pb2.ArmAuthorizationResponse.FromString,
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
    def AcceptArmAuthorization(request,
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
            '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/AcceptArmAuthorization',
            arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationRequest.SerializeToString,
            arm__authorizer__server_dot_arm__authorizer__server__pb2.AcceptArmAuthorizationResponse.FromString,
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
    def RejectArmAuthorization(request,
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
            '/mavsdk.rpc.arm_authorizer_server.ArmAuthorizerServerService/RejectArmAuthorization',
            arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationRequest.SerializeToString,
            arm__authorizer__server_dot_arm__authorizer__server__pb2.RejectArmAuthorizationResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
