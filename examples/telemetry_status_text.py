#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def print_status_text():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    async for status_text in drone.telemetry.status_text():
        print("Statustext:", status_text)


if __name__ == "__main__":
    asyncio.run(print_status_text())
