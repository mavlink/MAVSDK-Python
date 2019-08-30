#!/usr/bin/env python3

import asyncio
from mavsdk import Drone


async def print_flight_mode():
    drone = Drone()
    await drone.connect(drone_address="udp://:14540")

    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_flight_mode())
