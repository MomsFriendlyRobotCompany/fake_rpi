from .Base import Base


class IMU(Base):
	def __init__(self, dps=250):
		Base.__init__(self, self.__class__)
	def __del__(self):pass
	def get(self): return tuple([0]*9)


class AHRS(Base):
	def __init__(self, deg=False):
		super(Base, self).__init__()
	def getOrientation(self, accel, mag): return (0, 0, 0)
