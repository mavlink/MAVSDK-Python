# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import log_files_pb2, log_files_pb2_grpc
from enum import Enum


class ProgressData:
    """
     Progress data coming when downloading a log file.

     Parameters
     ----------
     progress : float
          Progress from 0 to 1

     """

    

    def __init__(
            self,
            progress):
        """ Initializes the ProgressData object """
        self.progress = progress

    def __eq__(self, to_compare):
        """ Checks if two ProgressData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressData object
            return \
                (self.progress == to_compare.progress)

        except AttributeError:
            return False

    def __str__(self):
        """ ProgressData in string representation """
        struct_repr = ", ".join([
                "progress: " + str(self.progress)
                ])

        return f"ProgressData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProgressData):
        """ Translates a gRPC struct to the SDK equivalent """
        return ProgressData(
                
                rpcProgressData.progress
                )

    def translate_to_rpc(self, rpcProgressData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProgressData.progress = self.progress
            
        
        


class Entry:
    """
     Log file entry type.

     Parameters
     ----------
     id : uint32_t
          ID of the log file, to specify a file to be downloaded

     date : std::string
          Date of the log file in UTC in ISO 8601 format "yyyy-mm-ddThh:mm:ssZ"

     size_bytes : uint32_t
          Size of file in bytes

     """

    

    def __init__(
            self,
            id,
            date,
            size_bytes):
        """ Initializes the Entry object """
        self.id = id
        self.date = date
        self.size_bytes = size_bytes

    def __eq__(self, to_compare):
        """ Checks if two Entry are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # Entry object
            return \
                (self.id == to_compare.id) and \
                (self.date == to_compare.date) and \
                (self.size_bytes == to_compare.size_bytes)

        except AttributeError:
            return False

    def __str__(self):
        """ Entry in string representation """
        struct_repr = ", ".join([
                "id: " + str(self.id),
                "date: " + str(self.date),
                "size_bytes: " + str(self.size_bytes)
                ])

        return f"Entry: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcEntry):
        """ Translates a gRPC struct to the SDK equivalent """
        return Entry(
                
                rpcEntry.id,
                
                
                rpcEntry.date,
                
                
                rpcEntry.size_bytes
                )

    def translate_to_rpc(self, rpcEntry):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcEntry.id = self.id
            
        
        
        
            
        rpcEntry.date = self.date
            
        
        
        
            
        rpcEntry.size_bytes = self.size_bytes
            
        
        


