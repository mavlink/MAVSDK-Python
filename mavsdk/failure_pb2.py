# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: failure/failure.proto
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
    'failure/failure.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15\x66\x61ilure/failure.proto\x12\x12mavsdk.rpc.failure\x1a\x14mavsdk_options.proto\"\x8f\x01\n\rInjectRequest\x12\x35\n\x0c\x66\x61ilure_unit\x18\x01 \x01(\x0e\x32\x1f.mavsdk.rpc.failure.FailureUnit\x12\x35\n\x0c\x66\x61ilure_type\x18\x02 \x01(\x0e\x32\x1f.mavsdk.rpc.failure.FailureType\x12\x10\n\x08instance\x18\x03 \x01(\x05\"K\n\x0eInjectResponse\x12\x39\n\x0e\x66\x61ilure_result\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.failure.FailureResult\"\x97\x02\n\rFailureResult\x12\x38\n\x06result\x18\x01 \x01(\x0e\x32(.mavsdk.rpc.failure.FailureResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xb7\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x04\x12\x11\n\rRESULT_DENIED\x10\x05\x12\x13\n\x0fRESULT_DISABLED\x10\x06\x12\x12\n\x0eRESULT_TIMEOUT\x10\x07*\xfd\x03\n\x0b\x46\x61ilureUnit\x12\x1c\n\x18\x46\x41ILURE_UNIT_SENSOR_GYRO\x10\x00\x12\x1d\n\x19\x46\x41ILURE_UNIT_SENSOR_ACCEL\x10\x01\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_MAG\x10\x02\x12\x1c\n\x18\x46\x41ILURE_UNIT_SENSOR_BARO\x10\x03\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_GPS\x10\x04\x12$\n FAILURE_UNIT_SENSOR_OPTICAL_FLOW\x10\x05\x12\x1b\n\x17\x46\x41ILURE_UNIT_SENSOR_VIO\x10\x06\x12\'\n#FAILURE_UNIT_SENSOR_DISTANCE_SENSOR\x10\x07\x12 \n\x1c\x46\x41ILURE_UNIT_SENSOR_AIRSPEED\x10\x08\x12\x1f\n\x1b\x46\x41ILURE_UNIT_SYSTEM_BATTERY\x10\x64\x12\x1d\n\x19\x46\x41ILURE_UNIT_SYSTEM_MOTOR\x10\x65\x12\x1d\n\x19\x46\x41ILURE_UNIT_SYSTEM_SERVO\x10\x66\x12!\n\x1d\x46\x41ILURE_UNIT_SYSTEM_AVOIDANCE\x10g\x12!\n\x1d\x46\x41ILURE_UNIT_SYSTEM_RC_SIGNAL\x10h\x12&\n\"FAILURE_UNIT_SYSTEM_MAVLINK_SIGNAL\x10i*\xd2\x01\n\x0b\x46\x61ilureType\x12\x13\n\x0f\x46\x41ILURE_TYPE_OK\x10\x00\x12\x14\n\x10\x46\x41ILURE_TYPE_OFF\x10\x01\x12\x16\n\x12\x46\x41ILURE_TYPE_STUCK\x10\x02\x12\x18\n\x14\x46\x41ILURE_TYPE_GARBAGE\x10\x03\x12\x16\n\x12\x46\x41ILURE_TYPE_WRONG\x10\x04\x12\x15\n\x11\x46\x41ILURE_TYPE_SLOW\x10\x05\x12\x18\n\x14\x46\x41ILURE_TYPE_DELAYED\x10\x06\x12\x1d\n\x19\x46\x41ILURE_TYPE_INTERMITTENT\x10\x07\x32g\n\x0e\x46\x61ilureService\x12U\n\x06Inject\x12!.mavsdk.rpc.failure.InjectRequest\x1a\".mavsdk.rpc.failure.InjectResponse\"\x04\x80\xb5\x18\x01\x42!\n\x11io.mavsdk.failureB\x0c\x46\x61ilureProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'failure.failure_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021io.mavsdk.failureB\014FailureProto'
  _globals['_FAILURESERVICE'].methods_by_name['Inject']._loaded_options = None
  _globals['_FAILURESERVICE'].methods_by_name['Inject']._serialized_options = b'\200\265\030\001'
  _globals['_FAILUREUNIT']._serialized_start=573
  _globals['_FAILUREUNIT']._serialized_end=1082
  _globals['_FAILURETYPE']._serialized_start=1085
  _globals['_FAILURETYPE']._serialized_end=1295
  _globals['_INJECTREQUEST']._serialized_start=68
  _globals['_INJECTREQUEST']._serialized_end=211
  _globals['_INJECTRESPONSE']._serialized_start=213
  _globals['_INJECTRESPONSE']._serialized_end=288
  _globals['_FAILURERESULT']._serialized_start=291
  _globals['_FAILURERESULT']._serialized_end=570
  _globals['_FAILURERESULT_RESULT']._serialized_start=387
  _globals['_FAILURERESULT_RESULT']._serialized_end=570
  _globals['_FAILURESERVICE']._serialized_start=1297
  _globals['_FAILURESERVICE']._serialized_end=1400
# @@protoc_insertion_point(module_scope)
