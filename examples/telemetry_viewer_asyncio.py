"""
As basic as it can get - this script just dumps some telemetry streams to the
command line! asyncio version
"""
from dronecore.aio import connect, get_event_loop


async def armed(telemetry):
    """ Armed watcher """
    async for status in telemetry.armed_watcher():
        print("ARMED: ", status)


async def in_air(telemetry):
    """ INAIR watcher """
    async for status in telemetry.in_air_watcher():
        print("IN_AIR: ", status)


async def position(telemetry):
    """ Position watcher """
    async for position in telemetry.position_watcher():
        print(position)


async def health(telemetry):
    """ Health watcher """
    async for health in telemetry.health_watcher():
        print(health)


async def battery(telemetry):
    """ Battery watcher """
    async for status in telemetry.battery_watcher():
        print(status)


async def start_tasks(loop):
    """ Start the coroutines, can be a coroutine itself or a
    *normal* function
    """
    # Connect to dronecore backend
    test = connect("127.0.0.1")

    loop.create_task(armed(test.telemetry))
    loop.create_task(in_air(test.telemetry))
    loop.create_task(position(test.telemetry))
    loop.create_task(health(test.telemetry))
    loop.create_task(battery(test.telemetry))

    # Or:
    # asyncio.ensure_future(create_task(armed(test.telemetry))
    # asyncio.ensure_future(create_task(in_air(test.telemetry))
    # asyncio.ensure_future(create_task(position(test.telemetry))
    # asyncio.ensure_future(create_task(health(test.telemetry))
    # asyncio.ensure_future(create_task(battery(test.telemetry))


if __name__ == "__main__":
    loop = get_event_loop()

    # Startup all tasks
    print("Starting async tasks")

    loop.run_until_complete(start_tasks(loop))
    # This would be the standart way to start the coroutines:
    # start_tasks(loop)

    print("Start the eventloop!\nCancel with Ctrl+c")
    loop.run_forever()
