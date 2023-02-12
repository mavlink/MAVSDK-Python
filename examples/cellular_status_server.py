#!/usr/bin/env python3

from mavsdk import System
from mavsdk.telemetry_server import CellularStatus
from mavsdk.telemetry_server import TelemetryServerError
from mavsdk.telemetry_server import ModemInfo

import asyncio

async def run():
    drone = System(mavsdk_server_address="localhost")

    await drone.connect(system_address="udp://localhost:14550")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    while True:
        cellular_status = CellularStatus(1,2,3,4,5,6,7,8,9.0,10,11.0,12.0,13.0,14,15,16,1,"hi")
        print(cellular_status)
        if await drone.telemetry_server.publish_cellular_status(cellular_status) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub cellular_status instance 1")

        await asyncio.sleep(1)

        modem_info = ModemInfo(1,2,3,4,"id","firmware","model")
        print(modem_info)
        if await drone.telemetry_server.publish_modem_info(modem_info) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub modem_info instance 1")

        await asyncio.sleep(1)

        cellular_status = CellularStatus(1,2,3,4,5,6,7,8,9.0,10,11.0,12.0,13.0,14,15,16,2,"hi")
        print(cellular_status)
        if await drone.telemetry_server.publish_cellular_status(cellular_status) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub cellular_status instance 2")

        await asyncio.sleep(1)

        modem_info = ModemInfo(2,2,3,4,"id","firmware","model")
        print(modem_info)
        if await drone.telemetry_server.publish_modem_info(modem_info) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub modem_info instance 2")

        await asyncio.sleep(1)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())