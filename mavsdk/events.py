# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import events_pb2, events_pb2_grpc
from enum import Enum


class LogLevel(Enum):
    """
     Log level type

     Values
     ------
     EMERGENCY
          Emergency

     ALERT
          Alert

     CRITICAL
          Critical

     ERROR
          Error

     WARNING
          Warning

     NOTICE
          Notice

     INFO
          Info

     DEBUG
          Debug

     """

    
    EMERGENCY = 0
    ALERT = 1
    CRITICAL = 2
    ERROR = 3
    WARNING = 4
    NOTICE = 5
    INFO = 6
    DEBUG = 7

    def translate_to_rpc(self):
        if self == LogLevel.EMERGENCY:
            return events_pb2.LOG_LEVEL_EMERGENCY
        if self == LogLevel.ALERT:
            return events_pb2.LOG_LEVEL_ALERT
        if self == LogLevel.CRITICAL:
            return events_pb2.LOG_LEVEL_CRITICAL
        if self == LogLevel.ERROR:
            return events_pb2.LOG_LEVEL_ERROR
        if self == LogLevel.WARNING:
            return events_pb2.LOG_LEVEL_WARNING
        if self == LogLevel.NOTICE:
            return events_pb2.LOG_LEVEL_NOTICE
        if self == LogLevel.INFO:
            return events_pb2.LOG_LEVEL_INFO
        if self == LogLevel.DEBUG:
            return events_pb2.LOG_LEVEL_DEBUG

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == events_pb2.LOG_LEVEL_EMERGENCY:
            return LogLevel.EMERGENCY
        if rpc_enum_value == events_pb2.LOG_LEVEL_ALERT:
            return LogLevel.ALERT
        if rpc_enum_value == events_pb2.LOG_LEVEL_CRITICAL:
            return LogLevel.CRITICAL
        if rpc_enum_value == events_pb2.LOG_LEVEL_ERROR:
            return LogLevel.ERROR
        if rpc_enum_value == events_pb2.LOG_LEVEL_WARNING:
            return LogLevel.WARNING
        if rpc_enum_value == events_pb2.LOG_LEVEL_NOTICE:
            return LogLevel.NOTICE
        if rpc_enum_value == events_pb2.LOG_LEVEL_INFO:
            return LogLevel.INFO
        if rpc_enum_value == events_pb2.LOG_LEVEL_DEBUG:
            return LogLevel.DEBUG

    def __str__(self):
        return self.name


