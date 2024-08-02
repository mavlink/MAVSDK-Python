#!/usr/bin/env python3

# This example shows how to use the follow me plugin

import asyncio
from mavsdk import System
from mavsdk.follow_me import (Config, FollowMeError, TargetLocation)


follow_height = 8.0  # in meters
# distance between drone and target
follow_distance = 2.0  # in meters
responsiveness = 0.02
altitude_mode = Config.FollowAltitudeMode.TARGET_GPS
max_follow_vel = 10
# direction relative to the target
follow_angle_deg = 0

# This list contains fake location coordinates
# (These coordinates are obtained from mission.py example)
fake_location = [[47.398039859999997, 8.5455725400000002],
                 [47.398036222362471, 8.5450146439425509],
                 [47.397825620791885, 8.5450092830163271]]


async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    # Arming the drone
    print("-- Arming")
    await drone.action.arm()

    # Follow me Mode requires some configuration to be done before starting
    # the mode
    conf = Config(follow_height, follow_distance, responsiveness,
                  altitude_mode, max_follow_vel, follow_angle_deg)
    await drone.follow_me.set_config(conf)

    print("-- Taking Off")
    await drone.action.takeoff()
    await asyncio.sleep(8)
    print("-- Starting Follow Me Mode")
    await drone.follow_me.start()
    await asyncio.sleep(8)

    # This for loop provides fake coordinates from the fake_location list for
    # the follow me mode to work.
    # In a simulator it won't make much sense though
    target = TargetLocation(0, 0, 0, 0, 0, 0)
    for latitude, longitude in fake_location:
        target.latitude_deg = latitude
        target.longitude_deg = longitude
        target.absolute_altitude_m = 480.0
        target.velocity_x_m_s = 0
        target.velocity_y_m_s = 0
        target.velocity_z_m_s = 0
        print("-- Following Target")
        await drone.follow_me.set_target_location(target)
        await asyncio.sleep(2)

    # Stopping the follow me mode
    print("-- Stopping Follow Me Mode")
    await drone.follow_me.stop()
    await asyncio.sleep(5)

    print("-- Landing")
    await drone.action.land()

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
