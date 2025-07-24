# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import action_server_pb2, action_server_pb2_grpc
from enum import Enum


class FlightMode(Enum):
    """
     Flight modes.

     For more information about flight modes, check out
     https://docs.px4.io/master/en/config/flight_mode.html.

     Values
     ------
     UNKNOWN
          Mode not known

     READY
          Armed and ready to take off

     TAKEOFF
          Taking off

     HOLD
          Holding (hovering in place (or circling for fixed-wing vehicles)

     MISSION
          In mission

     RETURN_TO_LAUNCH
          Returning to launch position (then landing)

     LAND
          Landing

     OFFBOARD
          In 'offboard' mode

     FOLLOW_ME
          In 'follow-me' mode

     MANUAL
          In 'Manual' mode

     ALTCTL
          In 'Altitude Control' mode

     POSCTL
          In 'Position Control' mode

     ACRO
          In 'Acro' mode

     STABILIZED
          In 'Stabilize' mode

     """

    
    UNKNOWN = 0
    READY = 1
    TAKEOFF = 2
    HOLD = 3
    MISSION = 4
    RETURN_TO_LAUNCH = 5
    LAND = 6
    OFFBOARD = 7
    FOLLOW_ME = 8
    MANUAL = 9
    ALTCTL = 10
    POSCTL = 11
    ACRO = 12
    STABILIZED = 13

    def translate_to_rpc(self):
        if self == FlightMode.UNKNOWN:
            return action_server_pb2.FLIGHT_MODE_UNKNOWN
        if self == FlightMode.READY:
            return action_server_pb2.FLIGHT_MODE_READY
        if self == FlightMode.TAKEOFF:
            return action_server_pb2.FLIGHT_MODE_TAKEOFF
        if self == FlightMode.HOLD:
            return action_server_pb2.FLIGHT_MODE_HOLD
        if self == FlightMode.MISSION:
            return action_server_pb2.FLIGHT_MODE_MISSION
        if self == FlightMode.RETURN_TO_LAUNCH:
            return action_server_pb2.FLIGHT_MODE_RETURN_TO_LAUNCH
        if self == FlightMode.LAND:
            return action_server_pb2.FLIGHT_MODE_LAND
        if self == FlightMode.OFFBOARD:
            return action_server_pb2.FLIGHT_MODE_OFFBOARD
        if self == FlightMode.FOLLOW_ME:
            return action_server_pb2.FLIGHT_MODE_FOLLOW_ME
        if self == FlightMode.MANUAL:
            return action_server_pb2.FLIGHT_MODE_MANUAL
        if self == FlightMode.ALTCTL:
            return action_server_pb2.FLIGHT_MODE_ALTCTL
        if self == FlightMode.POSCTL:
            return action_server_pb2.FLIGHT_MODE_POSCTL
        if self == FlightMode.ACRO:
            return action_server_pb2.FLIGHT_MODE_ACRO
        if self == FlightMode.STABILIZED:
            return action_server_pb2.FLIGHT_MODE_STABILIZED

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_UNKNOWN:
            return FlightMode.UNKNOWN
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_READY:
            return FlightMode.READY
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_TAKEOFF:
            return FlightMode.TAKEOFF
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_HOLD:
            return FlightMode.HOLD
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_MISSION:
            return FlightMode.MISSION
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_RETURN_TO_LAUNCH:
            return FlightMode.RETURN_TO_LAUNCH
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_LAND:
            return FlightMode.LAND
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_OFFBOARD:
            return FlightMode.OFFBOARD
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_FOLLOW_ME:
            return FlightMode.FOLLOW_ME
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_MANUAL:
            return FlightMode.MANUAL
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_ALTCTL:
            return FlightMode.ALTCTL
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_POSCTL:
            return FlightMode.POSCTL
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_ACRO:
            return FlightMode.ACRO
        if rpc_enum_value == action_server_pb2.FLIGHT_MODE_STABILIZED:
            return FlightMode.STABILIZED

    def __str__(self):
        return self.name