class Event:
    """
     Event type

     Parameters
     ----------
     compid : uint32_t
          The source component ID of the event

     message : std::string
          Short, single-line message

     description : std::string
          Detailed description (optional, might be multiple lines)

     log_level : LogLevel
          Log level of message

     event_namespace : std::string
          Namespace, e.g. "px4"

     event_name : std::string
          Event name (unique within the namespace)

     """

    

    def __init__(
            self,
            compid,
            message,
            description,
            log_level,
            event_namespace,
            event_name):
        """ Initializes the Event object """
        self.compid = compid
        self.message = message
        self.description = description
        self.log_level = log_level
        self.event_namespace = event_namespace
        self.event_name = event_name

    def __eq__(self, to_compare):
        """ Checks if two Event are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Event object
            return \
                (self.compid == to_compare.compid) and \
                (self.message == to_compare.message) and \
                (self.description == to_compare.description) and \
                (self.log_level == to_compare.log_level) and \
                (self.event_namespace == to_compare.event_namespace) and \
                (self.event_name == to_compare.event_name)

        except AttributeError:
            return False

    def __str__(self):
        """ Event in string representation """
        struct_repr = ", ".join([
                "compid: " + str(self.compid),
                "message: " + str(self.message),
                "description: " + str(self.description),
                "log_level: " + str(self.log_level),
                "event_namespace: " + str(self.event_namespace),
                "event_name: " + str(self.event_name)
                ])

        return f"Event: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcEvent):
        """ Translates a gRPC struct to the SDK equivalent """
        return Event(
                
                rpcEvent.compid,
                
                
                rpcEvent.message,
                
                
                rpcEvent.description,
                
                
                LogLevel.translate_from_rpc(rpcEvent.log_level),
                
                
                rpcEvent.event_namespace,
                
                
                rpcEvent.event_name
                )

    def translate_to_rpc(self, rpcEvent):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcEvent.compid = self.compid
            
        
        
        
            
        rpcEvent.message = self.message
            
        
        
        
            
        rpcEvent.description = self.description
            
        
        
        
            
        rpcEvent.log_level = self.log_level.translate_to_rpc()
            
        
        
        
            
        rpcEvent.event_namespace = self.event_namespace
            
        
        
        
            
        rpcEvent.event_name = self.event_name
            
        
        


class HealthAndArmingCheckProblem:
    """
     Health and arming check problem type

     Parameters
     ----------
     message : std::string
          Short, single-line message

     description : std::string
          Detailed description (optional, might be multiple lines)

     log_level : LogLevel
          Log level of message

     health_component : std::string
          Associated health component, e.g. "gps"

     """

    

    def __init__(
            self,
            message,
            description,
            log_level,
            health_component):
        """ Initializes the HealthAndArmingCheckProblem object """
        self.message = message
        self.description = description
        self.log_level = log_level
        self.health_component = health_component

    def __eq__(self, to_compare):
        """ Checks if two HealthAndArmingCheckProblem are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # HealthAndArmingCheckProblem object
            return \
                (self.message == to_compare.message) and \
                (self.description == to_compare.description) and \
                (self.log_level == to_compare.log_level) and \
                (self.health_component == to_compare.health_component)

        except AttributeError:
            return False

    def __str__(self):
        """ HealthAndArmingCheckProblem in string representation """
        struct_repr = ", ".join([
                "message: " + str(self.message),
                "description: " + str(self.description),
                "log_level: " + str(self.log_level),
                "health_component: " + str(self.health_component)
                ])

        return f"HealthAndArmingCheckProblem: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealthAndArmingCheckProblem):
        """ Translates a gRPC struct to the SDK equivalent """
        return HealthAndArmingCheckProblem(
                
                rpcHealthAndArmingCheckProblem.message,
                
                
                rpcHealthAndArmingCheckProblem.description,
                
                
                LogLevel.translate_from_rpc(rpcHealthAndArmingCheckProblem.log_level),
                
                
                rpcHealthAndArmingCheckProblem.health_component
                )

    def translate_to_rpc(self, rpcHealthAndArmingCheckProblem):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcHealthAndArmingCheckProblem.message = self.message
            
        
        
        
            
        rpcHealthAndArmingCheckProblem.description = self.description
            
        
        
        
            
        rpcHealthAndArmingCheckProblem.log_level = self.log_level.translate_to_rpc()
            
        
        
        
            
        rpcHealthAndArmingCheckProblem.health_component = self.health_component
            
        
        


