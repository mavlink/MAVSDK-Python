#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.gimbal import GimbalMode, ControlMode

async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Start printing gimbal position updates
    print_gimbal_position_task = asyncio.ensure_future(print_gimbal_position(drone))

    print("Taking control of gimbal")
    await drone.gimbal.take_control(ControlMode.PRIMARY)

    # Set the gimbal to YAW_LOCK (= 1) mode (see docs for the difference)
    # Other valid values: YAW_FOLLOW (= 0)
    # YAW_LOCK will fix the gimbal pointing to an absolute direction,
    # whereas YAW_FOLLOW will point relative to vehicle heading.
    print("Setting gimbal mode")
    await drone.gimbal.set_mode(GimbalMode.YAW_FOLLOW)

    print("Look forward first")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(1)

    print("Look down")
    await drone.gimbal.set_pitch_and_yaw(-90, 0)
    await asyncio.sleep(2)

    print("Back to horizontal")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(2)

    print("Slowly look up")
    await drone.gimbal.set_pitch_rate_and_yaw_rate(10, 0)
    await asyncio.sleep(3)

    print("Back to horizontal")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(2)

    print("Look right")
    await drone.gimbal.set_pitch_and_yaw(0, 90)
    await asyncio.sleep(2)

    print("Look forward again")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(2)

    print("Slowly look to the left")
    await drone.gimbal.set_pitch_rate_and_yaw_rate(0, -20)
    await asyncio.sleep(3)

    print("Look forward again")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(2)

    # Set the gimbal to track a region of interest (lat, lon, altitude)
    # Units are degrees and meters MSL respectively
    print("Look at a ROI (region of interest)")
    await drone.gimbal.set_roi_location(47.39743832, 8.5463316, 488)
    await asyncio.sleep(3)

    print("Look forward again")
    await drone.gimbal.set_pitch_and_yaw(0, 0)
    await asyncio.sleep(2)

    print("Release control of gimbal again")
    await drone.gimbal.release_control()

    print_gimbal_position_task.cancel()


async def print_gimbal_position(drone):
    # Report gimbal position updates asynchronously
    # Note that we are getting gimbal position updates in
    # euler angles; we can also get them as quaternions
    async for angle in drone.telemetry.camera_attitude_euler():
        print(f"Gimbal pitch: {angle.pitch_deg}, yaw: {angle.yaw_deg}")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
