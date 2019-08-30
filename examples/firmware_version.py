#!/usr/bin/env python3

import asyncio
from mavsdk import Drone


async def run():
    drone = Drone()
    await drone.connect(drone_address="udp://:14540")

    info = await drone.info.get_version()
    print(info)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
