#!/usr/bin/env python3

import asyncio  
from asyncio.tasks import sleep
from mavsdk import System
from mavsdk import telemetry
from mavsdk.mission import (MissionItem, MissionPlan)
from mavsdk.telemetry import (FlightMode)

logList=[] #to log all positions. 
recList=[] #to record position when in record mode.

async def run():
    # Init the drone
    drone = System()
    await drone.connect(system_address="udp://:14540")

    asyncio.ensure_future(print_battery(drone))
    asyncio.ensure_future(print_gps_info(drone))
    asyncio.ensure_future(print_in_air(drone))
    asyncio.ensure_future(print_position(drone))
    asyncio.ensure_future(log(drone))
    asyncio.ensure_future(fly(drone))

async def print_battery(drone):
    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent}")


async def print_gps_info(drone):
    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS info: {gps_info}")


async def print_in_air(drone):
    async for in_air in drone.telemetry.in_air():
        print(f"In air: {in_air}")


async def print_mission_progress(drone):
    async for mission_progress in drone.mission.mission_progress():
        print(f"Mission progress: "
              f"{mission_progress.current}/"
              f"{mission_progress.total}")

async def observe_is_in_air(drone, running_tasks):  #killer function
    """ Monitors whether the drone is flying or not and
    returns after landing """

    diditevertakeoff = False

    async for is_in_air in drone.telemetry.in_air():
        if is_in_air:
            diditevertakeoff = is_in_air

        if diditevertakeoff and not is_in_air:
            for task in running_tasks:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass
            await asyncio.get_event_loop().shutdown_asyncgens()

            return

async def fly(drone):   #main function
    print_mission_progress_task = asyncio.ensure_future(print_mission_progress(drone))
    running_tasks = [print_mission_progress_task]
    termination_task = asyncio.ensure_future(
        observe_is_in_air(drone, running_tasks))
    await termination_task

#EDITABLE CODE STARTS HERE

async def print_position(drone):
    async for position in drone.telemetry.position():
        print(position)

async def log(drone):
    global logList
    async for pos in drone.telemetry.position():
        logList.append((pos.latitude_deg),(pos.longitude_deg))
        await asyncio.sleep(0.5)

def getMissionPlan(copiedlist):
    mission_items=[]
    for itr in copiedlist:
        mission_items.append(MissionItem(itr[0],itr[1],25,10,True,float('nan'),float('nan'),
        MissionItem.CameraAction.NONE,float('nan'),float('nan'),float('nan'),float('nan')))

    return MissionPlan(mission_items)

async def Record(drone):
    global recList
    recList.clear()
    async for mode in telemetry.FlightMode():
        if mode==9:
            print("Record mode triggered")
            async for pos in drone.telemetry.position():
                recList.append((pos.latitude_deg),(pos.longitude_deg))            

async def PB():
    async for mode in telemetry.FlightMode():
        if mode==10:
            print("Playback mode triggered")
            mission_items=[]
            copy_list=recList.copy()
            mission_Plan=getMissionPlan(copy_list)
"""
    await drone.mission.set_return_to_launch_after_mission(False)

    print("-- Uploading mission")
    await drone.mission.upload_mission(mission_plan)

    print("-- Arming")
    await drone.action.arm()

    print("-- Starting mission")
    await drone.mission.start_mission()"""

async def PBL(drone): 
    global recList
    async for mode in telemetry.FlightMode():
        if mode==4:
            print("Playback Loop mode triggered")
            copy_list=recList.copy()
            loopList=recList.reverse()+recList
            mission_Plan=getMissionPlan(loopList)

#EDITABLE CODE ENDS HERE

if __name__ == "__main__":
    # Start the main function
    asyncio.ensure_future(run())


    # Runs the event loop until the program is canceled with e.g. CTRL-C
    asyncio.get_event_loop().run_forever()









"""            # NITYODAY CHANGES HERE
            for index, tuple in enumerate(copy_list):
	            lat = tuple[0]
	            long = tuple[1]
                
	            mission_items.append(MissionItem(lat,
                                     long,
                                     25,
                                     10,
                                     True,
                                     float('nan'),
                                     float('nan'),
                                     MissionItem.CameraAction.NONE,
                                     float('nan'),
                                     float('nan'),
                                     float('nan'),
                                     float('nan')))
with open('output.txt', 'r') as f:
    lines = f.read().splitlines()
    last_line = lines[-1]
    print last_line
"""