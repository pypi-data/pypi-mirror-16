Synapse SNAPpy library for Ivensense MPU-6050
=============================================

``snappy-mpu605`` is a SNAPpy library that communicates with the
Invensense MPU-6050 6-axis accelerometer/gyro.

Installation
------------

For use in Portal
~~~~~~~~~~~~~~~~~

Download and extract the latest release zip file to Portal’s
``snappyImages`` directory. By default, this is located at
``...\Documents\Portal\snappyImages`` on Windows.

For use with SNAPbuild
~~~~~~~~~~~~~~~~~~~~~~

The easiest way to install ``snappy-mpu6050`` for use with SNAPbuild is
using `pip`_::

    pip install snapy-mpu6050

Alternatively you can download the source, extract it, and install it::

    python setup.py install

Usage
-----

To use the ``snappy-mpu6050`` library functions, first import the
library:

.. code:: python

    from snappy_mpu6050 import *

.. _pip: https://pip.pypa.io/en/latest/installing.html
