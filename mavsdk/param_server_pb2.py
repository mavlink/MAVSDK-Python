# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: param_server/param_server.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fparam_server/param_server.proto\x12\x17mavsdk.rpc.param_server\x1a\x14mavsdk_options.proto\"\'\n\x17RetrieveParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"r\n\x18RetrieveParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x05\"5\n\x16ProvideParamIntRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\"b\n\x17ProvideParamIntResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\")\n\x19RetrieveParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"t\n\x1aRetrieveParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\x02\"7\n\x18ProvideParamFloatRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"d\n\x19ProvideParamFloatResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\"*\n\x1aRetrieveParamCustomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"u\n\x1bRetrieveParamCustomResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\x12\r\n\x05value\x18\x02 \x01(\t\"8\n\x19ProvideParamCustomRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"e\n\x1aProvideParamCustomResponse\x12G\n\x13param_server_result\x18\x01 \x01(\x0b\x32*.mavsdk.rpc.param_server.ParamServerResult\"\x1a\n\x18RetrieveAllParamsRequest\"O\n\x19RetrieveAllParamsResponse\x12\x32\n\x06params\x18\x01 \x01(\x0b\x32\".mavsdk.rpc.param_server.AllParams\"!\n\x1fSubscribeChangedParamIntRequest\"K\n\x17\x43hangedParamIntResponse\x12\x30\n\x05param\x18\x01 \x01(\x0b\x32!.mavsdk.rpc.param_server.IntParam\"#\n!SubscribeChangedParamFloatRequest\"O\n\x19\x43hangedParamFloatResponse\x12\x32\n\x05param\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.param_server.FloatParam\"$\n\"SubscribeChangedParamCustomRequest\"Q\n\x1a\x43hangedParamCustomResponse\x12\x33\n\x05param\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.param_server.CustomParam\"\'\n\x08IntParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05\")\n\nFloatParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x02\"*\n\x0b\x43ustomParam\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xba\x01\n\tAllParams\x12\x35\n\nint_params\x18\x01 \x03(\x0b\x32!.mavsdk.rpc.param_server.IntParam\x12\x39\n\x0c\x66loat_params\x18\x02 \x03(\x0b\x32#.mavsdk.rpc.param_server.FloatParam\x12;\n\rcustom_params\x18\x03 \x03(\x0b\x32$.mavsdk.rpc.param_server.CustomParam\"\xa1\x02\n\x11ParamServerResult\x12\x41\n\x06result\x18\x01 \x01(\x0e\x32\x31.mavsdk.rpc.param_server.ParamServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xb4\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NOT_FOUND\x10\x02\x12\x15\n\x11RESULT_WRONG_TYPE\x10\x03\x12\x1e\n\x1aRESULT_PARAM_NAME_TOO_LONG\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05\x12\x1f\n\x1bRESULT_PARAM_VALUE_TOO_LONG\x10\x06\x32\xec\n\n\x12ParamServerService\x12}\n\x10RetrieveParamInt\x12\x30.mavsdk.rpc.param_server.RetrieveParamIntRequest\x1a\x31.mavsdk.rpc.param_server.RetrieveParamIntResponse\"\x04\x80\xb5\x18\x01\x12z\n\x0fProvideParamInt\x12/.mavsdk.rpc.param_server.ProvideParamIntRequest\x1a\x30.mavsdk.rpc.param_server.ProvideParamIntResponse\"\x04\x80\xb5\x18\x01\x12\x83\x01\n\x12RetrieveParamFloat\x12\x32.mavsdk.rpc.param_server.RetrieveParamFloatRequest\x1a\x33.mavsdk.rpc.param_server.RetrieveParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11ProvideParamFloat\x12\x31.mavsdk.rpc.param_server.ProvideParamFloatRequest\x1a\x32.mavsdk.rpc.param_server.ProvideParamFloatResponse\"\x04\x80\xb5\x18\x01\x12\x86\x01\n\x13RetrieveParamCustom\x12\x33.mavsdk.rpc.param_server.RetrieveParamCustomRequest\x1a\x34.mavsdk.rpc.param_server.RetrieveParamCustomResponse\"\x04\x80\xb5\x18\x01\x12\x83\x01\n\x12ProvideParamCustom\x12\x32.mavsdk.rpc.param_server.ProvideParamCustomRequest\x1a\x33.mavsdk.rpc.param_server.ProvideParamCustomResponse\"\x04\x80\xb5\x18\x01\x12\x80\x01\n\x11RetrieveAllParams\x12\x31.mavsdk.rpc.param_server.RetrieveAllParamsRequest\x1a\x32.mavsdk.rpc.param_server.RetrieveAllParamsResponse\"\x04\x80\xb5\x18\x01\x12\x8e\x01\n\x18SubscribeChangedParamInt\x12\x38.mavsdk.rpc.param_server.SubscribeChangedParamIntRequest\x1a\x30.mavsdk.rpc.param_server.ChangedParamIntResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x94\x01\n\x1aSubscribeChangedParamFloat\x12:.mavsdk.rpc.param_server.SubscribeChangedParamFloatRequest\x1a\x32.mavsdk.rpc.param_server.ChangedParamFloatResponse\"\x04\x80\xb5\x18\x00\x30\x01\x12\x97\x01\n\x1bSubscribeChangedParamCustom\x12;.mavsdk.rpc.param_server.SubscribeChangedParamCustomRequest\x1a\x33.mavsdk.rpc.param_server.ChangedParamCustomResponse\"\x04\x80\xb5\x18\x00\x30\x01\x42*\n\x16io.mavsdk.param_serverB\x10ParamServerProtob\x06proto3')



