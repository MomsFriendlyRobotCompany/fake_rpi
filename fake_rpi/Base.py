from __future__ import print_function


class Base(object):
	def __init__(self, name=None):
		print('<<< WARNING: using fake raspberry pi interfaces >>>')
		if name:
			print('<<< Using: {} >>>'.format(name))
