"""
As basic as it can get - this script just dumps some telemetry streams to the
command line!
"""
import sys
from dronecore import connect, exit


if __name__ == "__main__":

    # Connect to a local running backend
    test = connect("127.0.0.1")

    # Armed stream
    test.telemetry.armed \
                  .subscribe(on_next=lambda armed: print("ARMED: ", armed))

    # In air stream
    test.telemetry.in_air \
                  .subscribe(on_next=lambda in_air: print("IN_AIR: ", in_air))

    # Position stream
    test.telemetry.position \
                  .subscribe(on_next=lambda position: print(position))

    # Health stream
    test.telemetry.health \
                  .subscribe(on_next=lambda health: print(health))

    # Battery stream
    test.telemetry.battery \
                  .subscribe(on_next=lambda battery: print(battery))

    # We need to block the main thread as the reactive scheduler is running
    # in the background
    input("Enter to exit\n")
    # Only way to exit the program without running threads throwing exceptions
    exit(0)
