#!/bin/python3

from itertools import product
from fractions import Fraction
from functools import reduce
from operator import mul

def main():
	allfracs = []
	
	for [i, j, k, l] in product(
		range(1, 10),
		range(0, 10),
		range(1, 10),
		range(0, 10),
	):
		x = Fraction(10 * i + j, 10 * k + l)
		if 0 < 10 * k + l \
		and not (j == 0 and l == 0) \
		and x < 1 \
		and any([
			k != 0 and j == l and x == Fraction(i, k),
			l != 0 and j == k and x == Fraction(i, l),
			k != 0 and i == l and x == Fraction(j, k),
			l != 0 and i == k and x == Fraction(j, l),
		]):
			allfracs.append(x)
	
	print(reduce(
		mul,
		allfracs,
		1,
	).denominator)

main()
