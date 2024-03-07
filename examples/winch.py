#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print(f"-- Winch action: load payload")
    await drone.winch.load_payload(instance=1)

    while True:
        print("Staying connected, press Ctrl-C to exit")
        await asyncio.sleep(1)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
