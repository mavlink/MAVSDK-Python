#!/usr/bin/env python3

"""
Feed simulated external-vision position data to PX4 using MAVSDK.

This simulator-only example reads MAVSDK's ground-truth position stream, converts
it to a local NED frame, adds configurable noise and delay, and sends it to PX4
through the Mocap plugin's VISION_POSITION_ESTIMATE API. Only horizontal and
vertical position are fused because MAVSDK's ground-truth stream does not provide
independent attitude or velocity.

The script does not arm, take off, or control the vehicle. Fly it separately
with QGroundControl, RC, a mission, or another MAVSDK client.

Prerequisites:
    - A PX4 simulator that publishes ground truth
    - pip install mavsdk

Usage:
    1. Start PX4 software-in-the-loop simulation.
    2. Run: python3 vision_position_estimate.py
    3. Press Ctrl+C to stop.

DELAY_MS delays sample delivery. When testing delay compensation, configure
EKF2_EV_DELAY accordingly and reboot PX4 before running the example.

For a real system, replace the ground-truth source and local-frame conversion
with measurements from the VIO or motion-capture system. Enable velocity or yaw
fusion only when those measurements are supplied in the documented frames.

PX4 external-position documentation:
https://docs.px4.io/main/en/ros/external_position_estimation.html
"""

import asyncio
import math
import random
import time
from collections import deque

from mavsdk import System
from mavsdk.mocap import (
    AngleBody,
    Covariance,
    PositionBody,
    VisionPositionEstimate,
)

CONNECT_ADDRESS = "udpin://0.0.0.0:14540"
SEND_RATE_HZ = 30.0
NOISE_POSITION_STDDEV_M = 0.02
DELAY_MS = 0
STATUS_INTERVAL_S = 2.0
GROUND_TRUTH_TIMEOUT_S = 10.0

# EKF2_EV_CTRL: bit 0 = horizontal position, bit 1 = vertical position.
EKF2_EV_CTRL_POSITION = 3
EARTH_RADIUS_M = 6378137.0


def global_to_local_ned(latitude_deg, longitude_deg, altitude_m, origin):
    """Convert nearby WGS84 coordinates to a local tangent-plane NED frame."""
    origin_latitude_deg, origin_longitude_deg, origin_altitude_m = origin
    latitude_delta_rad = math.radians(latitude_deg - origin_latitude_deg)
    longitude_delta_rad = math.radians(longitude_deg - origin_longitude_deg)
    origin_latitude_rad = math.radians(origin_latitude_deg)

    north_m = EARTH_RADIUS_M * latitude_delta_rad
    east_m = EARTH_RADIUS_M * math.cos(origin_latitude_rad) * longitude_delta_rad
    down_m = origin_altitude_m - altitude_m
    return north_m, east_m, down_m


def add_position_noise(position):
    """Add independent Gaussian noise to a local NED position sample."""
    return tuple(axis + random.gauss(0.0, NOISE_POSITION_STDDEV_M) for axis in position)


async def wait_for_connection(drone):
    print("Waiting for PX4...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Connected")
            return


