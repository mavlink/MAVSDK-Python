#!/usr/bin/env python3

import asyncio
import serial
from mavsdk import System, rtk
import base64

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
            print(
                "UBX class id {} and message id {}".format(
                    ord(ubx_class_id), ord(ubx_message_id)
                )
            )

        # The ubx message in full_data could be parsed with pyubx2.UBXReader
        return full_data


class RTCMParser:
    def __init__(self):
        self.debug = True
        self.crc_init = 0x01864CFB
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
    # Init the drone.
    # Note that connecting directly to a drone is not very useful here.
    # You probably want to set-up some MAVLink message routing inbetween
    # this script and the drone.
    # Good candidates for this are
    # 1. mavlink-router (https://github.com/mavlink-router/mavlink-router)
    # 2. MAVSDK (https://tinyurl.com/mavsdk-forwarding)
    # In the latter case you can use something like this here:
    # await drone.connect("udp://<IP address of the drone here>:14540")
    drone = System()
    await drone.connect()

    # Start the tasks
    _tasks = [
        asyncio.create_task(print_gps_info(drone)),
        asyncio.create_task(send_rtcm(drone)),
    ]

    # Keep the program running indefinitely
    exit_event = asyncio.Event()
    await exit_event.wait()


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def send_rtcm(drone):
    # Connect to a ublox RTK base station via USB.
    # Make sure that the baudrate matches the setting on the UBlox chip.
    # If you use UART instead, you should set the correct serial device.
    ublox = serial.Serial("/dev/ttyACM0", 9600)

    rtcm_parser = RTCMParser()
    ubx_parser = UBXParser()

    while True:
        try:
            # Depending on your configuration of the uBlox device,
            # we might receive different kinds of messages.
            # The first byte indicates what kind of message it is:
            # RTCM, UBX or NMEA. In this script we only process
            # RTCM messages, but UBX can be used to configure the
            # chip itself, for example by setting the frequency
            # of certain UBX/RTCM messages with UBX-CFG-MSG
            preamble = ublox.read(1)
            if len(preamble) == 0:
                continue

            if ord(preamble) == PREAMBLE_RTCM:
                rtcm_correction_data = rtcm_parser.read_packet(ublox, preamble)
                if rtcm_correction_data is None:
                    continue

                # Convert the rtcm data to a base64,
                # In MAVSDK v3 the rtcm data is expected
                # to be base64 encoded string .
                base64_rtcm_data = base64.b64encode(rtcm_correction_data).decode(
                    "utf-8"
                )

                # Send RTCM
                await drone.rtk.send_rtcm_data(rtk.RtcmData(base64_rtcm_data))

            elif ord(preamble) == PREAMBLE_UBX:
                ubx = ubx_parser.read_packet(ublox, preamble)
                if ubx is None:
                    continue

                # If configured properly, we might receive a lot of helpful
                # messages here, especially for a RTK base station.
                # For example, UBX-NAV-SVIN gives information about a
                # survey-in: Whether it's completed, its current accuracy
                # and its duration.

                # Another useful message is UBX-RXM-RAWX here, if you are
                # looking for Precise Point Positioning (PPP)

                # Check https://github.com/semuconsulting/pyubx2#generating on
                # how to configure the UBlox chip with a python script

            elif ord(preamble) == PREAMBLE_NMEA:
                # It's recommended to disable NMEA messages, so this script
                # does not have to differentiate between 3 kinds of messages

                # nmea = ublox.readline()
                # print(nmea)
                pass

        except Exception as e:
            print(f"Exception: {e}")


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
