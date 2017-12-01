from __future__ import print_function
from . import serial
import fake_rpi.smbus
import fake_rpi.RPi
from .Adafruit import LSM303
from .wrappers import printf
from .wrappers import toggle_print
from . import picamera
# from .RPi2 import _GPIO
from . import RPi2
# from fake_rpi import RPi2
# from fake_rpi import RPi.GPIO
# from fake_rpi.RPi.GPIO import GPIO
# from fake_rpi.RPi.GPIO import GPIO.PWM
# from RPi.GPIO import GPIO


from .version import __version__

__author__ = 'Kevin Walchko'
__license__ = 'MIT'
