# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: core/core.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'core/core.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x63ore/core.proto\x12\x0fmavsdk.rpc.core\"!\n\x1fSubscribeConnectionStateRequest\"U\n\x17\x43onnectionStateResponse\x12:\n\x10\x63onnection_state\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.core.ConnectionState\"-\n\x18SetMavlinkTimeoutRequest\x12\x11\n\ttimeout_s\x18\x01 \x01(\x01\"\x1b\n\x19SetMavlinkTimeoutResponse\"\'\n\x0f\x43onnectionState\x12\x14\n\x0cis_connected\x18\x02 \x01(\x08\x32\xf7\x01\n\x0b\x43oreService\x12z\n\x18SubscribeConnectionState\x12\x30.mavsdk.rpc.core.SubscribeConnectionStateRequest\x1a(.mavsdk.rpc.core.ConnectionStateResponse\"\x00\x30\x01\x12l\n\x11SetMavlinkTimeout\x12).mavsdk.rpc.core.SetMavlinkTimeoutRequest\x1a*.mavsdk.rpc.core.SetMavlinkTimeoutResponse\"\x00\x42\x1b\n\x0eio.mavsdk.coreB\tCoreProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'core.core_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016io.mavsdk.coreB\tCoreProto'
  _globals['_SUBSCRIBECONNECTIONSTATEREQUEST']._serialized_start=36
  _globals['_SUBSCRIBECONNECTIONSTATEREQUEST']._serialized_end=69
  _globals['_CONNECTIONSTATERESPONSE']._serialized_start=71
  _globals['_CONNECTIONSTATERESPONSE']._serialized_end=156
  _globals['_SETMAVLINKTIMEOUTREQUEST']._serialized_start=158
  _globals['_SETMAVLINKTIMEOUTREQUEST']._serialized_end=203
  _globals['_SETMAVLINKTIMEOUTRESPONSE']._serialized_start=205
  _globals['_SETMAVLINKTIMEOUTRESPONSE']._serialized_end=232
  _globals['_CONNECTIONSTATE']._serialized_start=234
  _globals['_CONNECTIONSTATE']._serialized_end=273
  _globals['_CORESERVICE']._serialized_start=276
  _globals['_CORESERVICE']._serialized_end=523
# @@protoc_insertion_point(module_scope)
