#!/usr/bin/env python3

import asyncio

from mavsdk.camera import (CameraError, Mode)
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print_mode_task = asyncio.ensure_future(print_mode(drone))
    print_status_task = asyncio.ensure_future(print_status(drone))
    running_tasks = [print_mode_task, print_status_task]

    print("Setting mode to 'PHOTO'")
    try:
        await drone.camera.set_mode(Mode.PHOTO)
    except CameraError as error:
        print(f"Setting mode failed with error code: {error._result.result}")

    await asyncio.sleep(2)

    print("Taking a photo")
    try:
        await drone.camera.take_photo()
    except CameraError as error:
        print(f"Couldn't take photo: {error._result.result}")

    # Shut down the running coroutines (here 'print_mode()' and
    # 'print_status()')
    for task in running_tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
    await asyncio.get_event_loop().shutdown_asyncgens()


async def print_mode(drone):
    async for mode in drone.camera.mode():
        print(f"Camera mode: {mode}")


async def print_status(drone):
    async for status in drone.camera.status():
        print(status)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
