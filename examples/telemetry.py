#!/usr/bin/env python3

import asyncio
import logging

from mavsdk import System

# Enable INFO level logging by default so that INFO messages are shown
logging.basicConfig(level=logging.INFO)


async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    # Start the tasks
    tasks = []
    tasks.append(asyncio.create_task(print_battery(drone)))
    tasks.append(asyncio.create_task(print_gps_info(drone)))
    tasks.append(asyncio.create_task(print_in_air(drone)))
    tasks.append(asyncio.create_task(print_position(drone)))

    # Keep the program running indefinitely
    exit_event = asyncio.Event()
    await exit_event.wait()


async def print_battery(drone):
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent}")


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def print_in_air(drone):
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_position(drone):
    async for position in drone.telemetry.position():
        print(position)


if __name__ == "__main__":
    # Start the main function
    asyncio.run(run())
