from fake_rpi import smbus


def test_smbus():
	i2c = smbus.SMBus(1)
	ret = i2c.read_byte_data(1, 2)
	assert isinstance(ret, int)
	# assert False
