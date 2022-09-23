#!/usr/bin/env python3

from fractions import Fraction
from operator import add, mul

def eulergen():
	yield 2
	
	k = 1
	while True:
		yield 1
		yield 2 * k
		k += 1
		yield 1

def backgen(g, n):
	for item in reversed(list(map(
		lambda t: t[0],
		zip(g, range(n))
	))):
		yield item

def main():
	approximation = Fraction(0)
	for item in backgen(eulergen(), 100):
		approximation = Fraction(1, item + approximation)
	
	approximation = 1 / approximation
	
	return sum(map(int,
		str(approximation.numerator)
	))

print(main())
