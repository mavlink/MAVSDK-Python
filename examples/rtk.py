#!/usr/bin/env python3

import asyncio
from mavsdk import System, rtk

# Some sample data that won't work because it needs to have the correct time
# information. However, that's the sort of bytes that can be expected.

# In a real case this data would be read from an ntrip service or read from
# a local GNSS base station.

rtcm_correction_data = bytes(
    [0xd3, 0x0, 0x6, 0x4c, 0xe0, 0x0, 0x88, 0x10, 0x97, 0xc2, 0x44, 0x8b])


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
    while True:
        try:
            # We convert the data to a string here as the API wants it even
            # though it should be raw bytes.
            # This creates odd an odd Python string that gets decoded on the
            # C++ server side.
            # With MAVSDK v2, the API will change to a vector of bytes instead
            # of this clunky string.

            await drone.rtk.send_rtcm_data(
                rtk.RtcmData(str(rtcm_correction_data)))

        except Exception as e:
            print(f"Exception: {e}")

        await asyncio.sleep(1)


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
