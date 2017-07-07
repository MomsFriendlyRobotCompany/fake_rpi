import numpy as np
# import platform
from .wrappers import printf
from .Base import Base


class BGR(object):
	"""Fake class"""

	@printf
	def __init__(self, sz):
		# constructor
		self.array = np.random.rand(*sz)

	@printf
	def truncate(self, num):
		# refreshes the fake image
		self.array = np.random.rand(*self.array.shape)


# class picamera(object):
# 	"""Fake class"""
class PiCamera(Base):
	"""Fake class"""
	resolution = (0, 0)

	def __init__(self):
		# empty constructor
		# print('WARNING: Fake_RPi PiCamera on {}'.format(platform.system().lower()))
		Base.__init__(self, self.__class__)
		pass

	def close(self):
		# this does nothing
		pass

	@printf
	def capture(self, image, format, use_video_port):
		# this does nothing
		pass


class array(object):
	"""Fake class"""

	@staticmethod
	def PiRGBArray(cam, size):
		return BGR(size)
