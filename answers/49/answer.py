#!/usr/bin/env python3

from itertools import product

from primes import primes
from gentools import threshLimit

def ispermut(t):
	key = sorted(str(t[0]))
	for item in t[1:]:
		if sorted(str(item)) != key:
			return False
	
	return True

def main():
	lowerbound = 1000
	upperbound = 10000
	
	searchspace = filter(
		lambda x: x >= lowerbound,
		threshLimit(primes, upperbound)
	)
	
	[x, y] = filter(
		lambda t: t[2] < upperbound and ispermut(t) and t[2] in primes,
		map(
			lambda t: [t[0], t[1], t[1] + t[1] - t[0]],
			filter(
				lambda t: t[0] < t[1],
				product(
					searchspace,
					repeat = 2
				)
			)
		)
	)
	
	choice = x
	if 1487 in x:
		choice = y
	
	return ''.join(map(str, sorted(choice)))

print(main())
