# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: offboard/offboard.proto
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
    'offboard/offboard.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17offboard/offboard.proto\x12\x13mavsdk.rpc.offboard\x1a\x14mavsdk_options.proto\"\x0e\n\x0cStartRequest\"M\n\rStartResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\r\n\x0bStopRequest\"L\n\x0cStopResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\x11\n\x0fIsActiveRequest\"%\n\x10IsActiveResponse\x12\x11\n\tis_active\x18\x01 \x01(\x08\"E\n\x12SetAttitudeRequest\x12/\n\x08\x61ttitude\x18\x01 \x01(\x0b\x32\x1d.mavsdk.rpc.offboard.Attitude\"S\n\x13SetAttitudeResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"[\n\x19SetActuatorControlRequest\x12>\n\x10\x61\x63tuator_control\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.offboard.ActuatorControl\"Z\n\x1aSetActuatorControlResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"R\n\x16SetAttitudeRateRequest\x12\x38\n\rattitude_rate\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.offboard.AttitudeRate\"W\n\x17SetAttitudeRateResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x15SetPositionNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\"V\n\x16SetPositionNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"_\n\x18SetPositionGlobalRequest\x12\x43\n\x13position_global_yaw\x18\x01 \x01(\x0b\x32&.mavsdk.rpc.offboard.PositionGlobalYaw\"Y\n\x19SetPositionGlobalResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"c\n\x16SetVelocityBodyRequest\x12I\n\x16velocity_body_yawspeed\x18\x01 \x01(\x0b\x32).mavsdk.rpc.offboard.VelocityBodyYawspeed\"W\n\x17SetVelocityBodyResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x15SetVelocityNedRequest\x12=\n\x10velocity_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"V\n\x16SetVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"\x9d\x01\n\x1dSetPositionVelocityNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\x12=\n\x10velocity_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\"\xe9\x01\n)SetPositionVelocityAccelerationNedRequest\x12=\n\x10position_ned_yaw\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.PositionNedYaw\x12=\n\x10velocity_ned_yaw\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.offboard.VelocityNedYaw\x12>\n\x10\x61\x63\x63\x65leration_ned\x18\x03 \x01(\x0b\x32$.mavsdk.rpc.offboard.AccelerationNed\"^\n\x1eSetPositionVelocityNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"j\n*SetPositionVelocityAccelerationNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"[\n\x19SetAccelerationNedRequest\x12>\n\x10\x61\x63\x63\x65leration_ned\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.offboard.AccelerationNed\"Z\n\x1aSetAccelerationNedResponse\x12<\n\x0foffboard_result\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.offboard.OffboardResult\"V\n\x08\x41ttitude\x12\x10\n\x08roll_deg\x18\x01 \x01(\x02\x12\x11\n\tpitch_deg\x18\x02 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"(\n\x14\x41\x63tuatorControlGroup\x12\x10\n\x08\x63ontrols\x18\x01 \x03(\x02\"L\n\x0f\x41\x63tuatorControl\x12\x39\n\x06groups\x18\x01 \x03(\x0b\x32).mavsdk.rpc.offboard.ActuatorControlGroup\"`\n\x0c\x41ttitudeRate\x12\x12\n\nroll_deg_s\x18\x01 \x01(\x02\x12\x13\n\x0bpitch_deg_s\x18\x02 \x01(\x02\x12\x11\n\tyaw_deg_s\x18\x03 \x01(\x02\x12\x14\n\x0cthrust_value\x18\x04 \x01(\x02\"R\n\x0ePositionNedYaw\x12\x0f\n\x07north_m\x18\x01 \x01(\x02\x12\x0e\n\x06\x65\x61st_m\x18\x02 \x01(\x02\x12\x0e\n\x06\x64own_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"\xfc\x01\n\x11PositionGlobalYaw\x12\x0f\n\x07lat_deg\x18\x01 \x01(\x01\x12\x0f\n\x07lon_deg\x18\x02 \x01(\x01\x12\r\n\x05\x61lt_m\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\x12J\n\raltitude_type\x18\x05 \x01(\x0e\x32\x33.mavsdk.rpc.offboard.PositionGlobalYaw.AltitudeType\"Y\n\x0c\x41ltitudeType\x12\x1a\n\x16\x41LTITUDE_TYPE_REL_HOME\x10\x00\x12\x16\n\x12\x41LTITUDE_TYPE_AMSL\x10\x01\x12\x15\n\x11\x41LTITUDE_TYPE_AGL\x10\x02\"h\n\x14VelocityBodyYawspeed\x12\x13\n\x0b\x66orward_m_s\x18\x01 \x01(\x02\x12\x11\n\tright_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x16\n\x0eyawspeed_deg_s\x18\x04 \x01(\x02\"X\n\x0eVelocityNedYaw\x12\x11\n\tnorth_m_s\x18\x01 \x01(\x02\x12\x10\n\x08\x65\x61st_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x04 \x01(\x02\"K\n\x0f\x41\x63\x63\x65lerationNed\x12\x12\n\nnorth_m_s2\x18\x01 \x01(\x02\x12\x11\n\teast_m_s2\x18\x02 \x01(\x02\x12\x11\n\tdown_m_s2\x18\x03 \x01(\x02\"\xb5\x02\n\x0eOffboardResult\x12:\n\x06result\x18\x01 \x01(\x0e\x32*.mavsdk.rpc.offboard.OffboardResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xd2\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x1a\n\x16RESULT_NO_SETPOINT_SET\x10\x07\x12\x11\n\rRESULT_FAILED\x10\x08\x32\xef\x0b\n\x0fOffboardService\x12P\n\x05Start\x12!.mavsdk.rpc.offboard.StartRequest\x1a\".mavsdk.rpc.offboard.StartResponse\"\x00\x12M\n\x04Stop\x12 .mavsdk.rpc.offboard.StopRequest\x1a!.mavsdk.rpc.offboard.StopResponse\"\x00\x12]\n\x08IsActive\x12$.mavsdk.rpc.offboard.IsActiveRequest\x1a%.mavsdk.rpc.offboard.IsActiveResponse\"\x04\x80\xb5\x18\x01\x12\x66\n\x0bSetAttitude\x12\'.mavsdk.rpc.offboard.SetAttitudeRequest\x1a(.mavsdk.rpc.offboard.SetAttitudeResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetActuatorControl\x12..mavsdk.rpc.offboard.SetActuatorControlRequest\x1a/.mavsdk.rpc.offboard.SetActuatorControlResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetAttitudeRate\x12+.mavsdk.rpc.offboard.SetAttitudeRateRequest\x1a,.mavsdk.rpc.offboard.SetAttitudeRateResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetPositionNed\x12*.mavsdk.rpc.offboard.SetPositionNedRequest\x1a+.mavsdk.rpc.offboard.SetPositionNedResponse\"\x04\x80\xb5\x18\x01\x12x\n\x11SetPositionGlobal\x12-.mavsdk.rpc.offboard.SetPositionGlobalRequest\x1a..mavsdk.rpc.offboard.SetPositionGlobalResponse\"\x04\x80\xb5\x18\x01\x12r\n\x0fSetVelocityBody\x12+.mavsdk.rpc.offboard.SetVelocityBodyRequest\x1a,.mavsdk.rpc.offboard.SetVelocityBodyResponse\"\x04\x80\xb5\x18\x01\x12o\n\x0eSetVelocityNed\x12*.mavsdk.rpc.offboard.SetVelocityNedRequest\x1a+.mavsdk.rpc.offboard.SetVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\x87\x01\n\x16SetPositionVelocityNed\x12\x32.mavsdk.rpc.offboard.SetPositionVelocityNedRequest\x1a\x33.mavsdk.rpc.offboard.SetPositionVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\xab\x01\n\"SetPositionVelocityAccelerationNed\x12>.mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedRequest\x1a?.mavsdk.rpc.offboard.SetPositionVelocityAccelerationNedResponse\"\x04\x80\xb5\x18\x01\x12{\n\x12SetAccelerationNed\x12..mavsdk.rpc.offboard.SetAccelerationNedRequest\x1a/.mavsdk.rpc.offboard.SetAccelerationNedResponse\"\x04\x80\xb5\x18\x01\x42#\n\x12io.mavsdk.offboardB\rOffboardProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'offboard.offboard_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\022io.mavsdk.offboardB\rOffboardProto'
  _globals['_OFFBOARDSERVICE'].methods_by_name['IsActive']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['IsActive']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAttitude']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAttitude']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetActuatorControl']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetActuatorControl']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAttitudeRate']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAttitudeRate']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionNed']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionNed']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionGlobal']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionGlobal']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetVelocityBody']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetVelocityBody']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetVelocityNed']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetVelocityNed']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionVelocityNed']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionVelocityNed']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionVelocityAccelerationNed']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetPositionVelocityAccelerationNed']._serialized_options = b'\200\265\030\001'
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAccelerationNed']._loaded_options = None
  _globals['_OFFBOARDSERVICE'].methods_by_name['SetAccelerationNed']._serialized_options = b'\200\265\030\001'
  _globals['_STARTREQUEST']._serialized_start=70
  _globals['_STARTREQUEST']._serialized_end=84
  _globals['_STARTRESPONSE']._serialized_start=86
  _globals['_STARTRESPONSE']._serialized_end=163
  _globals['_STOPREQUEST']._serialized_start=165
  _globals['_STOPREQUEST']._serialized_end=178
  _globals['_STOPRESPONSE']._serialized_start=180
  _globals['_STOPRESPONSE']._serialized_end=256
  _globals['_ISACTIVEREQUEST']._serialized_start=258
  _globals['_ISACTIVEREQUEST']._serialized_end=275
  _globals['_ISACTIVERESPONSE']._serialized_start=277
  _globals['_ISACTIVERESPONSE']._serialized_end=314
  _globals['_SETATTITUDEREQUEST']._serialized_start=316
  _globals['_SETATTITUDEREQUEST']._serialized_end=385
  _globals['_SETATTITUDERESPONSE']._serialized_start=387
  _globals['_SETATTITUDERESPONSE']._serialized_end=470
  _globals['_SETACTUATORCONTROLREQUEST']._serialized_start=472
  _globals['_SETACTUATORCONTROLREQUEST']._serialized_end=563
  _globals['_SETACTUATORCONTROLRESPONSE']._serialized_start=565
  _globals['_SETACTUATORCONTROLRESPONSE']._serialized_end=655
  _globals['_SETATTITUDERATEREQUEST']._serialized_start=657
  _globals['_SETATTITUDERATEREQUEST']._serialized_end=739
  _globals['_SETATTITUDERATERESPONSE']._serialized_start=741
  _globals['_SETATTITUDERATERESPONSE']._serialized_end=828
  _globals['_SETPOSITIONNEDREQUEST']._serialized_start=830
  _globals['_SETPOSITIONNEDREQUEST']._serialized_end=916
  _globals['_SETPOSITIONNEDRESPONSE']._serialized_start=918
  _globals['_SETPOSITIONNEDRESPONSE']._serialized_end=1004
  _globals['_SETPOSITIONGLOBALREQUEST']._serialized_start=1006
  _globals['_SETPOSITIONGLOBALREQUEST']._serialized_end=1101
  _globals['_SETPOSITIONGLOBALRESPONSE']._serialized_start=1103
  _globals['_SETPOSITIONGLOBALRESPONSE']._serialized_end=1192
  _globals['_SETVELOCITYBODYREQUEST']._serialized_start=1194
  _globals['_SETVELOCITYBODYREQUEST']._serialized_end=1293
  _globals['_SETVELOCITYBODYRESPONSE']._serialized_start=1295
  _globals['_SETVELOCITYBODYRESPONSE']._serialized_end=1382
  _globals['_SETVELOCITYNEDREQUEST']._serialized_start=1384
  _globals['_SETVELOCITYNEDREQUEST']._serialized_end=1470
  _globals['_SETVELOCITYNEDRESPONSE']._serialized_start=1472
  _globals['_SETVELOCITYNEDRESPONSE']._serialized_end=1558
  _globals['_SETPOSITIONVELOCITYNEDREQUEST']._serialized_start=1561
  _globals['_SETPOSITIONVELOCITYNEDREQUEST']._serialized_end=1718
  _globals['_SETPOSITIONVELOCITYACCELERATIONNEDREQUEST']._serialized_start=1721
  _globals['_SETPOSITIONVELOCITYACCELERATIONNEDREQUEST']._serialized_end=1954
  _globals['_SETPOSITIONVELOCITYNEDRESPONSE']._serialized_start=1956
  _globals['_SETPOSITIONVELOCITYNEDRESPONSE']._serialized_end=2050
  _globals['_SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE']._serialized_start=2052
  _globals['_SETPOSITIONVELOCITYACCELERATIONNEDRESPONSE']._serialized_end=2158
  _globals['_SETACCELERATIONNEDREQUEST']._serialized_start=2160
  _globals['_SETACCELERATIONNEDREQUEST']._serialized_end=2251
  _globals['_SETACCELERATIONNEDRESPONSE']._serialized_start=2253
  _globals['_SETACCELERATIONNEDRESPONSE']._serialized_end=2343
  _globals['_ATTITUDE']._serialized_start=2345
  _globals['_ATTITUDE']._serialized_end=2431
  _globals['_ACTUATORCONTROLGROUP']._serialized_start=2433
  _globals['_ACTUATORCONTROLGROUP']._serialized_end=2473
  _globals['_ACTUATORCONTROL']._serialized_start=2475
  _globals['_ACTUATORCONTROL']._serialized_end=2551
  _globals['_ATTITUDERATE']._serialized_start=2553
  _globals['_ATTITUDERATE']._serialized_end=2649
  _globals['_POSITIONNEDYAW']._serialized_start=2651
  _globals['_POSITIONNEDYAW']._serialized_end=2733
  _globals['_POSITIONGLOBALYAW']._serialized_start=2736
  _globals['_POSITIONGLOBALYAW']._serialized_end=2988
  _globals['_POSITIONGLOBALYAW_ALTITUDETYPE']._serialized_start=2899
  _globals['_POSITIONGLOBALYAW_ALTITUDETYPE']._serialized_end=2988
  _globals['_VELOCITYBODYYAWSPEED']._serialized_start=2990
  _globals['_VELOCITYBODYYAWSPEED']._serialized_end=3094
  _globals['_VELOCITYNEDYAW']._serialized_start=3096
  _globals['_VELOCITYNEDYAW']._serialized_end=3184
  _globals['_ACCELERATIONNED']._serialized_start=3186
  _globals['_ACCELERATIONNED']._serialized_end=3261
  _globals['_OFFBOARDRESULT']._serialized_start=3264
  _globals['_OFFBOARDRESULT']._serialized_end=3573
  _globals['_OFFBOARDRESULT_RESULT']._serialized_start=3363
  _globals['_OFFBOARDRESULT_RESULT']._serialized_end=3573
  _globals['_OFFBOARDSERVICE']._serialized_start=3576
  _globals['_OFFBOARDSERVICE']._serialized_end=5095
# @@protoc_insertion_point(module_scope)
