#!/usr/bin/env python

from __future__ import print_function
import grpc
import time
import threading
import sys

import dronecore_core.core_pb2 as dc_core
import dronecore_core.core_pb2_grpc as dc_core_grpc
import dronecore_action.action_pb2 as dc_action
import dronecore_action.action_pb2_grpc as dc_action_grpc
import dronecore_mission.mission_pb2 as dc_mission
import dronecore_mission.mission_pb2_grpc as dc_mission_grpc

thread_status = True

def wait_func(future_status):
    global thread_status
    ret = future_status.result()
    print(ret.result_str)
    thread_status = False

def run():
    global thread_status
    channel = grpc.insecure_channel('0.0.0.0:50051')
    core_stub = dc_core_grpc.CoreServiceStub(channel)
    action_stub = dc_action_grpc.ActionServiceStub(channel)
    mission_stub = dc_mission_grpc.MissionServiceStub(channel)

    devices_stream = core_stub.SubscribeDevices(dc_core.SubscribeDevicesRequest())
    devices = list(devices_stream)
    for device in devices:
        print("Connected device: {}".format(device.uuid.value))

    device_uuid = dc_core.UUID()
    if len(sys.argv) == 2:
        device_uuid.value = int(sys.argv[1])
    else:
        device_uuid.value = devices[0].uuid.value
    print("Using devices with UUID: {}".format(device_uuid.value))

    mission_items = []

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398170327054473,
        longitude_deg=8.5456490218639658,
        relative_altitude_m=10,
        speed_m_s=5,
        is_fly_through=False,
        gimbal_pitch_deg=20,
        gimbal_yaw_deg=60,
        camera_action=dc_mission.MissionItem.NONE))

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398241338125118,
        longitude_deg=8.5455360114574432,
        relative_altitude_m=10,
        speed_m_s=2,
        is_fly_through=True,
        gimbal_pitch_deg=0,
        gimbal_yaw_deg=-60,
        camera_action=dc_mission.MissionItem.TAKE_PHOTO))

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398139363821485,
        longitude_deg=8.5453846156597137,
        relative_altitude_m=10,
        speed_m_s=5,
        is_fly_through=True,
        gimbal_pitch_deg=-45,
        gimbal_yaw_deg=0,
        camera_action=dc_mission.MissionItem.START_VIDEO))

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398058617228855,
        longitude_deg=8.5454618036746979,
        relative_altitude_m=10,
        speed_m_s=2,
        is_fly_through=False,
        gimbal_pitch_deg=-90,
        gimbal_yaw_deg=30,
        camera_action=dc_mission.MissionItem.STOP_VIDEO))

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398100366082858,
        longitude_deg=8.5456969141960144,
        relative_altitude_m=10,
        speed_m_s=5,
        is_fly_through=False,
        gimbal_pitch_deg=-45,
        gimbal_yaw_deg=-30,
        camera_action=dc_mission.MissionItem.START_PHOTO_INTERVAL))

    mission_items.append(dc_mission.MissionItem(
        latitude_deg=47.398001890458097,
        longitude_deg=8.5455576181411743,
        relative_altitude_m=10,
        speed_m_s=5,
        is_fly_through=False,
        gimbal_pitch_deg=0,
        gimbal_yaw_deg=0,
        camera_action=dc_mission.MissionItem.STOP_PHOTO_INTERVAL))

    device_mission = dc_mission.Mission()
    device_mission.mission_items.extend(mission_items)

    sendMissionRequest = dc_mission.SendMissionRequest()
    sendMissionRequest.uuid.value = device_uuid.value
    sendMissionRequest.mission.CopyFrom(device_mission)

    mission_stub.SendMission(sendMissionRequest)
    time.sleep(1)

    armRequest = dc_action.ArmRequest()
    armRequest.uuid.value = device_uuid.value
    arm_result = action_stub.Arm(armRequest)

    time.sleep(1)

    startMissionRequest = dc_mission.StartMissionRequest()
    startMissionRequest.uuid.value = device_uuid.value
    future_status = mission_stub.StartMission.future(startMissionRequest)

    t = threading.Thread(target=wait_func, args=(future_status,))
    t.start()

    while(thread_status):
        print("Waiting for thread to exit")
        time.sleep(5)

if __name__ == '__main__':
    run()
