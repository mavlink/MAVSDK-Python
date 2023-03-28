#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    # Init the drone
    drone = System()
    await drone.connect()

    # Start the tasks
    asyncio.ensure_future(print_transponders(drone))

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    while True:
        print("Waiting for transponder messages")
        await asyncio.sleep(1)


async def print_transponders(drone):
    async for transponder in drone.transponder.transponder():
        print(transponder)


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
