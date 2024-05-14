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
         0,                         # start seq at 0
         3,                         # MAV_FRAME command. 3 is WGS84 + relative altitude
         16,                        # command. 16 is a basic waypoint
         1,                         # first one is current
         1,                         # auto-continue. 1: True, 0: False
         0,                         # param1 - hold time
         10,                        # param2 - Acceptance radius (if the sphere with this radius is hit, the waypoint counts as reached)
         0,                         # param3 - 0 means it should pass through the waypoint normally
         float('nan'),              # param4 - Desired yaw angle at waypoint. NaN to use the current system yaw heading mode
         int(47.40271757 * 10**7),  # param5 - latitude (multiplying by 10^7 due to MAV_FRAME)
         int(8.54285027 * 10**7),   # param6 - longitude
         30.0,                      # param7 - altitude
         0                          # mission_type. Specifies this item as a main command for the mission
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
