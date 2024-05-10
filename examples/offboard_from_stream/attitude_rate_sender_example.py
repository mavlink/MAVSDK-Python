"""
MAVSDK Offboard Control - Attitude Rate Control Sender
======================================================

This script provides an interface for controlling a drone's attitude rates (roll, pitch, yaw rates) and thrust
through keyboard inputs, utilizing MAVSDK over UDP. It features an interactive GUI built with Pygame
for real-time control and feedback, enabling dynamic adjustment of the drone's flight parameters.

Overview:
---------
- Sends control packets to command drone attitude rates and thrust in local body coordinates.
- Offers two modes of operation: 'Instant Reset' and 'Incremental Control', toggled by pressing 'M'.
- Provides a graphical interface to visualize and control the drone's attitude rates and thrust.

Setup Requirements:
-------------------
- A MAVSDK-compatible drone or a SITL setup running and accessible on the network.
- The receiver node (`receiver.py`) must be operational to handle and execute the commands sent from this script.
- Ensure that the receiver and this sender script are configured to communicate over the specified IP and port.

Key Functionalities:
--------------------
- **Attitude Rate Control**: Use W, S, A, D for adjusting pitch and roll rates.
   - W: Decrease pitch rate (nose down)
   - S: Increase pitch rate (nose up)
   - A: Decrease roll rate (left down)
   - D: Increase roll rate (right down)
- **Thrust Adjustment**: Up and Down arrow keys adjust thrust.
- **Yaw Rate Control**: Left and Right arrow keys adjust yaw rate.
- **Mode Switching**: Press 'M' to toggle between 'Instant Reset' and 'Incremental Control' modes.
- **Control Enable/Disable**: 'E' to enable sending commands, 'C' to cancel and send a stop command.
- **Emergency Hold**: Press 'H' to immediately hold the current attitude rates and thrust, effectively stopping any adjustments.
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
-------
- Alireza Ghaderi
- GitHub: alireza787b
- Date: May 2024

Dependencies:
-------------
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
ROLL_PITCH_RATE_STEP = 2.0  # degrees per second step for roll and pitch rate
YAW_RATE_STEP = 5.0  # degrees per second step for yaw rate
THRUST_STEP = 0.02  # thrust step
INCREMENTAL_MODE = False  # False for instant reset, True for incremental control

# Initialize Pygame and set up the display
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('MAVSDK Offboard Control - Attitude Rate Control')

# Colors, fonts, and initial settings
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 24)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Setup UDP socket for sending commands
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send_attitude_rate(roll_rate, pitch_rate, yaw_rate, thrust):
    """Send an attitude rate command to the drone."""
    packet = ControlPacket(
        mode=SetpointMode.ATTITUDE_RATE_CONTROL,
        enable_flag=True,
        yaw_control_flag=True,
        position=(0, 0, 0),  # Not used in attitude rate mode
        velocity=(0, 0, 0),  # Not used in attitude rate mode
        acceleration=(0, 0, 0),  # Not used in attitude rate mode
        attitude=(0, 0, 0, thrust),  # Thrust only
        attitude_rate=(roll_rate, pitch_rate, yaw_rate)
    )
    packed_data = packet.pack()
    sock.sendto(packed_data, (UDP_IP, UDP_PORT))

def display_text(message, position, font=FONT, color=TEXT_COLOR):
    """Displays text on the Pygame screen at the given position."""
    text = font.render(message, True, color)
    screen.blit(text, position)

class Button:
    """Button class to create interactive GUI buttons."""
    def __init__(self, text, position, size, action, release_action=None):
        self.text = text
        self.position = position
        self.size = size
        self.action = action
        self.release_action = release_action
        self.color = (100, 100, 100)
        self.active = False

    def draw(self, screen):
        color = (150, 150, 150) if self.active else self.color
        pygame.draw.rect(screen, color, (*self.position, *self.size))
        text_surface = SMALL_FONT.render(self.text, True, TEXT_COLOR)
        text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] // 2, self.position[1] + self.size[1] // 2))
        screen.blit(text_surface, text_rect)

    def click(self):
        self.active = True
        self.action()

    def release(self):
        self.active = False
        if self.release_action:
            self.release_action()

    def is_clicked(self, mouse_pos):
        x, y = mouse_pos
        return (self.position[0] <= x <= self.position[0] + self.size[0]) and (self.position[1] <= y <= self.position[1] + self.size[1])

# Movement control variables
roll_rate, pitch_rate, yaw_rate, thrust = 0, 0, 0, 0.5  # Start with a neutral thrust value
enabled = False

# Button actions
def enable_control():
    global enabled
    enabled = True

def disable_control():
    global enabled
    enabled = False
    send_attitude_rate(0, 0, 0, 0)

def reset_control():
    global roll_rate, pitch_rate, yaw_rate, thrust
    roll_rate, pitch_rate, yaw_rate, thrust = 0, 0, 0, 0.5  # Reset to neutral thrust

def adjust_pitch_rate_up():
    global pitch_rate
    pitch_rate += ROLL_PITCH_RATE_STEP if INCREMENTAL_MODE else ROLL_PITCH_RATE_STEP

def adjust_pitch_rate_down():
    global pitch_rate
    pitch_rate -= ROLL_PITCH_RATE_STEP if INCREMENTAL_MODE else ROLL_PITCH_RATE_STEP

def adjust_roll_rate_left():
    global roll_rate
    roll_rate -= ROLL_PITCH_RATE_STEP if INCREMENTAL_MODE else ROLL_PITCH_RATE_STEP

def adjust_roll_rate_right():
    global roll_rate
    roll_rate += ROLL_PITCH_RATE_STEP if INCREMENTAL_MODE else ROLL_PITCH_RATE_STEP

def increase_thrust():
    global thrust
    thrust = min(thrust + THRUST_STEP, 1.0)  # Ensure thrust does not exceed 1

def decrease_thrust():
    global thrust
    thrust = max(thrust - THRUST_STEP, 0)  # Ensure thrust does not go below 0

def yaw_rate_left():
    global yaw_rate
    yaw_rate -= YAW_RATE_STEP if not INCREMENTAL_MODE else (yaw_rate - YAW_RATE_STEP)

def yaw_rate_right():
    global yaw_rate
    yaw_rate += YAW_RATE_STEP if not INCREMENTAL_MODE else (yaw_rate + YAW_RATE_STEP)

def toggle_mode():
    global INCREMENTAL_MODE
    INCREMENTAL_MODE = not INCREMENTAL_MODE

# Reset functions for instant return mode
def reset_roll_rate():
    global roll_rate
    roll_rate = 0

def reset_pitch_rate():
    global pitch_rate
    pitch_rate = 0

def reset_thrust():
    # global thrust
    # thrust = 0.5  # Reset to mid thrust
    pass

def reset_yaw_rate():
    global yaw_rate
    yaw_rate = 0

# Button actions
def check_enabled(action):
    """Decorator-like function to execute the action only if controls are enabled."""
    def wrapper():
        if enabled:
            action()
    return wrapper

# Wrapper function to reset only if incremental mode is not active
def check_and_reset(action):
    """Decorator-like function to reset only if incremental mode is not active."""
    def wrapper():
        if not INCREMENTAL_MODE:
            action()
    return wrapper

# Button initialization with joystick-style layout
buttons = [
    Button('Enable', (50, 150), (100, 50), enable_control),
    Button('Disable', (50, 220), (100, 50), disable_control),
    Button('Hold', (50, 290), (100, 50), reset_control),
    Button('Mode', (50, 360), (100, 50), toggle_mode),  # Mode toggle button
    Button('Pitch Up', (600, 290), (100, 50), check_enabled(adjust_pitch_rate_up), check_and_reset(reset_pitch_rate)),
    Button('Pitch Down', (600, 150), (100, 50), check_enabled(adjust_pitch_rate_down), check_and_reset(reset_pitch_rate)),
    Button('Roll Left', (500, 220), (100, 50), check_enabled(adjust_roll_rate_left), check_and_reset(reset_roll_rate)),
    Button('Roll Right', (700, 220), (100, 50), check_enabled(adjust_roll_rate_right), check_and_reset(reset_roll_rate)),
    Button('Increase Thrust', (275, 150), (150, 50), check_enabled(increase_thrust), check_and_reset(reset_thrust)),
    Button('Decrease Thrust', (275, 290), (150, 50), check_enabled(decrease_thrust), check_and_reset(reset_thrust)),
    Button('Yaw Left', (200, 220), (100, 50), check_enabled(yaw_rate_left), check_and_reset(reset_yaw_rate)),
    Button('Yaw Right', (375, 220), (100, 50), check_enabled(yaw_rate_right), check_and_reset(reset_yaw_rate))
]

def main():
    """Main function to handle keyboard and mouse inputs for drone attitude rate control."""
    global INCREMENTAL_MODE, roll_rate, pitch_rate, yaw_rate, thrust
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        display_text("MAVSDK Offboard Control: Attitude Rate Control", (50, 20), font=FONT)
        display_text("Press 'E' to enable, 'C' to cancel, 'M' to toggle mode, 'H' to hold, 'Q' to quit", (50, 50), font=SMALL_FONT)
        mode_text = "Incremental" if INCREMENTAL_MODE else "Instant Reset"
        display_text(f"Mode: {mode_text}", (50, 80), font=SMALL_FONT)
        if enabled:
            display_text("Status: Enabled", (50, 100), font=SMALL_FONT, color=GREEN)
        else:
            display_text("Status: Disabled", (50, 100), font=SMALL_FONT, color=RED)
        display_text(f"Current Command: Roll Rate={roll_rate:.2f}, Pitch Rate={pitch_rate:.2f}, Yaw Rate={yaw_rate:.2f}, Thrust={thrust:.2f}", (50, 500), font=SMALL_FONT)
        display_text(f"IP: {UDP_IP}, Port: {UDP_PORT}, Rate: {SEND_RATE}s", (50, 550), font=SMALL_FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    send_attitude_rate(0, 0, 0, 0)  # Safety stop
                    running = False
                elif event.key == pygame.K_e:
                    enable_control()
                elif event.key == pygame.K_c:
                    disable_control()
                elif event.key == pygame.K_m:
                    toggle_mode()
                elif event.key == pygame.K_h:
                    reset_control()

                if enabled:
                    if event.key == pygame.K_w:
                        adjust_pitch_rate_up()
                    elif event.key == pygame.K_s:
                        adjust_pitch_rate_down()
                    elif event.key == pygame.K_a:
                        adjust_roll_rate_left()
                    elif event.key == pygame.K_d:
                        adjust_roll_rate_right()
                    elif event.key == pygame.K_UP:
                        increase_thrust()
                    elif event.key == pygame.K_DOWN:
                        decrease_thrust()
                    elif event.key == pygame.K_LEFT:
                        yaw_rate_left()
                    elif event.key == pygame.K_RIGHT:
                        yaw_rate_right()

            elif event.type == pygame.KEYUP:
                if not INCREMENTAL_MODE:
                    if event.key in [pygame.K_w, pygame.K_s]:
                        reset_pitch_rate()
                    elif event.key in [pygame.K_a, pygame.K_d]:
                        reset_roll_rate()
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                        reset_thrust()
                    elif event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        reset_yaw_rate()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in buttons:
                    if button.is_clicked(mouse_pos):
                        button.click()

            elif event.type == pygame.MOUSEBUTTONUP:
                for button in buttons:
                    button.release()

        if enabled:
            send_attitude_rate(roll_rate, pitch_rate, yaw_rate, thrust)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()
        clock.tick(1 / SEND_RATE)

    sock.close()
    pygame.quit()

if __name__ == "__main__":
    main()
