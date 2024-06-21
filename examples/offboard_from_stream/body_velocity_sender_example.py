"""
MAVSDK Offboard Control - Local Velocity Sender
=================================================

This script provides an interface for controlling a drone's velocity and yaw through keyboard inputs,
utilizing MAVSDK over UDP. It features an interactive GUI built with Pygame for real-time control and feedback,
enabling dynamic adjustment of the drone's flight parameters.

Overview:
---------
- Sends control packets to command drone movements in local body coordinates with optional yaw adjustments.
- Offers two modes of operation: 'Instant Reset' and 'Incremental Control', toggled by pressing 'M'.
- Provides a graphical interface to visualize and control the drone's movement and yaw.
- Includes on-screen joystick-like buttons that simulate keyboard commands via mouse clicks.

Setup Requirements:
-------------------
- A MAVSDK-compatible drone or a SITL setup running and accessible on the network.
- The receiver node (`receiver.py`) must be operational to handle and execute the commands sent from this script.
- Ensure that the receiver and this sender script are configured to communicate over the specified IP and port.

Features:
---------
- **Velocity Control**: Use W, A, S, D for forward, backward, left, and right movements respectively, or use the joystick-like buttons on the GUI.
- **Altitude Adjustment**: Use Up and Down arrow keys or GUI buttons to control altitude, with up increasing and down decreasing it.
- **Yaw Control**: Left and Right arrow keys adjust yaw, or use the corresponding GUI buttons.
- **Mode Switching**: Press 'M' to toggle between 'Instant Reset' and 'Incremental Control' modes.
- **Control Enable/Disable**: 'E' to enable sending commands, 'C' to cancel and send a stop command. These controls are also available via GUI buttons.
- **Emergency Hold**: Press 'H' to immediately stop all movements, with a corresponding GUI button for this action.
- **Application Exit**: Press 'Q' to safely exit the application, ensuring all movements are halted.

Usage Instructions:
-------------------
1. Ensure your MAVSDK setup (either SITL or a real drone) is operational and that `receiver.py` is running.
2. Start this script in a Python environment where Pygame is installed. The script's GUI will display on your screen.
3. Use the keyboard controls or the on-screen joystick buttons to command the drone. Ensure you start command transmission by pressing 'E' or using the 'Enable' button.

Safety Notice:
--------------
- When operating with a real drone, ensure you are in a safe, open environment to avoid any accidents.
- Always be prepared to take manual control of the drone if necessary.

Developer:
- Alireza Ghaderi
- GitHub: alireza787b
- Date: April 2024

Dependencies:
- Pygame for GUI operations.
- MAVSDK
- PX4
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
DEFAULT_SPEED = 1.0  # meters per second
YAW_RATE_STEP = 5.0  # degrees per step
INCREMENTAL_MODE = False  # False for instant reset, True for incremental control

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
        attitude_rate=(0, 0, yaw_rate)
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
velocity_x, velocity_y, velocity_z, yaw_rate = 0, 0, 0, 0
enabled = False

# Button actions
def enable_control():
    global enabled
    enabled = True

def disable_control():
    global enabled
    enabled = False
    send_velocity_body(0, 0, 0, 0)

def reset_control():
    global velocity_x, velocity_y, velocity_z, yaw_rate
    velocity_x, velocity_y, velocity_z, yaw_rate = 0, 0, 0, 0

def move_forward():
    global velocity_x
    velocity_x = velocity_x + DEFAULT_SPEED if INCREMENTAL_MODE else DEFAULT_SPEED

def move_backward():
    global velocity_x
    velocity_x = velocity_x - DEFAULT_SPEED if INCREMENTAL_MODE else -DEFAULT_SPEED

def move_left():
    global velocity_y
    velocity_y = velocity_y - DEFAULT_SPEED if INCREMENTAL_MODE else -DEFAULT_SPEED

def move_right():
    global velocity_y
    velocity_y = velocity_y + DEFAULT_SPEED if INCREMENTAL_MODE else DEFAULT_SPEED

def ascend():
    global velocity_z
    velocity_z = velocity_z - DEFAULT_SPEED if INCREMENTAL_MODE else -DEFAULT_SPEED

def descend():
    global velocity_z
    velocity_z = velocity_z + DEFAULT_SPEED if INCREMENTAL_MODE else DEFAULT_SPEED

def yaw_left():
    global yaw_rate
    yaw_rate = -YAW_RATE_STEP if not INCREMENTAL_MODE else (yaw_rate - YAW_RATE_STEP)

def yaw_right():
    global yaw_rate
    yaw_rate = YAW_RATE_STEP if not INCREMENTAL_MODE else (yaw_rate + YAW_RATE_STEP)

def toggle_mode():
    global INCREMENTAL_MODE
    INCREMENTAL_MODE = not INCREMENTAL_MODE

# Reset movement functions for instant return mode
def reset_velocity_x():
    global velocity_x
    velocity_x = 0

def reset_velocity_y():
    global velocity_y
    velocity_y = 0

def reset_velocity_z():
    global velocity_z
    velocity_z = 0

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

# Button initialization with updated joystick-style layout
buttons = [
    Button('Enable', (50, 150), (100, 50), enable_control),
    Button('Disable', (50, 220), (100, 50), disable_control),
    Button('Hold', (50, 290), (100, 50), reset_control),
    Button('Mode', (50, 360), (100, 50), toggle_mode),  # Mode toggle button
    Button('Forward', (600, 150), (100, 50), check_enabled(move_forward), check_and_reset(reset_velocity_x)),
    Button('Backward', (600, 290), (100, 50), check_enabled(move_backward), check_and_reset(reset_velocity_x)),
    Button('Left', (500, 220), (100, 50), check_enabled(move_left), check_and_reset(reset_velocity_y)),
    Button('Right', (700, 220), (100, 50), check_enabled(move_right), check_and_reset(reset_velocity_y)),
    Button('Ascend', (275, 150), (100, 50), check_enabled(ascend), check_and_reset(reset_velocity_z)),
    Button('Descend', (275, 290), (100, 50), check_enabled(descend), check_and_reset(reset_velocity_z)),
    Button('Yaw Left', (175, 220), (100, 50), check_enabled(yaw_left), check_and_reset(reset_yaw_rate)),
    Button('Yaw Right', (375, 220), (100, 50), check_enabled(yaw_right), check_and_reset(reset_yaw_rate))
]

def main():
    """Main function to handle keyboard and mouse inputs for drone control."""
    global INCREMENTAL_MODE, velocity_x, velocity_y, velocity_z, yaw_rate
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BACKGROUND_COLOR)
        display_text("MAVSDK Offboard Control: Local Velocity Sender", (50, 20), font=FONT)
        display_text("Press 'E' to enable, 'C' to cancel, 'M' to toggle mode, 'H' to hold, 'Q' to quit", (50, 50), font=SMALL_FONT)
        mode_text = "Incremental" if INCREMENTAL_MODE else "Instant Reset"
        display_text(f"Mode: {mode_text}", (50, 80), font=SMALL_FONT)
        if enabled:
            display_text("Status: Enabled", (50, 100), font=SMALL_FONT, color=GREEN)
        else:
            display_text("Status: Disabled", (50, 100), font=SMALL_FONT, color=RED)
        display_text(f"Current Command: Vx={velocity_x:.2f}, Vy={velocity_y:.2f}, Vz={velocity_z:.2f}, Yaw Rate={yaw_rate:.2f}", (50, 500), font=SMALL_FONT)
        display_text(f"IP: {UDP_IP}, Port: {UDP_PORT}, Rate: {SEND_RATE}s", (50, 550), font=SMALL_FONT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    send_velocity_body(0, 0, 0, 0)  # Safety stop
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
                        move_forward()
                    elif event.key == pygame.K_s:
                        move_backward()
                    elif event.key == pygame.K_a:
                        move_left()
                    elif event.key == pygame.K_d:
                        move_right()
                    elif event.key == pygame.K_UP:
                        ascend()
                    elif event.key == pygame.K_DOWN:
                        descend()
                    elif event.key == pygame.K_LEFT:
                        yaw_left()
                    elif event.key == pygame.K_RIGHT:
                        yaw_right()

            elif event.type == pygame.KEYUP:
                if not INCREMENTAL_MODE:
                    if event.key in [pygame.K_w, pygame.K_s]:
                        reset_velocity_x()
                    elif event.key in [pygame.K_a, pygame.K_d]:
                        reset_velocity_y()
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                        reset_velocity_z()
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
            send_velocity_body(velocity_x, velocity_y, velocity_z, yaw_rate)

        for button in buttons:
            button.draw(screen)

        pygame.display.flip()
        clock.tick(1 / SEND_RATE)

    sock.close()
    pygame.quit()

if __name__ == "__main__":
    main()
ضq

