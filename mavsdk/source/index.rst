.. MAVSDK-Python documentation main file, created by
   sphinx-quickstart on Sat May 30 10:40:26 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

|

.. image:: nature_adapted/static/sdk_logo_full.png
   :alt: MAVSDK logo
   :scale: 30%

MAVSDK-Python API reference
===========================


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   system
   plugins/index

Important Notes
---------------

- Python 3.7+ is required.
- You may need to run ``pip3`` instead of ``pip`` and ``python3`` instead of ``python``, depending of your system defaults.
- Auterion has a _Getting started with MAVSDK-Python: https://auterion.com/getting-started-with-mavsdk-python/ guide if you're a beginner and not sure where to start.

Install using pip from PyPi
---------------------------

To install simply run:

.. code:: bash

  pip3 install mavsdk


The package contains ``mavsdk_server`` already (previously called "backend"), which is started automatically when connecting (e.g. ``await drone.connect()``). Have a look at the examples to see it used in practice. It will be something like:

.. code:: python

  python
  from mavsdk import System
  ...
  drone = System()
  await drone.connect(system_address="udp://:14540")


Note: ``System()`` takes two named parameters: ``mavsdk_server_address`` and ``port``. When left empty, they default to ``None`` and ``50051``, respectively, and ``mavsdk_server -p 50051`` is run by ``await drone.connect()``. If ``mavsdk_server_address`` is set (e.g. to "localhost"), then ``await drone.connect()`` will not start the embedded ``mavsdk_server`` and will try to connect to a server running at this address. This is useful for platforms where ``mavsdk_server`` does not come embedded, for debugging purposes, and for running ``mavsdk_server`` in a place different than where the MAVSDK-Python script is run.

Run the examples
----------------

Once the package has been installed, the examples can be run:

.. code:: bash

  examples/takeoff_and_land.py

The examples assume that the embedded ``mavsdk_server`` binary can be run. In some cases (e.g. on Raspberry Pi), it may be necessary to run ``mavsdk_server`` manually, and therefore to set ``mavsdk_server_address='localhost'`` as described above.

Debug connection issues
-----------------------

In order to get more debugging information, it is possible to run the mavsdk_server binary separately.

For this case, let's assume the example was like this:

.. code:: python

  drone = System()
  await drone.connect(system_address="udp://:14540")


The mavsdk_server binary is installed using ``pip3``. If installed with ``pip3 --user`` it is usually (at least for Linux) to be found in ``~/.local/lib/python3.9/site-packages/mavsdk/bin/`` (of course depending on the Python version used).

It can then be run in a separate console with the ``system_address`` as an argument:

.. code:: bash

  ~/.local/lib/python3.9/site-packages/mavsdk/bin/mavsdk_server udp://:14540

Without an autopilot connecting, the output will look something like:

.. code:: bash

  [02:36:31|Info ] MAVSDK version: v0.50.0 (mavsdk_impl.cpp:28)
  [02:36:31|Info ] Waiting to discover system on udp://:14540... (connection_initiator.h:20)

Once an autopilot is discovered, something like this should be printed:

.. code:: bash

  [02:38:12|Info ] MAVSDK version: v0.50.0 (mavsdk_impl.cpp:28)
  [02:38:12|Info ] Waiting to discover system on udp://:14540... (connection_initiator.h:20)
  [02:39:01|Info ] New system on: 127.0.0.1:14580 (with sysid: 1) (udp_connection.cpp:194)
  [02:39:01|Debug] New: System ID: 1 Comp ID: 1 (mavsdk_impl.cpp:484)
  [02:39:01|Debug] Component Autopilot (1) added. (system_impl.cpp:355)
  [02:39:02|Debug] Discovered 1 component(s) (system_impl.cpp:523)
  [02:39:02|Info ] System discovered (connection_initiator.h:63)
  [02:39:02|Info ] Server started (grpc_server.cpp:52)
  [02:39:02|Info ] Server set to listen on 0.0.0.0:50051 (grpc_server.cpp:53)

This would look promising, and the example can now be run against this server, however, without ``system_address``:

.. code:: python
  drone = System()
  await drone.connect()


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
