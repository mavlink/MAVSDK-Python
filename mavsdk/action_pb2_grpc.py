# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import action_pb2 as action_dot_action__pb2


class ActionServiceStub(object):
    """Enable simple actions such as arming, taking off, and landing.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Arm = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Arm',
                request_serializer=action_dot_action__pb2.ArmRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.ArmResponse.FromString,
                )
        self.Disarm = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Disarm',
                request_serializer=action_dot_action__pb2.DisarmRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.DisarmResponse.FromString,
                )
        self.Takeoff = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Takeoff',
                request_serializer=action_dot_action__pb2.TakeoffRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.TakeoffResponse.FromString,
                )
        self.Land = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Land',
                request_serializer=action_dot_action__pb2.LandRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.LandResponse.FromString,
                )
        self.Reboot = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Reboot',
                request_serializer=action_dot_action__pb2.RebootRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.RebootResponse.FromString,
                )
        self.Shutdown = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Shutdown',
                request_serializer=action_dot_action__pb2.ShutdownRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.ShutdownResponse.FromString,
                )
        self.Terminate = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Terminate',
                request_serializer=action_dot_action__pb2.TerminateRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.TerminateResponse.FromString,
                )
        self.Kill = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/Kill',
                request_serializer=action_dot_action__pb2.KillRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.KillResponse.FromString,
                )
        self.ReturnToLaunch = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/ReturnToLaunch',
                request_serializer=action_dot_action__pb2.ReturnToLaunchRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.ReturnToLaunchResponse.FromString,
                )
        self.GotoLocation = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/GotoLocation',
                request_serializer=action_dot_action__pb2.GotoLocationRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.GotoLocationResponse.FromString,
                )
        self.TransitionToFixedwing = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/TransitionToFixedwing',
                request_serializer=action_dot_action__pb2.TransitionToFixedwingRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.TransitionToFixedwingResponse.FromString,
                )
        self.TransitionToMulticopter = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/TransitionToMulticopter',
                request_serializer=action_dot_action__pb2.TransitionToMulticopterRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.TransitionToMulticopterResponse.FromString,
                )
        self.GetTakeoffAltitude = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/GetTakeoffAltitude',
                request_serializer=action_dot_action__pb2.GetTakeoffAltitudeRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.GetTakeoffAltitudeResponse.FromString,
                )
        self.SetTakeoffAltitude = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/SetTakeoffAltitude',
                request_serializer=action_dot_action__pb2.SetTakeoffAltitudeRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.SetTakeoffAltitudeResponse.FromString,
                )
        self.GetMaximumSpeed = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/GetMaximumSpeed',
                request_serializer=action_dot_action__pb2.GetMaximumSpeedRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.GetMaximumSpeedResponse.FromString,
                )
        self.SetMaximumSpeed = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/SetMaximumSpeed',
                request_serializer=action_dot_action__pb2.SetMaximumSpeedRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.SetMaximumSpeedResponse.FromString,
                )
        self.GetReturnToLaunchAltitude = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/GetReturnToLaunchAltitude',
                request_serializer=action_dot_action__pb2.GetReturnToLaunchAltitudeRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.GetReturnToLaunchAltitudeResponse.FromString,
                )
        self.SetReturnToLaunchAltitude = channel.unary_unary(
                '/mavsdk.rpc.action.ActionService/SetReturnToLaunchAltitude',
                request_serializer=action_dot_action__pb2.SetReturnToLaunchAltitudeRequest.SerializeToString,
                response_deserializer=action_dot_action__pb2.SetReturnToLaunchAltitudeResponse.FromString,
                )


class ActionServiceServicer(object):
    """Enable simple actions such as arming, taking off, and landing.
    """

    def Arm(self, request, context):
        """
        Send command to arm the drone.

        Arming a drone normally causes motors to spin at idle.
        Before arming take all safety precautions and stand clear of the drone!
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Disarm(self, request, context):
        """
        Send command to disarm the drone.

        This will disarm a drone that considers itself landed. If flying, the drone should
        reject the disarm command. Disarming means that all motors will stop.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Takeoff(self, request, context):
        """
        Send command to take off and hover.

        This switches the drone into position control mode and commands
        it to take off and hover at the takeoff altitude.

        Note that the vehicle must be armed before it can take off.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Land(self, request, context):
        """
        Send command to land at the current position.

        This switches the drone to 'Land' flight mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Reboot(self, request, context):
        """
        Send command to reboot the drone components.

        This will reboot the autopilot, companion computer, camera and gimbal.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Shutdown(self, request, context):
        """
        Send command to shut down the drone components.

        This will shut down the autopilot, onboard computer, camera and gimbal.
        This command should only be used when the autopilot is disarmed and autopilots commonly
        reject it if they are not already ready to shut down.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Terminate(self, request, context):
        """
        Send command to terminate the drone.

        This will run the terminate routine as configured on the drone (e.g. disarm and open the parachute).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Kill(self, request, context):
        """
        Send command to kill the drone.

        This will disarm a drone irrespective of whether it is landed or flying.
        Note that the drone will fall out of the sky if this command is used while flying.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReturnToLaunch(self, request, context):
        """
        Send command to return to the launch (takeoff) position and land.

        This switches the drone into [Return mode](https://docs.px4.io/master/en/flight_modes/return.html) which
        generally means it will rise up to a certain altitude to clear any obstacles before heading
        back to the launch (takeoff) position and land there.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GotoLocation(self, request, context):
        """
        Send command to move the vehicle to a specific global position.

        The latitude and longitude are given in degrees (WGS84 frame) and the altitude
        in meters AMSL (above mean sea level).

        The yaw angle is in degrees (frame is NED, 0 is North, positive is clockwise).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransitionToFixedwing(self, request, context):
        """
        Send command to transition the drone to fixedwing.

        The associated action will only be executed for VTOL vehicles (on other vehicle types the
        command will fail). The command will succeed if called when the vehicle
        is already in fixedwing mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TransitionToMulticopter(self, request, context):
        """
        Send command to transition the drone to multicopter.

        The associated action will only be executed for VTOL vehicles (on other vehicle types the
        command will fail). The command will succeed if called when the vehicle
        is already in multicopter mode.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTakeoffAltitude(self, request, context):
        """
        Get the takeoff altitude (in meters above ground).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetTakeoffAltitude(self, request, context):
        """
        Set takeoff altitude (in meters above ground).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMaximumSpeed(self, request, context):
        """
        Get the vehicle maximum speed (in metres/second).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetMaximumSpeed(self, request, context):
        """
        Set vehicle maximum speed (in metres/second).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetReturnToLaunchAltitude(self, request, context):
        """
        Get the return to launch minimum return altitude (in meters).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetReturnToLaunchAltitude(self, request, context):
        """
        Set the return to launch minimum return altitude (in meters).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ActionServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Arm': grpc.unary_unary_rpc_method_handler(
                    servicer.Arm,
                    request_deserializer=action_dot_action__pb2.ArmRequest.FromString,
                    response_serializer=action_dot_action__pb2.ArmResponse.SerializeToString,
            ),
            'Disarm': grpc.unary_unary_rpc_method_handler(
                    servicer.Disarm,
                    request_deserializer=action_dot_action__pb2.DisarmRequest.FromString,
                    response_serializer=action_dot_action__pb2.DisarmResponse.SerializeToString,
            ),
            'Takeoff': grpc.unary_unary_rpc_method_handler(
                    servicer.Takeoff,
                    request_deserializer=action_dot_action__pb2.TakeoffRequest.FromString,
                    response_serializer=action_dot_action__pb2.TakeoffResponse.SerializeToString,
            ),
            'Land': grpc.unary_unary_rpc_method_handler(
                    servicer.Land,
                    request_deserializer=action_dot_action__pb2.LandRequest.FromString,
                    response_serializer=action_dot_action__pb2.LandResponse.SerializeToString,
            ),
            'Reboot': grpc.unary_unary_rpc_method_handler(
                    servicer.Reboot,
                    request_deserializer=action_dot_action__pb2.RebootRequest.FromString,
                    response_serializer=action_dot_action__pb2.RebootResponse.SerializeToString,
            ),
            'Shutdown': grpc.unary_unary_rpc_method_handler(
                    servicer.Shutdown,
                    request_deserializer=action_dot_action__pb2.ShutdownRequest.FromString,
                    response_serializer=action_dot_action__pb2.ShutdownResponse.SerializeToString,
            ),
            'Terminate': grpc.unary_unary_rpc_method_handler(
                    servicer.Terminate,
                    request_deserializer=action_dot_action__pb2.TerminateRequest.FromString,
                    response_serializer=action_dot_action__pb2.TerminateResponse.SerializeToString,
            ),
            'Kill': grpc.unary_unary_rpc_method_handler(
                    servicer.Kill,
                    request_deserializer=action_dot_action__pb2.KillRequest.FromString,
                    response_serializer=action_dot_action__pb2.KillResponse.SerializeToString,
            ),
            'ReturnToLaunch': grpc.unary_unary_rpc_method_handler(
                    servicer.ReturnToLaunch,
                    request_deserializer=action_dot_action__pb2.ReturnToLaunchRequest.FromString,
                    response_serializer=action_dot_action__pb2.ReturnToLaunchResponse.SerializeToString,
            ),
            'GotoLocation': grpc.unary_unary_rpc_method_handler(
                    servicer.GotoLocation,
                    request_deserializer=action_dot_action__pb2.GotoLocationRequest.FromString,
                    response_serializer=action_dot_action__pb2.GotoLocationResponse.SerializeToString,
            ),
            'TransitionToFixedwing': grpc.unary_unary_rpc_method_handler(
                    servicer.TransitionToFixedwing,
                    request_deserializer=action_dot_action__pb2.TransitionToFixedwingRequest.FromString,
                    response_serializer=action_dot_action__pb2.TransitionToFixedwingResponse.SerializeToString,
            ),
            'TransitionToMulticopter': grpc.unary_unary_rpc_method_handler(
                    servicer.TransitionToMulticopter,
                    request_deserializer=action_dot_action__pb2.TransitionToMulticopterRequest.FromString,
                    response_serializer=action_dot_action__pb2.TransitionToMulticopterResponse.SerializeToString,
            ),
            'GetTakeoffAltitude': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTakeoffAltitude,
                    request_deserializer=action_dot_action__pb2.GetTakeoffAltitudeRequest.FromString,
                    response_serializer=action_dot_action__pb2.GetTakeoffAltitudeResponse.SerializeToString,
            ),
            'SetTakeoffAltitude': grpc.unary_unary_rpc_method_handler(
                    servicer.SetTakeoffAltitude,
                    request_deserializer=action_dot_action__pb2.SetTakeoffAltitudeRequest.FromString,
                    response_serializer=action_dot_action__pb2.SetTakeoffAltitudeResponse.SerializeToString,
            ),
            'GetMaximumSpeed': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMaximumSpeed,
                    request_deserializer=action_dot_action__pb2.GetMaximumSpeedRequest.FromString,
                    response_serializer=action_dot_action__pb2.GetMaximumSpeedResponse.SerializeToString,
            ),
            'SetMaximumSpeed': grpc.unary_unary_rpc_method_handler(
                    servicer.SetMaximumSpeed,
                    request_deserializer=action_dot_action__pb2.SetMaximumSpeedRequest.FromString,
                    response_serializer=action_dot_action__pb2.SetMaximumSpeedResponse.SerializeToString,
            ),
            'GetReturnToLaunchAltitude': grpc.unary_unary_rpc_method_handler(
                    servicer.GetReturnToLaunchAltitude,
                    request_deserializer=action_dot_action__pb2.GetReturnToLaunchAltitudeRequest.FromString,
                    response_serializer=action_dot_action__pb2.GetReturnToLaunchAltitudeResponse.SerializeToString,
            ),
            'SetReturnToLaunchAltitude': grpc.unary_unary_rpc_method_handler(
                    servicer.SetReturnToLaunchAltitude,
                    request_deserializer=action_dot_action__pb2.SetReturnToLaunchAltitudeRequest.FromString,
                    response_serializer=action_dot_action__pb2.SetReturnToLaunchAltitudeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mavsdk.rpc.action.ActionService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ActionService(object):
    """Enable simple actions such as arming, taking off, and landing.
    """

    @staticmethod
    def Arm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Arm',
            action_dot_action__pb2.ArmRequest.SerializeToString,
            action_dot_action__pb2.ArmResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Disarm(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Disarm',
            action_dot_action__pb2.DisarmRequest.SerializeToString,
            action_dot_action__pb2.DisarmResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Takeoff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Takeoff',
            action_dot_action__pb2.TakeoffRequest.SerializeToString,
            action_dot_action__pb2.TakeoffResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Land(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Land',
            action_dot_action__pb2.LandRequest.SerializeToString,
            action_dot_action__pb2.LandResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Reboot(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Reboot',
            action_dot_action__pb2.RebootRequest.SerializeToString,
            action_dot_action__pb2.RebootResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Shutdown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Shutdown',
            action_dot_action__pb2.ShutdownRequest.SerializeToString,
            action_dot_action__pb2.ShutdownResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Terminate(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Terminate',
            action_dot_action__pb2.TerminateRequest.SerializeToString,
            action_dot_action__pb2.TerminateResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Kill(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/Kill',
            action_dot_action__pb2.KillRequest.SerializeToString,
            action_dot_action__pb2.KillResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReturnToLaunch(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/ReturnToLaunch',
            action_dot_action__pb2.ReturnToLaunchRequest.SerializeToString,
            action_dot_action__pb2.ReturnToLaunchResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GotoLocation(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/GotoLocation',
            action_dot_action__pb2.GotoLocationRequest.SerializeToString,
            action_dot_action__pb2.GotoLocationResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransitionToFixedwing(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/TransitionToFixedwing',
            action_dot_action__pb2.TransitionToFixedwingRequest.SerializeToString,
            action_dot_action__pb2.TransitionToFixedwingResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TransitionToMulticopter(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/TransitionToMulticopter',
            action_dot_action__pb2.TransitionToMulticopterRequest.SerializeToString,
            action_dot_action__pb2.TransitionToMulticopterResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTakeoffAltitude(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/GetTakeoffAltitude',
            action_dot_action__pb2.GetTakeoffAltitudeRequest.SerializeToString,
            action_dot_action__pb2.GetTakeoffAltitudeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetTakeoffAltitude(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/SetTakeoffAltitude',
            action_dot_action__pb2.SetTakeoffAltitudeRequest.SerializeToString,
            action_dot_action__pb2.SetTakeoffAltitudeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetMaximumSpeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/GetMaximumSpeed',
            action_dot_action__pb2.GetMaximumSpeedRequest.SerializeToString,
            action_dot_action__pb2.GetMaximumSpeedResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetMaximumSpeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/SetMaximumSpeed',
            action_dot_action__pb2.SetMaximumSpeedRequest.SerializeToString,
            action_dot_action__pb2.SetMaximumSpeedResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetReturnToLaunchAltitude(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/GetReturnToLaunchAltitude',
            action_dot_action__pb2.GetReturnToLaunchAltitudeRequest.SerializeToString,
            action_dot_action__pb2.GetReturnToLaunchAltitudeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetReturnToLaunchAltitude(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mavsdk.rpc.action.ActionService/SetReturnToLaunchAltitude',
            action_dot_action__pb2.SetReturnToLaunchAltitudeRequest.SerializeToString,
            action_dot_action__pb2.SetReturnToLaunchAltitudeResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
