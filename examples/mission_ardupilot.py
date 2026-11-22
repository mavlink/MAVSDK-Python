#!/usr/bin/env python3

"""
Fly a simple waypoint mission on ArduPilot (ArduCopter) using `mission_raw`.

The high-level `mission` plugin (see `mission.py`) is written around PX4 and
does not currently produce a mission that ArduPilot accepts or can fly:

  * It fills unused parameters with NaN (e.g. on the RTL item added by
    `set_return_to_launch_after_mission(True)`, or a TAKEOFF vehicle action).
    ArduPilot rejects that with MAV_MISSION_INVALID_PARAM1, which shows up as
    `MissionError: INVALID_ARGUMENT` in `upload_mission()`.
  * ArduPilot reserves mission item 0 for the home position, so the first
    waypoint would be overwritten.
  * ArduCopter refuses to start AUTO on the ground ("Auto: Missing Takeoff
    Cmd") unless the first real item is a NAV_TAKEOFF.

This example builds the MAVLink mission items directly so all three
requirements are met. To try it with ArduCopter SITL:

    sim_vehicle.py -v ArduCopter --console --map

then, in another terminal (MAVProxy forwards to udp 14550 by default):

    python3 mission_ardupilot.py
"""

import asyncio
import math

from mavsdk_grpc import System
from mavsdk_grpc.mission_raw import MissionItem

# MAVLink constants used below (see common.xml).
MAV_FRAME_GLOBAL = 0
MAV_FRAME_MISSION = 2
MAV_FRAME_GLOBAL_RELATIVE_ALT = 3
MAV_CMD_NAV_WAYPOINT = 16
MAV_CMD_NAV_RETURN_TO_LAUNCH = 20
MAV_CMD_NAV_TAKEOFF = 22
MAV_MISSION_TYPE_MISSION = 0

MISSION_ALTITUDE_M = 20.0

# Waypoints as offsets (north, east) in metres from home, so the mission works
# wherever SITL (or the real vehicle) happens to be.
WAYPOINT_OFFSETS_M = [(30.0, 0.0), (30.0, 30.0), (0.0, 30.0)]


def offset_position(lat_deg, lon_deg, north_m, east_m):
    """Small-distance approximation, good enough for a demo mission."""
    earth_radius_m = 6378137.0
    dlat = north_m / earth_radius_m
    dlon = east_m / (earth_radius_m * math.cos(math.radians(lat_deg)))
    return lat_deg + math.degrees(dlat), lon_deg + math.degrees(dlon)


def make_item(seq, frame, command, params=(0.0, 0.0, 0.0, 0.0), lat_deg=0.0, lon_deg=0.0, z=0.0):
    # ArduPilot range-checks param1-4: use 0, not NaN, for unused parameters.
    return MissionItem(
        seq,
        frame,
        command,
        1 if seq == 0 else 0,  # current
        1,  # autocontinue
        *params,
        int(round(lat_deg * 1e7)),
        int(round(lon_deg * 1e7)),
        z,
        MAV_MISSION_TYPE_MISSION,
    )


def build_mission(home):
    items = []

    # Item 0: home position. ArduPilot overwrites this with the actual home,
    # but it has to be there so that the following items keep their index.
    items.append(
        make_item(
            len(items),
            MAV_FRAME_GLOBAL,
            MAV_CMD_NAV_WAYPOINT,
            lat_deg=home.latitude_deg,
            lon_deg=home.longitude_deg,
            z=home.absolute_altitude_m,
        )
    )

    # Item 1: takeoff, required by ArduCopter to start AUTO from the ground.
    items.append(
        make_item(
            len(items),
            MAV_FRAME_GLOBAL_RELATIVE_ALT,
            MAV_CMD_NAV_TAKEOFF,
            lat_deg=home.latitude_deg,
            lon_deg=home.longitude_deg,
            z=MISSION_ALTITUDE_M,
        )
    )

    for north_m, east_m in WAYPOINT_OFFSETS_M:
        lat, lon = offset_position(home.latitude_deg, home.longitude_deg, north_m, east_m)
        items.append(
            make_item(
                len(items),
                MAV_FRAME_GLOBAL_RELATIVE_ALT,
                MAV_CMD_NAV_WAYPOINT,
                lat_deg=lat,
                lon_deg=lon,
                z=MISSION_ALTITUDE_M,
            )
        )

    # Last item: return to launch (and land).
    items.append(make_item(len(items), MAV_FRAME_MISSION, MAV_CMD_NAV_RETURN_TO_LAUNCH))

    return items


async def run():
    drone = System()
    await drone.connect(system_address="udpin://0.0.0.0:14550")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    async for home in drone.telemetry.home():
        break

    mission_items = build_mission(home)

    print(f"-- Uploading mission ({len(mission_items)} items)")
    await drone.mission_raw.upload_mission(mission_items)

    print_mission_progress_task = asyncio.ensure_future(print_mission_progress(drone))
    running_tasks = [print_mission_progress_task]
    termination_task = asyncio.ensure_future(observe_is_in_air(drone, running_tasks))

    print("-- Arming")
    await drone.action.arm()

    print("-- Starting mission")
    await drone.mission_raw.start_mission()

    await termination_task


async def print_mission_progress(drone):
    async for mission_progress in drone.mission_raw.mission_progress():
        print(f"Mission progress: {mission_progress.current}/{mission_progress.total}")


async def observe_is_in_air(drone, running_tasks):
    """Monitors whether the drone is flying or not and
    returns after landing"""

    was_in_air = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            was_in_air = is_in_air

        if was_in_air and not is_in_air:
            for task in running_tasks:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            await asyncio.get_event_loop().shutdown_asyncgens()

            return


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
