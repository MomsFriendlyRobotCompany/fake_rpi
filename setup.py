from __future__ import print_function
from setuptools import setup
from fake_rpi import __version__ as VERSION
import os
from setuptools.command.test import test as TestCommand
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
	def is_pure(self):
		return False


class BuildCommand(TestCommand):
	"""Build binaries/packages"""
	def run_tests(self):
		print('Delete dist directory')
		os.system('rm -fr dist')
		print('Run Nose tests')
		ret = os.system("nosetests -v tests")
		if ret > 0:
			print('<<< Nose tests failed >>>')
			return

		print('Building packages ...')
		os.system("python setup.py sdist")
		os.system("python2 setup.py bdist_wheel")
		os.system("python3 setup.py bdist_wheel")
		# os.system("twine upload dist/fake_rpi-{}*".format(VERSION))


class PublishCommand(TestCommand):
	"""Publish to Pypi"""
	def run_tests(self):
		print('Publishing to PyPi ...')
		os.system("twine upload dist/fake_rpi-{}*".format(VERSION))


setup(
	author='Kevin Walchko',
	author_email='kevin.walchko@outlook.com',
	name='fake_rpi',
	version=VERSION,
	description='A bunch of fake interfaces for development when not using the RPi or unit testing',
	long_description=open('readme.rst').read(),
	url='http://github.com/walchko/fake_rpi',
	classifiers=[
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.6',
		'Topic :: Software Development :: Libraries',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	license='MIT',
	keywords='raspberry pi fake i2c spi gpio serial',
	packages=['fake_rpi'],
	install_requires=[],
	cmdclass={
		'make': BuildCommand,
		'publish': PublishCommand
	},
	# scripts=[
	# 	'bin/set_id.py',
	# 	'bin/servo_ping.py',
	# 	'bin/set_angle.py',
	# 	'bin/set_baud_rate.py',
	# 	'bin/servo_reboot.py',
	# 	'bin/servo_reset.py'
	# ]
)
