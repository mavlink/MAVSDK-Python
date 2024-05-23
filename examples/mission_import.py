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
            print(f"-- Connected to drone!")
            break

    out = await drone.mission_raw.import_qgroundcontrol_mission(
        "example-mission.plan")

    print(f"{len(out.mission_items)} mission items and"
          f"{len(out.rally_items)} rally items imported.")

    await drone.mission_raw.upload_mission(out.mission_items)
    await drone.mission_raw.upload_rally_points(out.rally_items)

    print("Mission uploaded")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
