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

        full_data = preamble + ubx_sync_byte
        full_data += ubx_class_id + ubx_message_id
        full_data += length_lsb + length_msb
        full_data += pkt + checksum

        if self.debug:
            print("UBX class id {} and message id {}".format(
                ord(ubx_class_id),
                ord(ubx_message_id))
            )

        # The ubx message in full_data could be parsed with pyubx2.UBXReader
        return full_data


class RTCMParser:
    def __init__(self):
        self.debug = True
        self.crc_init = 0x01864cfb
        self._init_crc_table()

    def _init_crc_table(self):
        self.crc_table = [0] * 256
        for i in range(256):
            self.crc_table[i] = i << 16
            for j in range(8):
                self.crc_table[i] <<= 1
                if self.crc_table[i] & 0x1000000:
                    self.crc_table[i] ^= self.crc_init

    def crc24(self, msg):
        crc = 0
        for byte in msg:
            crc = ((crc << 8) & 0xFFFFFF) ^ self.crc_table[(crc >> 16) ^ byte]
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
                # This creates an odd Python string that gets decoded on the
                # C++ server side.
                # With MAVSDK v2, the API will change to a vector of bytes
                # instead of this clunky string.

                await drone.rtk.send_rtcm_data(
                    rtk.RtcmData(str(rtcm_correction_data)))

            elif ord(preamble) == PREAMBLE_UBX:
                ubx = ubx_parser.read_packet(ublox, preamble)
                if ubx is None:
                    continue
                # do something with the message

            elif ord(preamble) == PREAMBLE_NMEA:
                # warning: you should disable NMEA on your ublox chip!

                nmea = ublox.readline()
                # print(nmea)
                pass

        except Exception as e:
            print(f"Exception: {e}")

if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