async def vision_position_feed(drone):
    """Publish noisy, optionally delayed simulator truth as vision position."""
    ground_truth_stream = drone.telemetry.ground_truth()

    try:
        first_sample = await asyncio.wait_for(
            ground_truth_stream.__anext__(), timeout=GROUND_TRUTH_TIMEOUT_S
        )
    except asyncio.TimeoutError as exc:
        raise RuntimeError(
            "No simulator ground-truth data received. Check that the selected "
            "simulator publishes ground truth through PX4."
        ) from exc

    origin = (
        first_sample.latitude_deg,
        first_sample.longitude_deg,
        first_sample.absolute_altitude_m,
    )
    delay_samples = max(0, round(DELAY_MS * SEND_RATE_HZ / 1000.0))
    delay_buffer = deque()
    nan = float("nan")
    position_variance = NOISE_POSITION_STDDEV_M**2
    pose_covariance = [0.0] * 21
    pose_covariance[0] = position_variance
    pose_covariance[6] = position_variance
    pose_covariance[11] = position_variance
    pose_covariance[15] = nan
    pose_covariance[18] = nan
    pose_covariance[20] = nan
    pose_covariance = Covariance(pose_covariance)
    unknown_attitude = AngleBody(nan, nan, nan)
    frame_count = 0
    print_interval_frames = max(1, round(SEND_RATE_HZ * STATUS_INTERVAL_S))

    print(
        f"Publishing position at {SEND_RATE_HZ:.0f} Hz "
        f"(noise={NOISE_POSITION_STDDEV_M:.3f} m, delay={DELAY_MS} ms)"
    )

    async def publish_sample(sample):
        nonlocal frame_count

        position = global_to_local_ned(
            sample.latitude_deg,
            sample.longitude_deg,
            sample.absolute_altitude_m,
            origin,
        )
        delay_buffer.append(add_position_noise(position))

        if len(delay_buffer) <= delay_samples:
            return

        north_m, east_m, down_m = delay_buffer.popleft()
        vision_position = VisionPositionEstimate(
            time_usec=0,
            position_body=PositionBody(north_m, east_m, down_m),
            angle_body=unknown_attitude,
            pose_covariance=pose_covariance,
            reset_counter=0,
        )
        await drone.mocap.set_vision_position_estimate(vision_position)
        frame_count += 1

        if frame_count % print_interval_frames == 0:
            print(f"[VISION] N={north_m:+8.2f} m  E={east_m:+8.2f} m  D={down_m:+8.2f} m")

    await publish_sample(first_sample)

    async for sample in ground_truth_stream:
        await publish_sample(sample)


async def monitor_local_position(drone):
    """Display PX4's estimated local position without claiming fusion status."""
    last_print = 0.0
    start = time.monotonic()

    async for position_velocity in drone.telemetry.position_velocity_ned():
        elapsed = time.monotonic() - start

        if elapsed - last_print < STATUS_INTERVAL_S:
            continue

        last_print = elapsed
        position = position_velocity.position
        print(
            f"[PX4 EKF] N={position.north_m:+8.2f} m  "
            f"E={position.east_m:+8.2f} m  D={position.down_m:+8.2f} m"
        )


async def monitor_local_position_health(drone):
    """Report changes in PX4 local-position validity."""
    previous_state = None

    async for health in drone.telemetry.health():
        current_state = health.is_local_position_ok

        if current_state != previous_state:
            state_text = "valid" if current_state else "not valid"
            print(f"[HEALTH] PX4 local position is {state_text}")
            previous_state = current_state


async def run():
    drone = System()
    tasks = []
    previous_ev_ctrl = None

    await drone.connect(system_address=CONNECT_ADDRESS)
    await wait_for_connection(drone)

    try:
        previous_ev_ctrl = await drone.param.get_param_int("EKF2_EV_CTRL")
        await drone.param.set_param_int("EKF2_EV_CTRL", EKF2_EV_CTRL_POSITION)
        await drone.telemetry.set_rate_ground_truth(SEND_RATE_HZ)
        print(
            f"Temporarily set EKF2_EV_CTRL={EKF2_EV_CTRL_POSITION} "
            "(external-vision horizontal and vertical position)"
        )

        tasks = [
            asyncio.create_task(vision_position_feed(drone)),
            asyncio.create_task(monitor_local_position(drone)),
            asyncio.create_task(monitor_local_position_health(drone)),
        ]
        await asyncio.gather(*tasks)

    finally:
        for task in tasks:
            task.cancel()

        if tasks:
            await asyncio.gather(*tasks, return_exceptions=True)

        if previous_ev_ctrl is not None:
            await drone.param.set_param_int("EKF2_EV_CTRL", previous_ev_ctrl)
            print(f"Restored EKF2_EV_CTRL={previous_ev_ctrl}")

        await drone.close()


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\nStopped")
    except RuntimeError as error:
        print(f"\nError: {error}")
