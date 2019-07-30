#!/usr/bin/env python3

import asyncio

from mavsdk import start_mavlink
from mavsdk import connect as mavsdk_connect

start_mavlink(connection_url="udp://:14540")
drone = mavsdk_connect(host="127.0.0.1")


async def run():

    info = await drone.info.get_version()
    print(info)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
