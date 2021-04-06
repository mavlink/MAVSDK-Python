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
    # Start the main function
    asyncio.ensure_future(run())

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
