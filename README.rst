================
DronecodeSDK-Python
================

DroneCore is made of plugins bringing different features (e.g. action, telemetry, mission). Each plugin is defined by a corresponding `*.proto` file. The Python implementation creates a package containing the core plugins provided by DroneCore and a plugin manager to allow 3rd party plugins.

Cloning the repository
~~~~~~~~~~~~~~~~~~~~~~

Clone the repo (or your fork) and recursively update submodules:

.. code-block:: bash

    git clone https://github.com/Dronecode/DronecodeSDK-Python --recursive

This can be done as 2 steps, as shown below.

.. code-block:: bash

    git clone https://github.com/Dronecode/DronecodeSDK-Python
    git submodule update --init --recursive


Prerequisites
~~~~~~~~~~~~~

Install `grpcio` and `grpcio-tools`:

.. code-block:: bash

    $ python -m pip install grpcio grpcio-tools

Generate Protobuf / gRPC files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run the following helper script. It will generate the `*_pb2.py` and `*_pb2_grpc.py` files for each plugin. If the submodules are not initialized already, the script will take care of it.

.. code-block:: bash

    $ ./other/tools/run_protoc.sh

Install the package locally
~~~~~~~~~~~~~~~~~~~~~~~~~~~

First of all, Python bindings for the gRPC interface have to be generated using

.. code-block::

    ./other/tools/run_protoc.sh

After this step you can install a development (editable) version of the package using:

.. code-block:: bash

    $ pip install -e .

*NOTE: You should use a virtual environment*

Running the examples
~~~~~~~~~~~~~~~~~~~~

Once the package has been installed, the examples can be run.
