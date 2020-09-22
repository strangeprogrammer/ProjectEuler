#!/bin/python3

from memoize import memoize
from factors import pfactor_, pfactor

pfactor_ = memoize({})(pfactor_)

@memoize({})
def isprime(n):
	return pfactor(n) == [(n, 1)]

import itertools
from mu import mu

scorepoly = lambda a, b: mu((lambda n: not isprime(n * (n + a) + b)), itertools.count())

def main():
	curmax = 0
	
	for a, b in itertools.product(range(-999, 1000), range(-1000, 1001)):
		s = scorepoly(a, b)
		if curmax < s:
			curmax = s
			ma, mb = a, b
	
	return ma * mb

print(main())
