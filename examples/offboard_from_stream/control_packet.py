"""
ControlPacket Module for Drone Communication
============================================

Overview:
---------
This Python module provides the ControlPacket class, which is central to creating,
packing, and unpacking control packets used for drone control operations via MAVSDK
or other compatible UAV control systems. It supports a variety of control modalities
including position, velocity, acceleration, and direct attitude control.

The control packets are designed to be transmitted over UDP, enabling real-time
control of drones with high reliability and minimal latency. The packets include
comprehensive setpoints for sophisticated flight dynamics and maneuvers.

Features:
---------
- Multiple Control Modes: Supports various modes such as POSITION_GLOBAL_LATLON,
  POSITION_LOCAL_NED, VELOCITY_NED, and ATTITUDE_CONTROL, among others.
- Yaw Control: Optional direct yaw control alongside standard setpoints, allowing
  for dynamic adjustment of the drone's orientation.
- Binary Packing: Uses Python's `struct` module for efficient binary packing and
  unpacking of control data, suitable for high-performance network transmission.
- Error Handling: Robust error handling for data integrity checks using CRC and
  structured exception management.

Setpoint Modes Enum:
--------------------
- POSITION_GLOBAL_LATLON: Global coordinates (latitude, longitude, altitude)
- POSITION_LOCAL_NED: Local coordinates (north, east, down)
- VELOCITY_NED: Local frame velocity (north, east, down)
- VELOCITY_BODY: Body frame velocity (forward, right, down)
- POSITION_VELOCITY_NED: Combined local position and velocity
- POSITION_VELOCITY_ACCELERATION_NED: Combined position, velocity, and acceleration
- ACCELERATION_NED: Local frame acceleration
- ATTITUDE_CONTROL: Direct control of roll, pitch, yaw, and thrust
- YAW_CONTROL: Separate flag for explicit yaw control

Usage:
------
Instantiate a `ControlPacket` with desired setpoints and mode flags, then use
`pack()` to serialize for transmission and `unpack()` to deserialize received packets.
Example usage is provided in the sender and receiver scripts accompanying this module.

Author:
-------
Alireza Ghaderi
GitHub: alireza787b
Date: April 2024

Example:
--------
```python
packet = ControlPacket(
    mode=SetpointMode.POSITION_VELOCITY_NED | SetpointMode.YAW_CONTROL,
    enable_flag=True,
    yaw_control_flag=True,
    position=(10.0, 20.0, -5.0), NED: North(m),East,Down(m) | Global: lat(deg),long(deg),alt(m)
    velocity=(0.5, 0.5, 0.0),
    acceleration=(0.0, 0.0, 0.0),
    attitude=(0.0, 0.0, 30.0, 0.6),  # Yaw to 30 degrees, 60% thrust
    attitude_rate=(0, 0, 0)
)
packed_data = packet.pack()
unpacked_packet = ControlPacket.unpack(packed_data)
unpacked_packet.debug_print()
"""
import struct
import zlib
import time
from enum import Enum

class SetpointMode(Enum):
    POSITION_GLOBAL_LATLON = 0x40 # Not Tested
    POSITION_LOCAL_NED = 0x20 
    VELOCITY_NED = 0x80 # Not Tested
    VELOCITY_BODY = 0x100
    POSITION_VELOCITY_NED = 0x01 # Not Tested
    POSITION_VELOCITY_ACCELERATION_NED = 0x02 # Not Tested
    ACCELERATION_NED = 0x04 # Not Tested
    ATTITUDE_CONTROL = 0x08  # Direct attitude control including thrust
    ATTITUDE_RATE_CONTROL = 0x10
    YAW_CONTROL = 0x200  # Separate flag for yaw control in position NED mode

