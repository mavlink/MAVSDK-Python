"""
MAVSDK Offboard Control - Local Velocity Sender
=================================================

This script is designed to control a drone's velocity and yaw through keyboard inputs, interfacing via MAVSDK over UDP. It offers an interactive GUI built with Pygame for real-time control and feedback.

Overview:
---------
- Sends control packets to command drone movements in local body coordinates with optional yaw adjustments.
- Utilizes keyboard inputs for dynamic control (W, A, S, D, Arrow keys).
- Real-time feedback on current command and connection status via a Pygame-based GUI.

Setup Requirements:
-------------------
- A MAVSDK-compatible drone or a SITL setup running and accessible on the network.
- The receiver node (`receiver.py`) must be operational to handle and execute the commands sent from this script.
- Ensure that the receiver and this sender script are configured to communicate over the specified IP and port.

Key Functionalities:
--------------------
- **Velocity Control**: Use W, A, S, D for movement along the body frame's axes.
- **Altitude Adjustment**: Use the Up and Down arrow keys for vertical movement adjustments.
- **Yaw Control**: Use Left and Right arrow keys to adjust yaw.
- **Enable/Disable Commands**: Toggle command sending with 'E' to enable and 'C' to cancel.
- **Emergency Stop**: 'H' to hold (stop all movements) and 'Q' to quit the application safely.


Instructions for Use:
---------------------
1. Ensure your MAVSDK setup (either SITL or a real drone) is ready and the `receiver.py` script is running.
2. Adjust parameters such as IP, port, and control rates directly in the code if necessary.
3. Run this script in a Python environment where Pygame is installed.
4. Use the keyboard controls as outlined to command the drone.

Safety Notice:
--------------
- When using with a real drone, operate in a safe, open environment to avoid accidents.
- Always be ready to take manual control or stop the drone if necessary.

Author:
- Alireza Ghaderi
- GitHub: alireza787b
- Date: April 2024

Dependencies:
- Pygame for GUI operations.
- Python's `socket` library for UDP communication.
- `control_packet.py` for formatting control commands.
"""

import socket
import pygame
import sys
from control_packet import ControlPacket, SetpointMode

# Constants for communication and control
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SEND_RATE = 0.1  # Packet send rate in seconds (10 Hz)
DEFAULT_SPEED = 1.0  # meters per second
YAW_RATE_STEP = 10.0  # degrees per step

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('MAVSDK Offboard Control - Local Velocity Sender')

# Colors, fonts, and initial settings
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup UDP socket for sending commands
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_velocity_body(velocity_x, velocity_y, velocity_z, yaw_rate):
    """Send a velocity command with optional yaw rate to the drone."""
    packet = ControlPacket(
        mode=SetpointMode.VELOCITY_BODY,
        enable_flag=True,
        yaw_control_flag=True,
        position=(0, 0, 0),
        velocity=(velocity_x, velocity_y, velocity_z),
        acceleration=(0, 0, 0),
        attitude=(0, 0, 0, 0),
        attitude_rate=(0, 0, 0, yaw_rate)
    )
    packed_data = packet.pack()
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))

def display_text(message, position, font=FONT, color=TEXT_COLOR):
    """Displays text on the Pygame screen at the given position."""
    text = font.render(message, True, color)
    screen.blit(text, position)

def main():
    """Main function to handle keyboard inputs for drone control."""
    running = True
    enabled = False
    velocity_x, velocity_y, velocity_z, yaw_rate = 0, 0, 0, 0
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        display_text("MAVSDK Offboard Control: Local Velocity Sender", (50, 20), font=FONT)
        display_text("Press 'E' to enable, 'C' to cancel, 'H' to hold, 'Q' to quit", (50, 50), font=SMALL_FONT)
        if enabled:
            display_text("Status: Enabled", (50, 100), font=SMALL_FONT, color=GREEN)
        else:
            display_text("Status: Disabled", (50, 100), font=SMALL_FONT, color=RED)
        display_text(f"Current Command: Vx={velocity_x}, Vy={velocity_y}, Vz={velocity_z}, Yaw Rate={yaw_rate}", (50, 500), font=SMALL_FONT)
        display_text(f"IP: {UDP_IP}, Port: {UDP_PORT}, Rate: {SEND_RATE}s", (50, 550), font=SMALL_FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    send_velocity_body(0, 0, 0, 0)  # Safety stop
                    running = False
                elif event.key == pygame.K_e:
                    enabled = True
                elif event.key == pygame.K_c:
                    send_velocity_body(0, 0, 0, 0)  # Safety stop
                    enabled = False
                elif event.key == pygame.K_h:
                    velocity_x, velocity_y, velocity_z, yaw_rate = 0, 0, 0, 0

                if enabled:
                    if event.key == pygame.K_w:
                        velocity_x = DEFAULT_SPEED
                    elif event.key == pygame.K_s:
                        velocity_x = -DEFAULT_SPEED
                    elif event.key == pygame.K_a:
                        velocity_y = -DEFAULT_SPEED
                    elif event.key == pygame.K_d:
                        velocity_y = DEFAULT_SPEED
                    elif event.key == pygame.K_UP:
                        velocity_z = -DEFAULT_SPEED # Default Down was Up so Reversed
                    elif event.key == pygame.K_DOWN:
                        velocity_z = DEFAULT_SPEED # Default Down was Up so Reversed
                    elif event.key == pygame.K_LEFT: 
                        yaw_rate -= YAW_RATE_STEP
                    elif event.key == pygame.K_RIGHT:
                        yaw_rate += YAW_RATE_STEP

            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_w, pygame.K_s]:
                    velocity_x = 0
                elif event.key in [pygame.K_a, pygame.K_d]:
                    velocity_y = 0
                elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                    velocity_z = 0
                elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    yaw_rate = 0

        if enabled:
            send_velocity_body(velocity_x, velocity_y, velocity_z, yaw_rate)

        pygame.display.flip()
        clock.tick(1 / SEND_RATE)

    sock.close()
    pygame.quit()

if __name__ == "__main__":
    main()
