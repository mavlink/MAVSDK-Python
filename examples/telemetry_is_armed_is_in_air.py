#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    asyncio.ensure_future(print_is_armed(drone))
    asyncio.ensure_future(print_is_in_air(drone))


async def print_is_armed(drone):
    async for is_armed in drone.telemetry.armed():
        print("Is_armed:", is_armed)


async def print_is_in_air(drone):
    async for is_in_air in drone.telemetry.in_air():
        print("Is_in_air:", is_in_air)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
