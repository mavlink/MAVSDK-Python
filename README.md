# MAVSDK-Python

This is the Python wrapper for MAVSDK.

The Python wrapper is based on a gRPC client communicating with the gRPC server written in C++. To use the Python wrapper the gRPC server called "backend" needs to be running on the same system. The wrapper is essentially auto-generated from the message definitions ([proto files](https://github.com/mavlink/MAVSDK-Proto)).

## Important Notes

- Python 3.6+ is required (because the wrapper is based on [asyncio](https://docs.python.org/3.7/library/asyncio.html)).
- You may need to run `pip3` instead of `pip` and `python3` instead of `python`, depending of your system defaults.

## Install using pip from PyPy

To install mavsdk-python, simply run:

```sh
pip3 install mavsdk
```

The package contains `mavsdk_server` already (previously called "backend"). It needs to be run manually with `start_mavlink()`. Have a look at the examples to see it used in practice.

## Run the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```

## Build and run from sources

Note: this is more involved and targetted to contributors.

### Get the Python wrapper

Clone this repo and recursively update submodules:

```
git clone https://github.com/mavlink/MAVSDK-Python --recursive
cd MAVSDK-Python
```

### Install prerequisites

First install the protoc plugin (`protoc-gen-dcsdk`):

```
cd proto/pb_plugins
pip3 install -r requirements.txt
pip3 install -e .
```

You can check that the plugin was installed with `$ which protoc-gen-dcsdk`, as it should now be in the PATH.

Then go back to the root of the repo and install the dependencies of the SDK:

```
cd ../..
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

### Build mavsdk_server

MAVDSK-Python runs the `mavsdk_server` when `start_mavlink()` is called. Under the hood, this will run `mavsdk/bin/mavsdk_server`, which has to be built separately from [MAVSDK](https://github.com/mavlink/MAVSDK) and copied there.

For more help on this step, check the [docs on how to build from source](https://mavsdk.mavlink.io/develop/en/contributing/build.html).
