#!/usr/bin/env python3

from itertools import count
from math import sqrt

from primes import *
from gentools import threshLimit

def main():
	for i in count(3, 2):
		flag = False
		# makePrimes(i) # This call is redundant, but useful for legibility
		if isPrime(i):
			continue
		
		for prime in threshLimit(primes, i):
			subtotal = (i - prime) / 2
			sq = sqrt(subtotal)
			if sq == int(sq):
				flag = True
				break
		
		if not flag:
			return i

print(main())
