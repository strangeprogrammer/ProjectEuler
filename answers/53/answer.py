#!/usr/bin/env python3

# This is almost definitely *not* the most efficient way to solve this problem, but oh well.

from memoize import memoize

@memoize({})
def factorial(n):
	result = 1
	for i in range(1, n + 1):
		result *= i
	
	return result

def combinations(n, r):
	return factorial(n) / (factorial(r) * factorial(n - r))

def trianglegen(a, b):
	for i in range(a, b):
		for j in range(a, i):
			yield [i, j]

def main():
	return len(list(
		filter(
			lambda n: 1000000 < n,
			map(
				lambda t: combinations(*t),
				trianglegen(1, 101)
			)
		)
	))

print(main())
