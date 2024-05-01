"""
Drone Velocity and Yaw Control Sender
=====================================

This script enables real-time control of a drone's velocity and yaw using keyboard inputs.
It sends velocity setpoints in the body frame and commands for yaw adjustments, allowing
for dynamic control through familiar keyboard keys.

Key Bindings:
- 'W': Move forward
- 'S': Move backward
- 'A': Move left
- 'D': Move right
- Up Arrow: Increase altitude
- Down Arrow: Decrease altitude
- Left Arrow: Yaw left
- Right Arrow: Yaw right
- 'Q': Quit the application

The drone must be configured to receive and process these commands, typically in an offboard control mode.

Author:
- Alireza Ghaderi
- GitHub: alireza787b
- Date: April 2024
w
Usage:
Run the script in a compatible Python environment where the drone control system can
receive UDP packets. Use the keys to control the drone's movement and orientation.
"""

import socket
import sys
import select
from control_packet import ControlPacket, SetpointMode

import socket
import keyboard  # Using the keyboard library for non-blocking key reads
from control_packet import ControlPacket, SetpointMode

# Constants for communication and control
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
DEFAULT_SPEED = 1.0  # meters per second
DEFAULT_YAW_RATE = 5.0  # degrees per second, incremental

# Setup UDP socket for sending commands
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_velocity_body(velocity_x, velocity_y, velocity_z, yaw_rate=0):
    """Send a velocity command with optional yaw rate to the drone."""
    packet = ControlPacket(
        mode=SetpointMode.VELOCITY_BODY,
        enable_flag=True,
        yaw_control_flag=True,
        position=(0, 0, 0),
        velocity=(velocity_x, velocity_y, velocity_z),
        acceleration=(0, 0, 0),
        attitude=(0, 0, 0, yaw_rate),
        attitude_rate=(0, 0, 0, 0)
    )
    packed_data = packet.pack()
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))
    print(f"Sent: Velocity=({velocity_x}, {velocity_y}, {velocity_z}) Yaw={yaw_rate}")

def main():
    print("Drone Velocity and Yaw Control Sender Running...")
    print("Use W, A, S, D, Arrow keys, and H to control the drone. Press 'Q' to quit.")

    vx, vy, vz, yaw_rate = 0, 0, 0, 0

    while True:
        try:
            if keyboard.is_pressed('q'):
                print("Quitting...")
                break

            if keyboard.is_pressed('w'):
                vx = DEFAULT_SPEED
            elif keyboard.is_pressed('s'):
                vx = -DEFAULT_SPEED
            elif keyboard.is_pressed('a'):
                vy = -DEFAULT_SPEED
            elif keyboard.is_pressed('d'):
                vy = DEFAULT_SPEED

            if keyboard.is_pressed('up'):
                vz = DEFAULT_SPEED
            elif keyboard.is_pressed('down'):
                vz = -DEFAULT_SPEED

            if keyboard.is_pressed('left'):
                yaw_rate -= DEFAULT_YAW_RATE
            elif keyboard.is_pressed('right'):
                yaw_rate += DEFAULT_YAW_RATE

            if keyboard.is_pressed('h'):
                # Hold current velocities and yaw rate
                send_velocity_body(vx, vy, vz, yaw_rate)
                continue

            send_velocity_body(vx, vy, vz, yaw_rate)

        except Exception as e:
            print(f"Error: {str(e)}")

        # Reset velocities and yaw rate after sending to simulate continuous control
        vx, vy, vz, yaw_rate = 0, 0, 0, 0

    # Ensure the drone stops moving when the script exits
    send_velocity_body(0, 0, 0, 0)
    sock.close()

if __name__ == "__main__":
    main()
