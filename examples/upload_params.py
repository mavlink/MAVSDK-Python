#!/usr/bin/env python

import asyncio
import time
import argparse
from mavsdk import System
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "param_file", help="Param file to be uploaded with .params format")
    parser.add_argument(
        "connection_type", help="The connection type, either 'udp' or 'serial' python3 upload_params.py serial /dev/tty.usbmodem01:115200 or python3 upload_params.py udp :14540")
    parser.add_argument("port", help="The port for the connection")

    args = parser.parse_args()
    system_address = f"{args.connection_type}://{args.port}"
    param_file_name = f"{args.param_file}"

    with open(param_file_name) as file:
        for line in file:
            if not line.startswith("#"):
                columns = line.strip().split("\t")
                vehicle_id = columns[0]
                component_id = columns[1]
                name = columns[2]
                value = columns[3]
                type = columns[4]

    async def set_params():
        drone = System()
        await drone.connect(system_address=system_address)
        print("Connected to the Vehicle")
        param_plugin = drone.param
        params = await param_plugin.get_all_params()
        float_params = params.float_params
        int_params = params.int_params
        custom_params = params.custom_params
        int_param_names = [p.name for p in int_params]
        float_param_names = [p.name for p in float_params]
        custom_param_names = [p.name for p in custom_params]

        while True:
            async for is_in_air in drone.telemetry.in_air():
                if is_in_air:
                    print("The Vehicle not landed!")
                    time.sleep(4)
                else:
                    break

            with open(param_file_name, "r") as param_file:
                print("Uploading Parameters! Please do not arm the vehicle!")
                for line in tqdm(param_file, unit='lines'):
                    if not line.startswith("#"):
                        columns = line.strip().split("\t")
                        vehicle_id = columns[0]
                        component_id = columns[1]
                        name = columns[2]
                        value = columns[3]
                        type = columns[4]
                        if name in int_param_names:
                            await drone.param.set_param_int(name, int(value))
                        elif name in float_param_names:
                            await drone.param.set_param_float(name, float(value))
                        elif name in custom_param_names:
                            await drone.param.set_param_custom(name, value)

            print("Params uploaded!")

    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_params())


if __name__ == "__main__":
    main()