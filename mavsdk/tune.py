# -*- coding: utf-8 -*-
# DO NOT EDIT! This file is auto-generated from
# https://github.com/mavlink/MAVSDK-Python/tree/main/other/templates/py
from ._base import AsyncBase
from . import tune_pb2, tune_pb2_grpc
from enum import Enum


class SongElement(Enum):
    """
     An element of the tune

     Values
     ------
     STYLE_LEGATO
          After this element, start playing legato

     STYLE_NORMAL
          After this element, start playing normal

     STYLE_STACCATO
          After this element, start playing staccato

     DURATION_1
          After this element, set the note duration to 1

     DURATION_2
          After this element, set the note duration to 2

     DURATION_4
          After this element, set the note duration to 4

     DURATION_8
          After this element, set the note duration to 8

     DURATION_16
          After this element, set the note duration to 16

     DURATION_32
          After this element, set the note duration to 32

     NOTE_A
          Play note A

     NOTE_B
          Play note B

     NOTE_C
          Play note C

     NOTE_D
          Play note D

     NOTE_E
          Play note E

     NOTE_F
          Play note F

     NOTE_G
          Play note G

     NOTE_PAUSE
          Play a rest

     SHARP
          After this element, sharp the note (half a step up)

     FLAT
          After this element, flat the note (half a step down)

     OCTAVE_UP
          After this element, shift the note 1 octave up

     OCTAVE_DOWN
          After this element, shift the note 1 octave down

     """

    
    STYLE_LEGATO = 0
    STYLE_NORMAL = 1
    STYLE_STACCATO = 2
    DURATION_1 = 3
    DURATION_2 = 4
    DURATION_4 = 5
    DURATION_8 = 6
    DURATION_16 = 7
    DURATION_32 = 8
    NOTE_A = 9
    NOTE_B = 10
    NOTE_C = 11
    NOTE_D = 12
    NOTE_E = 13
    NOTE_F = 14
    NOTE_G = 15
    NOTE_PAUSE = 16
    SHARP = 17
    FLAT = 18
    OCTAVE_UP = 19
    OCTAVE_DOWN = 20

    def translate_to_rpc(self):
        if self == SongElement.STYLE_LEGATO:
            return tune_pb2.SONG_ELEMENT_STYLE_LEGATO
        if self == SongElement.STYLE_NORMAL:
            return tune_pb2.SONG_ELEMENT_STYLE_NORMAL
        if self == SongElement.STYLE_STACCATO:
            return tune_pb2.SONG_ELEMENT_STYLE_STACCATO
        if self == SongElement.DURATION_1:
            return tune_pb2.SONG_ELEMENT_DURATION_1
        if self == SongElement.DURATION_2:
            return tune_pb2.SONG_ELEMENT_DURATION_2
        if self == SongElement.DURATION_4:
            return tune_pb2.SONG_ELEMENT_DURATION_4
        if self == SongElement.DURATION_8:
            return tune_pb2.SONG_ELEMENT_DURATION_8
        if self == SongElement.DURATION_16:
            return tune_pb2.SONG_ELEMENT_DURATION_16
        if self == SongElement.DURATION_32:
            return tune_pb2.SONG_ELEMENT_DURATION_32
        if self == SongElement.NOTE_A:
            return tune_pb2.SONG_ELEMENT_NOTE_A
        if self == SongElement.NOTE_B:
            return tune_pb2.SONG_ELEMENT_NOTE_B
        if self == SongElement.NOTE_C:
            return tune_pb2.SONG_ELEMENT_NOTE_C
        if self == SongElement.NOTE_D:
            return tune_pb2.SONG_ELEMENT_NOTE_D
        if self == SongElement.NOTE_E:
            return tune_pb2.SONG_ELEMENT_NOTE_E
        if self == SongElement.NOTE_F:
            return tune_pb2.SONG_ELEMENT_NOTE_F
        if self == SongElement.NOTE_G:
            return tune_pb2.SONG_ELEMENT_NOTE_G
        if self == SongElement.NOTE_PAUSE:
            return tune_pb2.SONG_ELEMENT_NOTE_PAUSE
        if self == SongElement.SHARP:
            return tune_pb2.SONG_ELEMENT_SHARP
        if self == SongElement.FLAT:
            return tune_pb2.SONG_ELEMENT_FLAT
        if self == SongElement.OCTAVE_UP:
            return tune_pb2.SONG_ELEMENT_OCTAVE_UP
        if self == SongElement.OCTAVE_DOWN:
            return tune_pb2.SONG_ELEMENT_OCTAVE_DOWN

    @staticmethod
    def translate_from_rpc(rpc_enum_value):
        """ Parses a gRPC response """
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_STYLE_LEGATO:
            return SongElement.STYLE_LEGATO
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_STYLE_NORMAL:
            return SongElement.STYLE_NORMAL
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_STYLE_STACCATO:
            return SongElement.STYLE_STACCATO
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_1:
            return SongElement.DURATION_1
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_2:
            return SongElement.DURATION_2
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_4:
            return SongElement.DURATION_4
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_8:
            return SongElement.DURATION_8
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_16:
            return SongElement.DURATION_16
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_DURATION_32:
            return SongElement.DURATION_32
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_A:
            return SongElement.NOTE_A
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_B:
            return SongElement.NOTE_B
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_C:
            return SongElement.NOTE_C
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_D:
            return SongElement.NOTE_D
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_E:
            return SongElement.NOTE_E
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_F:
            return SongElement.NOTE_F
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_G:
            return SongElement.NOTE_G
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_NOTE_PAUSE:
            return SongElement.NOTE_PAUSE
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_SHARP:
            return SongElement.SHARP
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_FLAT:
            return SongElement.FLAT
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_OCTAVE_UP:
            return SongElement.OCTAVE_UP
        if rpc_enum_value == tune_pb2.SONG_ELEMENT_OCTAVE_DOWN:
            return SongElement.OCTAVE_DOWN

    def __str__(self):
        return self.name


