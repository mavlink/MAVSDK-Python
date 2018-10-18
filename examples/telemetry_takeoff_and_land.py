import asyncio

from dronecode_sdk.aio import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():
    """ Arms the system, initiates a takeof and finally lands the system """
    arm_status, _ = await drone.action.arm()
    print(f"-- Arm result: {arm_status}")

    # We do not need to proceed if the copter did not take off
    if not arm_status:
        return

    takeoff_result, _ = await drone.action.takeoff()
    print(f"-- Takeoff result: {takeoff_result}")

    await asyncio.sleep(5)

    land_result, _ = await drone.action.land()
    print(f"-- Land result: {land_result}")


async def print_position():
    """ Outputs the position """
    async for position in drone.telemetry.position():
        print("Altitude:", position.relative_altitude_m)


def setup_tasks():
    # Create asyncio tasks with the default eventloop
    # asyncio.create_task() is only callable when the event loop is already
    # running!!!
    asyncio.ensure_future(print_position())
    asyncio.ensure_future(run())


if __name__ == "__main__":

    # Setup asyncio tasks
    setup_tasks()

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
