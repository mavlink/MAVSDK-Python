#!/usr/bin/env python3

import asyncio
from mavsdk import Point, Polygon, System


async def run():

    drone = System(mavsdk_server_address="127.0.0.1")
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state.uuid}")
            break

    lat = 47.3977508
    lon = 8.5456074
    p1 = Point(lat - 0.0001, lon - 0.0001)
    p2 = Point(lat + 0.0001, lon - 0.0001)
    p3 = Point(lat + 0.0001, lon + 0.0001)
    p4 = Point(lat - 0.0001, lon + 0.0001)

    polygon = Polygon([p1, p2, p3, p4], Polygon.Type.INCLUSION)

    print("Uploading geofence...")
    await drone.geofence.upload_geofence([polygon])

    print("Geofence uploaded!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())
