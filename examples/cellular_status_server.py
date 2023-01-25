#!/usr/bin/env python3

from mavsdk import System
from mavsdk.telemetry_server import CellularStatus
from mavsdk.telemetry_server import TelemetryServerError

import asyncio

async def run():
    drone = System(mavsdk_server_address="localhost", port=50051,sysid=245,compid=190)
    #await drone.connect('udp://:14550')

    #drone = System()
    await drone.connect('udp://:14550')

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("-- Arming")
    await drone.action.arm()

    while True:

        cellular_status = CellularStatus(1,1,1,1,1,2,1,1,2,1,1,1,1,"hi",1.0,1.0)
        print(cellular_status)
        if await drone.telemetry_server.publish_cellular_status(cellular_status) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub cellular_status 0")

        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())