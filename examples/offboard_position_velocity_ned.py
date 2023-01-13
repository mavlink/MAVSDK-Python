#!/usr/bin/env python3

import asyncio

from mavsdk import System
from mavsdk.offboard import (PositionNedYaw, VelocityNedYaw, OffboardError)

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

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return


    async def print_z_velocity(drone):
        async for odom in drone.telemetry.position_velocity_ned():
            print(f"{odom.velocity.north_m_s} {odom.velocity.down_m_s}")

    asyncio.ensure_future(print_z_velocity(drone))

    print("-- Go 0m North, 0m East, -10m Down within local coordinate system")
    #await drone.offboard.set_position_velocity_ned(PositionNedYaw(0.0, 0.0, -10.0, 0.0),VelocityNedYaw(0.0,0.0,-1.0,0.0))
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -10.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 10m North, 0m East, 0m Down within local coordinate system")
    await drone.offboard.set_position_ned(PositionNedYaw(50.0, 0.0, -10.0, 0.0))
    #await drone.offboard.set_position_velocity_ned(PositionNedYaw(50.0, 0.0, -10.0, 0.0),VelocityNedYaw(1.0,0.0,0.0,0.0))
    await asyncio.sleep(20)

    await drone.action.land()


    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
