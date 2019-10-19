.. image:: https://raw.githubusercontent.com/MomsFriendlyRobotCompany/fake_rpi/master/pics/pi-python.jpg

Fake Raspberry Pi
====================

.. image:: https://img.shields.io/pypi/v/fake_rpi.svg
    :target: https://pypi.python.org/pypi/fake_rpi/
    :alt: Latest Version
.. image:: https://img.shields.io/pypi/l/fake_rpi.svg
    :target: https://pypi.python.org/pypi/fake_rpi/
    :alt: License
.. image:: https://travis-ci.org/MomsFriendlyRobotCompany/fake_rpi.svg?branch=master
    :target: https://travis-ci.org/MomsFriendlyRobotCompany/fake_rpi
    :alt: Travis-ci
.. image:: https://img.shields.io/pypi/pyversions/fake_rpi.svg
	:target:  https://pypi.python.org/pypi/fake_rpi/
	:alt: Python Versions


**Why??**

I do a lot of development on my Powerbook and I got tired of constantly creating
a fake interface for dev on my laptop and testing on Travis.ci.

- 2017 Apr 2: **Beta Quality**
- 2017 Apr 8: **Initial** python3 support ... this is a pain

So, does this simulate everything on a Raspberry Pi? **No!** Right now it simulates
what I use and need. Over time, more will be added. You are also welcome to
submit pull requests for things I haven't added yet.

============= =============================
Adafruit      LSM303(accelerometer)
GPIO          gpio pins
picamera      camera
RPi           PWM
smbus         i2c
serial        not done yet
============= =============================


Install
---------

The preferred way to install this is::

	pip install fake_rpi


Development
-------------

To submit pull requests and do development::

	git clone
	cd fake_rpi
	pip install -e .

Usage
-------

To fake `RPi.GPIO` or `smbus`, this following code must be executed before your application:

.. code-block:: python

	# Replace libraries by fake ones
	import sys
	import fake_rpi

	sys.modules['RPi'] = fake_rpi.RPi     # Fake RPi (GPIO)
	sys.modules['smbus'] = fake_rpi.smbus # Fake smbus (I2C)

Then you can keep your usual imports in your application:

.. code-block:: python

	import RPi.GPIO as GPIO
	import smbus

	GPIO.setmode(io.BCM) # now use the fake GPIO
	b = GPIO.input(21)

	sm = smbus.SMBus(1) # now use the fake smbus
	b = sm.read_byte_data(0x21, 0x32)  # read in a byte

Turning on/off fake calls logging:

.. code-block:: python

	from fake_rpi import toggle_print

	# by default it prints everything to std.error
	toggle_print(False)  # turn on/off printing

But I need ``smbus`` to return a specific byte for unit testing! Ok, then create a child of my ``smbus`` like below
and modify *only* the methods you need changed:

.. code-block:: python

	from fake_rpi import smbus
	from fake_rpi import printf

	class MyBus(smbus.SMBus):
		@printf
		def read_byte_data(self, i2c_addr, register):
			ret = 0xff
			if i2c_addr == 0x21:
				ret = 0x55
			elif i2c_addr == 0x25:
				ret = 0x11
			return ret

	sm = MyBus()
	b = sm.read_byte_data(0x21, 0x32)  # read in a byte

Printing On or Off
~~~~~~~~~~~~~~~~~~~~~

Here is the output from ``example.py`` in the ``git`` repo when the printing is
toggled on or off:

::

	kevin@Logan fake_rpi $ ./example.py
	<<< WARNING: using fake raspberry pi interfaces >>>

::

	kevin@Logan fake_rpi $ ./example.py
	<<< WARNING: using fake raspberry pi interfaces >>>
	fake_rpi.RPi.PWM.__init__()
	fake_rpi.RPi.PWM.start(5,)
	fake_rpi.smbus.SMBus.__init__(1,)
	fake_rpi.smbus.SMBus.write_byte_data(1, 2, 3)
	fake_rpi.smbus.SMBus.read_byte_data(1, 2): 21
	fake_rpi.smbus.SMBus.close()
	__main__.MyBus.__init__()
	__main__.MyBus.read_byte_data(1, 2): 72
	__main__.MyBus.read_i2c_block_data(1, 2, 3): [90, 90, 90]


Change Log
------------

========== ====== =========
2019-10-19 0.6.2  fix from scivision
2019-03-29 0.6.1  bug fix with randint range
2017-11-30 0.6.0  bug fix with printing
2017-10-23 0.5.3  bug fix with randint
2017-09-05 0.5.1  flushing out interfaces
2017-07-07 0.3.0  fixed bugs, print statement, and reduced dups
2017-04-08 0.1.0  initial python3 setup and support
2017-04-02 0.0.2  pushed to pypi with landscape.io fixes
2017-04-01 0.0.1  created
========== ====== =========

MIT License
--------------------

Copyright (c) 2017 Kevin J. Walchko

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
