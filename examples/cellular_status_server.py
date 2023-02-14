#!/usr/bin/env python3

from mavsdk import System
from mavsdk.telemetry_server import CellularStatus
from mavsdk.telemetry_server import TelemetryServerError
from mavsdk.telemetry_server import ModemInfo
from mavsdk.telemetry_server import OnboardComputerStatus
from mavsdk.telemetry_server import ComponentInfoBasic

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

        modem_info = ModemInfo(1,2,3,"modem_id","iccid","firmware","model")
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

        modem_info = ModemInfo(2,2,3,"modem_id","iccid","firmware","model")
        print(modem_info)
        if await drone.telemetry_server.publish_modem_info(modem_info) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub modem_info instance 2")

        await asyncio.sleep(1)

        comp_info = ComponentInfoBasic(1,2,"vendor_name","modem_name","software_version","hardware_version","serial_number")
        print(comp_info)
        if await drone.telemetry_server.publish_component_info_basic(comp_info) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub comp_info")


        await asyncio.sleep(1)

        a = [1,1,1]

        ocs_info = OnboardComputerStatus(1,2,3,a,a,a,a,4,a,a,5,6,a,a,a,a,a,a,a,a)

        print(ocs_info)
        if await drone.telemetry_server.publish_onboard_computer_status(ocs_info) is not TelemetryServerError:
            print("OK")
        else:
            print("mavsdk ran into error")
            return "error :("
        print("pub ocs_info")

        await asyncio.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())