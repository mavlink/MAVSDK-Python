# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from . import log_files_pb2 as log__files_dot_log__files__pb2

GRPC_GENERATED_VERSION = '1.70.0'
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
        + f' but the generated code in log_files/log_files_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class LogFilesServiceStub(object):
    """Allow to download log files from the vehicle after a flight is complete.
    For log streaming during flight check the logging plugin.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetEntries = channel.unary_unary(
                '/mavsdk.rpc.log_files.LogFilesService/GetEntries',
                request_serializer=log__files_dot_log__files__pb2.GetEntriesRequest.SerializeToString,
                response_deserializer=log__files_dot_log__files__pb2.GetEntriesResponse.FromString,
                _registered_method=True)
        self.SubscribeDownloadLogFile = channel.unary_stream(
                '/mavsdk.rpc.log_files.LogFilesService/SubscribeDownloadLogFile',
                request_serializer=log__files_dot_log__files__pb2.SubscribeDownloadLogFileRequest.SerializeToString,
                response_deserializer=log__files_dot_log__files__pb2.DownloadLogFileResponse.FromString,
                _registered_method=True)
        self.EraseAllLogFiles = channel.unary_unary(
                '/mavsdk.rpc.log_files.LogFilesService/EraseAllLogFiles',
                request_serializer=log__files_dot_log__files__pb2.EraseAllLogFilesRequest.SerializeToString,
                response_deserializer=log__files_dot_log__files__pb2.EraseAllLogFilesResponse.FromString,
                _registered_method=True)


class LogFilesServiceServicer(object):
    """Allow to download log files from the vehicle after a flight is complete.
    For log streaming during flight check the logging plugin.
    """

    def GetEntries(self, request, context):
        """Get List of log files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeDownloadLogFile(self, request, context):
        """Download log file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EraseAllLogFiles(self, request, context):
        """Erase all log files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LogFilesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetEntries': grpc.unary_unary_rpc_method_handler(
                    servicer.GetEntries,
                    request_deserializer=log__files_dot_log__files__pb2.GetEntriesRequest.FromString,
                    response_serializer=log__files_dot_log__files__pb2.GetEntriesResponse.SerializeToString,
            ),
            'SubscribeDownloadLogFile': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeDownloadLogFile,
                    request_deserializer=log__files_dot_log__files__pb2.SubscribeDownloadLogFileRequest.FromString,
                    response_serializer=log__files_dot_log__files__pb2.DownloadLogFileResponse.SerializeToString,
            ),
            'EraseAllLogFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.EraseAllLogFiles,
                    request_deserializer=log__files_dot_log__files__pb2.EraseAllLogFilesRequest.FromString,
                    response_serializer=log__files_dot_log__files__pb2.EraseAllLogFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.log_files.LogFilesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mavsdk.rpc.log_files.LogFilesService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class LogFilesService(object):
    """Allow to download log files from the vehicle after a flight is complete.
    For log streaming during flight check the logging plugin.
    """

    @staticmethod
    def GetEntries(request,
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
            '/mavsdk.rpc.log_files.LogFilesService/GetEntries',
            log__files_dot_log__files__pb2.GetEntriesRequest.SerializeToString,
            log__files_dot_log__files__pb2.GetEntriesResponse.FromString,
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
    def SubscribeDownloadLogFile(request,
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
            '/mavsdk.rpc.log_files.LogFilesService/SubscribeDownloadLogFile',
            log__files_dot_log__files__pb2.SubscribeDownloadLogFileRequest.SerializeToString,
            log__files_dot_log__files__pb2.DownloadLogFileResponse.FromString,
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
    def EraseAllLogFiles(request,
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
            '/mavsdk.rpc.log_files.LogFilesService/EraseAllLogFiles',
            log__files_dot_log__files__pb2.EraseAllLogFilesRequest.SerializeToString,
            log__files_dot_log__files__pb2.EraseAllLogFilesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
