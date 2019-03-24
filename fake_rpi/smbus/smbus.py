from fake_rpi.wrappers import printf
from random import randint
from fake_rpi.Base import Base

# randint(0,1024)


class SMBus(Base):
	@printf
	def __init__(self, bus=None, force=False):
		Base.__init__(self, self.__class__)

	@printf
	def write_byte_data(self, i2c_addr, register, value):
		pass

	@printf
	def write_byte(self, i2c_addr, value):
		pass

	@printf
	def read_byte_data(self, i2c_addr, register):
		return randint(0, 2**8-1)

	@printf
	def read_byte(self, i2c_addr):
		return randint(0, 2**8-1)

	@printf
	def read_word_data(self, i2c_addr, register):
		return [randint(0, 2**8-1)]*2

	@printf
	def write_word_data(self, i2c_addr, register, value):
		pass

	@printf
	def read_i2c_block_data(self, a, b, c):
		return [randint(0, 2**8-1)]*c

	@printf
	def write_i2c_block_data(self, i2c_addr, register, data):
		pass

	@printf
	def open(self, bus):
		pass

	@printf
	def close(self):
		pass
