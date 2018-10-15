import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():

    arm_result = await drone.action.arm()
    print("Arm result: " + arm_result[1].action_result.result_str)
    takeoff_result = await drone.action.takeoff()
    print("Takeoff result: " + takeoff_result[1].action_result.result_str)

    await asyncio.sleep(5)

    land_result = await drone.action.land()
    print("Land result: " + land_result[1].action_result.result_str)


loop = asyncio.get_event_loop()
loop.run_until_complete(run())
