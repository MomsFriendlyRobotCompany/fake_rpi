
from __future__ import division
from __future__ import print_function


class Serial(object):
	"""
	A dummy interface to test with when not hooked up to real hardware.
	"""
	cd = False
	cts = True
	dsr = False
	in_waiting = True
	out_waiting = False
	ri = False

	def __init__(self, port):
		pass

	def open(self):
		pass

	def setRTS(self):
		pass

	def read(self, size=1):
		pass

	def write(self, data):
		return len(data)

	def close(self):
		pass

	def flush(self):
		pass

	def set_output_flow_control(self, enable=True):
		pass

	def set_input_flow_control(self, enable=True):
		pass

	def cancel_read(self):
		pass

	def cancel_write(self):
		pass
