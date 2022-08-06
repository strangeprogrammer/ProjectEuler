#!/usr/bin/env python3

from fractions import Fraction

def getexpansion():
	expansion = Fraction(2, 1)
	while True:
		expansion = 1 / expansion
		yield 1 + expansion
		expansion = 2 + expansion

def main():
	return len(list(filter(
		lambda t: len(str(t[0].denominator)) < len(str(t[0].numerator)),
		zip(getexpansion(), range(1, 1000))
	)))

print(main())
