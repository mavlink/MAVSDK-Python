#!/usr/bin/env python3

import asyncio

from mavsdk import System
from mavsdk.failure import FailureType, FailureUnit

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    print("-- Enabling failure injection")
    await drone.param.set_param_int('SYS_FAILURE_EN', 1)

    print("-- Arming")
    await drone.action.arm()

    print("-- Taking off")
    await drone.action.takeoff()

    await asyncio.sleep(5)

    goto_lat = 0.0
    goto_lon = 0.0
    goto_alt = 0.0
    async for position in drone.telemetry.position():
        # Only need position once
        if position.latitude_deg and position.longitude_deg:
            goto_lat = position.latitude_deg
            goto_lon = position.longitude_deg
            goto_alt = position.absolute_altitude_m
            break

    print("-- Flying up")
    flying_alt = goto_alt + 20.0 # To fly drone 20m above the ground plane
    await drone.action.goto_location(goto_lat, goto_lon, flying_alt, 0)

    await asyncio.sleep(5)

    print("-- Injecting GPS failure")
    await drone.failure.inject(FailureUnit.SENSOR_GPS, FailureType.OFF, instance=0)

    print("-- Waiting 20s before exiting script...")
    await asyncio.sleep(20)

    print("-- Disabling failure injection")
    await drone.param.set_param_int('SYS_FAILURE_EN', 0)

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
