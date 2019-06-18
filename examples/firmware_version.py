#!/usr/bin/env python3

import asyncio

from mavsdk import connect as mavsdk_connect

drone = mavsdk_connect(host="127.0.0.1")


async def run():

    info = await drone.info.get_version()
    print(info)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
