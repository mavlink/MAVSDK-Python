#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def print_flight_mode():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode())
