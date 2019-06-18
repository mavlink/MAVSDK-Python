# MAVSDK-Python

This is the Python wrapper for MAVSDK.

The Python wrapper is based on a gRPC client communicating with the gRPC server written in C++. To use the Python wrapper the gRPC server called "backend" needs to be running on the same system. The wrapper is essentially auto-generated from the message definitions ([proto files](https://github.com/mavlink/MAVSDK-Proto)).

## Important Notes

- Python 3.6+ is required (because the wrapper is based on [asyncio](https://docs.python.org/3.7/library/asyncio.html)).
- You may need to run `pip3` instead of `pip` and `python3` instead of `python`, depending of your system defaults.

## Build and run backend

First, we need to build and run the backend which is the gRPC server that the Python wrapper will connect to.

**Note: it is planned to automate this step using package managers like brew, apt-get, etc. .**

```
git clone https://github.com/mavlink/MAVSDK --recursive
cd MAVSDK
mkdir -p build/default
cd build/default
cmake -DBUILD_BACKEND=ON ../..
cmake --build .
```

For more help on this step, check the [docs on how to build from source](https://sdk.dronecode.org/en/contributing/build.html).

Once this is built, start PX4 SITL and run the backend:

```
./src/backend/src/backend_bin
```

By default, the backend will connect using MAVLink on UDP port 14540 which is running by default when PX4 is run in SITL (software in the loop simulation). Run `$ ./src/backend/src/backend_bin --help` for more information.

## Get the Python wrapper

Clone this repo and recursively update submodules:

```
git clone https://github.com/mavlink/MAVSDK-Python --recursive
cd MAVSDK-Python
```

### Install prerequisites

First install the protoc plugin (`protoc-gen-dcsdk`):

```
cd proto/pb_plugins
pip install -r requirements.txt
pip install -e .
```

You can check that the plugin was installed with `$ which protoc-gen-dcsdk`, as it should now be in the PATH.

Then go back to the root of the repo and install the dependencies of the SDK:

```
cd ../..
pip install -r requirements.txt -r requirements-dev.txt
```

### Generate wrapper

Run the following helper script. It will generate the Python wrappers for each plugin. If the submodules are not initialized already, the script will take care of it.

```
./other/tools/run_protoc.sh
```

### Install the package locally

After generating the wrapper you can install a development (editable) version of the package using:

```
pip install -e .
```


### Running the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```
