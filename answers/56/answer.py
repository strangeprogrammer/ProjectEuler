#!/usr/bin/env python3

import itertools

def digitsum(n):
	return sum(map(
		int,
		list(str(n))
	))

def main():
	return max(map(
		lambda t: digitsum(t[0] ** t[1]),
		itertools.product(
			range(1, 100),
			repeat = 2
		)
	))

print(main())
