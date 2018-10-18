import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():
    """ Arms the system, initiates a takeof and finally lands the system """
    arm_result = await drone.action.arm()
    print("-- Arm result: " + arm_result[1].action_result.result_str)
    takeoff_result = await drone.action.takeoff()
    print("-- Takeoff result: " + takeoff_result[1].action_result.result_str)

    await asyncio.sleep(5)

    land_result = await drone.action.land()
    print("-- Land result: " + land_result[1].action_result.result_str)


async def print_position():
    """ Outputs the position """
    async for position in drone.telemetry.position():
        print("Altitude:", position.relative_altitude_m)


def setup_tasks():
    # Create asyncio tasks with the default eventloop
    asyncio.create_task(print_position())
    asyncio.create_task(run())


if __name__ == "__main__":

    # Setup asyncio tasks
    setup_tasks()

    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()
