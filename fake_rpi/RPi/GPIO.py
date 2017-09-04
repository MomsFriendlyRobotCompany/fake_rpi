from fake_rpi.wrappers import printf
from fake_rpi.Base import Base


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

# Values
LOW = 0
HIGH = 1

# Modes
BCM = 11
BOARD = 10

# Pull
PUD_OFF = 20
PUD_DOWN = 21
PUD_UP = 22

# Edges
RISING = 31
FALLING = 32
BOTH = 33

# Functions
OUT = 0
IN = 1
SERIAL = 40
SPI = 41
I2C = 42
HARD_PWM = 43
UNKNOWN = -1

# Versioning
RPI_REVISION = 2
VERSION = '0.5.6'

def __init__(self):
	Base.__init__(self, self.__class__)

@printf
def setwarnings(a): pass

@printf
def setmode(a): pass

@printf
def getmode(): return BCM

@printf
def setup(channel, state, initial=LOW, pull_up_down=None): pass

@printf
def input(a): return randint(0, 1)

@printf
def cleanup(a=None): pass

@printf
def output(channel, state): pass

@printf
def wait_for_edge(channel, edge): pass

@printf
def add_event_detect(channel, edge, callback=None, bouncetime=None): pass

@printf
def add_event_callback(channel, callback=None): pass

@printf
def remove_event_detect(channel): pass

@printf
def event_detected(channel): return False

@printf
def gpio_function(channel): return OUT
