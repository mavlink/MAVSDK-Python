#!/usr/bin/env pytho

import asyncio
from mavsdk import System


async def set_params(system, params, announcement):
    print(announcement)

    async for _ in system.telemetry.landed_state():
        break

    async for state in system.telemetry.landed_state():
        break

    print(f"Landed state: {state}")


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
    await set_params(drone, params_preflight, "Setting preflight parameters...")

    # Wait for 5 seconds
    await asyncio.sleep(5)

    params_gps_required = [
        ("EKF2_HGT_REF", 1),
        ("EKF2_EV_CTRL", 0),
        ("EKF2_GPS_CTRL", 7)
    ]
    await set_params(drone, params_gps_required, "Setting airborne (GPS Required) parameters...")

    # Wait for 10 seconds
    await asyncio.sleep(10)

    params_ev_required = [
        ("EKF2_HGT_REF", 3),
        ("EKF2_EV_CTRL", 15),
        ("EKF2_GPS_CTRL", 0)
    ]
    await set_params(drone, params_ev_required, "Setting airborne (EV Required) parameters...")

    # Start the tasks to print flight mode and system status
    print_mode_task = asyncio.ensure_future(print_mode(drone))
    print_status_task = asyncio.ensure_future(print_status(drone))
    running_tasks = [print_mode_task, print_status_task]

    # Wait for the tasks to complete
    await asyncio.gather(*running_tasks)

    await drone.close()

if __name__ == "__main__":
    asyncio.run(main())