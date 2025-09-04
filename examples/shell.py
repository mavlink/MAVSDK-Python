#!/usr/bin/env python3

import asyncio
import sys

from mavsdk import System

send_tasks = set()


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    tasks = {asyncio.create_task(observe_shell(drone))}

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    asyncio.get_event_loop().add_reader(sys.stdin, got_stdin_data, drone)
    print("nsh> ", end="", flush=True)


async def observe_shell(drone):
    async for output in drone.shell.receive():
        print(f"\n{output} ", end="", flush=True)


def got_stdin_data(drone):
    send_tasks.add(asyncio.create_task(send(drone, sys.stdin.readline())))


async def send(drone, command):
    await drone.shell.send(command)


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        pass
