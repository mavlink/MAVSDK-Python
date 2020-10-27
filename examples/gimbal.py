#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.gimbal import GimbalMode

async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Start printing gimbal position updates
    asyncio.ensure_future(print_gimbal_position(drone))

    # Arm and takeoff the drone
    await drone.action.arm()
    await drone.action.takeoff()

    # Set the gimbal to YAW_LOCK (= 1) mode (see docs for the difference)
    # Other valid values: YAW_FOLLOW (= 0)
    # YAW_LOCK will fix the gimbal pointing to an absolute direction,
    # whereas YAW_FOLLOW will point relative to vehicle heading.
    print("Setting gimbal mode")
    await drone.gimbal.set_mode(GimbalMode.YAW_LOCK)
    await asyncio.sleep(5)

    # Move the gimbal to point at pitch -40 degrees, yaw 30 degrees
    print("Setting pitch & yaw")
    await drone.gimbal.set_pitch_and_yaw(-40, 30)
    await asyncio.sleep(10)


    # Set the gimbal to track a region of interest (lat, lon, altitude)
    # Units are degrees and meters MSL respectively
    print("Setting RoI")
    await drone.gimbal.set_roi_location(28.452386, -13.867138, 28.5)
    await asyncio.sleep(10)

    await drone.action.land()
    await asyncio.sleep(5)



async def print_gimbal_position(drone):
    # Report gimbal position updates asynchronously
    # Note that we are getting gimbal position updates in
    # euler angles; we can also get them as quaternions
    async for position in drone.telemetry.camera_attitude_euler():
        print(position)


if __name__ == "__main__":
    # Start the main function
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
