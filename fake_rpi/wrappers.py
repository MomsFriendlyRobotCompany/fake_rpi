from __future__ import print_function

# http://www.saltycrane.com/blog/2010/03/simple-python-decorator-examples/

from functools import wraps

PRINT_ON = True


def toggle_print(p):
	global PRINT_ON
	PRINT_ON = p


def printf(f):
	@wraps(f)
	def wrapped(*args, **kwargs):
		r = f(*args, **kwargs)

		if len(args):
			c = str(args[0].__class__).split('\'')[1]  # grab self from the class method
		else:
			c = ''  # no class

		if PRINT_ON:
			if r:
				print('{}.{}{}: {}'.format(c, f.__name__, args[1:], r))
			else:
				print('{}.{}{}'.format(c, f.__name__, args[1:]))
		return r
	return wrapped
