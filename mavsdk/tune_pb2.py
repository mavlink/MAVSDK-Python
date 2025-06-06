# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: tune/tune.proto
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
    'tune/tune.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ftune/tune.proto\x12\x0fmavsdk.rpc.tune\"M\n\x0fPlayTuneRequest\x12:\n\x10tune_description\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.tune.TuneDescription\"D\n\x10PlayTuneResponse\x12\x30\n\x0btune_result\x18\x01 \x01(\x0b\x32\x1b.mavsdk.rpc.tune.TuneResult\"U\n\x0fTuneDescription\x12\x33\n\rsong_elements\x18\x01 \x03(\x0e\x32\x1c.mavsdk.rpc.tune.SongElement\x12\r\n\x05tempo\x18\x02 \x01(\x05\"\xe3\x01\n\nTuneResult\x12\x32\n\x06result\x18\x01 \x01(\x0e\x32\".mavsdk.rpc.tune.TuneResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\x8c\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x18\n\x14RESULT_INVALID_TEMPO\x10\x02\x12\x18\n\x14RESULT_TUNE_TOO_LONG\x10\x03\x12\x10\n\x0cRESULT_ERROR\x10\x04\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x05*\xd1\x04\n\x0bSongElement\x12\x1d\n\x19SONG_ELEMENT_STYLE_LEGATO\x10\x00\x12\x1d\n\x19SONG_ELEMENT_STYLE_NORMAL\x10\x01\x12\x1f\n\x1bSONG_ELEMENT_STYLE_STACCATO\x10\x02\x12\x1b\n\x17SONG_ELEMENT_DURATION_1\x10\x03\x12\x1b\n\x17SONG_ELEMENT_DURATION_2\x10\x04\x12\x1b\n\x17SONG_ELEMENT_DURATION_4\x10\x05\x12\x1b\n\x17SONG_ELEMENT_DURATION_8\x10\x06\x12\x1c\n\x18SONG_ELEMENT_DURATION_16\x10\x07\x12\x1c\n\x18SONG_ELEMENT_DURATION_32\x10\x08\x12\x17\n\x13SONG_ELEMENT_NOTE_A\x10\t\x12\x17\n\x13SONG_ELEMENT_NOTE_B\x10\n\x12\x17\n\x13SONG_ELEMENT_NOTE_C\x10\x0b\x12\x17\n\x13SONG_ELEMENT_NOTE_D\x10\x0c\x12\x17\n\x13SONG_ELEMENT_NOTE_E\x10\r\x12\x17\n\x13SONG_ELEMENT_NOTE_F\x10\x0e\x12\x17\n\x13SONG_ELEMENT_NOTE_G\x10\x0f\x12\x1b\n\x17SONG_ELEMENT_NOTE_PAUSE\x10\x10\x12\x16\n\x12SONG_ELEMENT_SHARP\x10\x11\x12\x15\n\x11SONG_ELEMENT_FLAT\x10\x12\x12\x1a\n\x16SONG_ELEMENT_OCTAVE_UP\x10\x13\x12\x1c\n\x18SONG_ELEMENT_OCTAVE_DOWN\x10\x14\x32`\n\x0bTuneService\x12Q\n\x08PlayTune\x12 .mavsdk.rpc.tune.PlayTuneRequest\x1a!.mavsdk.rpc.tune.PlayTuneResponse\"\x00\x42\x1b\n\x0eio.mavsdk.tuneB\tTuneProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tune.tune_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\016io.mavsdk.tuneB\tTuneProto'
  _globals['_SONGELEMENT']._serialized_start=503
  _globals['_SONGELEMENT']._serialized_end=1096
  _globals['_PLAYTUNEREQUEST']._serialized_start=36
  _globals['_PLAYTUNEREQUEST']._serialized_end=113
  _globals['_PLAYTUNERESPONSE']._serialized_start=115
  _globals['_PLAYTUNERESPONSE']._serialized_end=183
  _globals['_TUNEDESCRIPTION']._serialized_start=185
  _globals['_TUNEDESCRIPTION']._serialized_end=270
  _globals['_TUNERESULT']._serialized_start=273
  _globals['_TUNERESULT']._serialized_end=500
  _globals['_TUNERESULT_RESULT']._serialized_start=360
  _globals['_TUNERESULT_RESULT']._serialized_end=500
  _globals['_TUNESERVICE']._serialized_start=1098
  _globals['_TUNESERVICE']._serialized_end=1194
# @@protoc_insertion_point(module_scope)
