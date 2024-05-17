#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk import mission_raw


async def px4_connect_drone():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            return drone


async def run():
    drone = await px4_connect_drone()
    await run_drone(drone)


async def run_drone(drone):
    mission_items = []

    mission_items.append(mission_raw.MissionItem(
         # start seq at 0
         0,
         # MAV_FRAME command. 3 is WGS84 + relative altitude
         3,
         # command. 16 is a basic waypoint
         16,
         # first one is current
         1,
         # auto-continue. 1: True, 0: False
         1,
         # param1
         0,
         # param2 - Acceptance radius
         10,
         # param3 - 0 (pass through the waypoint normally)
         0,
         # param4 - Desired yaw angle at waypoint
         float('nan'),
         # param5 - latitude
         int(47.40271757 * 10**7),
         # param6 - longitude
         int(8.54285027 * 10**7),
         # param7 - altitude
         30.0,
         # mission_type.
         0
     ))

    mission_items.append(mission_raw.MissionItem(
        1,
        3,
        16,
        0,
        1,
        0,
        10,
        0,
        float('nan'),
        int(47.40271757 * 10**7),
        int(8.54361892 * 10**7),
        30.0,
        0
    ))

    print("-- Uploading mission")
    await drone.mission_raw.upload_mission(mission_items)
    print("-- Done")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
