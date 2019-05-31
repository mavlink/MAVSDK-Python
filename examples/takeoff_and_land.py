#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():

    print("Waiting for drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(5)

    print("-- Landing")
    await drone.action.land()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
