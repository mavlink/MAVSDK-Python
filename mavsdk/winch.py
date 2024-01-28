# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import winch_pb2, winch_pb2_grpc
from enum import Enum


class WinchAction(Enum):
    """
     Winch Action type.

     Values
     ------
     RELAXED
          Allow motor to freewheel

     RELATIVE_LENGTH_CONTROL
          Wind or unwind specified length of line, optionally using specified rate

     RATE_CONTROL
          Wind or unwind line at specified rate

     LOCK
          Perform the locking sequence to relieve motor while in the fully retracted position

     DELIVER
          Sequence of drop, slow down, touch down, reel up, lock

     HOLD
          Engage motor and hold current position

     RETRACT
          Return the reel to the fully retracted position

     LOAD_LINE
          Load the reel with line. The winch will calculate the total loaded length and stop when the tension exceeds a threshold

     ABANDON_LINE
          Spool out the entire length of the line

     LOAD_PAYLOAD
          Spools out just enough to present the hook to the user to load the payload

     """

    
    RELAXED = 0
    RELATIVE_LENGTH_CONTROL = 1
    RATE_CONTROL = 2
    LOCK = 3
    DELIVER = 4
    HOLD = 5
    RETRACT = 6
    LOAD_LINE = 7
    ABANDON_LINE = 8
    LOAD_PAYLOAD = 9

    def translate_to_rpc(self):
        if self == WinchAction.RELAXED:
            return winch_pb2.WINCH_ACTION_RELAXED
        if self == WinchAction.RELATIVE_LENGTH_CONTROL:
            return winch_pb2.WINCH_ACTION_RELATIVE_LENGTH_CONTROL
        if self == WinchAction.RATE_CONTROL:
            return winch_pb2.WINCH_ACTION_RATE_CONTROL
        if self == WinchAction.LOCK:
            return winch_pb2.WINCH_ACTION_LOCK
        if self == WinchAction.DELIVER:
            return winch_pb2.WINCH_ACTION_DELIVER
        if self == WinchAction.HOLD:
            return winch_pb2.WINCH_ACTION_HOLD
        if self == WinchAction.RETRACT:
            return winch_pb2.WINCH_ACTION_RETRACT
        if self == WinchAction.LOAD_LINE:
            return winch_pb2.WINCH_ACTION_LOAD_LINE
        if self == WinchAction.ABANDON_LINE:
            return winch_pb2.WINCH_ACTION_ABANDON_LINE
        if self == WinchAction.LOAD_PAYLOAD:
            return winch_pb2.WINCH_ACTION_LOAD_PAYLOAD

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RELAXED:
            return WinchAction.RELAXED
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RELATIVE_LENGTH_CONTROL:
            return WinchAction.RELATIVE_LENGTH_CONTROL
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RATE_CONTROL:
            return WinchAction.RATE_CONTROL
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOCK:
            return WinchAction.LOCK
        if rpc_enum_value == winch_pb2.WINCH_ACTION_DELIVER:
            return WinchAction.DELIVER
        if rpc_enum_value == winch_pb2.WINCH_ACTION_HOLD:
            return WinchAction.HOLD
        if rpc_enum_value == winch_pb2.WINCH_ACTION_RETRACT:
            return WinchAction.RETRACT
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOAD_LINE:
            return WinchAction.LOAD_LINE
        if rpc_enum_value == winch_pb2.WINCH_ACTION_ABANDON_LINE:
            return WinchAction.ABANDON_LINE
        if rpc_enum_value == winch_pb2.WINCH_ACTION_LOAD_PAYLOAD:
            return WinchAction.LOAD_PAYLOAD

    def __str__(self):
        return self.name


