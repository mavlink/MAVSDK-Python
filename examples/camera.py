#!/usr/bin/env python3

import asyncio
import logging

from mavsdk_grpc.camera import CameraError, Mode
from mavsdk_grpc import System

# Enable INFO level logging by default so that INFO messages are shown
logging.basicConfig(level=logging.INFO)


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    print("Waiting for a camera...")
    async for camera_list in drone.camera.camera_list():
        if camera_list.cameras:
            camera = camera_list.cameras[0]
            break
    print(
        f"-- Found camera {camera.vendor_name} {camera.model_name} "
        f"(component ID {camera.component_id})"
    )

    print_mode_task = asyncio.ensure_future(print_mode(drone))
    print_storage_task = asyncio.ensure_future(print_storage(drone))
    running_tasks = [print_mode_task, print_storage_task]

    print("Setting mode to 'PHOTO'")
    try:
        await drone.camera.set_mode(camera.component_id, Mode.PHOTO)
    except CameraError as error:
        print(f"Setting mode failed with error code: {error._result.result}")

    await asyncio.sleep(2)

    print("Taking a photo")
    try:
        await drone.camera.take_photo(camera.component_id)
    except CameraError as error:
        print(f"Couldn't take photo: {error._result.result}")

    # Shut down the running coroutines (here 'print_mode()' and
    # 'print_storage()')
    for task in running_tasks:
        task.cancel()
        try:
            await task
        except asyncio.CancelledError:
            pass
    await asyncio.get_event_loop().shutdown_asyncgens()


async def print_mode(drone):
    async for update in drone.camera.mode():
        print(f"Camera {update.component_id} mode: {update.mode}")


async def print_storage(drone):
    async for update in drone.camera.storage():
        print(f"Camera {update.component_id} storage: {update.storage}")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
