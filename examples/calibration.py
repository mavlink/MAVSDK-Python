#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("-- Starting gyro calibration")
    async for progress_data in drone.calibration.calibrate_gyro():
        print(progress_data)

    print("-- Starting magneto calibration")
    async for progress_data in drone.calibration.calibrate_magnetometer():
        print(progress_data)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
