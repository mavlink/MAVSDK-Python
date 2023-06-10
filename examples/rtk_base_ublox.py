#!/usr/bin/env python3

import asyncio
import serial
from mavsdk import System, rtk

PREAMBLE_RTCM = 0xD3
PREAMBLE_UBX = 0xB5
PREAMBLE_NMEA = 0x24

class UBXParser:
    def __init__(self):
        self.debug = False

    def read_packet(self, dev, preamble):
        ubx_sync_byte = dev.read(1)
        if len(ubx_sync_byte) == 0 or ord(ubx_sync_byte) != 0x62:
            return None
        ubx_class_id = dev.read(1)
        ubx_message_id = dev.read(1)
        length_lsb = dev.read(1)
        length_msb = dev.read(1)
        pkt_len = (ord(length_msb) << 8) + ord(length_lsb)
        pkt = dev.read(pkt_len)
        checksum = dev.read(2)
        full_data = preamble + ubx_sync_byte + ubx_class_id + ubx_message_id + length_lsb + length_msb + pkt + checksum
        if self.debug:
            print("Got UBX class id {} and message id {}".format(ord(ubx_class_id), ord(ubx_message_id)))

        # The ubx message in full_data could be parsed with e.g. pyubx2.UBXReader
        return full_data

class RTCMParser:
    def __init__(self):
        self.debug = True
        self.crc_table = [0x0, 0x864cfb, 0x8ad50d, 0xc99f6, 0x93e6e1, 0x15aa1a, 0x1933ec, 0x9f7f17, 0xa18139, 0x27cdc2, 0x2b5434, 0xad18cf, 0x3267d8, 0xb42b23, 0xb8b2d5, 0x3efe2e, 0xc54e89, 0x430272, 0x4f9b84, 0xc9d77f, 0x56a868, 0xd0e493, 0xdc7d65, 0x5a319e, 0x64cfb0, 0xe2834b, 0xee1abd, 0x685646, 0xf72951, 0x7165aa, 0x7dfc5c, 0xfbb0a7, 0xcd1e9, 0x8a9d12, 0x8604e4, 0x481f, 0x9f3708, 0x197bf3, 0x15e205, 0x93aefe, 0xad50d0, 0x2b1c2b, 0x2785dd, 0xa1c926, 0x3eb631, 0xb8faca, 0xb4633c, 0x322fc7, 0xc99f60, 0x4fd39b, 0x434a6d, 0xc50696, 0x5a7981, 0xdc357a, 0xd0ac8c, 0x56e077, 0x681e59, 0xee52a2, 0xe2cb54, 0x6487af, 0xfbf8b8, 0x7db443, 0x712db5, 0xf7614e, 0x19a3d2, 0x9fef29, 0x9376df, 0x153a24, 0x8a4533, 0xc09c8, 0x903e, 0x86dcc5, 0xb822eb, 0x3e6e10, 0x32f7e6, 0xb4bb1d, 0x2bc40a, 0xad88f1, 0xa11107, 0x275dfc, 0xdced5b, 0x5aa1a0, 0x563856, 0xd074ad, 0x4f0bba, 0xc94741, 0xc5deb7, 0x43924c, 0x7d6c62, 0xfb2099, 0xf7b96f, 0x71f594, 0xee8a83, 0x68c678, 0x645f8e, 0xe21375, 0x15723b, 0x933ec0, 0x9fa736, 0x19ebcd, 0x8694da, 0xd821, 0xc41d7, 0x8a0d2c, 0xb4f302, 0x32bff9, 0x3e260f, 0xb86af4, 0x2715e3, 0xa15918, 0xadc0ee, 0x2b8c15, 0xd03cb2, 0x567049, 0x5ae9bf, 0xdca544, 0x43da53, 0xc596a8, 0xc90f5e, 0x4f43a5, 0x71bd8b, 0xf7f170, 0xfb6886, 0x7d247d, 0xe25b6a, 0x641791, 0x688e67, 0xeec29c, 0x3347a4, 0xb50b5f, 0xb992a9, 0x3fde52, 0xa0a145, 0x26edbe, 0x2a7448, 0xac38b3, 0x92c69d, 0x148a66, 0x181390, 0x9e5f6b, 0x1207c, 0x876c87, 0x8bf571, 0xdb98a, 0xf6092d, 0x7045d6, 0x7cdc20, 0xfa90db, 0x65efcc, 0xe3a337, 0xef3ac1, 0x69763a, 0x578814, 0xd1c4ef, 0xdd5d19, 0x5b11e2, 0xc46ef5, 0x42220e, 0x4ebbf8, 0xc8f703, 0x3f964d, 0xb9dab6, 0xb54340, 0x330fbb, 0xac70ac, 0x2a3c57, 0x26a5a1, 0xa0e95a, 0x9e1774, 0x185b8f, 0x14c279, 0x928e82, 0xdf195, 0x8bbd6e, 0x872498, 0x16863, 0xfad8c4, 0x7c943f, 0x700dc9, 0xf64132, 0x693e25, 0xef72de, 0xe3eb28, 0x65a7d3, 0x5b59fd, 0xdd1506, 0xd18cf0, 0x57c00b, 0xc8bf1c, 0x4ef3e7, 0x426a11, 0xc426ea, 0x2ae476, 0xaca88d, 0xa0317b, 0x267d80, 0xb90297, 0x3f4e6c, 0x33d79a, 0xb59b61, 0x8b654f, 0xd29b4, 0x1b042, 0x87fcb9, 0x1883ae, 0x9ecf55, 0x9256a3, 0x141a58, 0xefaaff, 0x69e604, 0x657ff2, 0xe33309, 0x7c4c1e, 0xfa00e5, 0xf69913, 0x70d5e8, 0x4e2bc6, 0xc8673d, 0xc4fecb, 0x42b230, 0xddcd27, 0x5b81dc, 0x57182a, 0xd154d1, 0x26359f, 0xa07964, 0xace092, 0x2aac69, 0xb5d37e, 0x339f85, 0x3f0673, 0xb94a88, 0x87b4a6, 0x1f85d, 0xd61ab, 0x8b2d50, 0x145247, 0x921ebc, 0x9e874a, 0x18cbb1, 0xe37b16, 0x6537ed, 0x69ae1b, 0xefe2e0, 0x709df7, 0xf6d10c, 0xfa48fa, 0x7c0401, 0x42fa2f, 0xc4b6d4, 0xc82f22, 0x4e63d9, 0xd11cce, 0x575035, 0x5bc9c3, 0xdd8538]

    def crc24(self, msg):
        crc = 0
        for byte in msg:
            crc = ((crc<<8)&0xFFFFFF) ^ self.crc_table[(crc>>16) ^ byte]
        return crc

    def read_packet(self, dev, preamble):
        length_msb = dev.read(1)
        length_lsb = dev.read(1)
        pkt_len = ((ord(length_msb) & 0x3) << 8) + ord(length_lsb)
        pkt = dev.read(pkt_len)
        checksum = dev.read(3)

        full_data = preamble + length_msb + length_lsb + pkt + checksum
        rtcm_id = (pkt[0] << 4) + ((pkt[1] & 0xF0) >> 4)
        parity = (checksum[0] << 16) + (checksum[1] << 8) + checksum[2]
        if parity == self.crc24(full_data[:-3]):
            if self.debug:
                print("Got RTCM message with ID {}".format(rtcm_id))
            return full_data
        else:
            if self.debug:
                print("RTCM parity check failed. Skip message")
            return None

