# MAVSDK-Python

[![GitHub Actions Status](https://github.com/mavlink/MAVSDK-Python/workflows/PyPi%20Upload/badge.svg?branch=master)](https://github.com/mavlink/MAVSDK-Python/actions?query=branch%3Amaster)

This is the Python wrapper for MAVSDK.

The Python wrapper is based on a gRPC client communicating with the gRPC server written in C++. To use the Python wrapper the gRPC server called "backend" needs to be running on the same system. The wrapper is essentially auto-generated from the message definitions ([proto files](https://github.com/mavlink/MAVSDK-Proto)).


## Important Notes

- Python 3.6+ is required (because the wrapper is based on [asyncio](https://docs.python.org/3.7/library/asyncio.html)).
- You may need to run `pip3` instead of `pip` and `python3` instead of `python`, depending of your system defaults.
- Auterion has a [Getting started with MAVSDK-Python](https://auterion.com/getting-started-with-mavsdk-python/) guide if you're a beginner and not sure where to start.

## API Reference docs

-> [API Reference documentation](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/).

## Install using pip from PyPi

To install mavsdk-python, simply run:

```sh
pip3 install mavsdk
```

The package contains `mavsdk_server` already (previously called "backend"), which is started automatically when connecting (e.g. `await drone.connect()`). Have a look at the examples to see it used in practice. It will be something like:

```python
from mavsdk import System

...

drone = System()
await drone.connect(system_address="udp://:14540")
```

Note: `System()` takes two named parameters: `mavsdk_server_address` and `port`. When left empty, they default to `None` and `50051`, respectively, and `mavsdk_server -p 50051` is run by `await drone.connect()`. If `mavsdk_server_address` is set (e.g. to "localhost"), then `await drone.connect()` will not start the embedded `mavsdk_server` and will try to connect to a server running at this address. This is useful for platforms where `mavsdk_server` does not come embedded, for debugging purposes, and for running `mavsdk_server` in a place different than where the MAVSDK-Python script is run.

## Run the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```

The examples assume that the embedded `mavsdk_server` binary can be run. In some cases (e.g. on Raspberry Pi), it may be necessary to run `mavsdk_server` manually, and therefore to set `mavsdk_server_address='localhost'` as described above.

## Contribute

Note: this is more involved and targetted at contributors.

Most of the code is auto-generated from the [proto definitions](https://github.com/mavlink/mavsdk-proto), using our [templates](./other/templates). The generated files can be found in the [generated](./mavsdk/generated) folder. As a result, contributions are generally made in the templates or on the build system. Regularly, there is a need to update MAVSDK-Python to include the latest features defined in the proto definitions. This is described [below](#generate-the-code).

### Clone the repo

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
```

You can check that the plugin was installed with `$ which protoc-gen-dcsdk`, as it should now be in the PATH.

Then go back to the root of the repo and install the dependencies of the SDK:

```
cd ../..
pip3 install -r requirements.txt -r requirements-dev.txt
```

### Generate the code

Run the following helper script. It will generate the Python wrappers for each plugin.

```
./other/tools/run_protoc.sh
```

### Update `mavsdk_server` version

[MAVSDK_SERVER_VERSION](./MAVSDK_SERVER_VERSION) contains exactly the tag name of the `mavsdk_server` release corresponding to the version of MAVSDK-Python. When the [proto](./proto) submodule is updated here, chances are that `mavsdk_server` should be updated, too. Just edit this file, and the corresponding binary will be downloaded by the `setup.py` script (see below).

### Build and install the package locally

After generating the wrapper you can install a development (editable) version of the package using:

```
python3 setup.py build
pip3 install -e .
```

Note: MAVDSK-Python runs `mavsdk/bin/mavsdk_server` when `await drone.connect()` is called. This binary comes from [MAVSDK](https://github.com/mavlink/MAVSDK/releases) and is downloaded during the `setup.py` step above.


### Generate the API documentation

Make sure the version tag is set correctly before generating new documentation.

```
pip3 install -r requirements-docs.txt
make -C mavsdk html
```


### Release steps

1. Check all required pull requests are merged to master
2. Check [MAVSDK_SERVER_VERSION](MAVSDK_SERVER_VERSION) is set to the correct version of mavsdk_server.
3. Create git tag on laster master, e.g.:
   ```
   git switch master
   git pull
   git tag X.Y.Z
   git push --tags
   ```
4. Go to [releases page](https://github.com/mavlink/MAVSDK-Python/releases) and create new release.
   The CI will now:
   - Create and push a wheel for Windows, Linux and macOS to PyPi.
   - Generate the latest docs and push them to s3.
