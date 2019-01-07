#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")

async def run():
    """ Arms the system, initiates a takeof and finally lands the system """
    arm_status = await drone.action.arm()
    print(f"-- Arm result: {arm_status}")

    # We do not need to proceed if the copter did not take off
    if not arm_status:
        return

    takeoff_result = await drone.action.takeoff()
    print(f"-- Takeoff result: {takeoff_result}")

    await asyncio.sleep(5)

    land_result = await drone.action.land()
    print(f"-- Land result: {land_result}")


async def print_altitude():
    """ Prints the altitude """

    previous_altitude = None

    async for position in drone.telemetry.position():
        altitude = round(position.relative_altitude_m)
        if altitude != previous_altitude:
            previous_altitude = altitude
            print(f"Altitude: {altitude}")


async def observe_flight_mode():
    """ Monitors the flight mode """

    previous_flight_mode = None

    async for flight_mode in drone.telemetry.flight_mode():
        if flight_mode is not previous_flight_mode:
            previous_flight_mode = flight_mode
            print(f"Flight mode: {flight_mode}")


async def observe_is_in_air():
    """ Monitors whether the drone is flying or not and
    returns after landing """

    was_in_air = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            was_in_air = is_in_air

        if was_in_air and not is_in_air:
            await asyncio.get_event_loop().shutdown_asyncgens()
            return


def setup_tasks():
    asyncio.ensure_future(print_altitude())
    asyncio.ensure_future(observe_flight_mode())
    asyncio.ensure_future(run())


if __name__ == "__main__":
    setup_tasks()
    asyncio.get_event_loop().run_until_complete(observe_is_in_air())
