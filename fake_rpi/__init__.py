###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
# from __future__ import print_function
from . import serial
import fake_rpi.smbus
import fake_rpi.RPi
from .Adafruit import LSM303
from .wrappers import printf
from .wrappers import toggle_print
from . import picamera

try:
    from importlib.metadata import version # type: ignore
except ImportError:
    from importlib_metadata import version # type: ignore


__author__ = 'Kevin Walchko'
__license__ = 'MIT'
__version__ = version("fake_rpi")
