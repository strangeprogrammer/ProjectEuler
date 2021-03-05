#!/bin/python3

import itertools

# The search space could definately be optimized by observing that the number of digits in the product of 2 integers is no more than the sum of the number of digits of those 2 integers (can be shown using logarithms)

def converter(chararr): return int(''.join(chararr))

def main():
	jumbles = itertools.permutations(map(str, range(1, 9 + 1)))
	
	print(sum({
		converter(j[epos:])
		for j in jumbles
		for mpos in range(1, len(j) - 2)
		for epos in range(mpos + 1, len(j) - 1)
		if converter(j[:mpos]) * converter(j[mpos:epos]) == converter(j[epos:])
	}))

main()
