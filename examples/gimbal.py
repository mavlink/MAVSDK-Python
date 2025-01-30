#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.gimbal import GimbalMode, ControlMode, SendMode


async def get_gimbals(drone, timeout=10):
    gimbals_found = []  # List to store all gimbals found

    async def fetch_gimbals():
        # gimbal_list is a GimbalList object
        async for gimbal_list in drone.gimbal.gimbal_list():
            # gimbal_list.gimbals contains GimbalItem objects
            for gimbal in gimbal_list.gimbals:
                print(
                    f"Found Gimbal: ID={gimbal.gimbal_id}, "
                    f"Model={gimbal.model_name}, "
                    f"Vendor={gimbal.vendor_name}, "
                    f"Device ID={gimbal.gimbal_device_id}"
                )
                gimbals_found.append(gimbal)
        return

    try:
        # Apply timeout to async loop
        await asyncio.wait_for(fetch_gimbals(), timeout=timeout)
        return gimbals_found
    except asyncio.TimeoutError:
        print("Timeout: No gimbals found.")


async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    gimbals = await get_gimbals(drone)

    for gimbal in gimbals:

        # Start printing gimbal position updates
        print_gimbal_position_task = asyncio.create_task(
            print_gimbal_attitude(gimbal.gimbal_id, drone)
        )

        print("Taking control of gimbal with ID", gimbal.gimbal_id)
        await drone.gimbal.take_control(gimbal.gimbal_id, ControlMode.PRIMARY)

        print("Look forward with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(2)

        print("Look down with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, -90, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Back to horizontal with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Slowly look up with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angular_rates(
            gimbal.gimbal_id, 0, 5, 0, GimbalMode.YAW_FOLLOW, SendMode.STREAM
        )
        await asyncio.sleep(4)

        print("Back to horizontal with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Look right with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 90, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Look forward again with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Slowly look to the left with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angular_rates(
            gimbal.gimbal_id, 0, 0, -5, GimbalMode.YAW_FOLLOW, SendMode.STREAM
        )
        await asyncio.sleep(4)

        print("Look forward again with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        # Set the gimbal to track a region of interest (lat, lon, altitude)
        # Units are degrees and meters MSL respectively
        print(
            "Look at a ROI (region of interest) with gimbal ID",
            gimbal.gimbal_id)
        await drone.gimbal.set_roi_location(
            gimbal.gimbal_id, 47.39743832, 8.5463316, 488
        )
        await asyncio.sleep(4)

        print("Back to forward again with gimbal ID", gimbal.gimbal_id)
        await drone.gimbal.set_angles(
            gimbal.gimbal_id, 0, 0, 0, GimbalMode.YAW_FOLLOW, SendMode.ONCE
        )
        await asyncio.sleep(4)

        print("Release control of gimbal with ID", gimbal.gimbal_id)
        await drone.gimbal.release_control(gimbal.gimbal_id)

        print_gimbal_position_task.cancel()


async def print_gimbal_attitude(gimbal_id, drone):
    while True:
        attitude = await drone.gimbal.get_attitude(gimbal_id)
        print(
            f"Gimbal ID {gimbal_id} "
            f"pitch: {attitude.euler_angle_forward.pitch_deg}, "
            f"yaw: {attitude.euler_angle_forward.yaw_deg}")
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
