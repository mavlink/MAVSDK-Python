#!/usr/bin/env python

import grpc
import time
import sys

import dronecore.generated.core_pb2 as dc_core
import dronecore.generated.core_pb2_grpc as dc_core_grpc
import dronecore.generated.action_pb2 as dc_action
import dronecore.generated.action_pb2_grpc as dc_action_grpc


def run():
    channel = grpc.insecure_channel('0.0.0.0:50051')
    core_stub = dc_core_grpc.CoreServiceStub(channel)
    action_stub = dc_action_grpc.ActionServiceStub(channel)

    devices_stream = core_stub.SubscribeDevices(
        dc_core.SubscribeDevicesRequest())
    devices = list(devices_stream)
    for device in devices:
        print("Connected device: {}".format(device.uuid.value))

    device_uuid = dc_core.UUID()
    if len(sys.argv) == 2:
        device_uuid.value = int(sys.argv[1])
    else:
        device_uuid.value = devices[0].uuid.value
    print("Using devices with UUID: {}".format(device_uuid.value))

    armRequest = dc_action.ArmRequest()
    armRequest.uuid.value = device_uuid.value
    arm_result = action_stub.Arm(armRequest)
    if arm_result.result == dc_action.ActionResult.SUCCESS:
        print("arming ok")
    else:
        print("arming failed: " + arm_result.result_str)

    time.sleep(2)

    takeoffRequest = dc_action.TakeOffRequest()
    takeoffRequest.uuid.value = device_uuid.value
    takeoff_result = action_stub.TakeOff(takeoffRequest)
    if takeoff_result.result == dc_action.ActionResult.SUCCESS:
        print("takeoff ok")
    else:
        print("takeoff failed: " + takeoff_result.result_str)

    time.sleep(5)

    landRequest = dc_action.LandRequest()
    landRequest.uuid.value = device_uuid.value
    land_result = action_stub.Land(landRequest)
    if land_result.result == dc_action.ActionResult.SUCCESS:
        print("landing ok")
    else:
        print("landing failed: " + land_result.result_str)


if __name__ == '__main__':
    run()
