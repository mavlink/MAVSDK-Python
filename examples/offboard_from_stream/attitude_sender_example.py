"""
MAVSDK Offboard Control - Attitude Control Sender
=================================================

This script provides an interface for controlling a drone's attitude (roll, pitch, yaw) and thrust
through keyboard inputs, utilizing MAVSDK over UDP. It features an interactive GUI built with Pygame
for real-time control and feedback, enabling dynamic adjustment of the drone's flight parameters.

Overview:
---------
- Sends control packets to command drone attitudes and thrust in local body coordinates.
- Offers two modes of operation: 'Instant Reset' and 'Incremental Control', toggled by pressing 'M'.
- Provides a graphical interface to visualize and control the drone's orientation and thrust.

Setup Requirements:
-------------------
- A MAVSDK-compatible drone or a SITL setup running and accessible on the network.
- The receiver node (`receiver.py`) must be operational to handle and execute the commands sent from this script.
- Ensure that the receiver and this sender script are configured to communicate over the specified IP and port.

Key Functionalities:
--------------------
- **Attitude Control**: Use W, S, A, D for adjusting pitch and roll.
   - W: Decrease pitch (nose down)
   - S: Increase pitch (nose up)
   - A: Decrease roll (left down)
   - D: Increase roll (right down)
- **Thrust Adjustment**: Up and Down arrow keys adjust thrust.
- **Yaw Control**: Left and Right arrow keys adjust yaw.
- **Mode Switching**: Press 'M' to toggle between 'Instant Reset' and 'Incremental Control' modes.
- **Control Enable/Disable**: 'E' to enable sending commands, 'C' to cancel and send a stop command.
- **Emergency Hold**: Press 'H' to immediately hold the current attitude and thrust, effectively stopping any adjustments.
- **Application Exit**: Press 'Q' to safely exit the application, ensuring all movements are halted.

Usage Instructions:
-------------------
1. Ensure your MAVSDK setup (either SITL or a real drone) is operational and that `receiver.py` is running.
2. Start this script in a Python environment where Pygame is installed. The script's GUI will display on your screen.
3. Use the keyboard controls as outlined to command the drone. Ensure you start command transmission by pressing 'E' and can stop it anytime with 'H' or 'C'.

Safety Notice:
--------------
- When operating with a real drone, ensure you are in a safe, open environment to avoid any accidents.
- Always be prepared to take manual control of the drone if necessary.

Author:
- Alireza Ghaderi
- GitHub: alireza787b
- Date: April 2024

Dependencies:
- Pygame for GUI operations.
- MAVSDK for drone control interfacing.
- Python's `socket` library for UDP communication.
- `control_packet.py` for formatting control commands.

The code is designed to be clear and modifiable for different use cases, allowing adjustments to IP settings, control rates, and more directly within the script.
"""
import socket
import pygame
import sys
from control_packet import ControlPacket, SetpointMode

# Constants for communication and control
UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SEND_RATE = 0.1  # Packet send rate in seconds (10 Hz)
ROLL_PITCH_STEP = 2.0  # degrees step for roll and pitch
YAW_RATE_STEP = 5.0  # degrees step for yaw
THRUST_STEP = 0.05  # thrust step
INCREMENTAL_MODE = False  # False for instant reset, True for incremental control

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('MAVSDK Offboard Control - Attitude Control')

# Colors, fonts, and initial settings
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup UDP socket for sending commands
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_attitude(roll, pitch, yaw, thrust):
    """Send an attitude command to the drone."""
    packet = ControlPacket(
        mode=SetpointMode.ATTITUDE_CONTROL,
        enable_flag=True,
        yaw_control_flag=True,
        position=(0, 0, 0),  # Not used in attitude mode
        velocity=(0, 0, 0),  # Not used in attitude mode
        acceleration=(0, 0, 0),  # Not used in attitude mode
        attitude=(roll, pitch, yaw, thrust),
        attitude_rate=(0, 0, 0, 0)
    )
    packed_data = packet.pack()
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))

