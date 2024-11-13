"""
Sender Example for Drone Control
================================

This script demonstrates sending position setpoints in North-East-Down (NED) coordinates
with optional yaw control for drone navigation. It is part of a system designed to
control drones via MAVSDK or similar systems using UDP communication.

The script continuously sends control packets to a drone, following a circular path, and
allows real-time user interaction to start, pause, or stop the transmission.

Setpoint Modes:
---------------
- POSITION_GLOBAL_LATLON: Global coordinates (latitude, longitude, altitude)
- POSITION_LOCAL_NED: Local coordinates (north, east, down)
- VELOCITY_NED: Local frame velocity (north, east, down)
- VELOCITY_BODY: Body frame velocity (forward, right, down)
- POSITION_VELOCITY_NED: Combined local position and velocity
- POSITION_VELOCITY_ACCELERATION_NED: Combined position, velocity, and acceleration
- ACCELERATION_NED: Local frame acceleration
- ATTITUDE_CONTROL: Direct control of roll, pitch, yaw, and thrust
- YAW_CONTROL: Separate flag for yaw control

Commands:
- 's' - Start sending packets
- 'p' - Pause packet sending
- 'r' - Resume packet sending
- 'q' - Quit the sender application

Author:
- Alireza Ghaderi
- GitHub: alireza787b
- April 2024

Usage:
Run the script and use the commands listed above to control the packet transmission.
Ensure the receiving end is configured to accept and decode the packets based on the
ControlPacket structure.

"""
import socket
import sys
import time
import select
from math import sin, cos, pi
from control_packet import ControlPacket, SetpointMode

# Constants defining communication parameters and motion characteristics
SEND_RATE = 0.1  # Packet send rate in seconds (10 Hz)
RADIUS = 50  # Radius in meters for circular motion
CIRCLE_SPEED = 0.1  # Speed of circular motion in radians per second

# UDP socket setup for packet transmission
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_position_ned(n, e, d, yaw, yaw_control_flag, enabled=True):
    """Creates a control packet with specified position and yaw control settings."""
    """Sends a packed control packet over UDP. Displays packet details if debugging is enabled."""
    packet =  ControlPacket(
        mode=SetpointMode.POSITION_LOCAL_NED,
        enable_flag=enabled,
        yaw_control_flag=yaw_control_flag,
        position=(n, e, d),
        velocity=(0, 0, 0),
        acceleration=(0, 0, 0),
        attitude=(0, 0, yaw, 0.5),  
        attitude_rate=(0, 0, 0)
    )
    packed_data = packet.pack()
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))

def main():
    """Main function to handle user inputs and send UDP packets with setpoints."""
    print("Sender Example: Send position setpoints in NED with optional yaw control")
    print("Type 's' to start, 'p' to pause, 'r' to resume, 'q' to quit.")
    running = False
    paused = False
    angle = 0

    while True:
        # Non-blocking input check
        ready, _, _ = select.select([sys.stdin], [], [], 0)
        if ready:
            command = sys.stdin.readline().strip().lower()
            if command == 's':
                print("Starting to send position setpoints...")
                running = True
                paused = False
            elif command == 'p':
                print("Pausing the transmission...")
                paused = True
            elif command == 'r':
                print("Resuming the transmission...")
                paused = False
            elif command == 'q':
                print("Quitting the sender...")
                break

        if running and not paused:
            north = RADIUS * cos(angle)
            east = RADIUS * sin(angle)
            down = -10
            send_position_ned(north, east, down, 0.0, True, True)
            angle += CIRCLE_SPEED * SEND_RATE
            angle %= (2 * pi)  # Ensure the angle stays within the range 0 to 2*pi

        time.sleep(SEND_RATE)

if __name__ == "__main__":
    DEBUG = True  # Enable detailed debugging output
    main()