class TuneDescription:
    """
     Tune description, containing song elements and tempo.

     Parameters
     ----------
     song_elements : [SongElement]
          The list of song elements (notes, pauses, ...) to be played

     tempo : int32_t
          The tempo of the song (range: 32 - 255)

     """

    

    def __init__(
            self,
            song_elements,
            tempo):
        """ Initializes the TuneDescription object """
        self.song_elements = song_elements
        self.tempo = tempo

    def __eq__(self, to_compare):
        """ Checks if two TuneDescription are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TuneDescription object
            return \
                (self.song_elements == to_compare.song_elements) and \
                (self.tempo == to_compare.tempo)

        except AttributeError:
            return False

    def __str__(self):
        """ TuneDescription in string representation """
        struct_repr = ", ".join([
                "song_elements: " + str(self.song_elements),
                "tempo: " + str(self.tempo)
                ])

        return f"TuneDescription: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTuneDescription):
        """ Translates a gRPC struct to the SDK equivalent """
        return TuneDescription(
                
                list(map(lambda elem: SongElement.translate_from_rpc(elem), rpcTuneDescription.song_elements)),
                
                
                rpcTuneDescription.tempo
                )

    def translate_to_rpc(self, rpcTuneDescription):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpc_elems_list = []
        for elem in self.song_elements:
                
            rpc_elems_list.append(elem.translate_to_rpc())
                
        rpcTuneDescription.song_elements.extend(rpc_elems_list)
            
        
        
        
            
        rpcTuneDescription.tempo = self.tempo
            
        
        


class TuneResult:
    """
 

     Parameters
     ----------
     result : Result
          Result enum value

     result_str : std::string
          Human-readable English string describing the result

     """

    
    
    class Result(Enum):
        """
         Possible results returned for tune requests.

         Values
         ------
         UNKNOWN
              Unknown result

         SUCCESS
              Request succeeded

         INVALID_TEMPO
              Invalid tempo (range: 32 - 255)

         TUNE_TOO_LONG
              Invalid tune: encoded string must be at most 247 chars

         ERROR
              Failed to send the request

         NO_SYSTEM
              No system connected

         """

        
        UNKNOWN = 0
        SUCCESS = 1
        INVALID_TEMPO = 2
        TUNE_TOO_LONG = 3
        ERROR = 4
        NO_SYSTEM = 5

        def translate_to_rpc(self):
            if self == TuneResult.Result.UNKNOWN:
                return tune_pb2.TuneResult.RESULT_UNKNOWN
            if self == TuneResult.Result.SUCCESS:
                return tune_pb2.TuneResult.RESULT_SUCCESS
            if self == TuneResult.Result.INVALID_TEMPO:
                return tune_pb2.TuneResult.RESULT_INVALID_TEMPO
            if self == TuneResult.Result.TUNE_TOO_LONG:
                return tune_pb2.TuneResult.RESULT_TUNE_TOO_LONG
            if self == TuneResult.Result.ERROR:
                return tune_pb2.TuneResult.RESULT_ERROR
            if self == TuneResult.Result.NO_SYSTEM:
                return tune_pb2.TuneResult.RESULT_NO_SYSTEM

        @staticmethod
        def translate_from_rpc(rpc_enum_value):
            """ Parses a gRPC response """
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_UNKNOWN:
                return TuneResult.Result.UNKNOWN
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_SUCCESS:
                return TuneResult.Result.SUCCESS
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_INVALID_TEMPO:
                return TuneResult.Result.INVALID_TEMPO
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_TUNE_TOO_LONG:
                return TuneResult.Result.TUNE_TOO_LONG
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_ERROR:
                return TuneResult.Result.ERROR
            if rpc_enum_value == tune_pb2.TuneResult.RESULT_NO_SYSTEM:
                return TuneResult.Result.NO_SYSTEM

        def __str__(self):
            return self.name
    

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the TuneResult object """
        self.result = result
        self.result_str = result_str

    def __eq__(self, to_compare):
        """ Checks if two TuneResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # TuneResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __str__(self):
        """ TuneResult in string representation """
        struct_repr = ", ".join([
                "result: " + str(self.result),
                "result_str: " + str(self.result_str)
                ])

        return f"TuneResult: [{struct_repr}]"

    @staticmethod
    def translate_from_rpc(rpcTuneResult):
        """ Translates a gRPC struct to the SDK equivalent """
        return TuneResult(
                
                TuneResult.Result.translate_from_rpc(rpcTuneResult.result),
                
                
                rpcTuneResult.result_str
                )

    def translate_to_rpc(self, rpcTuneResult):
        """ Translates this SDK object into its gRPC equivalent """

        
        
            
        rpcTuneResult.result = self.result.translate_to_rpc()
            
        
        
        
            
        rpcTuneResult.result_str = self.result_str
            
        
        



class TuneError(Exception):
    """ Raised when a TuneResult is a fail code """

    def __init__(self, result, origin, *params):
        self._result = result
        self._origin = origin
        self._params = params

    def __str__(self):
        return f"{self._result.result}: '{self._result.result_str}'; origin: {self._origin}; params: {self._params}"


class Tune(AsyncBase):
    """
     Enable creating and sending a tune to be played on the system.

     Generated by dcsdkgen - MAVSDK Tune API
    """

    # Plugin name
    name = "Tune"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = tune_pb2_grpc.TuneServiceStub(channel)

    
    def _extract_result(self, response):
        """ Returns the response status and description """
        return TuneResult.translate_from_rpc(response.tune_result)
    

    async def play_tune(self, tune_description):
        """
         Send a tune to be played by the system.

         Parameters
         ----------
         tune_description : TuneDescription
              The tune to be played

         Raises
         ------
         TuneError
             If the request fails. The error contains the reason for the failure.
        """

        request = tune_pb2.PlayTuneRequest()
        
        tune_description.translate_to_rpc(request.tune_description)
                
            
        response = await self._stub.PlayTune(request)

        
        result = self._extract_result(response)

        if result.result != TuneResult.Result.SUCCESS:
            raise TuneError(result, "play_tune()", tune_description)
        