#!/usr/bin/env python3

import asyncio
import sys

from mavsdk import System


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    asyncio.ensure_future(observe_shell(drone))

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    asyncio.get_event_loop().add_reader(sys.stdin, got_stdin_data, drone)
    print("nsh> ", end='', flush=True)


async def observe_shell(drone):
    async for output in drone.shell.receive():
        print(f"\n{output} ", end='', flush=True)


def got_stdin_data(drone):
    asyncio.ensure_future(send(drone, sys.stdin.readline()))


async def send(drone, command):
    await drone.shell.send(command)


if __name__ == "__main__":
    asyncio.ensure_future(run())

    try:
        asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        pass
