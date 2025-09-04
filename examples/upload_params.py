#!/usr/bin/env python

import asyncio
import argparse
import anyio
from mavsdk import System
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "connection", help="Connection string (e.g. udpin://0.0.0.0:14540)"
    )
    parser.add_argument(
        "param_file", help="Param file to be uploaded with .params format"
    )

    args = parser.parse_args()

    asyncio.run(set_params(args))


async def set_params(args):
    drone = System()
    await drone.connect(system_address=args.connection)
    print("Connected to the Vehicle")
    param_plugin = drone.param
    params = await param_plugin.get_all_params()
    float_params = params.float_params
    int_params = params.int_params
    custom_params = params.custom_params
    int_param_names = [p.name for p in int_params]
    float_param_names = [p.name for p in float_params]
    custom_param_names = [p.name for p in custom_params]

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            print("Waiting until vehicle is landed...")
        else:
            break

    async with await anyio.open_file(args.param_file, "r") as param_file:
        print("Uploading Parameters... Please do not arm the vehicle!")
        contents = await param_file.read()
        lines = contents.splitlines()
        for line in tqdm(lines, unit='lines'):
            if line.startswith("#"):
                continue

            columns = line.strip().split("\t")
            _vehicle_id = columns[0]
            _component_id = columns[1]
            name = columns[2]
            value = columns[3]
            _type = columns[4]
            if name in int_param_names:
                await drone.param.set_param_int(name, int(value))
            elif name in float_param_names:
                await drone.param.set_param_float(name, float(value))
            elif name in custom_param_names:
                await drone.param.set_param_custom(name, value)

    print("Params uploaded!")


if __name__ == "__main__":
    main()