class ControlPacket:
    HEADER = 0xDEADBEEFDEADBEEF
    HEADER_FORMAT = ">Q"  # 8 bytes for header
    DATA_FORMAT = ">QIII3d3d3d4d3d"  # Updated format to include all required fields
    CRC_FORMAT = ">I"  # 4 bytes for CRC

    def __init__(self, mode, enable_flag, yaw_control_flag, position, velocity, acceleration, attitude, attitude_rate, timestamp=None):
        self.timestamp = timestamp if timestamp is not None else int(time.time() * 1e9)
        self.setpoint_flags = mode.value
        self.enable_flag = int(enable_flag)  # Ensure enable_flag is integer
        self.yaw_control_flag = int(yaw_control_flag)  # Ensure yaw_control_flag is integer
        self.position = position #NED: North(m),East,Down(m) | Global: lat(deg),long(deg),alt(m)
        self.velocity = velocity
        self.acceleration = acceleration
        self.attitude = attitude
        self.attitude_rate = attitude_rate

    def pack(self):
        # Ensure all values are properly converted and match the expected types
        enable_flag_int = 1 if self.enable_flag else 0  # Correct conversion of boolean to integer
        yaw_control_flag_int = 1 if self.yaw_control_flag else 0  # Correct conversion of boolean to integer

        # Ensure the timestamp is an integer
        timestamp_int = int(self.timestamp)

        # Pack all data components
        try:
            payload = struct.pack(
                self.DATA_FORMAT,
                timestamp_int,
                self.setpoint_flags,
                enable_flag_int,
                yaw_control_flag_int,
                *self.position,
                *self.velocity,
                *self.acceleration,
                *self.attitude,
                *self.attitude_rate
            )
        except struct.error as e:
            print(f"Struct error: {e}")
            print(f"Data being packed: {timestamp_int}, {self.setpoint_flags}, {enable_flag_int}, {yaw_control_flag_int}, {self.position}, {self.velocity}, {self.acceleration}, {self.attitude}, {self.attitude_rate}")
            raise

        crc = zlib.crc32(payload) & 0xffffffff
        return struct.pack(self.HEADER_FORMAT, self.HEADER) + payload + struct.pack(self.CRC_FORMAT, crc)


    @staticmethod
    def unpack(packet):
        header = struct.unpack(ControlPacket.HEADER_FORMAT, packet[:8])[0]
        if header != ControlPacket.HEADER:
            raise ValueError("Invalid packet header")
        payload, crc = packet[8:-4], packet[-4:]
        data = struct.unpack(ControlPacket.DATA_FORMAT, payload)
        if crc != struct.pack(ControlPacket.CRC_FORMAT, zlib.crc32(payload) & 0xffffffff):
            raise ValueError("CRC check failed")

        timestamp, setpoint_flags, enable_flag_int, yaw_control_flag_int = data[:4]
        position = data[4:7]
        velocity = data[7:10]
        acceleration = data[10:13]
        attitude = data[13:17]
        attitude_rate = data[17:20]

        # Convert integers back to booleans
        enable_flag = bool(enable_flag_int)
        yaw_control_flag = bool(yaw_control_flag_int)

        return ControlPacket(SetpointMode(setpoint_flags), enable_flag, yaw_control_flag,
                             position, velocity, acceleration, attitude, attitude_rate, timestamp)

    def debug_print(self):
        print("Control Packet:")
        print(f"Timestamp: {self.timestamp}")
        mode_name = self.get_mode_name()
        yaw_control = "enabled" if self.yaw_control_flag else "initial yaw maintained"
        enable_mode = "enabled" if self.enable_flag else "disabled"
        print(f"Setpoint Flags: {bin(self.setpoint_flags)} ({mode_name})")
        print(f"Enable Flag: {enable_mode}")
        print(f"Yaw Control: {yaw_control}")
        print("Position: ", self.position)
        print("Velocity: ", self.velocity)
        print("Acceleration: ", self.acceleration)
        print("Attitude: ", self.attitude)
        print("Attitude Rate: ", self.attitude_rate)

    def get_mode_name(self):
        for mode in SetpointMode:
            if mode.value & self.setpoint_flags:
                return mode.name
        return "Unknown Mode"
