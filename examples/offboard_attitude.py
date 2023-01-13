#!/usr/bin/env python3

# Warning: Only try this in simulation!
#          The direct attitude interface is a low level interface to be used
#          with caution. On real vehicles the thrust values are likely not
#          adjusted properly and you need to close the loop using altitude.

import asyncio

from mavsdk import System
from mavsdk.offboard import (Attitude, OffboardError)


async def run():
    """ Does Offboard control using attitude commands. """

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
    await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: \
              {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Go up at 70% thrust")
    await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.7))
    await asyncio.sleep(2)

    print("-- Roll 30 at 60% thrust")
    await drone.offboard.set_attitude(Attitude(30.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)

    print("-- Roll -30 at 60% thrust")
    await drone.offboard.set_attitude(Attitude(-30.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)

    print("-- Hover at 60% thrust")
    await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: \
              {error._result.result}")

    await drone.action.land()


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
