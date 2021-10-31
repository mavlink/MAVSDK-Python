# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import ftp_pb2, ftp_pb2_grpc
from enum import Enum


class ProgressData:
    """
     Progress data type for file transfer.

     Parameters
     ----------
     bytes_transferred : uint32_t
          The number of bytes already transferred.

     total_bytes : uint32_t
          The total bytes to transfer.

     """

    

    def __init__(
            self,
            bytes_transferred,
            total_bytes):
        """ Initializes the ProgressData object """
        self.bytes_transferred = bytes_transferred
        self.total_bytes = total_bytes

    def __eq__(self, to_compare):
        """ Checks if two ProgressData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressData object
            return \
                (self.bytes_transferred == to_compare.bytes_transferred) and \
                (self.total_bytes == to_compare.total_bytes)

        except AttributeError:
            return False

    def __str__(self):
        """ ProgressData in string representation """
        struct_repr = ", ".join([
                "bytes_transferred: " + str(self.bytes_transferred),
                "total_bytes: " + str(self.total_bytes)
                ])

        return f"ProgressData: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcProgressData):
        """ Translates a gRPC struct to the SDK equivalent """
        return ProgressData(
                
                rpcProgressData.bytes_transferred,
                
                
                rpcProgressData.total_bytes
                )

    def translate_to_rpc(self, rpcProgressData):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcProgressData.bytes_transferred = self.bytes_transferred
            
        
        
        
            
        rpcProgressData.total_bytes = self.total_bytes
            
        
        


class FtpResult:
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
         Possible results returned for FTP commands

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Success

         NEXT
              Intermediate message showing progress

         TIMEOUT
              Timeout

         BUSY
              Operation is already in progress

         FILE_IO_ERROR
              File IO operation error

         FILE_EXISTS
              File exists already

         FILE_DOES_NOT_EXIST
              File does not exist

         FILE_PROTECTED
              File is write protected

         INVALID_PARAMETER
              Invalid parameter

         UNSUPPORTED
              Unsupported command

         PROTOCOL_ERROR
              General protocol error

         NO_SYSTEM
              No system connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        NEXT = 2
        TIMEOUT = 3
        BUSY = 4
        FILE_IO_ERROR = 5
        FILE_EXISTS = 6
        FILE_DOES_NOT_EXIST = 7
        FILE_PROTECTED = 8
        INVALID_PARAMETER = 9
        UNSUPPORTED = 10
        PROTOCOL_ERROR = 11
        NO_SYSTEM = 12

        def translate_to_rpc(self):
            if self == FtpResult.Result.UNKNOWN:
                return ftp_pb2.FtpResult.RESULT_UNKNOWN
            if self == FtpResult.Result.SUCCESS:
                return ftp_pb2.FtpResult.RESULT_SUCCESS
            if self == FtpResult.Result.NEXT:
                return ftp_pb2.FtpResult.RESULT_NEXT
            if self == FtpResult.Result.TIMEOUT:
                return ftp_pb2.FtpResult.RESULT_TIMEOUT
            if self == FtpResult.Result.BUSY:
                return ftp_pb2.FtpResult.RESULT_BUSY
            if self == FtpResult.Result.FILE_IO_ERROR:
                return ftp_pb2.FtpResult.RESULT_FILE_IO_ERROR
            if self == FtpResult.Result.FILE_EXISTS:
                return ftp_pb2.FtpResult.RESULT_FILE_EXISTS
            if self == FtpResult.Result.FILE_DOES_NOT_EXIST:
                return ftp_pb2.FtpResult.RESULT_FILE_DOES_NOT_EXIST
            if self == FtpResult.Result.FILE_PROTECTED:
                return ftp_pb2.FtpResult.RESULT_FILE_PROTECTED
            if self == FtpResult.Result.INVALID_PARAMETER:
                return ftp_pb2.FtpResult.RESULT_INVALID_PARAMETER
            if self == FtpResult.Result.UNSUPPORTED:
                return ftp_pb2.FtpResult.RESULT_UNSUPPORTED
            if self == FtpResult.Result.PROTOCOL_ERROR:
                return ftp_pb2.FtpResult.RESULT_PROTOCOL_ERROR
            if self == FtpResult.Result.NO_SYSTEM:
                return ftp_pb2.FtpResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_UNKNOWN:
                return FtpResult.Result.UNKNOWN
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_SUCCESS:
                return FtpResult.Result.SUCCESS
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_NEXT:
                return FtpResult.Result.NEXT
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_TIMEOUT:
                return FtpResult.Result.TIMEOUT
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_BUSY:
                return FtpResult.Result.BUSY
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_FILE_IO_ERROR:
                return FtpResult.Result.FILE_IO_ERROR
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_FILE_EXISTS:
                return FtpResult.Result.FILE_EXISTS
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_FILE_DOES_NOT_EXIST:
                return FtpResult.Result.FILE_DOES_NOT_EXIST
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_FILE_PROTECTED:
                return FtpResult.Result.FILE_PROTECTED
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_INVALID_PARAMETER:
                return FtpResult.Result.INVALID_PARAMETER
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_UNSUPPORTED:
                return FtpResult.Result.UNSUPPORTED
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_PROTOCOL_ERROR:
                return FtpResult.Result.PROTOCOL_ERROR
            if rpc_enum_value == ftp_pb2.FtpResult.RESULT_NO_SYSTEM:
                return FtpResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the FtpResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two FtpResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # FtpResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ FtpResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"FtpResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcFtpResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return FtpResult(
                
                FtpResult.Result.translate_from_rpc(rpcFtpResult.result),
                
                
                rpcFtpResult.result_str
                )

    def translate_to_rpc(self, rpcFtpResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcFtpResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcFtpResult.result_str = self.result_str
            
        
        



class FtpError(Exception):
    """ Raised when a FtpResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Ftp(AsyncBase):
    """
     Implements file transfer functionality using MAVLink FTP.

     Generated by dcsdkgen - MAVSDK Ftp API
    """

    # Plugin name
    name = "Ftp"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = ftp_pb2_grpc.FtpServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return FtpResult.translate_from_rpc(response.ftp_result)
    

    async def reset(self):
        """
         Resets FTP server in case there are stale open sessions.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.ResetRequest()
        response = await self._stub.Reset(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "reset()")
        

    async def download(self, remote_file_path, local_dir):
        """
         Downloads a file to local directory.

         Parameters
         ----------
         remote_file_path : std::string
              The path of the remote file to download.

         local_dir : std::string
              The local directory to download to.

         Yields
         -------
         progress_data : ProgressData
              The progress data if result is next

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.SubscribeDownloadRequest()
        request.remote_file_path = remote_file_path
        request.local_dir = local_dir
        download_stream = self._stub.SubscribeDownload(request)

        try:
            async for response in download_stream:
                
                result = self._extract_result(response)

                success_codes = [FtpResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in FtpResult.Result]:
                    success_codes.append(FtpResult.Result.NEXT)

                if result.result not in success_codes:
                    raise FtpError(result, "download()", remote_file_path, local_dir)

                if result.result == FtpResult.Result.SUCCESS:
                    download_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            download_stream.cancel()

    async def upload(self, local_file_path, remote_dir):
        """
         Uploads local file to remote directory.

         Parameters
         ----------
         local_file_path : std::string
              The local file path to upload.

         remote_dir : std::string
              The remote directory to upload to.

         Yields
         -------
         progress_data : ProgressData
              The progress data if result is next

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.SubscribeUploadRequest()
        request.local_file_path = local_file_path
        request.remote_dir = remote_dir
        upload_stream = self._stub.SubscribeUpload(request)

        try:
            async for response in upload_stream:
                
                result = self._extract_result(response)

                success_codes = [FtpResult.Result.SUCCESS]
                if 'NEXT' in [return_code.name for return_code in FtpResult.Result]:
                    success_codes.append(FtpResult.Result.NEXT)

                if result.result not in success_codes:
                    raise FtpError(result, "upload()", local_file_path, remote_dir)

                if result.result == FtpResult.Result.SUCCESS:
                    upload_stream.cancel();
                    return
                

            
                yield ProgressData.translate_from_rpc(response.progress_data)
        finally:
            upload_stream.cancel()

    async def list_directory(self, remote_dir):
        """
         Lists items from a remote directory.

         Parameters
         ----------
         remote_dir : std::string
              The remote directory to list the contents for.

         Returns
         -------
         paths : [std::string]
              The found directory contents.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.ListDirectoryRequest()
        
            
        request.remote_dir = remote_dir
            
        response = await self._stub.ListDirectory(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "list_directory()", remote_dir)
        

        return response.paths
        

    async def create_directory(self, remote_dir):
        """
         Creates a remote directory.

         Parameters
         ----------
         remote_dir : std::string
              The remote directory to create.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.CreateDirectoryRequest()
        request.remote_dir = remote_dir
        response = await self._stub.CreateDirectory(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "create_directory()", remote_dir)
        

    async def remove_directory(self, remote_dir):
        """
         Removes a remote directory.

         Parameters
         ----------
         remote_dir : std::string
              The remote directory to remove.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.RemoveDirectoryRequest()
        request.remote_dir = remote_dir
        response = await self._stub.RemoveDirectory(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "remove_directory()", remote_dir)
        

    async def remove_file(self, remote_file_path):
        """
         Removes a remote file.

         Parameters
         ----------
         remote_file_path : std::string
              The path of the remote file to remove.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.RemoveFileRequest()
        request.remote_file_path = remote_file_path
        response = await self._stub.RemoveFile(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "remove_file()", remote_file_path)
        

    async def rename(self, remote_from_path, remote_to_path):
        """
         Renames a remote file or remote directory.

         Parameters
         ----------
         remote_from_path : std::string
              The remote source path.

         remote_to_path : std::string
              The remote destination path.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.RenameRequest()
        request.remote_from_path = remote_from_path
        request.remote_to_path = remote_to_path
        response = await self._stub.Rename(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "rename()", remote_from_path, remote_to_path)
        

    async def are_files_identical(self, local_file_path, remote_file_path):
        """
         Compares a local file to a remote file using a CRC32 checksum.

         Parameters
         ----------
         local_file_path : std::string
              The path of the local file.

         remote_file_path : std::string
              The path of the remote file.

         Returns
         -------
         are_identical : bool
              Whether the files are identical.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.AreFilesIdenticalRequest()
        
            
        request.local_file_path = local_file_path
            
        
            
        request.remote_file_path = remote_file_path
            
        response = await self._stub.AreFilesIdentical(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "are_files_identical()", local_file_path, remote_file_path)
        

        return response.are_identical
        

    async def set_root_directory(self, root_dir):
        """
         Set root directory for MAVLink FTP server.

         Parameters
         ----------
         root_dir : std::string
              The root directory to set.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.SetRootDirectoryRequest()
        request.root_dir = root_dir
        response = await self._stub.SetRootDirectory(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "set_root_directory()", root_dir)
        

    async def set_target_compid(self, compid):
        """
         Set target component ID. By default it is the autopilot.

         Parameters
         ----------
         compid : uint32_t
              The component ID to set.

         Raises
         ------
         FtpError
             If the request fails. The error contains the reason for the failure.
        """

        request = ftp_pb2.SetTargetCompidRequest()
        request.compid = compid
        response = await self._stub.SetTargetCompid(request)

        
        result = self._extract_result(response)

        if result.result != FtpResult.Result.SUCCESS:
            raise FtpError(result, "set_target_compid()", compid)
        

    async def get_our_compid(self):
        """
         Get our own component ID.

         Returns
         -------
         compid : uint32_t
              Our component ID.

         
        """

        request = ftp_pb2.GetOurCompidRequest()
        response = await self._stub.GetOurCompid(request)

        

        return response.compid
        