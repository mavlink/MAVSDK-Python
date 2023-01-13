#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    # Init the drone
    drone = System()
    #await drone.connect(system_address="udp://:14540")
    await drone.connect()

    # Start the tasks
    asyncio.ensure_future(print_transponders(drone))

async def print_transponders(drone):
    async for transponder in drone.transponder.transponder():
        print(transponder)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
