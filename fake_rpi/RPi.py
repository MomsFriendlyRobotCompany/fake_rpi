from .wrappers import printf

class PWM(object):

	@printf
	def __init__(self, channel=0, frequency=0):
		pass

	@printf
	def start(self, dc):
		pass

	def stop(self):
		pass

	def ChangeDutyCycle(self, dc):
		pass

	def ChangeFrequency(self, frequency):
		pass
