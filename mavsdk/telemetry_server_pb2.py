# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: telemetry_server/telemetry_server.proto
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
    'telemetry_server/telemetry_server.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import mavsdk_options_pb2 as mavsdk__options__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'telemetry_server/telemetry_server.proto\x12\x1bmavsdk.rpc.telemetry_server\x1a\x14mavsdk_options.proto\"\xc8\x01\n\x16PublishPositionRequest\x12\x37\n\x08position\x18\x01 \x01(\x0b\x32%.mavsdk.rpc.telemetry_server.Position\x12>\n\x0cvelocity_ned\x18\x02 \x01(\x0b\x32(.mavsdk.rpc.telemetry_server.VelocityNed\x12\x35\n\x07heading\x18\x03 \x01(\x0b\x32$.mavsdk.rpc.telemetry_server.Heading\"I\n\x12PublishHomeRequest\x12\x33\n\x04home\x18\x01 \x01(\x0b\x32%.mavsdk.rpc.telemetry_server.Position\"\xbf\x01\n\x17PublishSysStatusRequest\x12\x35\n\x07\x62\x61ttery\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.telemetry_server.Battery\x12\x1a\n\x12rc_receiver_status\x18\x02 \x01(\x08\x12\x13\n\x0bgyro_status\x18\x03 \x01(\x08\x12\x14\n\x0c\x61\x63\x63\x65l_status\x18\x04 \x01(\x08\x12\x12\n\nmag_status\x18\x05 \x01(\x08\x12\x12\n\ngps_status\x18\x06 \x01(\x08\"\x9c\x01\n\x1ePublishExtendedSysStateRequest\x12:\n\nvtol_state\x18\x01 \x01(\x0e\x32&.mavsdk.rpc.telemetry_server.VtolState\x12>\n\x0clanded_state\x18\x02 \x01(\x0e\x32(.mavsdk.rpc.telemetry_server.LandedState\"(\n\x13PublishInAirRequest\x12\x11\n\tis_in_air\x18\x01 \x01(\x08\"[\n\x19PublishLandedStateRequest\x12>\n\x0clanded_state\x18\x01 \x01(\x0e\x32(.mavsdk.rpc.telemetry_server.LandedState\"\x84\x01\n\x14PublishRawGpsRequest\x12\x34\n\x07raw_gps\x18\x01 \x01(\x0b\x32#.mavsdk.rpc.telemetry_server.RawGps\x12\x36\n\x08gps_info\x18\x02 \x01(\x0b\x32$.mavsdk.rpc.telemetry_server.GpsInfo\"N\n\x15PublishBatteryRequest\x12\x35\n\x07\x62\x61ttery\x18\x01 \x01(\x0b\x32$.mavsdk.rpc.telemetry_server.Battery\"R\n\x16PublishRcStatusRequest\x12\x38\n\trc_status\x18\x01 \x01(\x0b\x32%.mavsdk.rpc.telemetry_server.RcStatus\"X\n\x18PublishStatusTextRequest\x12<\n\x0bstatus_text\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.telemetry_server.StatusText\"Q\n\x16PublishOdometryRequest\x12\x37\n\x08odometry\x18\x01 \x01(\x0b\x32%.mavsdk.rpc.telemetry_server.Odometry\"t\n!PublishPositionVelocityNedRequest\x12O\n\x15position_velocity_ned\x18\x01 \x01(\x0b\x32\x30.mavsdk.rpc.telemetry_server.PositionVelocityNed\"[\n\x19PublishGroundTruthRequest\x12>\n\x0cground_truth\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.telemetry_server.GroundTruth\"B\n\x11PublishImuRequest\x12-\n\x03imu\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.telemetry_server.Imu\"H\n\x17PublishScaledImuRequest\x12-\n\x03imu\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.telemetry_server.Imu\"E\n\x14PublishRawImuRequest\x12-\n\x03imu\x18\x01 \x01(\x0b\x32 .mavsdk.rpc.telemetry_server.Imu\".\n\x1bPublishUnixEpochTimeRequest\x12\x0f\n\x07time_us\x18\x01 \x01(\x04\"d\n\x1cPublishDistanceSensorRequest\x12\x44\n\x0f\x64istance_sensor\x18\x01 \x01(\x0b\x32+.mavsdk.rpc.telemetry_server.DistanceSensor\"\x9c\x01\n\x16PublishAttitudeRequest\x12\x36\n\x05\x61ngle\x18\x01 \x01(\x0b\x32\'.mavsdk.rpc.telemetry_server.EulerAngle\x12J\n\x10\x61ngular_velocity\x18\x02 \x01(\x0b\x32\x30.mavsdk.rpc.telemetry_server.AngularVelocityBody\"o\n\"PublishVisualFlightRulesHudRequest\x12I\n\x12\x66ixed_wing_metrics\x18\x01 \x01(\x0b\x32-.mavsdk.rpc.telemetry_server.FixedwingMetrics\"n\n\x17PublishPositionResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"j\n\x13PublishHomeResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"o\n\x18PublishSysStatusResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"v\n\x1fPublishExtendedSysStateResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"l\n\x15PublishRawGpsResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"m\n\x16PublishBatteryResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"p\n\x19PublishStatusTextResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"n\n\x17PublishOdometryResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"y\n\"PublishPositionVelocityNedResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"q\n\x1aPublishGroundTruthResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"i\n\x12PublishImuResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"o\n\x18PublishScaledImuResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"l\n\x15PublishRawImuResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"s\n\x1cPublishUnixEpochTimeResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"t\n\x1dPublishDistanceSensorResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"n\n\x17PublishAttitudeResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"z\n#PublishVisualFlightRulesHudResponse\x12S\n\x17telemetry_server_result\x18\x01 \x01(\x0b\x32\x32.mavsdk.rpc.telemetry_server.TelemetryServerResult\"\x95\x01\n\x08Position\x12\x1d\n\x0clatitude_deg\x18\x01 \x01(\x01\x42\x07\x82\xb5\x18\x03NaN\x12\x1e\n\rlongitude_deg\x18\x02 \x01(\x01\x42\x07\x82\xb5\x18\x03NaN\x12$\n\x13\x61\x62solute_altitude_m\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12$\n\x13relative_altitude_m\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\'\n\x07Heading\x12\x1c\n\x0bheading_deg\x18\x01 \x01(\x01\x42\x07\x82\xb5\x18\x03NaN\"r\n\nQuaternion\x12\x12\n\x01w\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01x\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01y\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x12\n\x01z\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x14\n\x0ctimestamp_us\x18\x05 \x01(\x04\"s\n\nEulerAngle\x12\x19\n\x08roll_deg\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tpitch_deg\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x18\n\x07yaw_deg\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x14\n\x0ctimestamp_us\x18\x04 \x01(\x04\"l\n\x13\x41ngularVelocityBody\x12\x1b\n\nroll_rad_s\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1c\n\x0bpitch_rad_s\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tyaw_rad_s\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"`\n\x07GpsInfo\x12\x1d\n\x0enum_satellites\x18\x01 \x01(\x05\x42\x05\x82\xb5\x18\x01\x30\x12\x36\n\x08\x66ix_type\x18\x02 \x01(\x0e\x32$.mavsdk.rpc.telemetry_server.FixType\"\xdf\x02\n\x06RawGps\x12\x14\n\x0ctimestamp_us\x18\x01 \x01(\x04\x12\x14\n\x0clatitude_deg\x18\x02 \x01(\x01\x12\x15\n\rlongitude_deg\x18\x03 \x01(\x01\x12\x1b\n\x13\x61\x62solute_altitude_m\x18\x04 \x01(\x02\x12\x0c\n\x04hdop\x18\x05 \x01(\x02\x12\x0c\n\x04vdop\x18\x06 \x01(\x02\x12\x14\n\x0cvelocity_m_s\x18\x07 \x01(\x02\x12\x0f\n\x07\x63og_deg\x18\x08 \x01(\x02\x12\x1c\n\x14\x61ltitude_ellipsoid_m\x18\t \x01(\x02\x12 \n\x18horizontal_uncertainty_m\x18\n \x01(\x02\x12\x1e\n\x16vertical_uncertainty_m\x18\x0b \x01(\x02\x12 \n\x18velocity_uncertainty_m_s\x18\x0c \x01(\x02\x12\x1f\n\x17heading_uncertainty_deg\x18\r \x01(\x02\x12\x0f\n\x07yaw_deg\x18\x0e \x01(\x02\"I\n\x07\x42\x61ttery\x12\x1a\n\tvoltage_v\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\"\n\x11remaining_percent\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"|\n\x08RcStatus\x12%\n\x12was_available_once\x18\x01 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12\x1f\n\x0cis_available\x18\x02 \x01(\x08\x42\t\x82\xb5\x18\x05\x66\x61lse\x12(\n\x17signal_strength_percent\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"U\n\nStatusText\x12\x39\n\x04type\x18\x01 \x01(\x0e\x32+.mavsdk.rpc.telemetry_server.StatusTextType\x12\x0c\n\x04text\x18\x02 \x01(\t\"?\n\x15\x41\x63tuatorControlTarget\x12\x14\n\x05group\x18\x01 \x01(\x05\x42\x05\x82\xb5\x18\x01\x30\x12\x10\n\x08\x63ontrols\x18\x02 \x03(\x02\"?\n\x14\x41\x63tuatorOutputStatus\x12\x15\n\x06\x61\x63tive\x18\x01 \x01(\rB\x05\x82\xb5\x18\x01\x30\x12\x10\n\x08\x61\x63tuator\x18\x02 \x03(\x02\"\'\n\nCovariance\x12\x19\n\x11\x63ovariance_matrix\x18\x01 \x03(\x02\";\n\x0cVelocityBody\x12\r\n\x05x_m_s\x18\x01 \x01(\x02\x12\r\n\x05y_m_s\x18\x02 \x01(\x02\x12\r\n\x05z_m_s\x18\x03 \x01(\x02\"5\n\x0cPositionBody\x12\x0b\n\x03x_m\x18\x01 \x01(\x02\x12\x0b\n\x03y_m\x18\x02 \x01(\x02\x12\x0b\n\x03z_m\x18\x03 \x01(\x02\"\xa4\x05\n\x08Odometry\x12\x11\n\ttime_usec\x18\x01 \x01(\x04\x12@\n\x08\x66rame_id\x18\x02 \x01(\x0e\x32..mavsdk.rpc.telemetry_server.Odometry.MavFrame\x12\x46\n\x0e\x63hild_frame_id\x18\x03 \x01(\x0e\x32..mavsdk.rpc.telemetry_server.Odometry.MavFrame\x12@\n\rposition_body\x18\x04 \x01(\x0b\x32).mavsdk.rpc.telemetry_server.PositionBody\x12\x32\n\x01q\x18\x05 \x01(\x0b\x32\'.mavsdk.rpc.telemetry_server.Quaternion\x12@\n\rvelocity_body\x18\x06 \x01(\x0b\x32).mavsdk.rpc.telemetry_server.VelocityBody\x12O\n\x15\x61ngular_velocity_body\x18\x07 \x01(\x0b\x32\x30.mavsdk.rpc.telemetry_server.AngularVelocityBody\x12@\n\x0fpose_covariance\x18\x08 \x01(\x0b\x32\'.mavsdk.rpc.telemetry_server.Covariance\x12\x44\n\x13velocity_covariance\x18\t \x01(\x0b\x32\'.mavsdk.rpc.telemetry_server.Covariance\"j\n\x08MavFrame\x12\x13\n\x0fMAV_FRAME_UNDEF\x10\x00\x12\x16\n\x12MAV_FRAME_BODY_NED\x10\x08\x12\x18\n\x14MAV_FRAME_VISION_NED\x10\x10\x12\x17\n\x13MAV_FRAME_ESTIM_NED\x10\x12\"\x7f\n\x0e\x44istanceSensor\x12#\n\x12minimum_distance_m\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12#\n\x12maximum_distance_m\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12#\n\x12\x63urrent_distance_m\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\xb0\x01\n\x0eScaledPressure\x12\x14\n\x0ctimestamp_us\x18\x01 \x01(\x04\x12\x1d\n\x15\x61\x62solute_pressure_hpa\x18\x02 \x01(\x02\x12!\n\x19\x64ifferential_pressure_hpa\x18\x03 \x01(\x02\x12\x17\n\x0ftemperature_deg\x18\x04 \x01(\x02\x12-\n%differential_pressure_temperature_deg\x18\x05 \x01(\x02\"Y\n\x0bPositionNed\x12\x18\n\x07north_m\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x17\n\x06\x65\x61st_m\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x17\n\x06\x64own_m\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"D\n\x0bVelocityNed\x12\x11\n\tnorth_m_s\x18\x01 \x01(\x02\x12\x10\n\x08\x65\x61st_m_s\x18\x02 \x01(\x02\x12\x10\n\x08\x64own_m_s\x18\x03 \x01(\x02\"\x8d\x01\n\x13PositionVelocityNed\x12:\n\x08position\x18\x01 \x01(\x0b\x32(.mavsdk.rpc.telemetry_server.PositionNed\x12:\n\x08velocity\x18\x02 \x01(\x0b\x32(.mavsdk.rpc.telemetry_server.VelocityNed\"r\n\x0bGroundTruth\x12\x1d\n\x0clatitude_deg\x18\x01 \x01(\x01\x42\x07\x82\xb5\x18\x03NaN\x12\x1e\n\rlongitude_deg\x18\x02 \x01(\x01\x42\x07\x82\xb5\x18\x03NaN\x12$\n\x13\x61\x62solute_altitude_m\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\xde\x01\n\x10\x46ixedwingMetrics\x12\x1d\n\x0c\x61irspeed_m_s\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12$\n\x13throttle_percentage\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1f\n\x0e\x63limb_rate_m_s\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12 \n\x0fgroundspeed_m_s\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1c\n\x0bheading_deg\x18\x05 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12$\n\x13\x61\x62solute_altitude_m\x18\x06 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"i\n\x0f\x41\x63\x63\x65lerationFrd\x12\x1d\n\x0c\x66orward_m_s2\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1b\n\nright_m_s2\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1a\n\tdown_m_s2\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"o\n\x12\x41ngularVelocityFrd\x12\x1e\n\rforward_rad_s\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1c\n\x0bright_rad_s\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1b\n\ndown_rad_s\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"m\n\x10MagneticFieldFrd\x12\x1e\n\rforward_gauss\x18\x01 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1c\n\x0bright_gauss\x18\x02 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x1b\n\ndown_gauss\x18\x03 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\"\xa0\x02\n\x03Imu\x12\x46\n\x10\x61\x63\x63\x65leration_frd\x18\x01 \x01(\x0b\x32,.mavsdk.rpc.telemetry_server.AccelerationFrd\x12M\n\x14\x61ngular_velocity_frd\x18\x02 \x01(\x0b\x32/.mavsdk.rpc.telemetry_server.AngularVelocityFrd\x12I\n\x12magnetic_field_frd\x18\x03 \x01(\x0b\x32-.mavsdk.rpc.telemetry_server.MagneticFieldFrd\x12!\n\x10temperature_degc\x18\x04 \x01(\x02\x42\x07\x82\xb5\x18\x03NaN\x12\x14\n\x0ctimestamp_us\x18\x05 \x01(\x04\"\xb4\x02\n\x15TelemetryServerResult\x12I\n\x06result\x18\x01 \x01(\x0e\x32\x39.mavsdk.rpc.telemetry_server.TelemetryServerResult.Result\x12\x12\n\nresult_str\x18\x02 \x01(\t\"\xbb\x01\n\x06Result\x12\x12\n\x0eRESULT_UNKNOWN\x10\x00\x12\x12\n\x0eRESULT_SUCCESS\x10\x01\x12\x14\n\x10RESULT_NO_SYSTEM\x10\x02\x12\x1b\n\x17RESULT_CONNECTION_ERROR\x10\x03\x12\x0f\n\x0bRESULT_BUSY\x10\x04\x12\x19\n\x15RESULT_COMMAND_DENIED\x10\x05\x12\x12\n\x0eRESULT_TIMEOUT\x10\x06\x12\x16\n\x12RESULT_UNSUPPORTED\x10\x07*\xa4\x01\n\x07\x46ixType\x12\x13\n\x0f\x46IX_TYPE_NO_GPS\x10\x00\x12\x13\n\x0f\x46IX_TYPE_NO_FIX\x10\x01\x12\x13\n\x0f\x46IX_TYPE_FIX_2D\x10\x02\x12\x13\n\x0f\x46IX_TYPE_FIX_3D\x10\x03\x12\x15\n\x11\x46IX_TYPE_FIX_DGPS\x10\x04\x12\x16\n\x12\x46IX_TYPE_RTK_FLOAT\x10\x05\x12\x16\n\x12\x46IX_TYPE_RTK_FIXED\x10\x06*\x8d\x01\n\tVtolState\x12\x18\n\x14VTOL_STATE_UNDEFINED\x10\x00\x12\x1f\n\x1bVTOL_STATE_TRANSITION_TO_FW\x10\x01\x12\x1f\n\x1bVTOL_STATE_TRANSITION_TO_MC\x10\x02\x12\x11\n\rVTOL_STATE_MC\x10\x03\x12\x11\n\rVTOL_STATE_FW\x10\x04*\xf9\x01\n\x0eStatusTextType\x12\x1a\n\x16STATUS_TEXT_TYPE_DEBUG\x10\x00\x12\x19\n\x15STATUS_TEXT_TYPE_INFO\x10\x01\x12\x1b\n\x17STATUS_TEXT_TYPE_NOTICE\x10\x02\x12\x1c\n\x18STATUS_TEXT_TYPE_WARNING\x10\x03\x12\x1a\n\x16STATUS_TEXT_TYPE_ERROR\x10\x04\x12\x1d\n\x19STATUS_TEXT_TYPE_CRITICAL\x10\x05\x12\x1a\n\x16STATUS_TEXT_TYPE_ALERT\x10\x06\x12\x1e\n\x1aSTATUS_TEXT_TYPE_EMERGENCY\x10\x07*\x93\x01\n\x0bLandedState\x12\x18\n\x14LANDED_STATE_UNKNOWN\x10\x00\x12\x1a\n\x16LANDED_STATE_ON_GROUND\x10\x01\x12\x17\n\x13LANDED_STATE_IN_AIR\x10\x02\x12\x1b\n\x17LANDED_STATE_TAKING_OFF\x10\x03\x12\x18\n\x14LANDED_STATE_LANDING\x10\x04\x32\xd1\x12\n\x16TelemetryServerService\x12\x82\x01\n\x0fPublishPosition\x12\x33.mavsdk.rpc.telemetry_server.PublishPositionRequest\x1a\x34.mavsdk.rpc.telemetry_server.PublishPositionResponse\"\x04\x80\xb5\x18\x01\x12v\n\x0bPublishHome\x12/.mavsdk.rpc.telemetry_server.PublishHomeRequest\x1a\x30.mavsdk.rpc.telemetry_server.PublishHomeResponse\"\x04\x80\xb5\x18\x01\x12\x85\x01\n\x10PublishSysStatus\x12\x34.mavsdk.rpc.telemetry_server.PublishSysStatusRequest\x1a\x35.mavsdk.rpc.telemetry_server.PublishSysStatusResponse\"\x04\x80\xb5\x18\x01\x12\x9a\x01\n\x17PublishExtendedSysState\x12;.mavsdk.rpc.telemetry_server.PublishExtendedSysStateRequest\x1a<.mavsdk.rpc.telemetry_server.PublishExtendedSysStateResponse\"\x04\x80\xb5\x18\x01\x12|\n\rPublishRawGps\x12\x31.mavsdk.rpc.telemetry_server.PublishRawGpsRequest\x1a\x32.mavsdk.rpc.telemetry_server.PublishRawGpsResponse\"\x04\x80\xb5\x18\x01\x12\x7f\n\x0ePublishBattery\x12\x32.mavsdk.rpc.telemetry_server.PublishBatteryRequest\x1a\x33.mavsdk.rpc.telemetry_server.PublishBatteryResponse\"\x04\x80\xb5\x18\x01\x12\x88\x01\n\x11PublishStatusText\x12\x35.mavsdk.rpc.telemetry_server.PublishStatusTextRequest\x1a\x36.mavsdk.rpc.telemetry_server.PublishStatusTextResponse\"\x04\x80\xb5\x18\x01\x12\x82\x01\n\x0fPublishOdometry\x12\x33.mavsdk.rpc.telemetry_server.PublishOdometryRequest\x1a\x34.mavsdk.rpc.telemetry_server.PublishOdometryResponse\"\x04\x80\xb5\x18\x01\x12\xa3\x01\n\x1aPublishPositionVelocityNed\x12>.mavsdk.rpc.telemetry_server.PublishPositionVelocityNedRequest\x1a?.mavsdk.rpc.telemetry_server.PublishPositionVelocityNedResponse\"\x04\x80\xb5\x18\x01\x12\x8b\x01\n\x12PublishGroundTruth\x12\x36.mavsdk.rpc.telemetry_server.PublishGroundTruthRequest\x1a\x37.mavsdk.rpc.telemetry_server.PublishGroundTruthResponse\"\x04\x80\xb5\x18\x01\x12s\n\nPublishImu\x12..mavsdk.rpc.telemetry_server.PublishImuRequest\x1a/.mavsdk.rpc.telemetry_server.PublishImuResponse\"\x04\x80\xb5\x18\x01\x12\x85\x01\n\x10PublishScaledImu\x12\x34.mavsdk.rpc.telemetry_server.PublishScaledImuRequest\x1a\x35.mavsdk.rpc.telemetry_server.PublishScaledImuResponse\"\x04\x80\xb5\x18\x01\x12|\n\rPublishRawImu\x12\x31.mavsdk.rpc.telemetry_server.PublishRawImuRequest\x1a\x32.mavsdk.rpc.telemetry_server.PublishRawImuResponse\"\x04\x80\xb5\x18\x01\x12\x91\x01\n\x14PublishUnixEpochTime\x12\x38.mavsdk.rpc.telemetry_server.PublishUnixEpochTimeRequest\x1a\x39.mavsdk.rpc.telemetry_server.PublishUnixEpochTimeResponse\"\x04\x80\xb5\x18\x01\x12\x94\x01\n\x15PublishDistanceSensor\x12\x39.mavsdk.rpc.telemetry_server.PublishDistanceSensorRequest\x1a:.mavsdk.rpc.telemetry_server.PublishDistanceSensorResponse\"\x04\x80\xb5\x18\x01\x12\x82\x01\n\x0fPublishAttitude\x12\x33.mavsdk.rpc.telemetry_server.PublishAttitudeRequest\x1a\x34.mavsdk.rpc.telemetry_server.PublishAttitudeResponse\"\x04\x80\xb5\x18\x01\x12\xa6\x01\n\x1bPublishVisualFlightRulesHud\x12?.mavsdk.rpc.telemetry_server.PublishVisualFlightRulesHudRequest\x1a@.mavsdk.rpc.telemetry_server.PublishVisualFlightRulesHudResponse\"\x04\x80\xb5\x18\x01\x42\x32\n\x1aio.mavsdk.telemetry_serverB\x14TelemetryServerProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'telemetry_server.telemetry_server_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032io.mavsdk.telemetry_serverB\024TelemetryServerProto'
  _globals['_POSITION'].fields_by_name['latitude_deg']._loaded_options = None
  _globals['_POSITION'].fields_by_name['latitude_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITION'].fields_by_name['longitude_deg']._loaded_options = None
  _globals['_POSITION'].fields_by_name['longitude_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITION'].fields_by_name['absolute_altitude_m']._loaded_options = None
  _globals['_POSITION'].fields_by_name['absolute_altitude_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITION'].fields_by_name['relative_altitude_m']._loaded_options = None
  _globals['_POSITION'].fields_by_name['relative_altitude_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_HEADING'].fields_by_name['heading_deg']._loaded_options = None
  _globals['_HEADING'].fields_by_name['heading_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['w']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['w']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['x']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['x']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['y']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['y']._serialized_options = b'\202\265\030\003NaN'
  _globals['_QUATERNION'].fields_by_name['z']._loaded_options = None
  _globals['_QUATERNION'].fields_by_name['z']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['roll_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['roll_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['pitch_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['pitch_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_EULERANGLE'].fields_by_name['yaw_deg']._loaded_options = None
  _globals['_EULERANGLE'].fields_by_name['yaw_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['roll_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['roll_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['pitch_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['pitch_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['yaw_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYBODY'].fields_by_name['yaw_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_GPSINFO'].fields_by_name['num_satellites']._loaded_options = None
  _globals['_GPSINFO'].fields_by_name['num_satellites']._serialized_options = b'\202\265\030\0010'
  _globals['_BATTERY'].fields_by_name['voltage_v']._loaded_options = None
  _globals['_BATTERY'].fields_by_name['voltage_v']._serialized_options = b'\202\265\030\003NaN'
  _globals['_BATTERY'].fields_by_name['remaining_percent']._loaded_options = None
  _globals['_BATTERY'].fields_by_name['remaining_percent']._serialized_options = b'\202\265\030\003NaN'
  _globals['_RCSTATUS'].fields_by_name['was_available_once']._loaded_options = None
  _globals['_RCSTATUS'].fields_by_name['was_available_once']._serialized_options = b'\202\265\030\005false'
  _globals['_RCSTATUS'].fields_by_name['is_available']._loaded_options = None
  _globals['_RCSTATUS'].fields_by_name['is_available']._serialized_options = b'\202\265\030\005false'
  _globals['_RCSTATUS'].fields_by_name['signal_strength_percent']._loaded_options = None
  _globals['_RCSTATUS'].fields_by_name['signal_strength_percent']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ACTUATORCONTROLTARGET'].fields_by_name['group']._loaded_options = None
  _globals['_ACTUATORCONTROLTARGET'].fields_by_name['group']._serialized_options = b'\202\265\030\0010'
  _globals['_ACTUATOROUTPUTSTATUS'].fields_by_name['active']._loaded_options = None
  _globals['_ACTUATOROUTPUTSTATUS'].fields_by_name['active']._serialized_options = b'\202\265\030\0010'
  _globals['_DISTANCESENSOR'].fields_by_name['minimum_distance_m']._loaded_options = None
  _globals['_DISTANCESENSOR'].fields_by_name['minimum_distance_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_DISTANCESENSOR'].fields_by_name['maximum_distance_m']._loaded_options = None
  _globals['_DISTANCESENSOR'].fields_by_name['maximum_distance_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_DISTANCESENSOR'].fields_by_name['current_distance_m']._loaded_options = None
  _globals['_DISTANCESENSOR'].fields_by_name['current_distance_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITIONNED'].fields_by_name['north_m']._loaded_options = None
  _globals['_POSITIONNED'].fields_by_name['north_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITIONNED'].fields_by_name['east_m']._loaded_options = None
  _globals['_POSITIONNED'].fields_by_name['east_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_POSITIONNED'].fields_by_name['down_m']._loaded_options = None
  _globals['_POSITIONNED'].fields_by_name['down_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_GROUNDTRUTH'].fields_by_name['latitude_deg']._loaded_options = None
  _globals['_GROUNDTRUTH'].fields_by_name['latitude_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_GROUNDTRUTH'].fields_by_name['longitude_deg']._loaded_options = None
  _globals['_GROUNDTRUTH'].fields_by_name['longitude_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_GROUNDTRUTH'].fields_by_name['absolute_altitude_m']._loaded_options = None
  _globals['_GROUNDTRUTH'].fields_by_name['absolute_altitude_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['airspeed_m_s']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['airspeed_m_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['throttle_percentage']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['throttle_percentage']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['climb_rate_m_s']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['climb_rate_m_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['groundspeed_m_s']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['groundspeed_m_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['heading_deg']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['heading_deg']._serialized_options = b'\202\265\030\003NaN'
  _globals['_FIXEDWINGMETRICS'].fields_by_name['absolute_altitude_m']._loaded_options = None
  _globals['_FIXEDWINGMETRICS'].fields_by_name['absolute_altitude_m']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ACCELERATIONFRD'].fields_by_name['forward_m_s2']._loaded_options = None
  _globals['_ACCELERATIONFRD'].fields_by_name['forward_m_s2']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ACCELERATIONFRD'].fields_by_name['right_m_s2']._loaded_options = None
  _globals['_ACCELERATIONFRD'].fields_by_name['right_m_s2']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ACCELERATIONFRD'].fields_by_name['down_m_s2']._loaded_options = None
  _globals['_ACCELERATIONFRD'].fields_by_name['down_m_s2']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['forward_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['forward_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['right_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['right_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['down_rad_s']._loaded_options = None
  _globals['_ANGULARVELOCITYFRD'].fields_by_name['down_rad_s']._serialized_options = b'\202\265\030\003NaN'
  _globals['_MAGNETICFIELDFRD'].fields_by_name['forward_gauss']._loaded_options = None
  _globals['_MAGNETICFIELDFRD'].fields_by_name['forward_gauss']._serialized_options = b'\202\265\030\003NaN'
  _globals['_MAGNETICFIELDFRD'].fields_by_name['right_gauss']._loaded_options = None
  _globals['_MAGNETICFIELDFRD'].fields_by_name['right_gauss']._serialized_options = b'\202\265\030\003NaN'
  _globals['_MAGNETICFIELDFRD'].fields_by_name['down_gauss']._loaded_options = None
  _globals['_MAGNETICFIELDFRD'].fields_by_name['down_gauss']._serialized_options = b'\202\265\030\003NaN'
  _globals['_IMU'].fields_by_name['temperature_degc']._loaded_options = None
  _globals['_IMU'].fields_by_name['temperature_degc']._serialized_options = b'\202\265\030\003NaN'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishPosition']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishPosition']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishHome']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishHome']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishSysStatus']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishSysStatus']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishExtendedSysState']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishExtendedSysState']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishRawGps']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishRawGps']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishBattery']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishBattery']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishStatusText']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishStatusText']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishOdometry']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishOdometry']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishPositionVelocityNed']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishPositionVelocityNed']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishGroundTruth']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishGroundTruth']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishImu']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishImu']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishScaledImu']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishScaledImu']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishRawImu']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishRawImu']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishUnixEpochTime']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishUnixEpochTime']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishDistanceSensor']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishDistanceSensor']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishAttitude']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishAttitude']._serialized_options = b'\200\265\030\001'
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishVisualFlightRulesHud']._loaded_options = None
  _globals['_TELEMETRYSERVERSERVICE'].methods_by_name['PublishVisualFlightRulesHud']._serialized_options = b'\200\265\030\001'
  _globals['_FIXTYPE']._serialized_start=8247
  _globals['_FIXTYPE']._serialized_end=8411
  _globals['_VTOLSTATE']._serialized_start=8414
  _globals['_VTOLSTATE']._serialized_end=8555
  _globals['_STATUSTEXTTYPE']._serialized_start=8558
  _globals['_STATUSTEXTTYPE']._serialized_end=8807
  _globals['_LANDEDSTATE']._serialized_start=8810
  _globals['_LANDEDSTATE']._serialized_end=8957
  _globals['_PUBLISHPOSITIONREQUEST']._serialized_start=95
  _globals['_PUBLISHPOSITIONREQUEST']._serialized_end=295
  _globals['_PUBLISHHOMEREQUEST']._serialized_start=297
  _globals['_PUBLISHHOMEREQUEST']._serialized_end=370
  _globals['_PUBLISHSYSSTATUSREQUEST']._serialized_start=373
  _globals['_PUBLISHSYSSTATUSREQUEST']._serialized_end=564
  _globals['_PUBLISHEXTENDEDSYSSTATEREQUEST']._serialized_start=567
  _globals['_PUBLISHEXTENDEDSYSSTATEREQUEST']._serialized_end=723
  _globals['_PUBLISHINAIRREQUEST']._serialized_start=725
  _globals['_PUBLISHINAIRREQUEST']._serialized_end=765
  _globals['_PUBLISHLANDEDSTATEREQUEST']._serialized_start=767
  _globals['_PUBLISHLANDEDSTATEREQUEST']._serialized_end=858
  _globals['_PUBLISHRAWGPSREQUEST']._serialized_start=861
  _globals['_PUBLISHRAWGPSREQUEST']._serialized_end=993
  _globals['_PUBLISHBATTERYREQUEST']._serialized_start=995
  _globals['_PUBLISHBATTERYREQUEST']._serialized_end=1073
  _globals['_PUBLISHRCSTATUSREQUEST']._serialized_start=1075
  _globals['_PUBLISHRCSTATUSREQUEST']._serialized_end=1157
  _globals['_PUBLISHSTATUSTEXTREQUEST']._serialized_start=1159
  _globals['_PUBLISHSTATUSTEXTREQUEST']._serialized_end=1247
  _globals['_PUBLISHODOMETRYREQUEST']._serialized_start=1249
  _globals['_PUBLISHODOMETRYREQUEST']._serialized_end=1330
  _globals['_PUBLISHPOSITIONVELOCITYNEDREQUEST']._serialized_start=1332
  _globals['_PUBLISHPOSITIONVELOCITYNEDREQUEST']._serialized_end=1448
  _globals['_PUBLISHGROUNDTRUTHREQUEST']._serialized_start=1450
  _globals['_PUBLISHGROUNDTRUTHREQUEST']._serialized_end=1541
  _globals['_PUBLISHIMUREQUEST']._serialized_start=1543
  _globals['_PUBLISHIMUREQUEST']._serialized_end=1609
  _globals['_PUBLISHSCALEDIMUREQUEST']._serialized_start=1611
  _globals['_PUBLISHSCALEDIMUREQUEST']._serialized_end=1683
  _globals['_PUBLISHRAWIMUREQUEST']._serialized_start=1685
  _globals['_PUBLISHRAWIMUREQUEST']._serialized_end=1754
  _globals['_PUBLISHUNIXEPOCHTIMEREQUEST']._serialized_start=1756
  _globals['_PUBLISHUNIXEPOCHTIMEREQUEST']._serialized_end=1802
  _globals['_PUBLISHDISTANCESENSORREQUEST']._serialized_start=1804
  _globals['_PUBLISHDISTANCESENSORREQUEST']._serialized_end=1904
  _globals['_PUBLISHATTITUDEREQUEST']._serialized_start=1907
  _globals['_PUBLISHATTITUDEREQUEST']._serialized_end=2063
  _globals['_PUBLISHVISUALFLIGHTRULESHUDREQUEST']._serialized_start=2065
  _globals['_PUBLISHVISUALFLIGHTRULESHUDREQUEST']._serialized_end=2176
  _globals['_PUBLISHPOSITIONRESPONSE']._serialized_start=2178
  _globals['_PUBLISHPOSITIONRESPONSE']._serialized_end=2288
  _globals['_PUBLISHHOMERESPONSE']._serialized_start=2290
  _globals['_PUBLISHHOMERESPONSE']._serialized_end=2396
  _globals['_PUBLISHSYSSTATUSRESPONSE']._serialized_start=2398
  _globals['_PUBLISHSYSSTATUSRESPONSE']._serialized_end=2509
  _globals['_PUBLISHEXTENDEDSYSSTATERESPONSE']._serialized_start=2511
  _globals['_PUBLISHEXTENDEDSYSSTATERESPONSE']._serialized_end=2629
  _globals['_PUBLISHRAWGPSRESPONSE']._serialized_start=2631
  _globals['_PUBLISHRAWGPSRESPONSE']._serialized_end=2739
  _globals['_PUBLISHBATTERYRESPONSE']._serialized_start=2741
  _globals['_PUBLISHBATTERYRESPONSE']._serialized_end=2850
  _globals['_PUBLISHSTATUSTEXTRESPONSE']._serialized_start=2852
  _globals['_PUBLISHSTATUSTEXTRESPONSE']._serialized_end=2964
  _globals['_PUBLISHODOMETRYRESPONSE']._serialized_start=2966
  _globals['_PUBLISHODOMETRYRESPONSE']._serialized_end=3076
  _globals['_PUBLISHPOSITIONVELOCITYNEDRESPONSE']._serialized_start=3078
  _globals['_PUBLISHPOSITIONVELOCITYNEDRESPONSE']._serialized_end=3199
  _globals['_PUBLISHGROUNDTRUTHRESPONSE']._serialized_start=3201
  _globals['_PUBLISHGROUNDTRUTHRESPONSE']._serialized_end=3314
  _globals['_PUBLISHIMURESPONSE']._serialized_start=3316
  _globals['_PUBLISHIMURESPONSE']._serialized_end=3421
  _globals['_PUBLISHSCALEDIMURESPONSE']._serialized_start=3423
  _globals['_PUBLISHSCALEDIMURESPONSE']._serialized_end=3534
  _globals['_PUBLISHRAWIMURESPONSE']._serialized_start=3536
  _globals['_PUBLISHRAWIMURESPONSE']._serialized_end=3644
  _globals['_PUBLISHUNIXEPOCHTIMERESPONSE']._serialized_start=3646
  _globals['_PUBLISHUNIXEPOCHTIMERESPONSE']._serialized_end=3761
  _globals['_PUBLISHDISTANCESENSORRESPONSE']._serialized_start=3763
  _globals['_PUBLISHDISTANCESENSORRESPONSE']._serialized_end=3879
  _globals['_PUBLISHATTITUDERESPONSE']._serialized_start=3881
  _globals['_PUBLISHATTITUDERESPONSE']._serialized_end=3991
  _globals['_PUBLISHVISUALFLIGHTRULESHUDRESPONSE']._serialized_start=3993
  _globals['_PUBLISHVISUALFLIGHTRULESHUDRESPONSE']._serialized_end=4115
  _globals['_POSITION']._serialized_start=4118
  _globals['_POSITION']._serialized_end=4267
  _globals['_HEADING']._serialized_start=4269
  _globals['_HEADING']._serialized_end=4308
  _globals['_QUATERNION']._serialized_start=4310
  _globals['_QUATERNION']._serialized_end=4424
  _globals['_EULERANGLE']._serialized_start=4426
  _globals['_EULERANGLE']._serialized_end=4541
  _globals['_ANGULARVELOCITYBODY']._serialized_start=4543
  _globals['_ANGULARVELOCITYBODY']._serialized_end=4651
  _globals['_GPSINFO']._serialized_start=4653
  _globals['_GPSINFO']._serialized_end=4749
  _globals['_RAWGPS']._serialized_start=4752
  _globals['_RAWGPS']._serialized_end=5103
  _globals['_BATTERY']._serialized_start=5105
  _globals['_BATTERY']._serialized_end=5178
  _globals['_RCSTATUS']._serialized_start=5180
  _globals['_RCSTATUS']._serialized_end=5304
  _globals['_STATUSTEXT']._serialized_start=5306
  _globals['_STATUSTEXT']._serialized_end=5391
  _globals['_ACTUATORCONTROLTARGET']._serialized_start=5393
  _globals['_ACTUATORCONTROLTARGET']._serialized_end=5456
  _globals['_ACTUATOROUTPUTSTATUS']._serialized_start=5458
  _globals['_ACTUATOROUTPUTSTATUS']._serialized_end=5521
  _globals['_COVARIANCE']._serialized_start=5523
  _globals['_COVARIANCE']._serialized_end=5562
  _globals['_VELOCITYBODY']._serialized_start=5564
  _globals['_VELOCITYBODY']._serialized_end=5623
  _globals['_POSITIONBODY']._serialized_start=5625
  _globals['_POSITIONBODY']._serialized_end=5678
  _globals['_ODOMETRY']._serialized_start=5681
  _globals['_ODOMETRY']._serialized_end=6357
  _globals['_ODOMETRY_MAVFRAME']._serialized_start=6251
  _globals['_ODOMETRY_MAVFRAME']._serialized_end=6357
  _globals['_DISTANCESENSOR']._serialized_start=6359
  _globals['_DISTANCESENSOR']._serialized_end=6486
  _globals['_SCALEDPRESSURE']._serialized_start=6489
  _globals['_SCALEDPRESSURE']._serialized_end=6665
  _globals['_POSITIONNED']._serialized_start=6667
  _globals['_POSITIONNED']._serialized_end=6756
  _globals['_VELOCITYNED']._serialized_start=6758
  _globals['_VELOCITYNED']._serialized_end=6826
  _globals['_POSITIONVELOCITYNED']._serialized_start=6829
  _globals['_POSITIONVELOCITYNED']._serialized_end=6970
  _globals['_GROUNDTRUTH']._serialized_start=6972
  _globals['_GROUNDTRUTH']._serialized_end=7086
  _globals['_FIXEDWINGMETRICS']._serialized_start=7089
  _globals['_FIXEDWINGMETRICS']._serialized_end=7311
  _globals['_ACCELERATIONFRD']._serialized_start=7313
  _globals['_ACCELERATIONFRD']._serialized_end=7418
  _globals['_ANGULARVELOCITYFRD']._serialized_start=7420
  _globals['_ANGULARVELOCITYFRD']._serialized_end=7531
  _globals['_MAGNETICFIELDFRD']._serialized_start=7533
  _globals['_MAGNETICFIELDFRD']._serialized_end=7642
  _globals['_IMU']._serialized_start=7645
  _globals['_IMU']._serialized_end=7933
  _globals['_TELEMETRYSERVERRESULT']._serialized_start=7936
  _globals['_TELEMETRYSERVERRESULT']._serialized_end=8244
  _globals['_TELEMETRYSERVERRESULT_RESULT']._serialized_start=8057
  _globals['_TELEMETRYSERVERRESULT_RESULT']._serialized_end=8244
  _globals['_TELEMETRYSERVERSERVICE']._serialized_start=8960
  _globals['_TELEMETRYSERVERSERVICE']._serialized_end=11345
# @@protoc_insertion_point(module_scope)
