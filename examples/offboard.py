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

from mavsdk import connect as mavsdk_connect
from mavsdk import (
    Attitude,
    OffboardError,
    PositionNEDYaw,
    VelocityBodyYawspeed,
    VelocityNEDYaw,
)

drone = mavsdk_connect(host="127.0.0.1")


async def run_offb_ctrl_velocity_ned():
    """ Does Offboard control using velocity NED co-ordinates. """

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


async def run_offb_ctrl_velocity_body():
    """ Does Offboard control using velocity body co-ordinates. """

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Turn clock-wise and climb")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, -1.0, 60.0))
    await asyncio.sleep(5)

    print("-- Turn back anti-clockwise")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, -60.0))
    await asyncio.sleep(5)

    print("-- Wait for a bit")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(2)

    print("-- Fly a circle")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(5.0, 0.0, 0.0, 30.0))
    await asyncio.sleep(15)

    print("-- Wait for a bit")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(5)

    print("-- Fly a circle sideways")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, -5.0, 0.0, 30.0))
    await asyncio.sleep(15)

    print("-- Wait for a bit")
    await drone.offboard.set_velocity_body(VelocityBodyYawspeed(0.0, 0.0, 0.0, 0.0))
    await asyncio.sleep(8)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


async def run_offb_ctrl_pos_ned():
    """ Does Offboard control using position NED co-ordinates. """

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_position_ned(PositionNEDYaw(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Go 0m North, 0m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_ned(PositionNEDYaw(0.0, 0.0, -5.0, 0.0))
    await asyncio.sleep(10)

    print("-- Go 5m North, 0m East, -5m Down within local coordinate system, turn to face East")
    await drone.offboard.set_position_ned(PositionNEDYaw(5.0, 0.0, -5.0, 90.0))
    await asyncio.sleep(10)

    print("-- Go 5m North, 10m East, -5m Down within local coordinate system")
    await drone.offboard.set_position_ned(PositionNEDYaw(5.0, 10.0, -5.0, 90.0))
    await asyncio.sleep(15)

    print("-- Go 0m North, 10m East, 0m Down within local coordinate system, turn to face South")
    await drone.offboard.set_position_ned(PositionNEDYaw(0.0, 10.0, 0.0, 180.0))
    await asyncio.sleep(10)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


async def run_offb_ctrl_attitude():
    """ Does Offboard control using attitude commands. """

    print("-- Arming")
    await drone.action.arm()

    print("-- Setting initial setpoint")
    await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.0))

    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code: {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    print("-- Roll 30 at 60% thrust")
    await drone.offboard.set_attitude(Attitude(30.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)

    print("-- Roll -30 at 60% thrust")
    await drone.offboard.set_attitude(Attitude(-30.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)


    print("-- Roll 0 at 60% thrust")
    await drone.offboard.set_attitude(Attitude(0.0, 0.0, 0.0, 0.6))
    await asyncio.sleep(2)

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Stopping offboard mode failed with error code: {error._result.result}")


loop = asyncio.get_event_loop()
loop.run_until_complete(run_offb_ctrl_velocity_ned())
