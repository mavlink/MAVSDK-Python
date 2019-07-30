#!/usr/bin/env python3

import asyncio

from mavsdk import start_mavlink
from mavsdk import connect as mavsdk_connect

start_mavlink(connection_url="udp://:14540")
drone = mavsdk_connect(host="127.0.0.1")


async def print_battery():
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent}")


async def print_gps_info():
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def print_in_air():
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_position():
    async for position in drone.telemetry.position():
        print(position)


def setup_tasks():
    # Create asyncio tasks with the default eventloop
    # asyncio.create_task() is only callable when the event loop is already
    # running!!!
    asyncio.ensure_future(print_battery())
    asyncio.ensure_future(print_gps_info())
    asyncio.ensure_future(print_in_air())
    asyncio.ensure_future(print_position())


if __name__ == "__main__":

    # Setup asyncio tasks
    setup_tasks()

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
