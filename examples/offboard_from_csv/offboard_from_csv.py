"""
Script: offboard_from_csv.py
Author: Alireza Ghaderi
Contact: p30planets@gmail.com
GitHub: github.com/alireza787b
Last Updated: 31 May 2023

This script controls a drone in offboard mode using a trajectory
defined in a CSV file.
It establishes a connection with the drone, reads the trajectory
data from the CSV file, and commands the drone to
follow the trajectory.
At the end of the trajectory, the drone returns to
its home position and lands.

Make sure that the drone is properly configured for offboard control
before running this script.
Adjust the time resolution in the script (timeStep = 0.1 seconds)
if needed for your application.


Prerequisites:
- MAVSDK library
(Refer to the MAVSDK documentation for installation instructions)
- Drone setup for offboard control
- Valid global position estimate for the drone

Usage:
python offboard_from_csv.py

Inputs:
- CSV file "active.csv" located in the same directory as this script.
This file contains the trajectory data. The CSV structure is as follows:
    - t: time in seconds
    - px, py, pz: position in NED (North-East-Down) coordinates
    - vx, vy, vz: velocity in NED coordinates
    - ax, ay, az: acceleration in NED coordinates
    - mode: mode code representing different stages of the drone's movement
     (see Mode Codes below for more details)
- An image "trajectory_plot.png" located in the
  directory named "trajectory_plot".
  This image provides a visual preview of the trajectory.

Outputs:
- Drone movement following the trajectory defined in the CSV file.
The drone returns to its home position to land after performing the trajectory.

Example Usage:
1. Ensure drone connection to the system and a valid global position estimate.
2. Place trajectory data in "active.csv".
3. Run the script.

Mode Codes:
0: "On the ground",
10: "Initial climbing state",
20: "Initial holding after climb",
30: "Moving to start point",
40: "Holding at start point",
50: "Moving to maneuvering start point",
60: "Holding at maneuver start point",
70: "Maneuvering (trajectory)",
80: "Holding at the end of the trajectory coordinate",
90: "Returning to home coordinate",
100: "Landing"

Additional Information:
- For a step-by-step guide on using the MAVSDK library for controlling drones,
  refer to the video tutorial provided in the GitHub repository (alireza787b).
- More sophisticated drone show projects and multiple drone simulation examples
  are available in the mavsdk_drone_show repo:
  https://github.com/alireza787b/mavsdk_drone_show

Note:
- As of May 2023, set_position_velocity_acceleration_ned is not yet available
  in the default build for the mavsdk-Python Installation with pip3.
  If you need to input acceleration, you should build MAVSDK for yourself.
"""


import asyncio
import csv
from mavsdk import System
from mavsdk.offboard import PositionNedYaw, VelocityNedYaw
from mavsdk.offboard import AccelerationNed, OffboardError
from mavsdk.telemetry import LandedState


# Find the current waypoint based on time
def get_current_waypoint(waypoints, time):
    return next((wp for wp in waypoints if time <= wp[0]), None)


async def run():
    # Define a dictionary to map mode codes to their descriptions
    mode_descriptions = {
        0: "On the ground",
        10: "Initial climbing state",
        20: "Initial holding after climb",
        30: "Moving to start point",
        40: "Holding at start point",
        50: "Moving to maneuvering start point",
        60: "Holding at maneuver start point",
        70: "Maneuvering (trajectory)",
        80: "Holding at the end of the trajectory coordinate",
        90: "Returning to home coordinate",
        100: "Landing"
    }

    # Connect to the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for the drone to connect
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    # Wait for the drone to have a global position estimate
    print("Waiting for drone to have a global position estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- Global position estimate OK")
            break

    # Arm the drone
    print("-- Arming")
    await drone.action.arm()

    # Set the```python
    # Set the initial setpoint
    print("-- Setting initial setpoint")
    startSetpoint = PositionNedYaw(0.0, 0.0, 0.0, 0.0)
    await drone.offboard.set_position_ned(startSetpoint)

    # Start offboard mode
    print("-- Starting offboard")
    try:
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Starting offboard mode failed with error code:"
              f" {error._result.result}")
        print("-- Disarming")
        await drone.action.disarm()
        return

    waypoints = []

    # Read data from the CSV file
    with open("active.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            waypoints.append((float(row["t"]),
                              float(row["px"]),
                              float(row["py"]),
                              float(row["pz"]),
                              float(row["vx"]),
                              float(row["vy"]),
                              float(row["vz"]),
                              float(row["ax"]),
                              float(row["ay"]),
                              float(row["az"]),
                              int(row["mode"])))

    print("-- Performing trajectory")
    total_duration = waypoints[-1][0]
    # Total duration is the time of the last waypoint
    t = 0  # Initialize time variable
    last_mode = 0
    while t <= total_duration:
        current_waypoint = get_current_waypoint(waypoints, t)
        if current_waypoint is None:
            # Reached the end of the trajectory
            break

        position = current_waypoint[1:4]
        velocity = current_waypoint[4:7]
        acceleration = current_waypoint[7:10]
        mode_code = current_waypoint[-1]
        if last_mode != mode_code:
            # Print the mode number and its description
            print(" Mode number: " + f"{mode_code}, "
                  f"Description: {mode_descriptions[mode_code]}")
            last_mode = mode_code
        # set_position_velocity_acceleration_ned is not yet available
        # in the default build for MAVSDK-Python Installation with pip3
        # If you need to input acceleration,
        # you should build MAVSDK for yourself.
        await drone.offboard.set_position_velocity_ned(
            PositionNedYaw(*position, current_waypoint[10]),
            VelocityNedYaw(*velocity, current_waypoint[10])
        )
        # await drone.offboard.set_position_velocity_acceleration_ned(
        #     PositionNedYaw(*position, current_waypoint[10]),
        #     VelocityNedYaw(*velocity, current_waypoint[10]),
        #     AccelerationNed(*acceleration, current_waypoint[10])
        # )

        timeStep = 0.1
        await asyncio.sleep(timeStep)  # Time resolution of 0.1 seconds
        t += timeStep

    print("-- Shape completed")

    print("-- Landing")
    await drone.action.land()

    async for state in drone.telemetry.landed_state():
        if state == LandedState.ON_GROUND:
            break

    print("-- Stopping offboard")
    try:
        await drone.offboard.stop()
    except Exception as error:
        print(f"Stopping offboard mode failed with error: {error}")

    print("-- Disarming")
    await drone.action.disarm()

if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