_RETRIEVEPARAMINTREQUEST = DESCRIPTOR.message_types_by_name['RetrieveParamIntRequest']
_RETRIEVEPARAMINTRESPONSE = DESCRIPTOR.message_types_by_name['RetrieveParamIntResponse']
_PROVIDEPARAMINTREQUEST = DESCRIPTOR.message_types_by_name['ProvideParamIntRequest']
_PROVIDEPARAMINTRESPONSE = DESCRIPTOR.message_types_by_name['ProvideParamIntResponse']
_RETRIEVEPARAMFLOATREQUEST = DESCRIPTOR.message_types_by_name['RetrieveParamFloatRequest']
_RETRIEVEPARAMFLOATRESPONSE = DESCRIPTOR.message_types_by_name['RetrieveParamFloatResponse']
_PROVIDEPARAMFLOATREQUEST = DESCRIPTOR.message_types_by_name['ProvideParamFloatRequest']
_PROVIDEPARAMFLOATRESPONSE = DESCRIPTOR.message_types_by_name['ProvideParamFloatResponse']
_RETRIEVEPARAMCUSTOMREQUEST = DESCRIPTOR.message_types_by_name['RetrieveParamCustomRequest']
_RETRIEVEPARAMCUSTOMRESPONSE = DESCRIPTOR.message_types_by_name['RetrieveParamCustomResponse']
_PROVIDEPARAMCUSTOMREQUEST = DESCRIPTOR.message_types_by_name['ProvideParamCustomRequest']
_PROVIDEPARAMCUSTOMRESPONSE = DESCRIPTOR.message_types_by_name['ProvideParamCustomResponse']
_RETRIEVEALLPARAMSREQUEST = DESCRIPTOR.message_types_by_name['RetrieveAllParamsRequest']
_RETRIEVEALLPARAMSRESPONSE = DESCRIPTOR.message_types_by_name['RetrieveAllParamsResponse']
_SUBSCRIBECHANGEDPARAMINTREQUEST = DESCRIPTOR.message_types_by_name['SubscribeChangedParamIntRequest']
_CHANGEDPARAMINTRESPONSE = DESCRIPTOR.message_types_by_name['ChangedParamIntResponse']
_SUBSCRIBECHANGEDPARAMFLOATREQUEST = DESCRIPTOR.message_types_by_name['SubscribeChangedParamFloatRequest']
_CHANGEDPARAMFLOATRESPONSE = DESCRIPTOR.message_types_by_name['ChangedParamFloatResponse']
_SUBSCRIBECHANGEDPARAMCUSTOMREQUEST = DESCRIPTOR.message_types_by_name['SubscribeChangedParamCustomRequest']
_CHANGEDPARAMCUSTOMRESPONSE = DESCRIPTOR.message_types_by_name['ChangedParamCustomResponse']
_INTPARAM = DESCRIPTOR.message_types_by_name['IntParam']
_FLOATPARAM = DESCRIPTOR.message_types_by_name['FloatParam']
_CUSTOMPARAM = DESCRIPTOR.message_types_by_name['CustomParam']
_ALLPARAMS = DESCRIPTOR.message_types_by_name['AllParams']
_PARAMSERVERRESULT = DESCRIPTOR.message_types_by_name['ParamServerResult']
_PARAMSERVERRESULT_RESULT = _PARAMSERVERRESULT.enum_types_by_name['Result']
RetrieveParamIntRequest = _reflection.GeneratedProtocolMessageType('RetrieveParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMINTREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamIntRequest)
  })
