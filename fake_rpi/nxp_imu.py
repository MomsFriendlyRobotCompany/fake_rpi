class IMU(object):
	def __init__(self, dps=250): pass
	def __del__(self):pass
	def get(self): return tuple([0]*9)


class AHRS(object):
	def __init__(self, deg=False): pass
	def getOrientation(self, accel, mag): return (0, 0, 0)
