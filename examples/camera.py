#!/usr/bin/env python3

import asyncio

from mavsdk import (CameraError, CameraMode)
from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    asyncio.ensure_future(print_camera_mode(drone))
    asyncio.ensure_future(print_camera_status(drone))

    print("Setting mode to 'PHOTO'")
    try:
        await drone.camera.set_mode(CameraMode.PHOTO)
    except CameraError as error:
        print(f"Setting mode failed with error code: {error._result.result}")

    await asyncio.sleep(2)

    print("Taking a photo")
    try:
        await drone.camera.take_photo()
    except CameraError as error:
        print(f"Couldn't take photo: {error._result.result}")

    # Shut down the running coroutines (here 'print_camera_mode()' and 'print_camera_status()')
    await asyncio.get_event_loop().shutdown_asyncgens()

async def print_camera_mode(drone):
    async for camera_mode in drone.camera.mode():
        print(f"Camera mode: {camera_mode}")

async def print_camera_status(drone):
    async for camera_status in drone.camera.camera_status():
        print(camera_status)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