_sym_db.RegisterMessage(RetrieveParamIntRequest)

RetrieveParamIntResponse = _reflection.GeneratedProtocolMessageType('RetrieveParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMINTRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamIntResponse)
  })
_sym_db.RegisterMessage(RetrieveParamIntResponse)

ProvideParamIntRequest = _reflection.GeneratedProtocolMessageType('ProvideParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMINTREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamIntRequest)
  })
_sym_db.RegisterMessage(ProvideParamIntRequest)

ProvideParamIntResponse = _reflection.GeneratedProtocolMessageType('ProvideParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMINTRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamIntResponse)
  })
_sym_db.RegisterMessage(ProvideParamIntResponse)

RetrieveParamFloatRequest = _reflection.GeneratedProtocolMessageType('RetrieveParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMFLOATREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamFloatRequest)
  })
_sym_db.RegisterMessage(RetrieveParamFloatRequest)

RetrieveParamFloatResponse = _reflection.GeneratedProtocolMessageType('RetrieveParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMFLOATRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamFloatResponse)
  })
_sym_db.RegisterMessage(RetrieveParamFloatResponse)

ProvideParamFloatRequest = _reflection.GeneratedProtocolMessageType('ProvideParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMFLOATREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamFloatRequest)
  })
_sym_db.RegisterMessage(ProvideParamFloatRequest)

ProvideParamFloatResponse = _reflection.GeneratedProtocolMessageType('ProvideParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMFLOATRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamFloatResponse)
  })
_sym_db.RegisterMessage(ProvideParamFloatResponse)

RetrieveParamCustomRequest = _reflection.GeneratedProtocolMessageType('RetrieveParamCustomRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMCUSTOMREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamCustomRequest)
  })
_sym_db.RegisterMessage(RetrieveParamCustomRequest)

RetrieveParamCustomResponse = _reflection.GeneratedProtocolMessageType('RetrieveParamCustomResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEPARAMCUSTOMRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveParamCustomResponse)
  })
_sym_db.RegisterMessage(RetrieveParamCustomResponse)

ProvideParamCustomRequest = _reflection.GeneratedProtocolMessageType('ProvideParamCustomRequest', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMCUSTOMREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamCustomRequest)
  })
_sym_db.RegisterMessage(ProvideParamCustomRequest)

ProvideParamCustomResponse = _reflection.GeneratedProtocolMessageType('ProvideParamCustomResponse', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDEPARAMCUSTOMRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ProvideParamCustomResponse)
  })
_sym_db.RegisterMessage(ProvideParamCustomResponse)

RetrieveAllParamsRequest = _reflection.GeneratedProtocolMessageType('RetrieveAllParamsRequest', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEALLPARAMSREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveAllParamsRequest)
  })
_sym_db.RegisterMessage(RetrieveAllParamsRequest)

RetrieveAllParamsResponse = _reflection.GeneratedProtocolMessageType('RetrieveAllParamsResponse', (_message.Message,), {
  'DESCRIPTOR' : _RETRIEVEALLPARAMSRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.RetrieveAllParamsResponse)
  })
_sym_db.RegisterMessage(RetrieveAllParamsResponse)