class StatusFlags:
    """
     Winch Status Flags.

     The status flags are defined in mavlink
     https://mavlink.io/en/messages/common.html#MAV_WINCH_STATUS_FLAG.

     Multiple status fields can be set simultaneously. Mavlink does
     not specify which states are mutually exclusive.

     Parameters
     ----------
     healthy : bool
          Winch is healthy

     fully_retracted : bool
          Winch line is fully retracted

     moving : bool
          Winch motor is moving

     clutch_engaged : bool
          Winch clutch is engaged allowing motor to move freely

     locked : bool
          Winch is locked by locking mechanism

     dropping : bool
          Winch is gravity dropping payload

     arresting : bool
          Winch is arresting payload descent

     ground_sense : bool
          Winch is using torque measurements to sense the ground

     retracting : bool
          Winch is returning to the fully retracted position

     redeliver : bool
          Winch is redelivering the payload. This is a failover state if the line tension goes above a threshold during RETRACTING.

     abandon_line : bool
          Winch is abandoning the line and possibly payload. Winch unspools the entire calculated line length. This is a failover state from REDELIVER if the number of attempts exceeds a threshold.

     locking : bool
          Winch is engaging the locking mechanism

     load_line : bool
          Winch is spooling on line

     load_payload : bool
          Winch is loading a payload

     """

    

    def __init__(
            self,
            healthy,
            fully_retracted,
            moving,
            clutch_engaged,
            locked,
            dropping,
            arresting,
            ground_sense,
            retracting,
            redeliver,
            abandon_line,
            locking,
            load_line,
            load_payload):
        """ Initializes the StatusFlags object """
        self.healthy = healthy
        self.fully_retracted = fully_retracted
        self.moving = moving
        self.clutch_engaged = clutch_engaged
        self.locked = locked
        self.dropping = dropping
        self.arresting = arresting
        self.ground_sense = ground_sense
        self.retracting = retracting
        self.redeliver = redeliver
        self.abandon_line = abandon_line
        self.locking = locking
        self.load_line = load_line
        self.load_payload = load_payload

    def __eq__(self, to_compare):
        """ Checks if two StatusFlags are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # StatusFlags object
            return \
                (self.healthy == to_compare.healthy) and \
                (self.fully_retracted == to_compare.fully_retracted) and \
                (self.moving == to_compare.moving) and \
                (self.clutch_engaged == to_compare.clutch_engaged) and \
                (self.locked == to_compare.locked) and \
                (self.dropping == to_compare.dropping) and \
                (self.arresting == to_compare.arresting) and \
                (self.ground_sense == to_compare.ground_sense) and \
                (self.retracting == to_compare.retracting) and \
                (self.redeliver == to_compare.redeliver) and \
                (self.abandon_line == to_compare.abandon_line) and \
                (self.locking == to_compare.locking) and \
                (self.load_line == to_compare.load_line) and \
                (self.load_payload == to_compare.load_payload)

        except AttributeError:
            return False

    def __str__(self):
        """ StatusFlags in string representation """
        struct_repr = ", ".join([
                "healthy: " + str(self.healthy),
                "fully_retracted: " + str(self.fully_retracted),
                "moving: " + str(self.moving),
                "clutch_engaged: " + str(self.clutch_engaged),
                "locked: " + str(self.locked),
                "dropping: " + str(self.dropping),
                "arresting: " + str(self.arresting),
                "ground_sense: " + str(self.ground_sense),
                "retracting: " + str(self.retracting),
                "redeliver: " + str(self.redeliver),
                "abandon_line: " + str(self.abandon_line),
                "locking: " + str(self.locking),
                "load_line: " + str(self.load_line),
                "load_payload: " + str(self.load_payload)
                ])

        return f"StatusFlags: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStatusFlags):
        """ Translates a gRPC struct to the SDK equivalent """
        return StatusFlags(
                
                rpcStatusFlags.healthy,
                
                
                rpcStatusFlags.fully_retracted,
                
                
                rpcStatusFlags.moving,
                
                
                rpcStatusFlags.clutch_engaged,
                
                
                rpcStatusFlags.locked,
                
                
                rpcStatusFlags.dropping,
                
                
                rpcStatusFlags.arresting,
                
                
                rpcStatusFlags.ground_sense,
                
                
                rpcStatusFlags.retracting,
                
                
                rpcStatusFlags.redeliver,
                
                
                rpcStatusFlags.abandon_line,
                
                
                rpcStatusFlags.locking,
                
                
                rpcStatusFlags.load_line,
                
                
                rpcStatusFlags.load_payload
                )

    def translate_to_rpc(self, rpcStatusFlags):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStatusFlags.healthy = self.healthy
            
        
        
        
            
        rpcStatusFlags.fully_retracted = self.fully_retracted
            
        
        
        
            
        rpcStatusFlags.moving = self.moving
            
        
        
        
            
        rpcStatusFlags.clutch_engaged = self.clutch_engaged
            
        
        
        
            
        rpcStatusFlags.locked = self.locked
            
        
        
        
            
        rpcStatusFlags.dropping = self.dropping
            
        
        
        
            
        rpcStatusFlags.arresting = self.arresting
            
        
        
        
            
        rpcStatusFlags.ground_sense = self.ground_sense
            
        
        
        
            
        rpcStatusFlags.retracting = self.retracting
            
        
        
        
            
        rpcStatusFlags.redeliver = self.redeliver
            
        
        
        
            
        rpcStatusFlags.abandon_line = self.abandon_line
            
        
        
        
            
        rpcStatusFlags.locking = self.locking
            
        
        
        
            
        rpcStatusFlags.load_line = self.load_line
            
        
        
        
            
        rpcStatusFlags.load_payload = self.load_payload
            
        
        


class Status:
    """
     Status type.

     Parameters
     ----------
     time_usec : uint64_t
          Time in usec

     line_length_m : float
          Length of the line in meters

     speed_m_s : float
          Speed in meters per second

     tension_kg : float
          Tension in kilograms

     voltage_v : float
          Voltage in volts

     current_a : float
          Current in amperes

     temperature_c : int32_t
          Temperature in Celsius

     status_flags : StatusFlags
          Status flags

     """

    

    def __init__(
            self,
            time_usec,
            line_length_m,
            speed_m_s,
            tension_kg,
            voltage_v,
            current_a,
            temperature_c,
            status_flags):
        """ Initializes the Status object """
        self.time_usec = time_usec
        self.line_length_m = line_length_m
        self.speed_m_s = speed_m_s
        self.tension_kg = tension_kg
        self.voltage_v = voltage_v
        self.current_a = current_a
        self.temperature_c = temperature_c
        self.status_flags = status_flags

    def __eq__(self, to_compare):
        """ Checks if two Status are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Status object
            return \
                (self.time_usec == to_compare.time_usec) and \
                (self.line_length_m == to_compare.line_length_m) and \
                (self.speed_m_s == to_compare.speed_m_s) and \
                (self.tension_kg == to_compare.tension_kg) and \
                (self.voltage_v == to_compare.voltage_v) and \
                (self.current_a == to_compare.current_a) and \
                (self.temperature_c == to_compare.temperature_c) and \
                (self.status_flags == to_compare.status_flags)

        except AttributeError:
            return False

    def __str__(self):
        """ Status in string representation """
        struct_repr = ", ".join([
                "time_usec: " + str(self.time_usec),
                "line_length_m: " + str(self.line_length_m),
                "speed_m_s: " + str(self.speed_m_s),
                "tension_kg: " + str(self.tension_kg),
                "voltage_v: " + str(self.voltage_v),
                "current_a: " + str(self.current_a),
                "temperature_c: " + str(self.temperature_c),
                "status_flags: " + str(self.status_flags)
                ])

        return f"Status: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcStatus):
        """ Translates a gRPC struct to the SDK equivalent """
        return Status(
                
                rpcStatus.time_usec,
                
                
                rpcStatus.line_length_m,
                
                
                rpcStatus.speed_m_s,
                
                
                rpcStatus.tension_kg,
                
                
                rpcStatus.voltage_v,
                
                
                rpcStatus.current_a,
                
                
                rpcStatus.temperature_c,
                
                
                StatusFlags.translate_from_rpc(rpcStatus.status_flags)
                )

    def translate_to_rpc(self, rpcStatus):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcStatus.time_usec = self.time_usec
            
        
        
        
            
        rpcStatus.line_length_m = self.line_length_m
            
        
        
        
            
        rpcStatus.speed_m_s = self.speed_m_s
            
        
        
        
            
        rpcStatus.tension_kg = self.tension_kg
            
        
        
        
            
        rpcStatus.voltage_v = self.voltage_v
            
        
        
        
            
        rpcStatus.current_a = self.current_a
            
        
        
        
            
        rpcStatus.temperature_c = self.temperature_c
            
        
        
        
            
        self.status_flags.translate_to_rpc(rpcStatus.status_flags)
            
        
        


