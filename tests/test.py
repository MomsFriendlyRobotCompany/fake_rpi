from __future__ import print_function

# Faking
import sys
import fake_rpi

sys.modules['RPi'] = fake_rpi.RPi
sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO
sys.modules['smbus'] = fake_rpi.smbus
sys.modules['picamera'] = fake_rpi.picamera
sys.modules['serial'] = fake_rpi.serial

import RPi.GPIO as GPIO
import smbus
import picamera
import serial


def test_smbus():
    i2c = smbus.SMBus(1)

    for i in range(1000):
        ret = i2c.read_byte_data(1, 2)
        assert isinstance(ret, int)
        assert 0 <= ret <= 2**8

        b = i2c.read_word_data(1, 2)
        # assert len(b) == 2
        # for n in b:
        #     assert 0 <= ret <= 2**8
        assert isinstance(b, int)
        assert 0 <= b <= 2**16

        d = i2c.read_i2c_block_data(1, 2, 6)
        assert len(d) == 6
        for n in d:
            # assert 0 <= ret <= 2**8
            assert 0 <= n <= 2**8


def test_pwm():
    pwm = GPIO.PWM()
    pwm.ChangeDutyCycle(1)
    pwm.ChangeFrequency(1)
    assert True, "there really is much to sim here"


def test_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(1, GPIO.IN)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, True)
    GPIO.output(2, False)
    GPIO.getmode()
    input1 = GPIO.input(1)
    GPIO.cleanup()
    assert True


def test_picamera():
    im_shape = (10, 10)
    c = picamera.PiCamera()
    bgr = picamera.array.PiRGBArray(c, size=im_shape)
    # assert c.resolution == (100, 100)
    c.capture(1, 2, 3)
    im = bgr.array
    assert im.shape == im_shape
    bgr.truncate(0)
    assert True


def test_serial():
    s = serial.Serial()
    # try opening and it should fail
    s.port  = '/dev/serial'
    s.open()
    assert s.isOpen() is True
