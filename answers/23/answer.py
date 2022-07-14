#!/bin/python3

import factors

def isabundant(n):
	if sum(factors.divisors(n)) > n:
		return True
	else:
		return False

findabundants = lambda n: set(filter(isabundant, range(1, n)))

import itertools
import operator

def findabundsums(n):
	fa = findabundants(n)
	return set(itertools.starmap(operator.add, itertools.product(fa, fa)))

findnonsums = lambda n: set(range(1, 2 * n)) - set(findabundsums(n))

def main():
	return sum(filter(lambda x: x < 28124, findnonsums(28124)))

print(main())
