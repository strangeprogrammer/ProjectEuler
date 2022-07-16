#!/usr/bin/env sed -e 3q;d;

# DO NOT RUN THIS FILE DIRECTLY - import it instead

from primes import primes
from gentools import threshLimit

from itertools import dropwhile, starmap, product
import operator
from math import sqrt

__all__ = [
	'factors',
	'divisors',
]

def factors_(n):
	global primes
	
	if n <= 1:
		return []
	
	divisor = n
	for i in threshLimit(primes, sqrt(n) + 1):
		if n % i == 0:
			divisor = i
			break
	
	return [divisor, *factors_(n // divisor)]

def factors(n):
	if n == 1:
		return [(1, 1)]
	l0 = sorted(factors_(n))
	facts = []
	while 0 < len(l0):
		l1 = list(
			dropwhile(
				lambda x: x == l0[0],
				l0
			)
		)
		facts.append((l0[0], len(l0) - len(l1)))
		l0 = l1
	
	return facts

def divisors_(facts):
	try:
		prime, exp = facts.pop()
	except IndexError:
		return [1]
	divs = []
	for i in range(0, exp + 1):
		divs.append(prime ** i)
	return starmap(
		operator.mul,
		product(
			divs,
			divisors_(facts)
		)
	)

def divisors(n):
	return sorted(divisors_(factors(n)))
