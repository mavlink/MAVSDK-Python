#!/usr/bin/env python3

import asyncio
from mavsdk import System, mavlink_direct
import json
import random


async def send_airspeed():
    drone = System()
    print("Waiting for drone to connect...")
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("-- Connected to drone!")
            break

    await drone.mavlink_direct.load_custom_xml("""
    <mavlink>
      <messages>
        <message id="295" name="AIRSPEED">
          <description>Airspeed information from a sensor.</description>
          <field type="uint8_t" name="id" instance="true">Sensor ID.</field>
          <field type="float" name="airspeed" units="m/s">Calibrated airspeed (CAS).</field>
          <field type="int16_t" name="temperature" units="cdegC">Temperature. INT16_MAX for value unknown/not supplied.</field>
          <field type="float" name="raw_press" units="hPa">Raw differential pressure. NaN for value unknown/not supplied.</field>
          <field type="uint8_t" name="flags" enum="AIRSPEED_SENSOR_FLAGS">Airspeed sensor flags.</field>
        </message>
      </messages>
    </mavlink>
    """)  # noqa: E501

    for i in range(20):
        print(f"Sending airspeed {i}...")
        fields = {
            "id": 0,
            "airspeed": random.random() * 10,
            "temperature": 20 * 100,
            "raw_press": 1010,
            "flags": 0,
        }

        message = mavlink_direct.MavlinkMessage(
            message_name="AIRSPEED",
            system_id=245,
            component_id=25,
            target_system_id=0,
            target_component_id=0,
            fields_json=json.dumps(fields),
        )
        await drone.mavlink_direct.send_message(message)
        await asyncio.sleep(0.1)


if __name__ == "__main__":
    asyncio.run(send_airspeed())
