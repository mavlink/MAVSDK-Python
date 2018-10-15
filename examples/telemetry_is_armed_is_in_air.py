import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def print_is_armed():
    async for is_armed in drone.telemetry.armed():
        print("Is_armed:", is_armed)


async def print_is_in_air():
    async for is_in_air in drone.telemetry.in_air():
        print("Is_in_air:", is_in_air)


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(print_is_armed(), print_is_in_air()))
