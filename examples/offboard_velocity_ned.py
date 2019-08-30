#!/usr/bin/env python3

"""
Some caveats when attempting to run the examples in non-gps environments:

- `drone.action.arm()` will return a `COMMAND_DENIED` result because the action requires switching
  to LOITER mode first, something that is currently not supported in a non-gps environment. You will
  need to temporarily disable this part here:
  `https://github.com/mavlink/MAVSDK/blob/develop/plugins/action/action_impl.cpp#L61-L65`

- `drone.offboard.stop()` will also return a `COMMAND_DENIED` result because it requires a mode
  switch to HOLD, something that is currently not supported in a non-gps environment.
"""

import asyncio

from mavsdk import Drone
from mavsdk import (OffboardError, VelocityNEDYaw)


async def run():
    """ Does Offboard control using velocity NED coordinates. """

    drone = Drone()
    await drone.connect(drone_address="udp://:14540")

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Go up 2 m/s")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, -2.0, 0.0))
    await asyncio.sleep(4)

    print("-- Go North 2 m/s, turn to face East")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(2.0, 0.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Go South 2 m/s, turn to face West")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(-2.0, 0.0, 0.0, 270.0))
    await asyncio.sleep(4)

    print("-- Go West 2 m/s, turn to face East")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, -2.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Go East 2 m/s")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 2.0, 0.0, 90.0))
    await asyncio.sleep(4)

    print("-- Turn to face South")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 0.0, 180.0))
    await asyncio.sleep(2)

    print("-- Go down 1 m/s, turn to face North")
    await drone.offboard.set_velocity_ned(VelocityNEDYaw(0.0, 0.0, 1.0, 0.0))
    await asyncio.sleep(4)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