class HealthAndArmingCheckMode:
    """
     Arming checks for a specific mode

     Parameters
     ----------
     mode_name : std::string
          Mode name, e.g. "Position"

     can_arm_or_run : bool
          If disarmed: indicates if arming is possible. If armed: indicates if the mode can be selected

     problems : [HealthAndArmingCheckProblem]
          List of reported problems for the mode

     """

    

    def __init__(
            self,
            mode_name,
            can_arm_or_run,
            problems):
        """ Initializes the HealthAndArmingCheckMode object """
        self.mode_name = mode_name
        self.can_arm_or_run = can_arm_or_run
        self.problems = problems

    def __eq__(self, to_compare):
        """ Checks if two HealthAndArmingCheckMode are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # HealthAndArmingCheckMode object
            return \
                (self.mode_name == to_compare.mode_name) and \
                (self.can_arm_or_run == to_compare.can_arm_or_run) and \
                (self.problems == to_compare.problems)

        except AttributeError:
            return False

    def __str__(self):
        """ HealthAndArmingCheckMode in string representation """
        struct_repr = ", ".join([
                "mode_name: " + str(self.mode_name),
                "can_arm_or_run: " + str(self.can_arm_or_run),
                "problems: " + str(self.problems)
                ])

        return f"HealthAndArmingCheckMode: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealthAndArmingCheckMode):
        """ Translates a gRPC struct to the SDK equivalent """
        return HealthAndArmingCheckMode(
                
                rpcHealthAndArmingCheckMode.mode_name,
                
                
                rpcHealthAndArmingCheckMode.can_arm_or_run,
                
                
                list(map(lambda elem: HealthAndArmingCheckProblem.translate_from_rpc(elem), rpcHealthAndArmingCheckMode.problems))
                )

    def translate_to_rpc(self, rpcHealthAndArmingCheckMode):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcHealthAndArmingCheckMode.mode_name = self.mode_name
            
        
        
        
            
        rpcHealthAndArmingCheckMode.can_arm_or_run = self.can_arm_or_run
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.problems:
                
            rpc_elem = events_pb2.HealthAndArmingCheckProblem()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcHealthAndArmingCheckMode.problems.extend(rpc_elems_list)
            
        
        


class HealthComponentReport:
    """
     Health component report type

     Parameters
     ----------
     name : std::string
          Unique component name, e.g. "gps"

     label : std::string
          Human readable label of the component, e.g. "GPS" or "Accelerometer"

     is_present : bool
          If the component is present

     has_error : bool
          If the component has errors

     has_warning : bool
          If the component has warnings

     """

    

    def __init__(
            self,
            name,
            label,
            is_present,
            has_error,
            has_warning):
        """ Initializes the HealthComponentReport object """
        self.name = name
        self.label = label
        self.is_present = is_present
        self.has_error = has_error
        self.has_warning = has_warning

    def __eq__(self, to_compare):
        """ Checks if two HealthComponentReport are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # HealthComponentReport object
            return \
                (self.name == to_compare.name) and \
                (self.label == to_compare.label) and \
                (self.is_present == to_compare.is_present) and \
                (self.has_error == to_compare.has_error) and \
                (self.has_warning == to_compare.has_warning)

        except AttributeError:
            return False

    def __str__(self):
        """ HealthComponentReport in string representation """
        struct_repr = ", ".join([
                "name: " + str(self.name),
                "label: " + str(self.label),
                "is_present: " + str(self.is_present),
                "has_error: " + str(self.has_error),
                "has_warning: " + str(self.has_warning)
                ])

        return f"HealthComponentReport: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealthComponentReport):
        """ Translates a gRPC struct to the SDK equivalent """
        return HealthComponentReport(
                
                rpcHealthComponentReport.name,
                
                
                rpcHealthComponentReport.label,
                
                
                rpcHealthComponentReport.is_present,
                
                
                rpcHealthComponentReport.has_error,
                
                
                rpcHealthComponentReport.has_warning
                )

    def translate_to_rpc(self, rpcHealthComponentReport):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcHealthComponentReport.name = self.name
            
        
        
        
            
        rpcHealthComponentReport.label = self.label
            
        
        
        
            
        rpcHealthComponentReport.is_present = self.is_present
            
        
        
        
            
        rpcHealthComponentReport.has_error = self.has_error
            
        
        
        
            
        rpcHealthComponentReport.has_warning = self.has_warning
            
        
        