class AllowableFlightModes:
    """
     State to check if the vehicle can transition to
     respective flightmodes

     Parameters
     ----------
     can_auto_mode : bool
          Auto/mission mode 

     can_guided_mode : bool
          Guided mode

     can_stabilize_mode : bool
          Stabilize mode

     """

    

    def __init__(
            self,
            can_auto_mode,
            can_guided_mode,
            can_stabilize_mode):
        """ Initializes the AllowableFlightModes object """
        self.can_auto_mode = can_auto_mode
        self.can_guided_mode = can_guided_mode
        self.can_stabilize_mode = can_stabilize_mode

    def __eq__(self, to_compare):
        """ Checks if two AllowableFlightModes are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # AllowableFlightModes object
            return \
                (self.can_auto_mode == to_compare.can_auto_mode) and \
                (self.can_guided_mode == to_compare.can_guided_mode) and \
                (self.can_stabilize_mode == to_compare.can_stabilize_mode)

        except AttributeError:
            return False

    def __str__(self):
        """ AllowableFlightModes in string representation """
        struct_repr = ", ".join([
                "can_auto_mode: " + str(self.can_auto_mode),
                "can_guided_mode: " + str(self.can_guided_mode),
                "can_stabilize_mode: " + str(self.can_stabilize_mode)
                ])

        return f"AllowableFlightModes: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcAllowableFlightModes):
        """ Translates a gRPC struct to the SDK equivalent """
        return AllowableFlightModes(
                
                rpcAllowableFlightModes.can_auto_mode,
                
                
                rpcAllowableFlightModes.can_guided_mode,
                
                
                rpcAllowableFlightModes.can_stabilize_mode
                )

    def translate_to_rpc(self, rpcAllowableFlightModes):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcAllowableFlightModes.can_auto_mode = self.can_auto_mode
            
        
        
        
            
        rpcAllowableFlightModes.can_guided_mode = self.can_guided_mode
            
        
        
        
            
        rpcAllowableFlightModes.can_stabilize_mode = self.can_stabilize_mode
            
        
        


class ArmDisarm:
    """
     Arming message type

     Parameters
     ----------
     arm : bool
          Should vehicle arm

     force : bool
          Should arm override pre-flight checks

     """

    

    def __init__(
            self,
            arm,
            force):
        """ Initializes the ArmDisarm object """
        self.arm = arm
        self.force = force

    def __eq__(self, to_compare):
        """ Checks if two ArmDisarm are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ArmDisarm object
            return \
                (self.arm == to_compare.arm) and \
                (self.force == to_compare.force)

        except AttributeError:
            return False

    def __str__(self):
        """ ArmDisarm in string representation """
        struct_repr = ", ".join([
                "arm: " + str(self.arm),
                "force: " + str(self.force)
                ])

        return f"ArmDisarm: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcArmDisarm):
        """ Translates a gRPC struct to the SDK equivalent """
        return ArmDisarm(
                
                rpcArmDisarm.arm,
                
                
                rpcArmDisarm.force
                )

    def translate_to_rpc(self, rpcArmDisarm):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcArmDisarm.arm = self.arm
            
        
        
        
            
        rpcArmDisarm.force = self.force
            
        
        


