#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.server_utility import StatusTextType

"""
This example shows how to use server_utility plugin to send status messages.

The messages will appear in GCS log. In order to debug messages you can use:
  - QGroundControll MAVLink Inspector
  - Wireshark (https://mavlink.io/en/guide/wireshark.html)

In this example we are changing sysid in order to show our message along the
other messages in QGroundControll interface.
"""


async def run():

    drone = System(sysid=1)
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            await drone.server_utility.send_status_text(
                StatusTextType.INFO, "Hello world!")
            break

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
