#!/bin/python3

# Suppose that we want to form a predicate indicating whether or not an input value 'P_n' is a Pentagonal Number. Then, we should be able to take the function inverse of 'P_n' and find a positive integer:
#	P_n	= n * (3 * n - 1) / 2
#	2 * P_n	= n * (3 * n - 1)
#	2 * P_n	= 3 * n ** 2 - n
#	0	= 3 * n ** 2 - n - 2 * P_n
#	n	= (-(-1) +- sqrt((-1)**2 - 4 * 3 * (-2 * P_n))) / (2 * 3)
#	n	= (1 +- sqrt(1 + 24 * P_n)) / 6
# Note that we can simply drop the '-' in this expression since not doing so would result in either some fraction or a negative number:
#	n	= (1 + sqrt(1 + 24 * P_n)) / 6
# Furthermore, since the sub-expression:
#	k	= sqrt(1 + 24 * P_n)
# Must equal 5 (mod 6) for 'n' to result in an integer, we can simply check whether or not 'k' fulfills this modular property instead of checking whether or not 'n' is an integer.

from math import sqrt

def triangleGen(n):
	for i in range(1, n):
		for j in range(1, i):
			yield (i, j)

def penta(n):
	return n * (3 * n - 1) // 2

def ispenta(pn):
	k = sqrt(1 + 24 * pn)
	if k % 6 == 5:
		return True
	else:
		return False

def main():
	[[x, y]] = list(filter(
		lambda t: ispenta(t[0] + t[1]),
		filter(
			lambda t: ispenta(t[0] - t[1]),
			map(
				lambda t: (penta(t[0]), penta(t[1])),
				triangleGen(10000)
			)
		)
	))
	return x - y

print(main())
