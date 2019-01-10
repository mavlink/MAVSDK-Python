#!/usr/bin/env python3

import asyncio

from dronecode_sdk import connect as dronecode_sdk_connect
from dronecode_sdk import (MissionItem, MissionItems)

drone = dronecode_sdk_connect(host="127.0.0.1")


async def run():
    my_items = []
    my_items.append(MissionItem(47.398039859999997, 8.5455725400000002, 25, 10, True, 0, 0, MissionItem.CameraAction.NONE, 0))
    my_items.append(MissionItem(47.398036222362471, 8.5450146439425509, 25, 10, True, 0, 0, MissionItem.CameraAction.NONE, 0))
    my_items.append(MissionItem(47.397825620791885, 8.5450092830163271, 25, 10, True, 0, 0, MissionItem.CameraAction.NONE, 0))

    await drone.mission.set_return_to_launch_after_mission(True)

    print("-- Uploading mission")
    mission_items = MissionItems(my_items)
    await drone.mission.upload_mission(mission_items)

    print("-- Arming")
    await drone.action.arm()

    print("-- Starting mission")
    await drone.mission.start_mission()


async def print_mission_progress():
    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: {mission_progress.current_item_index}/{mission_progress.mission_count}")


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
    asyncio.ensure_future(run())
    asyncio.ensure_future(print_mission_progress())


if __name__ == "__main__":
    setup_tasks()
    asyncio.get_event_loop().run_until_complete(observe_is_in_air())