class LogFilesResult:
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
         Possible results returned for calibration commands

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         NEXT
              Progress update

         NO_LOGFILES
              No log files found

         TIMEOUT
              A timeout happened

         INVALID_ARGUMENT
              Invalid argument

         FILE_OPEN_FAILED
              File open failed

         NO_SYSTEM
              No system is connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NEXT = 2
        NO_LOGFILES = 3
        TIMEOUT = 4
        INVALID_ARGUMENT = 5
        FILE_OPEN_FAILED = 6
        NO_SYSTEM = 7

        def translate_to_rpc(self):
            if self == LogFilesResult.Result.UNKNOWN:
                return log_files_pb2.LogFilesResult.RESULT_UNKNOWN
            if self == LogFilesResult.Result.SUCCESS:
                return log_files_pb2.LogFilesResult.RESULT_SUCCESS
            if self == LogFilesResult.Result.NEXT:
                return log_files_pb2.LogFilesResult.RESULT_NEXT
            if self == LogFilesResult.Result.NO_LOGFILES:
                return log_files_pb2.LogFilesResult.RESULT_NO_LOGFILES
            if self == LogFilesResult.Result.TIMEOUT:
                return log_files_pb2.LogFilesResult.RESULT_TIMEOUT
            if self == LogFilesResult.Result.INVALID_ARGUMENT:
                return log_files_pb2.LogFilesResult.RESULT_INVALID_ARGUMENT
            if self == LogFilesResult.Result.FILE_OPEN_FAILED:
                return log_files_pb2.LogFilesResult.RESULT_FILE_OPEN_FAILED
            if self == LogFilesResult.Result.NO_SYSTEM:
                return log_files_pb2.LogFilesResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_UNKNOWN:
                return LogFilesResult.Result.UNKNOWN
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_SUCCESS:
                return LogFilesResult.Result.SUCCESS
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_NEXT:
                return LogFilesResult.Result.NEXT
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_NO_LOGFILES:
                return LogFilesResult.Result.NO_LOGFILES
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_TIMEOUT:
                return LogFilesResult.Result.TIMEOUT
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_INVALID_ARGUMENT:
                return LogFilesResult.Result.INVALID_ARGUMENT
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_FILE_OPEN_FAILED:
                return LogFilesResult.Result.FILE_OPEN_FAILED
            if rpc_enum_value == log_files_pb2.LogFilesResult.RESULT_NO_SYSTEM:
                return LogFilesResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the LogFilesResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two LogFilesResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # LogFilesResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ LogFilesResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"LogFilesResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcLogFilesResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return LogFilesResult(
                
                LogFilesResult.Result.translate_from_rpc(rpcLogFilesResult.result),
                
                
                rpcLogFilesResult.result_str
                )

    def translate_to_rpc(self, rpcLogFilesResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcLogFilesResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcLogFilesResult.result_str = self.result_str
            
        
        



class LogFilesError(Exception):
    """ Raised when a LogFilesResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class LogFiles(AsyncBase):
    """
     Allow to download log files from the vehicle after a flight is complete.
     For log streaming during flight check the logging plugin.

     Generated by dcsdkgen - MAVSDK LogFiles API
    """

    # Plugin name
    name = "LogFiles"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = log_files_pb2_grpc.LogFilesServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return LogFilesResult.translate_from_rpc(response.log_files_result)
    

    async def get_entries(self):
        """
         Get List of log files.

         Returns
         -------
         entries : [Entry]
              List of entries

         Raises
         ------
         LogFilesError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_files_pb2.GetEntriesRequest()
        response = await self._stub.GetEntries(request)

        
        result = self._extract_result(response)

        if result.result != LogFilesResult.Result.SUCCESS:
            raise LogFilesError(result, "get_entries()")
        

        entries = []
        for entries_rpc in response.entries:
            entries.append(Entry.translate_from_rpc(entries_rpc))

        return entries
            

    async def download_log_file(self, entry, path):
        """
         Download log file.

         Parameters
         ----------
         entry : Entry
              Entry of the log file to download.

         path : std::string
              Path of where to download log file to.

         Yields
         -------
         progress : ProgressData
              Progress if result is progress

         Raises
         ------
         LogFilesError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_files_pb2.SubscribeDownloadLogFileRequest()
        
        entry.translate_to_rpc(request.entry)
                
            
        request.path = path
        download_log_file_stream = self._stub.SubscribeDownloadLogFile(request)

        try:
            async for response in download_log_file_stream:
                
                result = self._extract_result(response)

                success_codes = [LogFilesResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in LogFilesResult.Result]:
                    success_codes.append(LogFilesResult.Result.NEXT)

                if result.result not in success_codes:
                    raise LogFilesError(result, "download_log_file()", entry, path)

                if result.result == LogFilesResult.Result.SUCCESS:
                    download_log_file_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress)
        finally:
            download_log_file_stream.cancel()

    async def download_log_file(self, entry, path):
        """
         Download log file synchronously.

         Parameters
         ----------
         entry : Entry
              Entry of the log file to download.

         path : std::string
              Path of where to download log file to.

         Returns
         -------
         progress : ProgressData
              Progress if result is progress

         Raises
         ------
         LogFilesError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_files_pb2.DownloadLogFileRequest()
        
            
                
        entry.translate_to_rpc(request.entry)
                
            
        
            
        request.path = path
            
        response = await self._stub.DownloadLogFile(request)

        
        result = self._extract_result(response)

        if result.result != LogFilesResult.Result.SUCCESS:
            raise LogFilesError(result, "download_log_file()", entry, path)
        

        return ProgressData.translate_from_rpc(response.progress)
            

    async def erase_all_log_files(self):
        """
         Erase all log files.

         Raises
         ------
         LogFilesError
             If the request fails. The error contains the reason for the failure.
        """

        request = log_files_pb2.EraseAllLogFilesRequest()
        response = await self._stub.EraseAllLogFiles(request)

        
        result = self._extract_result(response)

        if result.result != LogFilesResult.Result.SUCCESS:
            raise LogFilesError(result, "erase_all_log_files()")
        