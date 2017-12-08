# DroneCore-Python

DroneCore is made of plugins bringing different features (e.g. action, telemetry, mission). Each plugin is defined by a corresponding `*.proto` file. The Python implementation creates one package for each plugin.

## Packages

There are currently 4 packages:

- dronecore
- dronecore_action
- dronecore_mission
- dronecore_telemetry

## Build a package

_(Note that you might want to do all of that in a virtual environment)._

### Prerequisites

Install `grpcio` and `grpcio-tools`:

```
$ python -m pip install grpcio grpcio-tools
```

### Generate Protobuf / gRPC files

Run the following helper script. It will generate the `*_pb2.py` and `*_pb2_grpc.py` files for each plugin.

```
$ ./tools/run_protoc.sh
```

### Install a module locally

From the root of a package (at the level of its _setup.py_), run:

```
$ python -m pip install .
```

## Running the examples

Once the packages have been installed, the examples can be run.
