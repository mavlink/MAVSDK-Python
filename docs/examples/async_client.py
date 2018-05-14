#!/usr/bin/env python

from __future__ import print_function
import grpc
import time
import threading
import sys

import dronecore.generated.core_pb2 as dc_core
import dronecore.generated.core_pb2_grpc as dc_core_grpc
import dronecore.generated.action_pb2 as dc_action
import dronecore.generated.action_pb2_grpc as dc_action_grpc
import dronecore.generated.telemetry_pb2 as dc_telemetry
import dronecore.generated.telemetry_pb2_grpc as dc_telemetry_grpc


class Colors:
    BLUE = "\033[34m"
    RESET = "\033[0m"


def wait_until(status):
    ret = status.result()
    return ret


def print_altitude(telemetry_stub, device_uuid, stop):
    subscribePositionRequest = dc_telemetry.SubscribePositionRequest()
    subscribePositionRequest.uuid.value = device_uuid.value
    positions_stream = telemetry_stub.SubscribePosition(
        subscribePositionRequest)

    for i, position in enumerate(positions_stream):
        # Position updates with SITL are too fast, we skip 9/10.
        if i % 10 == 0:
            print(Colors.BLUE, end="")
            print("Got relative altitude: {:.2f} m".
                  format(position.relative_altitude_m))
            print(Colors.RESET, end="")
        if stop.is_set():
            break


def run():
    channel = grpc.insecure_channel('0.0.0.0:50051')
    core_stub = dc_core_grpc.CoreServiceStub(channel)
    action_stub = dc_action_grpc.ActionServiceStub(channel)
    telemetry_stub = dc_telemetry_grpc.TelemetryServiceStub(channel)

    devices_stream = core_stub.SubscribeDevices(
        dc_core.SubscribeDevicesRequest())
    devices = list(devices_stream)
    for device in devices:
        print("Connected to device: {}".format(device.uuid.value))

    device_uuid = dc_core.UUID()
    if len(sys.argv) == 2:
        device_uuid.value = int(sys.argv[1])
    else:
        device_uuid.value = devices[0].uuid.value

    # We use this stop event later to stop the thread.
    t_stop = threading.Event()
    t = threading.Thread(
        target=print_altitude,
        args=(
            telemetry_stub,
            device_uuid,
            t_stop))
    t.start()

    armRequest = dc_action.ArmRequest()
    armRequest.uuid.value = device_uuid.value
    arm_result = action_stub.Arm.future(armRequest)
    arm_result = wait_until(arm_result)
    if arm_result.result == dc_action.ActionResult.SUCCESS:
        print("arming ok")
    else:
        print("arming failed: " + arm_result.result_str)

    time.sleep(2)

    takeoffRequest = dc_action.TakeOffRequest()
    takeoffRequest.uuid.value = device_uuid.value
    takeoff_result = action_stub.TakeOff.future(takeoffRequest)
    takeoff_result = wait_until(takeoff_result)
    if takeoff_result.result == dc_action.ActionResult.SUCCESS:
        print("takeoff ok")
    else:
        print("takeoff failed: " + takeoff_result.result_str)

    time.sleep(5)

    landRequest = dc_action.LandRequest()
    landRequest.uuid.value = device_uuid.value
    land_result = action_stub.Land.future(landRequest)
    land_result = wait_until(land_result)
    if land_result.result == dc_action.ActionResult.SUCCESS:
        print("landing ok")
    else:
        print("landing failed: " + land_result.result_str)
    time.sleep(3)

    t_stop.set()


if __name__ == '__main__':
    run()
