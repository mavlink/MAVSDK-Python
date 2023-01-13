#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def print_flight_mode():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