class ActionServerResult:
    """
     Result type.

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for action requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request was successful

         NO_SYSTEM
              No system is connected

         CONNECTION_ERROR
              Connection error

         BUSY
              Vehicle is busy

         COMMAND_DENIED
              Command refused by vehicle

         COMMAND_DENIED_LANDED_STATE_UNKNOWN
              Command refused because landed state is unknown

         COMMAND_DENIED_NOT_LANDED
              Command refused because vehicle not landed

         TIMEOUT
              Request timed out

         VTOL_TRANSITION_SUPPORT_UNKNOWN
              Hybrid/VTOL transition support is unknown

         NO_VTOL_TRANSITION_SUPPORT
              Vehicle does not support hybrid/VTOL transitions

         PARAMETER_ERROR
              Error getting or setting parameter

         NEXT
              Intermediate message showing progress or instructions on the next steps

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        CONNECTION_ERROR = 3
        BUSY = 4
        COMMAND_DENIED = 5
        COMMAND_DENIED_LANDED_STATE_UNKNOWN = 6
        COMMAND_DENIED_NOT_LANDED = 7
        TIMEOUT = 8
        VTOL_TRANSITION_SUPPORT_UNKNOWN = 9
        NO_VTOL_TRANSITION_SUPPORT = 10
        PARAMETER_ERROR = 11
        NEXT = 12

        def translate_to_rpc(self):
            if self == ActionServerResult.Result.UNKNOWN:
                return action_server_pb2.ActionServerResult.RESULT_UNKNOWN
            if self == ActionServerResult.Result.SUCCESS:
                return action_server_pb2.ActionServerResult.RESULT_SUCCESS
            if self == ActionServerResult.Result.NO_SYSTEM:
                return action_server_pb2.ActionServerResult.RESULT_NO_SYSTEM
            if self == ActionServerResult.Result.CONNECTION_ERROR:
                return action_server_pb2.ActionServerResult.RESULT_CONNECTION_ERROR
            if self == ActionServerResult.Result.BUSY:
                return action_server_pb2.ActionServerResult.RESULT_BUSY
            if self == ActionServerResult.Result.COMMAND_DENIED:
                return action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED
            if self == ActionServerResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if self == ActionServerResult.Result.COMMAND_DENIED_NOT_LANDED:
                return action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED_NOT_LANDED
            if self == ActionServerResult.Result.TIMEOUT:
                return action_server_pb2.ActionServerResult.RESULT_TIMEOUT
            if self == ActionServerResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return action_server_pb2.ActionServerResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN
            if self == ActionServerResult.Result.NO_VTOL_TRANSITION_SUPPORT:
                return action_server_pb2.ActionServerResult.RESULT_NO_VTOL_TRANSITION_SUPPORT
            if self == ActionServerResult.Result.PARAMETER_ERROR:
                return action_server_pb2.ActionServerResult.RESULT_PARAMETER_ERROR
            if self == ActionServerResult.Result.NEXT:
                return action_server_pb2.ActionServerResult.RESULT_NEXT

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_UNKNOWN:
                return ActionServerResult.Result.UNKNOWN
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_SUCCESS:
                return ActionServerResult.Result.SUCCESS
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_NO_SYSTEM:
                return ActionServerResult.Result.NO_SYSTEM
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_CONNECTION_ERROR:
                return ActionServerResult.Result.CONNECTION_ERROR
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_BUSY:
                return ActionServerResult.Result.BUSY
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED:
                return ActionServerResult.Result.COMMAND_DENIED
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED_LANDED_STATE_UNKNOWN:
                return ActionServerResult.Result.COMMAND_DENIED_LANDED_STATE_UNKNOWN
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_COMMAND_DENIED_NOT_LANDED:
                return ActionServerResult.Result.COMMAND_DENIED_NOT_LANDED
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_TIMEOUT:
                return ActionServerResult.Result.TIMEOUT
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_VTOL_TRANSITION_SUPPORT_UNKNOWN:
                return ActionServerResult.Result.VTOL_TRANSITION_SUPPORT_UNKNOWN
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_NO_VTOL_TRANSITION_SUPPORT:
                return ActionServerResult.Result.NO_VTOL_TRANSITION_SUPPORT
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_PARAMETER_ERROR:
                return ActionServerResult.Result.PARAMETER_ERROR
            if rpc_enum_value == action_server_pb2.ActionServerResult.RESULT_NEXT:
                return ActionServerResult.Result.NEXT

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the ActionServerResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two ActionServerResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ActionServerResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ ActionServerResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"ActionServerResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcActionServerResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return ActionServerResult(
                
                ActionServerResult.Result.translate_from_rpc(rpcActionServerResult.result),
                
                
                rpcActionServerResult.result_str
                )

    def translate_to_rpc(self, rpcActionServerResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcActionServerResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcActionServerResult.result_str = self.result_str
            
        
        



class ActionServerError(Exception):
    """ Raised when a ActionServerResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class ActionServer(AsyncBase):
    """
     Provide vehicle actions (as a server) such as arming, taking off, and landing.

     Generated by dcsdkgen - MAVSDK ActionServer API
    """

    # Plugin name
    name = "ActionServer"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = action_server_pb2_grpc.ActionServerServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return ActionServerResult.translate_from_rpc(response.action_server_result)
    

    async def arm_disarm(self):
        """
         Subscribe to ARM/DISARM commands

         Yields
         -------
         arm : ArmDisarm
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeArmDisarmRequest()
        arm_disarm_stream = self._stub.SubscribeArmDisarm(request)

        try:
            async for response in arm_disarm_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "arm_disarm()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    arm_disarm_stream.cancel();
                    return
                

            
                yield ArmDisarm.translate_from_rpc(response.arm)
        finally:
            arm_disarm_stream.cancel()

    async def flight_mode_change(self):
        """
         Subscribe to DO_SET_MODE

         Yields
         -------
         flight_mode : FlightMode
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeFlightModeChangeRequest()
        flight_mode_change_stream = self._stub.SubscribeFlightModeChange(request)

        try:
            async for response in flight_mode_change_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "flight_mode_change()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    flight_mode_change_stream.cancel();
                    return
                

            
                yield FlightMode.translate_from_rpc(response.flight_mode)
        finally:
            flight_mode_change_stream.cancel()

    async def takeoff(self):
        """
         Subscribe to takeoff command

         Yields
         -------
         takeoff : bool
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeTakeoffRequest()
        takeoff_stream = self._stub.SubscribeTakeoff(request)

        try:
            async for response in takeoff_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "takeoff()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    takeoff_stream.cancel();
                    return
                

            
                yield response.takeoff
        finally:
            takeoff_stream.cancel()

    async def land(self):
        """
         Subscribe to land command

         Yields
         -------
         land : bool
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeLandRequest()
        land_stream = self._stub.SubscribeLand(request)

        try:
            async for response in land_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "land()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    land_stream.cancel();
                    return
                

            
                yield response.land
        finally:
            land_stream.cancel()

    async def reboot(self):
        """
         Subscribe to reboot command

         Yields
         -------
         reboot : bool
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeRebootRequest()
        reboot_stream = self._stub.SubscribeReboot(request)

        try:
            async for response in reboot_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "reboot()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    reboot_stream.cancel();
                    return
                

            
                yield response.reboot
        finally:
            reboot_stream.cancel()

    async def shutdown(self):
        """
         Subscribe to shutdown command

         Yields
         -------
         shutdown : bool
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeShutdownRequest()
        shutdown_stream = self._stub.SubscribeShutdown(request)

        try:
            async for response in shutdown_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "shutdown()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    shutdown_stream.cancel();
                    return
                

            
                yield response.shutdown
        finally:
            shutdown_stream.cancel()

    async def terminate(self):
        """
         Subscribe to terminate command

         Yields
         -------
         terminate : bool
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SubscribeTerminateRequest()
        terminate_stream = self._stub.SubscribeTerminate(request)

        try:
            async for response in terminate_stream:
                
                result = self._extract_result(response)

                success_codes = [ActionServerResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in ActionServerResult.Result]:
                    success_codes.append(ActionServerResult.Result.NEXT)

                if result.result not in success_codes:
                    raise ActionServerError(result, "terminate()")

                if result.result == ActionServerResult.Result.SUCCESS:
                    terminate_stream.cancel();
                    return
                

            
                yield response.terminate
        finally:
            terminate_stream.cancel()

    async def set_allow_takeoff(self, allow_takeoff):
        """
         Can the vehicle takeoff

         Parameters
         ----------
         allow_takeoff : bool
              Is takeoff allowed?

         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetAllowTakeoffRequest()
        request.allow_takeoff = allow_takeoff
        response = await self._stub.SetAllowTakeoff(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_allow_takeoff()", allow_takeoff)
        

    async def set_armable(self, armable, force_armable):
        """
         Can the vehicle arm when requested

         Parameters
         ----------
         armable : bool
              Is Armable now?

         force_armable : bool
              Is armable with force?

         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetArmableRequest()
        request.armable = armable
        request.force_armable = force_armable
        response = await self._stub.SetArmable(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_armable()", armable, force_armable)
        

    async def set_disarmable(self, disarmable, force_disarmable):
        """
         Can the vehicle disarm when requested

         Parameters
         ----------
         disarmable : bool
              Is disarmable now?

         force_disarmable : bool
              Is disarmable with force? (Kill)

         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetDisarmableRequest()
        request.disarmable = disarmable
        request.force_disarmable = force_disarmable
        response = await self._stub.SetDisarmable(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_disarmable()", disarmable, force_disarmable)
        

    async def set_allowable_flight_modes(self, flight_modes):
        """
         Set which modes the vehicle can transition to (Manual always allowed)

         Parameters
         ----------
         flight_modes : AllowableFlightModes
             
         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetAllowableFlightModesRequest()
        
        flight_modes.translate_to_rpc(request.flight_modes)
                
            
        response = await self._stub.SetAllowableFlightModes(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_allowable_flight_modes()", flight_modes)
        

    async def get_allowable_flight_modes(self):
        """
         Get which modes the vehicle can transition to (Manual always allowed)

         Returns
         -------
         flight_modes : AllowableFlightModes
             
         
        """

        request = action_server_pb2.GetAllowableFlightModesRequest()
        response = await self._stub.GetAllowableFlightModes(request)

        

        return AllowableFlightModes.translate_from_rpc(response.flight_modes)
            

    async def set_armed_state(self, is_armed):
        """
         Set/override the armed/disarmed state of the vehicle directly, and notify subscribers

         Parameters
         ----------
         is_armed : bool
              Is armed now?

         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetArmedStateRequest()
        request.is_armed = is_armed
        response = await self._stub.SetArmedState(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_armed_state()", is_armed)
        

    async def set_flight_mode(self, flight_mode):
        """
         Set/override the flight mode of the vehicle directly, and notify subscribers

         Parameters
         ----------
         flight_mode : FlightMode
              Current vehicle flight mode, e.g. Takeoff/Mission/Land/etc.

         Raises
         ------
         ActionServerError
             If the request fails. The error contains the reason for the failure.
        """

        request = action_server_pb2.SetFlightModeRequest()
        
        request.flight_mode = flight_mode.translate_to_rpc()
                
            
        response = await self._stub.SetFlightMode(request)

        
        result = self._extract_result(response)

        if result.result != ActionServerResult.Result.SUCCESS:
            raise ActionServerError(result, "set_flight_mode()", flight_mode)
        