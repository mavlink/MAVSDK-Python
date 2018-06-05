"""
Arms the copter, sets a takeoff height and performs a takeoff
"""
import asyncio
from dronecore.aio import connect, get_event_loop


async def main(takeoff_alt):
    # Connect to a local running backend
    test = connect("127.0.0.1")

    print(f"Setting takeoff altitude to {takeoff_alt}")
    status = await test.action.set_takeoff_altitude(takeoff_alt)

    if not status:
        print("Failed to set takeoff height")
    print("Success!")

    print("Arming system")
    # Use this if you want to inspect the response incase arming failed:
    # status, response = await test.action.arm()
    status = await test.action.arm()

    if not status:
        print("Arming failed!")
        return

    print("Success! You better take cover now ;-)")

    print("Initiating takeoff")

    if not await test.action.takeoff():
        print("Could not takeoff!")

    print("System is in air.")

    print("Letting it fly for 20 seconds...")
    await asyncio.sleep(20)
    print("Landing!")
    await test.action.land()




if __name__ == "__main__":
    get_event_loop().run_until_complete(main(10))
    # get_event_loop().run_forever()

