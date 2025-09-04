#!/usr/bin/env python3

import asyncio
import logging
from mavsdk import System

# Enable INFO level logging by default so that INFO messages are shown
logging.basicConfig(level=logging.INFO)


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    info = await drone.info.get_version()
    print(info)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