async def run():
    # Init the drone
    drone = System()
    await drone.connect()

    # Start the tasks
    asyncio.ensure_future(print_gps_info(drone))
    asyncio.ensure_future(send_rtcm(drone))

    while True:
        await asyncio.sleep(1)


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def send_rtcm(drone):

    # Connect to a ublox RTK base station via USB
    ublox = serial.Serial("/dev/ttyACM0", 9600)
    rtcm_parser = RTCMParser()
    ubx_parser = UBXParser()

    while True:
        try:
            preamble = ublox.read(1)
            if len(preamble) == 0:
                continue

            if ord(preamble) == PREAMBLE_RTCM:
                rtcm_correction_data = rtcm_parser.read_packet(ublox, preamble)
                if rtcm_correction_data is None:
                    continue

                # We convert the data to a string here as the API wants it even
                # though it should be raw bytes.
                # This creates odd an odd Python string that gets decoded on the
                # C++ server side.
                # With MAVSDK v2, the API will change to a vector of bytes instead
                # of this clunky string.

                await drone.rtk.send_rtcm_data(
                    rtk.RtcmData(str(rtcm_correction_data)))

            elif ord(preamble) == PREAMBLE_UBX:
                ubx = ubx_parser.read_packet(ublox, preamble)
                if ubx is None:
                    continue
                # do something with the message

            elif ord(preamble) == PREAMBLE_NMEA:
                # silently ignore this case, but you should disable NMEA on your ublox chip
                nmea = ublox.readline()
                # print(nmea)
                pass

        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
