###############################################
# The MIT License (MIT)
# Copyright (c) 2017 Kevin Walchko
# see LICENSE for full details
##############################################

class Base(object):
    def __init__(self, name=None):
        print('<<< WARNING: using fake raspberry pi interfaces >>>')
        if name:
            print('<<< Using: {} >>>'.format(name))
