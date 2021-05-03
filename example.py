#!/usr/bin/env python

from fake_rpi import printf
from fake_rpi import toggle_print

# Replace libraries by fake ones
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO
sys.modules['smbus'] = fake_rpi.smbus

# Then keep the transparent import everywhere in the application and dependencies
import RPi
import RPi.GPIO as GPIO
import smbus


toggle_print(True)  # turn on/off printing

pwm = GPIO.PWM()
pwm.start(5)

i2c = smbus.SMBus(1)
i2c.write_byte_data(1, 2, 3)
i2c.read_byte_data(1, 2)
i2c.close()


class MyBus(smbus.SMBus):
    """
    Here I want to over ride how this behaves for testing
    """
    @printf
    def __init__(self):
        pass

    @printf
    def read_byte_data(self, a, b):
        ret = 0x71 if a == 0x68 else 0x48
        return ret


i2c = MyBus()
i2c.read_byte_data(1, 2)
i2c.read_i2c_block_data(1, 2, 3)


class MyGPIO(RPi._GPIO):
    def setup(self, channel, state, initial=0, pull_up_down=None):
        self._inputs[channel] = state


GPIO = MyGPIO()
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, 1)  # fake GPIO input is set to 1
GPIO.setup(22, 0)  # fake GPIO input is set to 0
b = GPIO.input(21)
b = GPIO.input(22)