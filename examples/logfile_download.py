#!/usr/bin/env python3

import asyncio
from mavsdk import System
import sys


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    entries = await get_entries(drone)
    for entry in entries:
        await download_log(drone, entry)


async def download_log(drone, entry):
    date_without_colon = entry.date.replace(":", "-")
    filename = f"./log-{date_without_colon}.ulog"
    print(f"Downloading: log {entry.id} from {entry.date} to {filename}")
    previous_progress = -1
    async for progress in drone.log_files.download_log_file(entry, filename):
        new_progress = round(progress.progress*100)
        if new_progress != previous_progress:
            sys.stdout.write(f"\r{new_progress} %")
            sys.stdout.flush()
            previous_progress = new_progress
    print()


async def get_entries(drone):
    entries = await drone.log_files.get_entries()
    for entry in entries:
        print(f"Log {entry.id} from {entry.date}")
    return entries


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
