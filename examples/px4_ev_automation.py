#!/usr/bin/env python

"""
This example can be used to switch between External Vision or
MOCAP (EV) fusion and GNSS data fusion in PX4 firmware (v1.14 and later)
with time-based switching.

The mechanism is such that it puts the flight controller to fuse both GNSS and
EV at the beginning (such that EKF2 decides which one to consume).

More information:
    https://docs.px4.io/main/en/ros/external_position_estimation.html
"""

import asyncio
from mavsdk import System


async def set_params(system, params, announcement):
    print(announcement)

    async for _ in system.telemetry.landed_state():
        break

    async for state in system.telemetry.landed_state():
        break

    print(f"Landed state: {state}")


async def print_status(drone):
    async for flight_mode in drone.telemetry.flight_mode():
        print(f"Flight Mode: {flight_mode}")

    async for health in drone.telemetry.health():
        print(f"System status: {health.is_gyrometer_calibration_ok}")

    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent}%")

    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")

    async for armed in drone.telemetry.armed():
        print(f"Armed: {armed}")


async def print_mode(drone):
    async for flight_mode in drone.telemetry.flight_mode():
        print(f"Flight Mode: {flight_mode}")


async def main():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    params_preflight = [
        ("EKF2_HGT_REF", 0),
        ("EKF2_EV_CTRL", 15),
        ("EKF2_GPS_CTRL", 7)
    ]
    await set_params(drone, params_preflight, "Setting preflight params...")

    # Wait for 5 seconds
    await asyncio.sleep(5)

    params_gps_required = [
        ("EKF2_HGT_REF", 1),
        ("EKF2_EV_CTRL", 0),
        ("EKF2_GPS_CTRL", 7)
    ]
    await set_params(drone, params_gps_required, "Setting GPS params...")

    # Wait for 10 seconds
    await asyncio.sleep(10)

    params_ev_required = [
        ("EKF2_HGT_REF", 3),
        ("EKF2_EV_CTRL", 15),
        ("EKF2_GPS_CTRL", 0)
    ]
    await set_params(drone, params_ev_required, "Setting EV params...")

    # Start the tasks to print flight mode and system status
    print_mode_task = asyncio.ensure_future(print_mode(drone))
    print_status_task = asyncio.ensure_future(print_status(drone))
    running_tasks = [print_mode_task, print_status_task]

    # Wait for the tasks to complete
    await asyncio.gather(*running_tasks)

    await drone.close()


if __name__ == "__main__":
    asyncio.run(main())
