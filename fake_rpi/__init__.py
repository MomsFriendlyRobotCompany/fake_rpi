from __future__ import print_function
from . import serial
from . import smbus
from . import RPi
from .Adafruit import LSM303
from .wrappers import printf
from .wrappers import toggle_print
from . import picamera
from .version import __version__

__author__ = 'Kevin Walchko'
__license__ = 'MIT'


print('<<< WARNING: using fake raspberry pi interfaces >>>')
