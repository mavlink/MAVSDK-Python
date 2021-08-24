#!/usr/bin/env python3

import asyncio  
from asyncio.tasks import sleep
from mavsdk import System
from mavsdk import telemetry
from mavsdk.mission import (MissionItem, MissionPlan)
from mavsdk.telemetry import (FlightMode)

recList=[] #to record position when in record mode.
#EDITABLE CODE STARTS HERE

async def print_Telemetry_All(drone):
    async for telemetry in drone.telemetry():
        print(f"Flight Mode: {telemetry.FlightMode}") #printing Flightmode
        print(f"Position: {telemetry.position}") #Printing position
        print(f"Battery Left: {telemetry.battery.remaining_percent}") #Printing REMAINING BATTERY 
        print(f"GPS Info: {telemetry.gps_info}")#Printing GPS info
        print(f"Mission progress: {drone.mission.mission_progress.current} / {drone.mission.mission_progress.ctotal}")
        #Printing mission progress
        await asyncio.sleep(1)

async def log(drone): #logging it all in a file.
    with open('output.txt', 'w') as f:
        async for telem in drone.telemetry():
            f.write(str(f"Flight Mode: {telemetry.FlightMode} | Position: {telem.position} | Battery Left: {telem.battery.remaining_percent} | GPS Info: {telem.gps_info} | Mission progress: {drone.mission.mission_progress.current} / {drone.mission.mission_progress.ctotal}"))
            await asyncio.sleep(1)

def getMissionPlan(copiedlist): #make a mission plan from copied recorded list
    mission_items=[] #temporary mission items list
    for itr in copiedlist: #filling in all the mission items in the list
        mission_items.append(MissionItem(itr[0],itr[1],25,10,True,float('nan'),float('nan'),
        MissionItem.CameraAction.NONE,float('nan'),float('nan'),float('nan'),float('nan')))
    return MissionPlan(mission_items) #returning with the mission plan made out of mission items

async def Record(drone): 
    global recList 
    recList.clear() #clear it before starting to record.
    async for mode in telemetry.FlightMode(): 
        if mode==9: # Manual mode
            print("Record mode triggered") 
            async for pos in drone.telemetry.position(): #append the coordinates to the list. 
                recList.append((pos.latitude_deg),(pos.longitude_deg))
                await asyncio.sleep(1)

async def PB(): #playback mode
    async for mode in telemetry.FlightMode():
        if mode==10: # Altitude Control mode
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

async def run():
    drone = System() # Init the drone
    await drone.connect(system_address="udp://:14540") # Connect the drone
    asyncio.ensure_future(print_Telemetry_All(drone)) #Print all important data
    asyncio.ensure_future(log(drone)) #Log Position and battery.

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