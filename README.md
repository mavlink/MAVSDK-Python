# DronecodeSDK-Python

This is the Python wrapper for the Dronecode SDK.

The Python wrapper is based on a gRPC client communicating with the gRPC server written in C++. To use the Python wrapper the gRPC server called "backend" needs to be running on the same system. The wrapper is essentially auto-generated from the message definitions ([proto files](https://github.com/Dronecode/DronecodeSDK-Proto)).

## Important Notes

- Python 3.6+ is required (because the wrapper is based on [asyncio](https://docs.python.org/3.7/library/asyncio.html)).


## Build and run backend

First, we need to build and run the backend which is the gRPC server that the Python wrapper will connect to.

**Note: it is planned to automate this step using package managers like brew, apt-get, etc. .**

```
git clone https://github.com/Dronecode/DronecodeSDK --recursive
cd DronecodeSDK
make BUILD_BACKEND=1
```

For more help on this step, check the [docs on how to build from source](https://sdk.dronecode.org/en/contributing/build.html).

Once this is built, start PX4 SITL and run the backend:

```
./build/default/backend/src/backend_bin
```

By default, the backend will connect using MAVLink on UDP port 14540 which is running by default when PX4 is run in SITL (software in the loop simulation).
To change the connection port, check [this line in the backend](https://github.com/Dronecode/DronecodeSDK/blob/d4fb6ca56f8e4ce01252ed498835c500e477d2d2/backend/src/backend.cpp#L19). For now, the backend is limited to UDP even though the core supports UDP, TCP, and serial.

## Get the Python wrapper

Clone this repo and recursively update submodules:

```
git clone https://github.com/Dronecode/DronecodeSDK-Python --recursive
cd DronecodeSDK-Python
```


### Install prerequisites

```
pip3 install -r requirements.txt -r requirements-dev.txt
```

### Generate wrapper

Run the following helper script. It will generate the Python wrappers for each plugin. If the submodules are not initialized already, the script will take care of it.

```
./other/tools/run_protoc.sh
```

### Install the package locally

After generating the wrapper you can install a development (editable) version of the package using:

```
pip3 install -e .
```


### Running the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```
