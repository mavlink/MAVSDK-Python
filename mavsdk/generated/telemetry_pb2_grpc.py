# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import telemetry_pb2 as telemetry__pb2


class TelemetryServiceStub(object):
  """
  Allow users to get vehicle telemetry and state information
  (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.SubscribePosition = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribePosition',
        request_serializer=telemetry__pb2.SubscribePositionRequest.SerializeToString,
        response_deserializer=telemetry__pb2.PositionResponse.FromString,
        )
    self.SubscribeHome = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeHome',
        request_serializer=telemetry__pb2.SubscribeHomeRequest.SerializeToString,
        response_deserializer=telemetry__pb2.HomeResponse.FromString,
        )
    self.SubscribeInAir = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeInAir',
        request_serializer=telemetry__pb2.SubscribeInAirRequest.SerializeToString,
        response_deserializer=telemetry__pb2.InAirResponse.FromString,
        )
    self.SubscribeArmed = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeArmed',
        request_serializer=telemetry__pb2.SubscribeArmedRequest.SerializeToString,
        response_deserializer=telemetry__pb2.ArmedResponse.FromString,
        )
    self.SubscribeAttitudeQuaternion = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeAttitudeQuaternion',
        request_serializer=telemetry__pb2.SubscribeAttitudeQuaternionRequest.SerializeToString,
        response_deserializer=telemetry__pb2.AttitudeQuaternionResponse.FromString,
        )
    self.SubscribeAttitudeEuler = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeAttitudeEuler',
        request_serializer=telemetry__pb2.SubscribeAttitudeEulerRequest.SerializeToString,
        response_deserializer=telemetry__pb2.AttitudeEulerResponse.FromString,
        )
    self.SubscribeAttitudeAngularVelocityBody = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeAttitudeAngularVelocityBody',
        request_serializer=telemetry__pb2.SubscribeAttitudeAngularVelocityBodyRequest.SerializeToString,
        response_deserializer=telemetry__pb2.AttitudeAngularVelocityBodyResponse.FromString,
        )
    self.SubscribeCameraAttitudeQuaternion = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeCameraAttitudeQuaternion',
        request_serializer=telemetry__pb2.SubscribeCameraAttitudeQuaternionRequest.SerializeToString,
        response_deserializer=telemetry__pb2.CameraAttitudeQuaternionResponse.FromString,
        )
    self.SubscribeCameraAttitudeEuler = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeCameraAttitudeEuler',
        request_serializer=telemetry__pb2.SubscribeCameraAttitudeEulerRequest.SerializeToString,
        response_deserializer=telemetry__pb2.CameraAttitudeEulerResponse.FromString,
        )
    self.SubscribeGroundSpeedNed = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeGroundSpeedNed',
        request_serializer=telemetry__pb2.SubscribeGroundSpeedNedRequest.SerializeToString,
        response_deserializer=telemetry__pb2.GroundSpeedNedResponse.FromString,
        )
    self.SubscribeGpsInfo = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeGpsInfo',
        request_serializer=telemetry__pb2.SubscribeGpsInfoRequest.SerializeToString,
        response_deserializer=telemetry__pb2.GpsInfoResponse.FromString,
        )
    self.SubscribeBattery = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeBattery',
        request_serializer=telemetry__pb2.SubscribeBatteryRequest.SerializeToString,
        response_deserializer=telemetry__pb2.BatteryResponse.FromString,
        )
    self.SubscribeFlightMode = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeFlightMode',
        request_serializer=telemetry__pb2.SubscribeFlightModeRequest.SerializeToString,
        response_deserializer=telemetry__pb2.FlightModeResponse.FromString,
        )
    self.SubscribeHealth = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeHealth',
        request_serializer=telemetry__pb2.SubscribeHealthRequest.SerializeToString,
        response_deserializer=telemetry__pb2.HealthResponse.FromString,
        )
    self.SubscribeRcStatus = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeRcStatus',
        request_serializer=telemetry__pb2.SubscribeRcStatusRequest.SerializeToString,
        response_deserializer=telemetry__pb2.RcStatusResponse.FromString,
        )
    self.SubscribeStatusText = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeStatusText',
        request_serializer=telemetry__pb2.SubscribeStatusTextRequest.SerializeToString,
        response_deserializer=telemetry__pb2.StatusTextResponse.FromString,
        )
    self.SubscribeActuatorControlTarget = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeActuatorControlTarget',
        request_serializer=telemetry__pb2.SubscribeActuatorControlTargetRequest.SerializeToString,
        response_deserializer=telemetry__pb2.ActuatorControlTargetResponse.FromString,
        )
    self.SubscribeActuatorOutputStatus = channel.unary_stream(
        '/mavsdk.rpc.telemetry.TelemetryService/SubscribeActuatorOutputStatus',
        request_serializer=telemetry__pb2.SubscribeActuatorOutputStatusRequest.SerializeToString,
        response_deserializer=telemetry__pb2.ActuatorOutputStatusResponse.FromString,
        )


class TelemetryServiceServicer(object):
  """
  Allow users to get vehicle telemetry and state information
  (e.g. battery, GPS, RC connection, flight mode etc.) and set telemetry update rates.
  """

  def SubscribePosition(self, request, context):
    """Subscribe to 'position' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeHome(self, request, context):
    """Subscribe to 'home position' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeInAir(self, request, context):
    """Subscribe to in-air updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeArmed(self, request, context):
    """Subscribe to armed updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeAttitudeQuaternion(self, request, context):
    """Subscribe to 'attitude' updates (quaternion).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeAttitudeEuler(self, request, context):
    """Subscribe to 'attitude' updates (euler).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeAttitudeAngularVelocityBody(self, request, context):
    """Subscribe to 'attitude' updates (angular velocity)
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeCameraAttitudeQuaternion(self, request, context):
    """Subscribe to 'camera attitude' updates (quaternion).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeCameraAttitudeEuler(self, request, context):
    """Subscribe to 'camera attitude' updates (euler).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeGroundSpeedNed(self, request, context):
    """Subscribe to 'ground speed' updates (NED).
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeGpsInfo(self, request, context):
    """Subscribe to 'GPS info' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeBattery(self, request, context):
    """Subscribe to 'battery' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeFlightMode(self, request, context):
    """Subscribe to 'flight mode' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeHealth(self, request, context):
    """Subscribe to 'health' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeRcStatus(self, request, context):
    """Subscribe to 'RC status' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeStatusText(self, request, context):
    """Subscribe to 'status text' updates.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeActuatorControlTarget(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeActuatorOutputStatus(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_TelemetryServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'SubscribePosition': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribePosition,
          request_deserializer=telemetry__pb2.SubscribePositionRequest.FromString,
          response_serializer=telemetry__pb2.PositionResponse.SerializeToString,
      ),
      'SubscribeHome': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeHome,
          request_deserializer=telemetry__pb2.SubscribeHomeRequest.FromString,
          response_serializer=telemetry__pb2.HomeResponse.SerializeToString,
      ),
      'SubscribeInAir': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeInAir,
          request_deserializer=telemetry__pb2.SubscribeInAirRequest.FromString,
          response_serializer=telemetry__pb2.InAirResponse.SerializeToString,
      ),
      'SubscribeArmed': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeArmed,
          request_deserializer=telemetry__pb2.SubscribeArmedRequest.FromString,
          response_serializer=telemetry__pb2.ArmedResponse.SerializeToString,
      ),
      'SubscribeAttitudeQuaternion': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeAttitudeQuaternion,
          request_deserializer=telemetry__pb2.SubscribeAttitudeQuaternionRequest.FromString,
          response_serializer=telemetry__pb2.AttitudeQuaternionResponse.SerializeToString,
      ),
      'SubscribeAttitudeEuler': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeAttitudeEuler,
          request_deserializer=telemetry__pb2.SubscribeAttitudeEulerRequest.FromString,
          response_serializer=telemetry__pb2.AttitudeEulerResponse.SerializeToString,
      ),
      'SubscribeAttitudeAngularVelocityBody': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeAttitudeAngularVelocityBody,
          request_deserializer=telemetry__pb2.SubscribeAttitudeAngularVelocityBodyRequest.FromString,
          response_serializer=telemetry__pb2.AttitudeAngularVelocityBodyResponse.SerializeToString,
      ),
      'SubscribeCameraAttitudeQuaternion': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeCameraAttitudeQuaternion,
          request_deserializer=telemetry__pb2.SubscribeCameraAttitudeQuaternionRequest.FromString,
          response_serializer=telemetry__pb2.CameraAttitudeQuaternionResponse.SerializeToString,
      ),
      'SubscribeCameraAttitudeEuler': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeCameraAttitudeEuler,
          request_deserializer=telemetry__pb2.SubscribeCameraAttitudeEulerRequest.FromString,
          response_serializer=telemetry__pb2.CameraAttitudeEulerResponse.SerializeToString,
      ),
      'SubscribeGroundSpeedNed': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeGroundSpeedNed,
          request_deserializer=telemetry__pb2.SubscribeGroundSpeedNedRequest.FromString,
          response_serializer=telemetry__pb2.GroundSpeedNedResponse.SerializeToString,
      ),
      'SubscribeGpsInfo': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeGpsInfo,
          request_deserializer=telemetry__pb2.SubscribeGpsInfoRequest.FromString,
          response_serializer=telemetry__pb2.GpsInfoResponse.SerializeToString,
      ),
      'SubscribeBattery': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeBattery,
          request_deserializer=telemetry__pb2.SubscribeBatteryRequest.FromString,
          response_serializer=telemetry__pb2.BatteryResponse.SerializeToString,
      ),
      'SubscribeFlightMode': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeFlightMode,
          request_deserializer=telemetry__pb2.SubscribeFlightModeRequest.FromString,
          response_serializer=telemetry__pb2.FlightModeResponse.SerializeToString,
      ),
      'SubscribeHealth': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeHealth,
          request_deserializer=telemetry__pb2.SubscribeHealthRequest.FromString,
          response_serializer=telemetry__pb2.HealthResponse.SerializeToString,
      ),
      'SubscribeRcStatus': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeRcStatus,
          request_deserializer=telemetry__pb2.SubscribeRcStatusRequest.FromString,
          response_serializer=telemetry__pb2.RcStatusResponse.SerializeToString,
      ),
      'SubscribeStatusText': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeStatusText,
          request_deserializer=telemetry__pb2.SubscribeStatusTextRequest.FromString,
          response_serializer=telemetry__pb2.StatusTextResponse.SerializeToString,
      ),
      'SubscribeActuatorControlTarget': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeActuatorControlTarget,
          request_deserializer=telemetry__pb2.SubscribeActuatorControlTargetRequest.FromString,
          response_serializer=telemetry__pb2.ActuatorControlTargetResponse.SerializeToString,
      ),
      'SubscribeActuatorOutputStatus': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeActuatorOutputStatus,
          request_deserializer=telemetry__pb2.SubscribeActuatorOutputStatusRequest.FromString,
          response_serializer=telemetry__pb2.ActuatorOutputStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'mavsdk.rpc.telemetry.TelemetryService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
