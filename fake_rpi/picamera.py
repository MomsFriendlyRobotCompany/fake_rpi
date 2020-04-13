###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################
import numpy as np  # type: ignore
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
#     """Fake class"""
class PiCamera(Base):
    """Fake class"""
    resolution = (0, 0)

    def __init__(self, resolution=None):
        # empty constructor
        # print('WARNING: Fake_RPi PiCamera on {}'.format(platform.system().lower()))
        Base.__init__(self, self.__class__)
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def close(self):
        # this does nothing
        pass

    @printf
    def capture(self, output, format=None, use_video_port=False, resize=None, splitter_port=0, **options):
        # this does nothing
        pass


class array(object):
    """Fake class"""

    @staticmethod
    def PiRGBArray(cam, size):
        return BGR(size)
