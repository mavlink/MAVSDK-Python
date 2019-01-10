#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect
from dronecode_sdk import (CameraError, CameraMode)

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():
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

async def print_camera_mode():
    async for camera_mode in drone.camera.mode():
        print(f"Camera mode: {camera_mode}")

async def print_camera_status():
    async for camera_status in drone.camera.camera_status():
        print(camera_status)


if __name__ == "__main__":
    asyncio.ensure_future(print_camera_mode())
    asyncio.ensure_future(print_camera_status())

    asyncio.get_event_loop().run_until_complete(run())
