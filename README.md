# MAVSDK-Python

## Trusk changes

> This is a fork with local changes to support a **custom ArduPilot flight-mode number for offboard control**.

By default, starting offboard control forces ArduPilot into `GUIDED` mode. In this fork you can pass a custom
mode number instead. It is wired through the `StartRequest` proto message as a new `mode` field.

### What changed

- `offboard.proto`: `StartRequest` gained a `uint32 mode` field (`0` keeps the default `GUIDED` behaviour).
- `offboard.py` (generated): `Offboard` accepts a `mode_number` constructor argument (default `4` = `GUIDED`)
  and `Offboard.start()` accepts an optional `mode`:
  ```python
  offboard = drone.offboard(mode_number=3)   # 3 = AUTO on ArduPilot
  await offboard.start()
  # or, per call:
  await offboard.start(mode=3)
  ```

### Why it isn't lost on regeneration

The Python-side constructor/`start()` customisations are baked into the code-generation template
`other/templates/py/file.j2`, so running `hatch run generate` reproduces them. The gRPC `mode` field is
defined in `proto/protos/offboard/offboard.proto`.

### How to build both projects

The commands below assume that `trusk-mavsdk-cpp` and `trusk-mavsdk` are sibling directories. First build the
patched `mavsdk_server` by following the `Trusk changes` section of `../trusk-mavsdk-cpp/README.md`. Then, from this
Python repository root:

```sh
git submodule update --init --recursive
python3 -m pip install hatch

# Use the exact C++ build directory so another stale or cross-compiled server cannot be selected.
export MAVSDK_CPP_PROJECT_ROOT="$(realpath ../trusk-mavsdk-cpp/cpp/build/default)"
# On x86-64 Linux, this also makes an accidental release fallback use the host architecture.
export MAVSDK_SERVER_ARCH=x86_64

hatch run build
```

`hatch run build` installs the generator from the local proto submodule, regenerates the Python bindings, copies
`mavsdk_server` into `mavsdk/bin/`, and builds the wheel and source distribution. Confirm that it prints
`Found local mavsdk_server`. If it reports that no local server was found, it falls back to the upstream release
in `MAVSDK_SERVER_VERSION`, which does not contain this fork's local C++ changes.

For individual development steps, use:

```sh
hatch run generate          # regenerate mavsdk/*.py and protobuf stubs
hatch run download-server   # copy the local server into mavsdk/bin/
hatch run install-local     # install this checkout in editable mode
```

`MAVSDK_CPP_PROJECT_ROOT` is searched recursively and the newest executable is selected, so point it at the
intended build directory rather than the entire C++ checkout. Setting `MAVSDK_BUILD_PURE` skips the embedded
server entirely and is only appropriate when the server will be managed separately.

The default C++ build uses shared libraries from its build tree. Keep that tree available and verify the copied
server with `ldd mavsdk/bin/mavsdk_server`; copying the executable alone does not make the wheel portable.

The `mode` behaviour then works end-to-end: Python client → gRPC → `mavsdk_server` → `MAV_CMD_DO_SET_MODE`.

### NVIDIA Jetson Orin Nano (ARM64/aarch64)

Build both projects natively on the Jetson. This is preferred because the C++ repository does not provide a
JetPack/glibc-sysroot-specific cross-compilation recipe. After building the C++ server in the dedicated
`cpp/build/jetson-aarch64` directory described in the sibling README, run:

```sh
# In trusk-mavsdk on the Jetson
uname -m  # expected: aarch64
git submodule update --init --recursive
python3 -m pip install hatch

export MAVSDK_CPP_PROJECT_ROOT="$(realpath ../trusk-mavsdk-cpp/cpp/build/jetson-aarch64)"
export MAVSDK_SERVER_ARCH=aarch64

hatch run build
hatch run install-local  # optional editable development installation

file mavsdk/bin/mavsdk_server
ldd mavsdk/bin/mavsdk_server
```

Confirm that the downloader prints `Found local mavsdk_server`, `file` identifies an ARM/AArch64 ELF executable,
and `ldd` has no `not found` entries. `MAVSDK_SERVER_ARCH=aarch64` affects only a release-download fallback; it
does not compile the C++ server or choose among local binaries. The default shared build and a wheel containing
it remain tied to the matching C++ build tree and are not automatically portable to other ARM64 or JetPack/glibc
systems.

