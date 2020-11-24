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
   :maxdepth: 5
   :caption: Contents:

   system
   plugins/index

Important Notes
---------------

- Python 3.6+ is required.
- You may need to run ``pip3`` instead of ``pip`` and ``python3`` instead of ``python``, depending of your system defaults.
- Auterion has a _Getting started with MAVSDK-Python: https://auterion.com/getting-started-with-mavsdk-python/ guide if you're a beginner and not sure where to start.

Install using pip from PyPi
---------------------------

To install simply run:

  pip3 install mavsdk


The package contains ``mavsdk_server`` already (previously called "backend"), which is started automatically when connecting (e.g. ``await drone.connect()``). Have a look at the examples to see it used in practice. It will be something like:

  python
  from mavsdk import System

  ...

  drone = System()
  await drone.connect(system_address="udp://:14540")


Note: ``System()`` takes two named parameters: ``mavsdk_server_address`` and ``port``. When left empty, they default to ``None`` and ``50051``, respectively, and ``mavsdk_server -p 50051`` is run by ``await drone.connect()``. If ``mavsdk_server_address`` is set (e.g. to "localhost"), then ``await drone.connect()`` will not start the embedded ``mavsdk_server`` and will try to connect to a server running at this address. This is useful for platforms where ``mavsdk_server`` does not come embedded, for debugging purposes, and for running ``mavsdk_server`` in a place different than where the MAVSDK-Python script is run.

Run the examples
----------------

Once the package has been installed, the examples can be run:

  examples/takeoff_and_land.py

The examples assume that the embedded ``mavsdk_server`` binary can be run. In some cases (e.g. on Raspberry Pi), it may be necessary to run ``mavsdk_server`` manually, and therefore to set ``mavsdk_server_address='localhost'`` as described above.


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
