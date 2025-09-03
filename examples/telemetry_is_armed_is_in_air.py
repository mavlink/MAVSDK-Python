#!/usr/bin/env python3

import asyncio
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    asyncio.ensure_future(print_is_armed(drone))
    asyncio.ensure_future(print_is_in_air(drone))

    # Keep the program running indefinitely
    exit_event = asyncio.Event()
    await exit_event.wait()


async def print_is_armed(drone):
    async for is_armed in drone.telemetry.armed():
        print("Is_armed:", is_armed)


async def print_is_in_air(drone):
    async for is_in_air in drone.telemetry.in_air():
        print("Is_in_air:", is_in_air)


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
