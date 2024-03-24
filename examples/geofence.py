#!/usr/bin/env python3

import asyncio
from mavsdk import System
from mavsdk.geofence import Point, Polygon, FenceType, GeofenceData, Circle

"""
This example shows how to use the geofence plugin.

Note: The behavior when your vehicle hits the geofence is NOT configured
in this example.

FenceType:
    INCLUSION: The vehicle will not go outside the fence area.
    EXCLUSION: The vehicle will not come inside the fence area.

"""


async def run():

    # Connect to the Simulation
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for the drone to connect
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    # Fetch the home location coordinates, in order to set a boundary around
    # the home location.
    print("Fetching home location coordinates...")
    async for terrain_info in drone.telemetry.home():
        latitude = terrain_info.latitude_deg
        longitude = terrain_info.longitude_deg
        break

    await asyncio.sleep(1)

    # Define your geofence boundary
    p1 = Point(latitude - 0.0001, longitude - 0.0001)
    p2 = Point(latitude + 0.0001, longitude - 0.0001)
    p3 = Point(latitude + 0.0001, longitude + 0.0001)
    p4 = Point(latitude - 0.0001, longitude + 0.0001)

    # Create a polygon object using your points
    polygon = Polygon([p1, p2, p3, p4], FenceType.INCLUSION)

    # circle = Circle(p1, 10.0, FenceType.INCLUSION)

    # Sending the circle object is necessary in the geofence data,
    # so if you don't want to set the circular geofence, send it like this.
    circle = Circle(Point(0, 0), 0, FenceType.INCLUSION)

    geofenceData = GeofenceData([polygon], [circle])

    # Upload the geofence to your vehicle
    print("Uploading geofence...")
    await drone.geofence.upload_geofence(geofenceData)

    print("Geofence uploaded!")


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