def display_text(message, position, font=FONT, color=TEXT_COLOR):
    """Displays text on the Pygame screen at the given position."""
    text = font.render(message, True, color)
    screen.blit(text, position)

def main():
    """Main function to handle keyboard inputs for drone attitude control."""
    global INCREMENTAL_MODE
    running = True
    enabled = False
    roll, pitch, yaw, thrust = 0, 0, 0, 0.5  # Start with a neutral thrust value
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        display_text("MAVSDK Offboard Control: Attitude Control", (50, 20), font=FONT)
        display_text("Press 'E' to enable, 'C' to cancel, 'M' to toggle mode, 'H' to hold, 'Q' to quit", (50, 50), font=SMALL_FONT)
        mode_text = "Incremental" if INCREMENTAL_MODE else "Instant Reset"
        display_text(f"Mode: {mode_text}", (50, 80), font=SMALL_FONT)
        if enabled:
            display_text("Status: Enabled", (50, 100), font=SMALL_FONT, color=GREEN)
        else:
            display_text("Status: Disabled", (50, 100), font=SMALL_FONT, color=RED)
        display_text(f"Current Command: Roll={roll}, Pitch={pitch}, Yaw={yaw}, Thrust={thrust}", (50, 500), font=SMALL_FONT)
        display_text(f"IP: {UDP_IP}, Port: {UDP_PORT}, Rate: {SEND_RATE}s", (50, 550), font=SMALL_FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    send_attitude(0, 0, 0, 0)  # Safety stop
                    running = False
                elif event.key == pygame.K_e:
                    enabled = True
                elif event.key == pygame.K_c:
                    send_attitude(0, 0, 0, 0)  # Safety stop
                    enabled = False
                elif event.key == pygame.K_m:
                    INCREMENTAL_MODE = not INCREMENTAL_MODE
                elif event.key == pygame.K_h:
                    roll, pitch, yaw, thrust = 0, 0, 0, 0.5  # Reset to neutral thrust

                if enabled:
                    if event.key == pygame.K_w:
                        pitch -= ROLL_PITCH_STEP if INCREMENTAL_MODE else -ROLL_PITCH_STEP
                    elif event.key == pygame.K_s:
                        pitch += ROLL_PITCH_STEP if INCREMENTAL_MODE else ROLL_PITCH_STEP
                    elif event.key == pygame.K_a:
                        roll -= ROLL_PITCH_STEP if INCREMENTAL_MODE else -ROLL_PITCH_STEP
                    elif event.key == pygame.K_d:
                        roll += ROLL_PITCH_STEP if INCREMENTAL_MODE else ROLL_PITCH_STEP
                    elif event.key == pygame.K_UP:
                        thrust = min(thrust + THRUST_STEP, 1.0)  # Ensure thrust does not exceed 1
                    elif event.key == pygame.K_DOWN:
                        thrust = max(thrust - THRUST_STEP, 0)  # Ensure thrust does not go below 0
                    elif event.key == pygame.K_LEFT:
                        yaw -= YAW_RATE_STEP if INCREMENTAL_MODE else -YAW_RATE_STEP
                    elif event.key == pygame.K_RIGHT:
                        yaw += YAW_RATE_STEP if INCREMENTAL_MODE else YAW_RATE_STEP

            elif event.type == pygame.KEYUP:
                if not INCREMENTAL_MODE:
                    if event.key in [pygame.K_w, pygame.K_s]:
                        pitch = 0
                    elif event.key in [pygame.K_a, pygame.K_d]:
                        roll = 0
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                        thrust = 0.5  # Reset to mid thrust
                    elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        yaw = 0

        if enabled:
            send_attitude(roll, pitch, yaw, thrust)

        pygame.display.flip()
        clock.tick(1 / SEND_RATE)

    sock.close()
    pygame.quit()

if __name__ == "__main__":
    main()
