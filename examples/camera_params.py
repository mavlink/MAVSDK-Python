#!/usr/bin/env python3

import asyncio

from aioconsole import ainput
from mavsdk import System
from mavsdk.camera import (CameraError, Mode, Option, Setting)


usage_str = """
Usage:
  p    print current (changeable) camera settings
  m    change camera mode
  s    change a setting

"""

camera_mode = Mode.UNKNOWN
current_settings = []
possible_setting_options = []

async def run():
    drone = System()
    await drone.connect(system_address="udp://:14540")

    asyncio.ensure_future(observe_current_settings(drone))
    asyncio.ensure_future(observe_camera_mode(drone))
    asyncio.ensure_future(observe_possible_setting_options(drone))

    while(True):
        entered_input = await ainput(usage_str)

        if (entered_input == "p"):
            print(f"\n=== Current settings ===\n")
            print_current_settings()
        elif (entered_input == "m"):
            print(f"\n=== Possible modes ===\n")
            print(f"1. PHOTO")
            print(f"2. VIDEO")

            try:
                index_mode = await make_user_choose_camera_mode()
            except ValueError:
                print("Invalid index")
                continue

            if (index_mode == 1):
                chosen_mode = Mode.PHOTO
            else:
                chosen_mode = Mode.VIDEO

            print(f"Setting camera mode to {chosen_mode}!")

            try:
                await drone.camera.set_mode(chosen_mode)
                print(f" --> Succeeded")
            except CameraError as error:
                print(f" --> Failed with code: {error._result.result_str}")
        elif (entered_input == "s"):
            print(f"\n=== Possible settings ===\n")
            print_possible_settings(possible_setting_options)

            try:
                index_setting = await make_user_choose_setting(possible_setting_options)
            except ValueError:
                print("Invalid index")
                continue

            selected_setting = possible_setting_options[index_setting - 1]
            possible_options = selected_setting.options

            print(f"\n=== Available options ===")
            print(f"Setting: {selected_setting.setting_id}")
            if (not selected_setting.is_range):
                print(f"Options:")
                try:
                    print_possible_options(possible_options)
                    index_option = await make_user_choose_option(possible_options)
                    selected_option = possible_options[index_option - 1]

                    print(f"Setting {selected_setting.setting_id} to {selected_option.option_description}!")
                    setting = Setting(selected_setting.setting_id, "", selected_option, selected_setting.is_range)
                except ValueError:
                    print("Invalid index")
                    continue
            else:
                try:
                    selected_value = await make_user_choose_option_range(possible_options)

                    print(f"Setting {selected_setting.setting_id} to {selected_value}!")
                    setting = Setting(selected_setting.setting_id, "", Option(selected_value, ""), selected_setting.is_range)
                except ValueError:
                    print("Invalid value")
                    continue

            try:
                await drone.camera.set_setting(setting)
                print(f" --> Succeeded")
            except CameraError as error:
                print(f" --> Failed with code: {error._result.result_str}")
        else:
            print("Invalid input!")
            continue

async def observe_camera_mode(drone):
    global camera_mode
    async for mode in drone.camera.mode():
        camera_mode = mode

async def observe_current_settings(drone):
    global current_settings
    async for settings in drone.camera.current_settings():
        current_settings = settings

async def observe_possible_setting_options(drone):
    global possible_setting_options
    async for settings in drone.camera.possible_setting_options():
        possible_setting_options = settings

def print_current_settings():
    print(f"* CAM_MODE: {camera_mode}")
    for setting in current_settings:
        print(f"* {setting.setting_id}: {setting.setting_description}")
        if setting.is_range:
            print(f"    -> {setting.option.option_id}")
        else:
            print(f"    -> {setting.option.option_description}")

async def make_user_choose_camera_mode():
    index_mode_str = await ainput(f"\nWhich mode do you want? [1..2] >>> ")
    index_mode = int(index_mode_str)
    if (index_mode < 1 or index_mode > 2):
        raise ValueError()

    return index_mode

def print_possible_settings(possible_settings):
    i = 1
    for setting in possible_settings:
        print(f"{i}. {setting.setting_id}: {setting.setting_description}")
        i += 1

async def make_user_choose_setting(possible_settings):
    n_settings = len(possible_settings)
    index_setting_str = await ainput(f"\nWhich setting do you want to change? [1..{n_settings}] >>> ")

    index_setting = int(index_setting_str)
    if (index_setting < 1 or index_setting > n_settings):
        raise ValueError()

    return index_setting

def print_possible_options(possible_options):
    i = 1
    for possible_option in possible_options:
        print(f"{i}. {possible_option.option_description}")
        i += 1

async def make_user_choose_option(possible_options):
    n_options = len(possible_options)
    index_option_str = await ainput(f"\nWhich option do you want? [1..{n_options}] >>> ")

    index_option = int(index_option_str)
    if (index_option < 1 or index_option > n_options):
        raise ValueError()

    return index_option

async def make_user_choose_option_range(possible_options):
    min_value = float(possible_options[0].option_id)
    max_value = float(possible_options[1].option_id)

    interval_text = ""
    if len(possible_options) == 3:
        interval_value = float(possible_options[2].option_id)
        interval_text = f"interval: {interval_value}"

    value_str = await ainput(f"\nWhat value do you want? [{min_value}, {max_value}] {interval_text} >>> ")

    value = float(value_str)
    if (value < min_value or value > max_value):
        raise ValueError()

    return str(value)


if __name__ == "__main__":
    # Run the asyncio loop
    asyncio.run(run())