SubscribeChangedParamIntRequest = _reflection.GeneratedProtocolMessageType('SubscribeChangedParamIntRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANGEDPARAMINTREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.SubscribeChangedParamIntRequest)
  })
_sym_db.RegisterMessage(SubscribeChangedParamIntRequest)

ChangedParamIntResponse = _reflection.GeneratedProtocolMessageType('ChangedParamIntResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEDPARAMINTRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ChangedParamIntResponse)
  })
_sym_db.RegisterMessage(ChangedParamIntResponse)

SubscribeChangedParamFloatRequest = _reflection.GeneratedProtocolMessageType('SubscribeChangedParamFloatRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANGEDPARAMFLOATREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.SubscribeChangedParamFloatRequest)
  })
_sym_db.RegisterMessage(SubscribeChangedParamFloatRequest)

ChangedParamFloatResponse = _reflection.GeneratedProtocolMessageType('ChangedParamFloatResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEDPARAMFLOATRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ChangedParamFloatResponse)
  })
_sym_db.RegisterMessage(ChangedParamFloatResponse)

SubscribeChangedParamCustomRequest = _reflection.GeneratedProtocolMessageType('SubscribeChangedParamCustomRequest', (_message.Message,), {
  'DESCRIPTOR' : _SUBSCRIBECHANGEDPARAMCUSTOMREQUEST,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.SubscribeChangedParamCustomRequest)
  })
_sym_db.RegisterMessage(SubscribeChangedParamCustomRequest)

ChangedParamCustomResponse = _reflection.GeneratedProtocolMessageType('ChangedParamCustomResponse', (_message.Message,), {
  'DESCRIPTOR' : _CHANGEDPARAMCUSTOMRESPONSE,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ChangedParamCustomResponse)
  })
_sym_db.RegisterMessage(ChangedParamCustomResponse)

IntParam = _reflection.GeneratedProtocolMessageType('IntParam', (_message.Message,), {
  'DESCRIPTOR' : _INTPARAM,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.IntParam)
  })
_sym_db.RegisterMessage(IntParam)

FloatParam = _reflection.GeneratedProtocolMessageType('FloatParam', (_message.Message,), {
  'DESCRIPTOR' : _FLOATPARAM,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.FloatParam)
  })
_sym_db.RegisterMessage(FloatParam)

CustomParam = _reflection.GeneratedProtocolMessageType('CustomParam', (_message.Message,), {
  'DESCRIPTOR' : _CUSTOMPARAM,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.CustomParam)
  })
_sym_db.RegisterMessage(CustomParam)

AllParams = _reflection.GeneratedProtocolMessageType('AllParams', (_message.Message,), {
  'DESCRIPTOR' : _ALLPARAMS,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.AllParams)
  })
_sym_db.RegisterMessage(AllParams)

ParamServerResult = _reflection.GeneratedProtocolMessageType('ParamServerResult', (_message.Message,), {
  'DESCRIPTOR' : _PARAMSERVERRESULT,
  '__module__' : 'param_server.param_server_pb2'
  # @@protoc_insertion_point(class_scope:mavsdk.rpc.param_server.ParamServerResult)
  })
_sym_db.RegisterMessage(ParamServerResult)

