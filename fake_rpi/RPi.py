from .wrappers import printf
from .Base import Base


class PWM(Base):

	@printf
	def __init__(self, channel=0, frequency=0):
		Base.__init__(self, self.__class__)

	@printf
	def start(self, dc):
		pass

	def stop(self):
		pass

	def ChangeDutyCycle(self, dc):
		pass

	def ChangeFrequency(self, frequency):
		pass


class GPIO(Base):

	LOW = 0
	HIGH = 1
	IN = 1
	OUT = 0
	BCM = 11
	BOARD = 10
	PUD_UP = 22
	PUD_DOWN = 21
	I2C = 42
	SPI = 41
	RISING = 31
	UNKNOWN = -1

	def __init__(self):
		Base.__init__(self, self.__class__)

	@printf
	def setwarnings(a): pass

	@printf
	def setmode(a): pass

	@printf
	def getmode(): return BCM

	@printf
	def setup(channel, state, initial=LOW): pass

	@printf
	def input(a): return randint(0, 1)

	@printf
	def cleanup(a=None): pass

	@printf
	def output(channel, state): pass