class HealthAndArmingCheckReport:
    """
     Health and arming check report type

     Parameters
     ----------
     current_mode_intention : HealthAndArmingCheckMode
          Report for currently intended mode

     health_components : [HealthComponentReport]
          Health components list (e.g. for "gps")

     all_problems : [HealthAndArmingCheckProblem]
          Complete list of problems

     """

    

    def __init__(
            self,
            current_mode_intention,
            health_components,
            all_problems):
        """ Initializes the HealthAndArmingCheckReport object """
        self.current_mode_intention = current_mode_intention
        self.health_components = health_components
        self.all_problems = all_problems

    def __eq__(self, to_compare):
        """ Checks if two HealthAndArmingCheckReport are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # HealthAndArmingCheckReport object
            return \
                (self.current_mode_intention == to_compare.current_mode_intention) and \
                (self.health_components == to_compare.health_components) and \
                (self.all_problems == to_compare.all_problems)

        except AttributeError:
            return False

    def __str__(self):
        """ HealthAndArmingCheckReport in string representation """
        struct_repr = ", ".join([
                "current_mode_intention: " + str(self.current_mode_intention),
                "health_components: " + str(self.health_components),
                "all_problems: " + str(self.all_problems)
                ])

        return f"HealthAndArmingCheckReport: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcHealthAndArmingCheckReport):
        """ Translates a gRPC struct to the SDK equivalent """
        return HealthAndArmingCheckReport(
                
                HealthAndArmingCheckMode.translate_from_rpc(rpcHealthAndArmingCheckReport.current_mode_intention),
                
                
                list(map(lambda elem: HealthComponentReport.translate_from_rpc(elem), rpcHealthAndArmingCheckReport.health_components)),
                
                
                list(map(lambda elem: HealthAndArmingCheckProblem.translate_from_rpc(elem), rpcHealthAndArmingCheckReport.all_problems))
                )

    def translate_to_rpc(self, rpcHealthAndArmingCheckReport):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        self.current_mode_intention.translate_to_rpc(rpcHealthAndArmingCheckReport.current_mode_intention)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.health_components:
                
            rpc_elem = events_pb2.HealthComponentReport()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcHealthAndArmingCheckReport.health_components.extend(rpc_elems_list)
            
        
        
        
            
        rpc_elems_list = []
        for elem in self.all_problems:
                
            rpc_elem = events_pb2.HealthAndArmingCheckProblem()
            elem.translate_to_rpc(rpc_elem)
            rpc_elems_list.append(rpc_elem)
                
        rpcHealthAndArmingCheckReport.all_problems.extend(rpc_elems_list)
            
        
        


class EventsResult:
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
         Possible results returned

         Values
         ------
         SUCCESS
              Successful result

         NOT_AVAILABLE
              Not available

         CONNECTION_ERROR
              Connection error

         UNSUPPORTED
              Unsupported

         DENIED
              Denied

         FAILED
              Failed

         TIMEOUT
              Timeout

         NO_SYSTEM
              No system available

         UNKNOWN
              Unknown result

         """

        
        SUCCESS = 0
        NOT_AVAILABLE = 1
        CONNECTION_ERROR = 2
        UNSUPPORTED = 3
        DENIED = 4
        FAILED = 5
        TIMEOUT = 6
        NO_SYSTEM = 7
        UNKNOWN = 8

        def translate_to_rpc(self):
            if self == EventsResult.Result.SUCCESS:
                return events_pb2.EventsResult.RESULT_SUCCESS
            if self == EventsResult.Result.NOT_AVAILABLE:
                return events_pb2.EventsResult.RESULT_NOT_AVAILABLE
            if self == EventsResult.Result.CONNECTION_ERROR:
                return events_pb2.EventsResult.RESULT_CONNECTION_ERROR
            if self == EventsResult.Result.UNSUPPORTED:
                return events_pb2.EventsResult.RESULT_UNSUPPORTED
            if self == EventsResult.Result.DENIED:
                return events_pb2.EventsResult.RESULT_DENIED
            if self == EventsResult.Result.FAILED:
                return events_pb2.EventsResult.RESULT_FAILED
            if self == EventsResult.Result.TIMEOUT:
                return events_pb2.EventsResult.RESULT_TIMEOUT
            if self == EventsResult.Result.NO_SYSTEM:
                return events_pb2.EventsResult.RESULT_NO_SYSTEM
            if self == EventsResult.Result.UNKNOWN:
                return events_pb2.EventsResult.RESULT_UNKNOWN

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == events_pb2.EventsResult.RESULT_SUCCESS:
                return EventsResult.Result.SUCCESS
            if rpc_enum_value == events_pb2.EventsResult.RESULT_NOT_AVAILABLE:
                return EventsResult.Result.NOT_AVAILABLE
            if rpc_enum_value == events_pb2.EventsResult.RESULT_CONNECTION_ERROR:
                return EventsResult.Result.CONNECTION_ERROR
            if rpc_enum_value == events_pb2.EventsResult.RESULT_UNSUPPORTED:
                return EventsResult.Result.UNSUPPORTED
            if rpc_enum_value == events_pb2.EventsResult.RESULT_DENIED:
                return EventsResult.Result.DENIED
            if rpc_enum_value == events_pb2.EventsResult.RESULT_FAILED:
                return EventsResult.Result.FAILED
            if rpc_enum_value == events_pb2.EventsResult.RESULT_TIMEOUT:
                return EventsResult.Result.TIMEOUT
            if rpc_enum_value == events_pb2.EventsResult.RESULT_NO_SYSTEM:
                return EventsResult.Result.NO_SYSTEM
            if rpc_enum_value == events_pb2.EventsResult.RESULT_UNKNOWN:
                return EventsResult.Result.UNKNOWN

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the EventsResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two EventsResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # EventsResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ EventsResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"EventsResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcEventsResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return EventsResult(
                
                EventsResult.Result.translate_from_rpc(rpcEventsResult.result),
                
                
                rpcEventsResult.result_str
                )

    def translate_to_rpc(self, rpcEventsResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcEventsResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcEventsResult.result_str = self.result_str
            
        
        



class EventsError(Exception):
    """ Raised when a EventsResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Events(AsyncBase):
    """
     Get event notifications, such as takeoff, or arming checks

     Generated by dcsdkgen - MAVSDK Events API
    """

    # Plugin name
    name = "Events"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = events_pb2_grpc.EventsServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return EventsResult.translate_from_rpc(response.events_result)
    

    async def events(self):
        """
         Subscribe to event updates.

         Yields
         -------
         event : Event
              The event

         
        """

        request = events_pb2.SubscribeEventsRequest()
        events_stream = self._stub.SubscribeEvents(request)

        try:
            async for response in events_stream:
                

            
                yield Event.translate_from_rpc(response.event)
        finally:
            events_stream.cancel()

    async def health_and_arming_checks(self):
        """
         Subscribe to arming check updates.

         Yields
         -------
         report : HealthAndArmingCheckReport
              The report

         
        """

        request = events_pb2.SubscribeHealthAndArmingChecksRequest()
        health_and_arming_checks_stream = self._stub.SubscribeHealthAndArmingChecks(request)

        try:
            async for response in health_and_arming_checks_stream:
                

            
                yield HealthAndArmingCheckReport.translate_from_rpc(response.report)
        finally:
            health_and_arming_checks_stream.cancel()

    async def get_health_and_arming_checks_report(self):
        """
         Get the latest report.

         Returns
         -------
         report : HealthAndArmingCheckReport
              The report

         Raises
         ------
         EventsError
             If the request fails. The error contains the reason for the failure.
        """

        request = events_pb2.GetHealthAndArmingChecksReportRequest()
        response = await self._stub.GetHealthAndArmingChecksReport(request)

        
        result = self._extract_result(response)

        if result.result != EventsResult.Result.SUCCESS:
            raise EventsError(result, "get_health_and_arming_checks_report()")
        

        return HealthAndArmingCheckReport.translate_from_rpc(response.report)
            