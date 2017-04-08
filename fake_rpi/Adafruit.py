import random


class HW(object):
	def write8(self, a, b):
		pass

class LSM303(object):
	"""
	Dummy interface for testing outside of linux/RPi where I don't have
	access to I2C and the real sensor.
	"""
	def __init__(self, hires=True, accel_address=0, mag_address=0, i2c=None, **kwargs):
		random.seed()  # init for random data
		self._mag = HW()
		self._accel = HW()
		
	def set_mag_gain(self, gain=0):
		pass

	def read(self):
		"""
		Since there isn't a real sensor connected, read() creates random
		data.
		"""
		data = []*6
		for i in range(6):
			data[i] = random.uniform(-2048, 2048)
		accel = data[:3]
		mag = data[3:]
		return (accel, mag)