class WinchResult:
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
         Possible results returned for winch action requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request was successful

         NO_SYSTEM
              No system is connected

         BUSY
              Temporarily rejected

         TIMEOUT
              Request timed out

         UNSUPPORTED
              Action not supported

         FAILED
              Action failed

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NO_SYSTEM = 2
        BUSY = 3
        TIMEOUT = 4
        UNSUPPORTED = 5
        FAILED = 6

        def translate_to_rpc(self):
            if self == WinchResult.Result.UNKNOWN:
                return winch_pb2.WinchResult.RESULT_UNKNOWN
            if self == WinchResult.Result.SUCCESS:
                return winch_pb2.WinchResult.RESULT_SUCCESS
            if self == WinchResult.Result.NO_SYSTEM:
                return winch_pb2.WinchResult.RESULT_NO_SYSTEM
            if self == WinchResult.Result.BUSY:
                return winch_pb2.WinchResult.RESULT_BUSY
            if self == WinchResult.Result.TIMEOUT:
                return winch_pb2.WinchResult.RESULT_TIMEOUT
            if self == WinchResult.Result.UNSUPPORTED:
                return winch_pb2.WinchResult.RESULT_UNSUPPORTED
            if self == WinchResult.Result.FAILED:
                return winch_pb2.WinchResult.RESULT_FAILED

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_UNKNOWN:
                return WinchResult.Result.UNKNOWN
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_SUCCESS:
                return WinchResult.Result.SUCCESS
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_NO_SYSTEM:
                return WinchResult.Result.NO_SYSTEM
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_BUSY:
                return WinchResult.Result.BUSY
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_TIMEOUT:
                return WinchResult.Result.TIMEOUT
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_UNSUPPORTED:
                return WinchResult.Result.UNSUPPORTED
            if rpc_enum_value == winch_pb2.WinchResult.RESULT_FAILED:
                return WinchResult.Result.FAILED

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the WinchResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two WinchResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # WinchResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ WinchResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"WinchResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcWinchResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return WinchResult(
                
                WinchResult.Result.translate_from_rpc(rpcWinchResult.result),
                
                
                rpcWinchResult.result_str
                )

    def translate_to_rpc(self, rpcWinchResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcWinchResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcWinchResult.result_str = self.result_str
            
        
        



class WinchError(Exception):
    """ Raised when a WinchResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Winch(AsyncBase):
    """
     Allows users to send winch actions, as well as receive status information from winch systems.

     Generated by dcsdkgen - MAVSDK Winch API
    """

    # Plugin name
    name = "Winch"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = winch_pb2_grpc.WinchServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return WinchResult.translate_from_rpc(response.winch_result)
    

    async def status(self):
        """
         Subscribe to 'winch status' updates.

         Yields
         -------
         status : Status
              The next 'winch status' state

         
        """

        request = winch_pb2.SubscribeStatusRequest()
        status_stream = self._stub.SubscribeStatus(request)

        try:
            async for response in status_stream:
                

            
                yield Status.translate_from_rpc(response.status)
        finally:
            status_stream.cancel()

    async def relax(self, instance):
        """
         Allow motor to freewheel.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RelaxRequest()
        request.instance = instance
        response = await self._stub.Relax(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "relax()", instance)
        

    async def relative_length_control(self, instance, length_m, rate_m_s):
        """
         Wind or unwind specified length of line, optionally using specified rate.

         Parameters
         ----------
         instance : uint32_t
              Instance ID of the winch addressed by this request

         length_m : float
              Length of line to unwind or wind

         rate_m_s : float
              Rate at which to wind or unwind the line

         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RelativeLengthControlRequest()
        request.instance = instance
        request.length_m = length_m
        request.rate_m_s = rate_m_s
        response = await self._stub.RelativeLengthControl(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "relative_length_control()", instance, length_m, rate_m_s)
        

    async def rate_control(self, instance, rate_m_s):
        """
         Wind or unwind line at specified rate.

         Parameters
         ----------
         instance : uint32_t
             
         rate_m_s : float
              Rate at which to wind or unwind the line

         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RateControlRequest()
        request.instance = instance
        request.rate_m_s = rate_m_s
        response = await self._stub.RateControl(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "rate_control()", instance, rate_m_s)
        

    async def lock(self, instance):
        """
         Perform the locking sequence to relieve motor while in the fully retracted position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LockRequest()
        request.instance = instance
        response = await self._stub.Lock(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "lock()", instance)
        

    async def deliver(self, instance):
        """
         Sequence of drop, slow down, touch down, reel up, lock.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.DeliverRequest()
        request.instance = instance
        response = await self._stub.Deliver(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "deliver()", instance)
        

    async def hold(self, instance):
        """
         Engage motor and hold current position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.HoldRequest()
        request.instance = instance
        response = await self._stub.Hold(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "hold()", instance)
        

    async def retract(self, instance):
        """
         Return the reel to the fully retracted position.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.RetractRequest()
        request.instance = instance
        response = await self._stub.Retract(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "retract()", instance)
        

    async def load_line(self, instance):
        """
         Load the reel with line.

         The winch will calculate the total loaded length and stop when the tension exceeds a threshold.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LoadLineRequest()
        request.instance = instance
        response = await self._stub.LoadLine(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "load_line()", instance)
        

    async def abandon_line(self, instance):
        """
         Spool out the entire length of the line.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.AbandonLineRequest()
        request.instance = instance
        response = await self._stub.AbandonLine(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "abandon_line()", instance)
        

    async def load_payload(self, instance):
        """
         Spools out just enough to present the hook to the user to load the payload.

         Parameters
         ----------
         instance : uint32_t
             
         Raises
         ------
         WinchError
             If the request fails. The error contains the reason for the failure.
        """

        request = winch_pb2.LoadPayloadRequest()
        request.instance = instance
        response = await self._stub.LoadPayload(request)

        
        result = self._extract_result(response)

        if result.result != WinchResult.Result.SUCCESS:
            raise WinchError(result, "load_payload()", instance)
        