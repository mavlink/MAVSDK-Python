# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: action_server/action_server.proto
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
    'action_server/action_server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!action_server/action_server.proto\x12\x18mavsdk.rpc.action_server\x1a\x14mavsdk_options.proto\"/\n\x16SetAllowTakeoffRequest\x12\x15\n\rallow_takeoff\x18\x01 \x01(\x08\";\n\x11SetArmableRequest\x12\x0f\n\x07\x61rmable\x18\x01 \x01(\x08\x12\x15\n\rforce_armable\x18\x02 \x01(\x08\"D\n\x14SetDisarmableRequest\x12\x12\n\ndisarmable\x18\x01 \x01(\x08\x12\x18\n\x10\x66orce_disarmable\x18\x02 \x01(\x08\"f\n\x1eSetAllowableFlightModesRequest\x12\x44\n\x0c\x66light_modes\x18\x01 \x01(\x0b\x32..mavsdk.rpc.action_server.AllowableFlightModes\"(\n\x14SetArmedStateRequest\x12\x10\n\x08is_armed\x18\x01 \x01(\x08\"Q\n\x14SetFlightModeRequest\x12\x39\n\x0b\x66light_mode\x18\x01 \x01(\x0e\x32$.mavsdk.rpc.action_server.FlightMode\" \n\x1eGetAllowableFlightModesRequest\"\x1b\n\x19SubscribeArmDisarmRequest\"\"\n SubscribeFlightModeChangeRequest\"\x19\n\x17SubscribeTakeoffRequest\"\x16\n\x14SubscribeLandRequest\"\x18\n\x16SubscribeRebootRequest\"\x1a\n\x18SubscribeShutdownRequest\"\x1b\n\x19SubscribeTerminateRequest\"\x91\x01\n\x11\x41rmDisarmResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x30\n\x03\x61rm\x18\x02 \x01(\x0b\x32#.mavsdk.rpc.action_server.ArmDisarm\"\xa1\x01\n\x18\x46lightModeChangeResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x39\n\x0b\x66light_mode\x18\x02 \x01(\x0e\x32$.mavsdk.rpc.action_server.FlightMode\"n\n\x0fTakeoffResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x0f\n\x07takeoff\x18\x02 \x01(\x08\"h\n\x0cLandResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x0c\n\x04land\x18\x02 \x01(\x08\"l\n\x0eRebootResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x0e\n\x06reboot\x18\x02 \x01(\x08\"p\n\x10ShutdownResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x10\n\x08shutdown\x18\x02 \x01(\x08\"r\n\x11TerminateResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\x12\x11\n\tterminate\x18\x02 \x01(\x08\"`\n\x12SetArmableResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"c\n\x15SetDisarmableResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"m\n\x1fSetAllowableFlightModesResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"e\n\x17SetAllowTakeoffResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"g\n\x1fGetAllowableFlightModesResponse\x12\x44\n\x0c\x66light_modes\x18\x01 \x01(\x0b\x32..mavsdk.rpc.action_server.AllowableFlightModes\"c\n\x15SetArmedStateResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"c\n\x15SetFlightModeResponse\x12J\n\x14\x61\x63tion_server_result\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.action_server.ActionServerResult\"b\n\x14\x41llowableFlightModes\x12\x15\n\rcan_auto_mode\x18\x01 \x01(\x08\x12\x17\n\x0f\x63\x61n_guided_mode\x18\x02 \x01(\x08\x12\x1a\n\x12\x63\x61n_stabilize_mode\x18\x03 \x01(\x08\"\'\n\tArmDisarm\x12\x0b\n\x03\x61rm\x18\x01 \x01(\x08\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\"\xe9\x03\n\x12\x41\x63tionServerResult\x12\x43\n\x06result\x18\x01 \x01(\x0e\x32\x33.mavsdk.rpc.action_server.ActionServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xf9\x02\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12.\n*RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN\x10\x06\x12$\n RESULT_COMMAND_DENIED_NOT_LANDED\x10\x07\x12\x12\n\x0eRESULT_TIMEOUT\x10\x08\x12*\n&RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN\x10\t\x12%\n!RESULT_NO_VTOL_TRANSITION_SUPPORT\x10\n\x12\x1a\n\x16RESULT_PARAMETER_ERROR\x10\x0b\x12\x0f\n\x0bRESULT_NEXT\x10\x0c*\xeb\x02\n\nFlightMode\x12\x17\n\x13\x46LIGHT_MODE_UNKNOWN\x10\x00\x12\x15\n\x11\x46LIGHT_MODE_READY\x10\x01\x12\x17\n\x13\x46LIGHT_MODE_TAKEOFF\x10\x02\x12\x14\n\x10\x46LIGHT_MODE_HOLD\x10\x03\x12\x17\n\x13\x46LIGHT_MODE_MISSION\x10\x04\x12 \n\x1c\x46LIGHT_MODE_RETURN_TO_LAUNCH\x10\x05\x12\x14\n\x10\x46LIGHT_MODE_LAND\x10\x06\x12\x18\n\x14\x46LIGHT_MODE_OFFBOARD\x10\x07\x12\x19\n\x15\x46LIGHT_MODE_FOLLOW_ME\x10\x08\x12\x16\n\x12\x46LIGHT_MODE_MANUAL\x10\t\x12\x16\n\x12\x46LIGHT_MODE_ALTCTL\x10\n\x12\x16\n\x12\x46LIGHT_MODE_POSCTL\x10\x0b\x12\x14\n\x10\x46LIGHT_MODE_ACRO\x10\x0c\x12\x1a\n\x16\x46LIGHT_MODE_STABILIZED\x10\r2\x8d\x0e\n\x13\x41\x63tionServerService\x12~\n\x12SubscribeArmDisarm\x12\x33.mavsdk.rpc.action_server.SubscribeArmDisarmRequest\x1a+.mavsdk.rpc.action_server.ArmDisarmResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x93\x01\n\x19SubscribeFlightModeChange\x12:.mavsdk.rpc.action_server.SubscribeFlightModeChangeRequest\x1a\x32.mavsdk.rpc.action_server.FlightModeChangeResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12x\n\x10SubscribeTakeoff\x12\x31.mavsdk.rpc.action_server.SubscribeTakeoffRequest\x1a).mavsdk.rpc.action_server.TakeoffResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12o\n\rSubscribeLand\x12..mavsdk.rpc.action_server.SubscribeLandRequest\x1a&.mavsdk.rpc.action_server.LandResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12u\n\x0fSubscribeReboot\x12\x30.mavsdk.rpc.action_server.SubscribeRebootRequest\x1a(.mavsdk.rpc.action_server.RebootResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12{\n\x11SubscribeShutdown\x12\x32.mavsdk.rpc.action_server.SubscribeShutdownRequest\x1a*.mavsdk.rpc.action_server.ShutdownResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12~\n\x12SubscribeTerminate\x12\x33.mavsdk.rpc.action_server.SubscribeTerminateRequest\x1a+.mavsdk.rpc.action_server.TerminateResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12|\n\x0fSetAllowTakeoff\x12\x30.mavsdk.rpc.action_server.SetAllowTakeoffRequest\x1a\x31.mavsdk.rpc.action_server.SetAllowTakeoffResponse\"\x04\x80\xb5\x18\x01\x12m\n\nSetArmable\x12+.mavsdk.rpc.action_server.SetArmableRequest\x1a,.mavsdk.rpc.action_server.SetArmableResponse\"\x04\x80\xb5\x18\x01\x12v\n\rSetDisarmable\x12..mavsdk.rpc.action_server.SetDisarmableRequest\x1a/.mavsdk.rpc.action_server.SetDisarmableResponse\"\x04\x80\xb5\x18\x01\x12\x94\x01\n\x17SetAllowableFlightModes\x12\x38.mavsdk.rpc.action_server.SetAllowableFlightModesRequest\x1a\x39.mavsdk.rpc.action_server.SetAllowableFlightModesResponse\"\x04\x80\xb5\x18\x01\x12\x94\x01\n\x17GetAllowableFlightModes\x12\x38.mavsdk.rpc.action_server.GetAllowableFlightModesRequest\x1a\x39.mavsdk.rpc.action_server.GetAllowableFlightModesResponse\"\x04\x80\xb5\x18\x01\x12v\n\rSetArmedState\x12..mavsdk.rpc.action_server.SetArmedStateRequest\x1a/.mavsdk.rpc.action_server.SetArmedStateResponse\"\x04\x80\xb5\x18\x01\x12v\n\rSetFlightMode\x12..mavsdk.rpc.action_server.SetFlightModeRequest\x1a/.mavsdk.rpc.action_server.SetFlightModeResponse\"\x04\x80\xb5\x18\x01\x42,\n\x17io.mavsdk.action_serverB\x11\x41\x63tionServerProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'action_server.action_server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\027io.mavsdk.action_serverB\021ActionServerProto'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeArmDisarm']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeArmDisarm']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeFlightModeChange']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeFlightModeChange']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeTakeoff']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeTakeoff']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeLand']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeLand']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeReboot']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeReboot']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeShutdown']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeShutdown']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeTerminate']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SubscribeTerminate']._serialized_options = b'\200\265\030\000'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetAllowTakeoff']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetAllowTakeoff']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetArmable']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetArmable']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetDisarmable']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetDisarmable']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetAllowableFlightModes']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetAllowableFlightModes']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['GetAllowableFlightModes']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['GetAllowableFlightModes']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetArmedState']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetArmedState']._serialized_options = b'\200\265\030\001'
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetFlightMode']._loaded_options = None
  _globals['_ACTIONSERVERSERVICE'].methods_by_name['SetFlightMode']._serialized_options = b'\200\265\030\001'
  _globals['_FLIGHTMODE']._serialized_start=2951
  _globals['_FLIGHTMODE']._serialized_end=3314
  _globals['_SETALLOWTAKEOFFREQUEST']._serialized_start=85
  _globals['_SETALLOWTAKEOFFREQUEST']._serialized_end=132
  _globals['_SETARMABLEREQUEST']._serialized_start=134
  _globals['_SETARMABLEREQUEST']._serialized_end=193
  _globals['_SETDISARMABLEREQUEST']._serialized_start=195
  _globals['_SETDISARMABLEREQUEST']._serialized_end=263
  _globals['_SETALLOWABLEFLIGHTMODESREQUEST']._serialized_start=265
  _globals['_SETALLOWABLEFLIGHTMODESREQUEST']._serialized_end=367
  _globals['_SETARMEDSTATEREQUEST']._serialized_start=369
  _globals['_SETARMEDSTATEREQUEST']._serialized_end=409
  _globals['_SETFLIGHTMODEREQUEST']._serialized_start=411
  _globals['_SETFLIGHTMODEREQUEST']._serialized_end=492
  _globals['_GETALLOWABLEFLIGHTMODESREQUEST']._serialized_start=494
  _globals['_GETALLOWABLEFLIGHTMODESREQUEST']._serialized_end=526
  _globals['_SUBSCRIBEARMDISARMREQUEST']._serialized_start=528
  _globals['_SUBSCRIBEARMDISARMREQUEST']._serialized_end=555
  _globals['_SUBSCRIBEFLIGHTMODECHANGEREQUEST']._serialized_start=557
  _globals['_SUBSCRIBEFLIGHTMODECHANGEREQUEST']._serialized_end=591
  _globals['_SUBSCRIBETAKEOFFREQUEST']._serialized_start=593
  _globals['_SUBSCRIBETAKEOFFREQUEST']._serialized_end=618
  _globals['_SUBSCRIBELANDREQUEST']._serialized_start=620
  _globals['_SUBSCRIBELANDREQUEST']._serialized_end=642
  _globals['_SUBSCRIBEREBOOTREQUEST']._serialized_start=644
  _globals['_SUBSCRIBEREBOOTREQUEST']._serialized_end=668
  _globals['_SUBSCRIBESHUTDOWNREQUEST']._serialized_start=670
  _globals['_SUBSCRIBESHUTDOWNREQUEST']._serialized_end=696
  _globals['_SUBSCRIBETERMINATEREQUEST']._serialized_start=698
  _globals['_SUBSCRIBETERMINATEREQUEST']._serialized_end=725
  _globals['_ARMDISARMRESPONSE']._serialized_start=728
  _globals['_ARMDISARMRESPONSE']._serialized_end=873
  _globals['_FLIGHTMODECHANGERESPONSE']._serialized_start=876
  _globals['_FLIGHTMODECHANGERESPONSE']._serialized_end=1037
  _globals['_TAKEOFFRESPONSE']._serialized_start=1039
  _globals['_TAKEOFFRESPONSE']._serialized_end=1149
  _globals['_LANDRESPONSE']._serialized_start=1151
  _globals['_LANDRESPONSE']._serialized_end=1255
  _globals['_REBOOTRESPONSE']._serialized_start=1257
  _globals['_REBOOTRESPONSE']._serialized_end=1365
  _globals['_SHUTDOWNRESPONSE']._serialized_start=1367
  _globals['_SHUTDOWNRESPONSE']._serialized_end=1479
  _globals['_TERMINATERESPONSE']._serialized_start=1481
  _globals['_TERMINATERESPONSE']._serialized_end=1595
  _globals['_SETARMABLERESPONSE']._serialized_start=1597
  _globals['_SETARMABLERESPONSE']._serialized_end=1693
  _globals['_SETDISARMABLERESPONSE']._serialized_start=1695
  _globals['_SETDISARMABLERESPONSE']._serialized_end=1794
  _globals['_SETALLOWABLEFLIGHTMODESRESPONSE']._serialized_start=1796
  _globals['_SETALLOWABLEFLIGHTMODESRESPONSE']._serialized_end=1905
  _globals['_SETALLOWTAKEOFFRESPONSE']._serialized_start=1907
  _globals['_SETALLOWTAKEOFFRESPONSE']._serialized_end=2008
  _globals['_GETALLOWABLEFLIGHTMODESRESPONSE']._serialized_start=2010
  _globals['_GETALLOWABLEFLIGHTMODESRESPONSE']._serialized_end=2113
  _globals['_SETARMEDSTATERESPONSE']._serialized_start=2115
  _globals['_SETARMEDSTATERESPONSE']._serialized_end=2214
  _globals['_SETFLIGHTMODERESPONSE']._serialized_start=2216
  _globals['_SETFLIGHTMODERESPONSE']._serialized_end=2315
  _globals['_ALLOWABLEFLIGHTMODES']._serialized_start=2317
  _globals['_ALLOWABLEFLIGHTMODES']._serialized_end=2415
  _globals['_ARMDISARM']._serialized_start=2417
  _globals['_ARMDISARM']._serialized_end=2456
  _globals['_ACTIONSERVERRESULT']._serialized_start=2459
  _globals['_ACTIONSERVERRESULT']._serialized_end=2948
  _globals['_ACTIONSERVERRESULT_RESULT']._serialized_start=2571
  _globals['_ACTIONSERVERRESULT_RESULT']._serialized_end=2948
  _globals['_ACTIONSERVERSERVICE']._serialized_start=3317
  _globals['_ACTIONSERVERSERVICE']._serialized_end=5122
# @@protoc_insertion_point(module_scope)
