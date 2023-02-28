#!/usr/bin/env python3

# Description: This is an example made by Ascend Engineering to provide parameters uploading capability by MAVSDK-Python and using .params file. 
# Janitor in place: Farhang Naderi :)

import asyncio,time,argparse
from mavsdk import System
#param_file_name = "file.params"
parser = argparse.ArgumentParser()
parser.add_argument("param_file", help="Param file to be uploaded with .params format")
parser.add_argument("connection_type", help="The connection type, either 'udp' or 'serial' python3 upload_params_paramsync.py serial /dev/tty.usbmodem01:115200 or python3 upload_params_paramsync.py udp :14540")
parser.add_argument("port", help="The port for the connection")

args = parser.parse_args()
system_address = f"{args.connection_type}://{args.port}"
param_file_name = f"{args.param_file}"

# Open the file and read it into a list of rows

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
    # Create a mavsdk.System object to access the system.
    drone = System()

    # Connect to the drone.
    # Just leaving these here for later use in case args were not useful
    #await drone.connect(system_address="udp://:14540")
    #await drone.connect(system_address="serial:///dev/tty.usbmodem01:115200")
    #await drone.connect(system_address="serial:///dev/ttyS0:921600")    # This is for a companion comp tried with RPi
    await drone.connect(system_address=system_address)
    print("Connected to the Vehicle")
    # Create a mavsdk.Param object to access the parameters.
    param_plugin = drone.param
    # Get all of the parameters on the drone cached
    params = await param_plugin.get_all_params()
    float_params = params.float_params
    int_params = params.int_params
    custom_params = params.custom_params
    int_param_names = [p.name for p in int_params]
    float_param_names = [p.name for p in float_params]
    custom_param_names = [p.name for p in custom_params]

#Check if the vehicle is not flying and wait till it lands:
    while True:
        is_in_air = await drone.telemetry.in_air().__anext__()
        if is_in_air:
            print("The Vehicle not landed!")
            time.sleep(4)
        else:
            break
    with open(param_file_name, "r") as param_file:
        # for line in param_file: 
        print("Uploading Paramerters! Please do not arm the vehicle!")
        for line in tqdm(param_file,unit='lines'): 
            if not line.startswith("#"):
                columns = line.strip().split("\t")
                vehicle_id = columns[0]
                component_id = columns[1]
                name = columns[2]
                value = columns[3]
                type = columns[4]
                # With relying on cached params:
                if name in int_param_names:
                    await drone.param.set_param_int(name, int(value))
                elif name in float_param_names:
                    await drone.param.set_param_float(name, float(value))
                elif name in custom_param_names:
                    await drone.param.set_param_custom(name, value)

                # Theo other wey around with relying on .params file
                # if type == 6:
                #     await drone.param.set_param_int(name, int(value))
                # elif type == 9:
                #     await drone.param.set_param_float(name, float(value))
                # #elif type== custom type value here if any:
                # #   await drone.param.set_param_custom(name, value)                
    print("Params uploaded!")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(set_params())
