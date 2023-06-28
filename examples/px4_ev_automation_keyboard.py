#!/usr/bin/env python

"""
This example can be used to switch between External Vision or MOCAP (EV)
fusion and GNSS data fusion in PX4 firmware (v1.14 and on) by using
keyboard inputs from the user.

The mechanism is such that it puts the flight controller to fuse both GNSS and
EV at the beginning (such that EKF2 decides which one to consume).

The user can later choose between different fusion types by keyboard later.

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

    params_gps_required = [
        ("EKF2_HGT_REF", 1),
        ("EKF2_EV_CTRL", 0),
        ("EKF2_GPS_CTRL", 7),
    ]

    params_ev_required = [
        ("EKF2_HGT_REF", 3),
        ("EKF2_EV_CTRL", 15),
        ("EKF2_GPS_CTRL", 0),
    ]

    while True:
        async for is_armed in drone.telemetry.armed():
            if not is_armed:
                break

            async for in_air in drone.telemetry.in_air():
                if not in_air:
                    break

                mode = input("Enter mode ('EV', 'GPS', or 'Multi-fusion'): ")
                if mode.lower() == "ev":
                    await set_params(
                        drone,
                        params_ev_required,
                        "Setting airborne (EV Required) parameters..."
                    )
                    break
                elif mode.lower() == "gps":
                    await set_params(
                        drone,
                        params_gps_required,
                        "Setting airborne (GPS Required) parameters..."
                    )
                    break
                elif mode.lower() == "multi-fusion":
                    await set_params(
                        drone,
                        params_preflight,
                        "Setting airborne (Multi-fusion) parameters..."
                    )
                    break
                else:
                    print("Invalid mode: 'ev', 'gps', or 'multi-fusion'.")

    await drone.telemetry.close()


if __name__ == "__main__":
    asyncio.run(main())