[![GitHub Actions Status](https://github.com/mavlink/MAVSDK-Python/workflows/Check%20and%20PyPi%20Upload/badge.svg?branch=main)](https://github.com/mavlink/MAVSDK-Python/actions/workflows/main.yml?query=branch%3Amain)

This is the Python wrapper for MAVSDK.

The Python wrapper is based on a gRPC client communicating with the gRPC server written in C++. To use the Python wrapper the gRPC server called "backend" needs to be running on the same system. The wrapper is essentially auto-generated from the message definitions ([proto files](https://github.com/mavlink/MAVSDK-Proto)).


## Important Notes

- Python 3.7+ is required (because the wrapper is based on [asyncio](https://docs.python.org/3.7/library/asyncio.html)).
- You may need to run `pip3` instead of `pip` and `python3` instead of `python`, depending of your system defaults.
- Auterion used to have a [Getting started with MAVSDK-Python (web.archive.org)](https://web.archive.org/web/20201211155626/https://auterion.com/getting-started-with-mavsdk-python/) guide if you're a beginner and not sure where to start.

## API Reference docs

-> [API Reference documentation](http://mavsdk-python-docs.s3-website.eu-central-1.amazonaws.com/).

## Install using pip from PyPi

**Note for Raspberry Pi 1/2 and Zero:**

> MAVSDK-Python requires grpcio. However, there are no binary packets of grpcio for armv6 available via pip (also see [files on pypi.org](https://pypi.org/project/grpcio/#files)).
> In this case, install grpcio via the package manager, e.g. `sudo apt-get install python3-grpcio`.


To install mavsdk-python, simply run:

```sh
pip3 install mavsdk
```

The package contains `mavsdk_server` already (previously called "backend"), which is started automatically when connecting (e.g. `await drone.connect()`). Have a look at the examples to see it used in practice. It will be something like:

```python
from mavsdk import System

...

drone = System()
await drone.connect(system_address="udpin://0.0.0.0:14540")
```

Note: `System()` takes two named parameters: `mavsdk_server_address` and `port`. When left empty, they default to `None` and `50051`, respectively, and `mavsdk_server -p 50051` is run by `await drone.connect()`. If `mavsdk_server_address` is set (e.g. to "localhost"), then `await drone.connect()` will not start the embedded `mavsdk_server` and will try to connect to a server running at this address. This is useful for platforms where `mavsdk_server` does not come embedded, for debugging purposes, and for running `mavsdk_server` in a place different than where the MAVSDK-Python script is run.

## Run the examples

Once the package has been installed, the examples can be run:

```
examples/takeoff_and_land.py
```

The examples assume that the embedded `mavsdk_server` binary can be run. In some cases (e.g. on Raspberry Pi), it may be necessary to run `mavsdk_server` manually, and therefore to set `mavsdk_server_address='localhost'` as described above.

## Contribute

Note: this is more involved and targeted at contributors.

Most of the code is auto-generated from the [proto definitions](https://github.com/mavlink/mavsdk-proto), using our [templates](./other/templates). The generated plugin modules and protobuf stubs are written directly under [`mavsdk/`](./mavsdk). As a result, contributions are generally made in the templates or on the build system. Regularly, there is a need to update MAVSDK-Python to include the latest features defined in the proto definitions. This is described [below](#generate-the-code).

### Clone the repo

Clone this fork and initialize its submodules:

```sh
git clone --recursive https://github.com/trusk-technology/MAVSDK-Python.git trusk-mavsdk
cd trusk-mavsdk
```

### Install prerequisites

Install [Hatch](https://hatch.pypa.io/latest/install/), which creates the development environment from
`pyproject.toml`:

```sh
python3 -m pip install hatch
git submodule update --init --recursive
```

### Generate the code

Use the Hatch script to install `protoc-gen-mavsdk` from `proto/pb_plugins` and generate the Python wrappers for
each plugin:

```sh
hatch run generate
```

### Adding support for new plugins

In case you updated the `./proto` submodule to include a new plugin, you will also have to manually edit the file `mavsdk/system.py` to register the plugin.

### Update `mavsdk_server` version

[MAVSDK_SERVER_VERSION](./MAVSDK_SERVER_VERSION) contains the tag of the upstream `mavsdk_server` release used
as a fallback. `hatch run download-server` first searches below `MAVSDK_CPP_PROJECT_ROOT` for a local executable.
Only when none is found does it download the release identified by this file. When the [proto](./proto) submodule
is updated, both the local C++ server and this fallback version may need to be updated.

### Build and install the package locally

To generate the wrappers, copy the locally built server, and install this checkout in editable mode, use:

```sh
hatch run generate
hatch run download-server
hatch run install-local
```

To build wheel and source-distribution artifacts instead, use the complete workflow:

```sh
hatch run build
```

On Linux ARM release-download fallbacks, `MAVSDK_SERVER_ARCH` can be set to `armv6l`, `armv7l`, `aarch64`, or
an accepted x86 alias. On Windows, the downloader accepts `x86`, `x64`, and `arm64`. This variable does not
select or validate a locally built executable; use a narrow `MAVSDK_CPP_PROJECT_ROOT` and verify the copied
binary with `file` when architecture matters.

MAVSDK-Python starts `mavsdk/bin/mavsdk_server` when `await drone.connect()` is called without an external server
address. That binary may have been copied from the local C++ build or downloaded from the upstream release
fallback. Do not run the legacy `python3 setup.py build` after copying the patched server: that path uses its own
release downloader and can replace the local executable.


### Generate the API documentation

Make sure the version tag is set correctly before generating new documentation.

```
pip3 install -r requirements-docs.txt
make -C mavsdk html
```

### Formatting checks before committing

We use the following checks in [CI](.github/workflows/main.yml):

```
pipx run ruff format --check --line-length=100 examples
pipx run ruff check --select=ASYNC,RUF006,E,F --line-length=100 examples
pipx run ruff check --select=PERF --line-length=100 .
pipx run codespell .
```

### Release steps

1. Check the proto submodule is up-to-date and the generated code has been updated.
2. Check all required pull requests are merged to main
3. Check [MAVSDK_SERVER_VERSION](MAVSDK_SERVER_VERSION) is set to the correct version of mavsdk_server.
4. Create git tag on laster main, e.g.:
   ```
   git switch main
   git pull
   git tag X.Y.Z
   git push --tags
   ```
5. Go to [releases page](https://github.com/mavlink/MAVSDK-Python/releases) and create new release.
   The CI will now:
   - Create and push a wheel for Windows, Linux and macOS to PyPi.
   - Generate the latest docs and push them to s3.
