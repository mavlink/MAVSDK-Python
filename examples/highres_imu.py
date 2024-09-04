import asyncio
from mavsdk import System


async def get_imu_data():
    # Connect to the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    # Wait for the drone to connect
    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone is connected!")
            break

    telemetry = drone.telemetry

    # Set the rate at which IMU data is updated (in Hz)
    await telemetry.set_rate_imu(200.0)

    # Fetch and print IMU data
    print("Fetching IMU data...")
    async for imu in telemetry.imu():
        # Print data in HIGHRES_IMU format
        print(f"HIGHRES_IMU (105)")
        print(f"Time (us): {imu.timestamp_us}")
        print(f"X Acceleration (m/s^2): {imu.acceleration_frd.forward_m_s2}")
        print(f"Y Acceleration (m/s^2): {imu.acceleration_frd.right_m_s2}")
        print(f"Z Acceleration (m/s^2): {imu.acceleration_frd.down_m_s2}")
        print(f"X Gyro (rad/s): {imu.angular_velocity_frd.forward_rad_s}")
        print(f"Y Gyro (rad/s): {imu.angular_velocity_frd.right_rad_s}")
        print(f"Z Gyro (rad/s): {imu.angular_velocity_frd.down_rad_s}")
        print(f"X Mag (gauss): {imu.magnetic_field_frd.forward_gauss}")
        print(f"Y Mag (gauss): {imu.magnetic_field_frd.right_gauss}")
        print(f"Z Mag (gauss): {imu.magnetic_field_frd.down_gauss}")
        print(f"Temperature (°C): {imu.temperature_degc}")
        print("-----------------------------------------")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_imu_data())
