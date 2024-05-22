#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():

    drone = System(mavsdk_server_address='localhost', port=50051)
    await drone.connect(system_address="serial:///dev/ttyACM0:57600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("directory list", await drone.ftp.list_directory("/"))


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
