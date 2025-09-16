#!/usr/bin/env python3

import asyncio
from mavsdk import System
import json


async def print_messages():
    drone = System()
    print("Waiting for drone to connect...")
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    async for message in drone.mavlink_direct.message("ATTITUDE"):
        fields = json.loads(message.fields_json)

        # Format as JSON again for the reader but this time with indenting.
        fields_formatted = json.dumps(fields, indent=4)

        print(f"{message.message_name} from {message.system_id}/{message.component_id}:")
        print("----")
        print(f"{fields_formatted}")
        print("----")


if __name__ == "__main__":
    asyncio.run(print_messages())
