#!/usr/bin/env python3

import asyncio

from mavsdk import System
import mavsdk.mission_raw


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone discovered!")
            break

    mission_import_data = await drone.mission_raw.import_qgroundcontrol_mission("example-mission.plan")
    print(f"{len(mission_import_data.mission_items)} mission items imported")
    await drone.mission_raw.upload_mission(mission_import_data.mission_items)
    print("Mission uploaded")



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
