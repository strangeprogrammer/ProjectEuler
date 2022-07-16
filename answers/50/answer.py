#!/usr/bin/env python3

from itertools import count

from primes import primes
from memoize import memoize
from gentools import threshLimit, ffable

def coordinateGen(bottom, top, delta0 = None):
	if delta0 is None:
		delta0 = top - bottom - 1
	for delta in range(delta0, -1, -1):
		for base in range(bottom, top - delta):
			yield [base, base + delta]

d = {}
@memoize(d)
def sumprimes(i, j):
	global d
	if (i, j + 1, ()) in d:
		return sumprimes(i, j + 1) - primes[j]
	elif (i - 1, j - 1, ()) in d:
		return sumprimes(i - 1, j - 1) - primes[i - 1] + primes[j - 1]
	else:
		return sum(primes[i:j])

def main():
	limit = 1000000
	
	checklist = ffable(coordinateGen(
		0,
		len(list(threshLimit(primes, limit))) + 1,
		delta0 = 700
	))
	
	for [i, j] in checklist:
		candidate = sumprimes(i, j)
		
		if limit <= candidate:
			checklist.ff(lambda t: t[0] == 0)
			continue
		
		if candidate in primes:
			return candidate

print(main())
