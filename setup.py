from __future__ import print_function
from setuptools import setup, find_packages
from fake_rpi.version import __version__ as VERSION
from build_utils import BuildCommand
from build_utils import PublishCommand
from build_utils import BinaryDistribution


PACKAGE_NAME = 'fake_rpi'
BuildCommand.pkg = PACKAGE_NAME
PublishCommand.pkg = PACKAGE_NAME
PublishCommand.version = VERSION


setup(
	author='Kevin Walchko',
	author_email='walchko@users.noreply.github.com',
	name=PACKAGE_NAME,
	version=VERSION,
	description='A bunch of fake interfaces for development when not using the RPi or unit testing',
	long_description=open('readme.rst').read(),
	url='http://github.com/walchko/{}'.format(PACKAGE_NAME),
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
	keywords=['raspberry', 'pi', 'fake', 'fake_rpi', 'i2c', 'spi', 'gpio', 'serial'],
	packages=find_packages('.'),
	install_requires=['build_utils', 'numpy'],
	cmdclass={
		'make': BuildCommand,
		'publish': PublishCommand
	}
)
