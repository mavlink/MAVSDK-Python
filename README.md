# DroneCore-Python

DroneCore is made of plugins bringing different features (e.g. action, telemetry, mission). Each plugin is defined by a corresponding `*.proto` file. The Python implementation creates one package for each plugin.



## Packages

There are currently 4 packages:

- dronecore_core
- dronecore_action
- dronecore_mission
- dronecore_telemetry

## Build Packages

> **Note** You may want to do all of the following in a virtual environment.

### Prerequisites

Install `grpcio` and `grpcio-tools`:

```
$ python -m pip install grpcio grpcio-tools
```

### Get Source/Clone Repo

Clone the repo (or your fork) and recursively update submodules:
```
git clone https://github.com/dronecore/DroneCore-Python.git --recursive
```

This can be done as 2 steps, as shown below.
```
git clone https://github.com/<your fork>/DroneCore-Python.git
git submodule update --init --recursive
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
