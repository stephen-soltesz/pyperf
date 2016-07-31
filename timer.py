#!/usr/bin/python

import time

class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        self.usecs = self.secs * 1000000  # microseconds
        self.nsecs = self.secs * 1000000000  # nanoseconds
        if self.verbose:
            print 'elapsed time: %f ms' % self.msecs
