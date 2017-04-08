from .wrappers import printf
from random import randint

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


@printf
def setwarnings(a):
	pass


@printf
def setmode(a):
	pass


@printf
def getmode():
	return BCM


@printf
def setup(channel, state, initial=LOW):
	pass


@printf
def input(a):
	return randint(0, 1)


@printf
def cleanup(a=None):
	pass


@printf
def output(channel, state):
	pass
