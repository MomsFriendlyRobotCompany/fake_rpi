#!/usr/bin/env python

from fake_rpi import RPi
from fake_rpi import smbus
from fake_rpi import printf
from fake_rpi import toggle_print

toggle_print(True)  # turn on/off printing

pwm = RPi.PWM()
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