_PARAMSERVERSERVICE = DESCRIPTOR.services_by_name['ParamServerService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\026io.mavsdk.param_serverB\020ParamServerProto'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamInt']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamInt']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamInt']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamFloat']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamFloat']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamFloat']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamCustom']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveParamCustom']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamCustom']._options = None
  _PARAMSERVERSERVICE.methods_by_name['ProvideParamCustom']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['RetrieveAllParams']._options = None
  _PARAMSERVERSERVICE.methods_by_name['RetrieveAllParams']._serialized_options = b'\200\265\030\001'
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamInt']._options = None
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamInt']._serialized_options = b'\200\265\030\000'
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamFloat']._options = None
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamFloat']._serialized_options = b'\200\265\030\000'
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamCustom']._options = None
  _PARAMSERVERSERVICE.methods_by_name['SubscribeChangedParamCustom']._serialized_options = b'\200\265\030\000'
  _RETRIEVEPARAMINTREQUEST._serialized_start=82
  _RETRIEVEPARAMINTREQUEST._serialized_end=121
  _RETRIEVEPARAMINTRESPONSE._serialized_start=123
  _RETRIEVEPARAMINTRESPONSE._serialized_end=237
  _PROVIDEPARAMINTREQUEST._serialized_start=239
  _PROVIDEPARAMINTREQUEST._serialized_end=292
  _PROVIDEPARAMINTRESPONSE._serialized_start=294
  _PROVIDEPARAMINTRESPONSE._serialized_end=392
  _RETRIEVEPARAMFLOATREQUEST._serialized_start=394
  _RETRIEVEPARAMFLOATREQUEST._serialized_end=435
  _RETRIEVEPARAMFLOATRESPONSE._serialized_start=437
  _RETRIEVEPARAMFLOATRESPONSE._serialized_end=553
  _PROVIDEPARAMFLOATREQUEST._serialized_start=555
  _PROVIDEPARAMFLOATREQUEST._serialized_end=610
  _PROVIDEPARAMFLOATRESPONSE._serialized_start=612
  _PROVIDEPARAMFLOATRESPONSE._serialized_end=712
  _RETRIEVEPARAMCUSTOMREQUEST._serialized_start=714
  _RETRIEVEPARAMCUSTOMREQUEST._serialized_end=756
  _RETRIEVEPARAMCUSTOMRESPONSE._serialized_start=758
  _RETRIEVEPARAMCUSTOMRESPONSE._serialized_end=875
  _PROVIDEPARAMCUSTOMREQUEST._serialized_start=877
  _PROVIDEPARAMCUSTOMREQUEST._serialized_end=933
  _PROVIDEPARAMCUSTOMRESPONSE._serialized_start=935
  _PROVIDEPARAMCUSTOMRESPONSE._serialized_end=1036
  _RETRIEVEALLPARAMSREQUEST._serialized_start=1038
  _RETRIEVEALLPARAMSREQUEST._serialized_end=1064
  _RETRIEVEALLPARAMSRESPONSE._serialized_start=1066
  _RETRIEVEALLPARAMSRESPONSE._serialized_end=1145
  _SUBSCRIBECHANGEDPARAMINTREQUEST._serialized_start=1147
  _SUBSCRIBECHANGEDPARAMINTREQUEST._serialized_end=1180
  _CHANGEDPARAMINTRESPONSE._serialized_start=1182
  _CHANGEDPARAMINTRESPONSE._serialized_end=1257
  _SUBSCRIBECHANGEDPARAMFLOATREQUEST._serialized_start=1259
  _SUBSCRIBECHANGEDPARAMFLOATREQUEST._serialized_end=1294
  _CHANGEDPARAMFLOATRESPONSE._serialized_start=1296
  _CHANGEDPARAMFLOATRESPONSE._serialized_end=1375
  _SUBSCRIBECHANGEDPARAMCUSTOMREQUEST._serialized_start=1377
  _SUBSCRIBECHANGEDPARAMCUSTOMREQUEST._serialized_end=1413
  _CHANGEDPARAMCUSTOMRESPONSE._serialized_start=1415
  _CHANGEDPARAMCUSTOMRESPONSE._serialized_end=1496
  _INTPARAM._serialized_start=1498
  _INTPARAM._serialized_end=1537
  _FLOATPARAM._serialized_start=1539
  _FLOATPARAM._serialized_end=1580
  _CUSTOMPARAM._serialized_start=1582
  _CUSTOMPARAM._serialized_end=1624
  _ALLPARAMS._serialized_start=1627
  _ALLPARAMS._serialized_end=1813
  _PARAMSERVERRESULT._serialized_start=1816
  _PARAMSERVERRESULT._serialized_end=2105
  _PARAMSERVERRESULT_RESULT._serialized_start=1925
  _PARAMSERVERRESULT_RESULT._serialized_end=2105
  _PARAMSERVERSERVICE._serialized_start=2108
  _PARAMSERVERSERVICE._serialized_end=3496
# @@protoc_insertion_point(module_scope)
