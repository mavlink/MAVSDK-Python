#!/usr/bin/env python3

import asyncio

from mavsdk import start_mavlink
from mavsdk import connect as mavsdk_connect

start_mavlink()
drone = mavsdk_connect(host="127.0.0.1")


async def print_flight_mode():
    async for flight_mode in drone.telemetry.flight_mode():
        print("FlightMode:", flight_mode)


loop = asyncio.get_event_loop()
loop.run_until_complete(print_flight_mode())
