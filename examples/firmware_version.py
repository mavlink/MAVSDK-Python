#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():

    info = await drone.info.getVersion()
    print(info)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
