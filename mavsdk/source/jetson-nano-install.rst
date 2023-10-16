.. _jetson-nano-install:

Jetson Nano Install
===================

Ubuntu 18.04
------------

To install MAVSDK-Python on a Jetson Nano with Ubuntu 18.04 (which is old and pas end-of-life, by the way), you need to get a newer version of Python 3 and make sure pip is up-to-date.

Install Python 3.8:

.. code:: bash

  sudo apt update
  sudo apt install python3.8


Upgrade pip:

.. code:: bash

   python3.8 -m pip install --upgrade pip

Now install mavsdk:

.. code:: bash

   python3.8 -m pip install --upgrade mavsdk

Ubuntu 20.04
------------

The normal instructions should work with Ubuntu 20.04:

Install mavsdk:

.. code:: bash

   python3 -m pip install --upgrade mavsdk
