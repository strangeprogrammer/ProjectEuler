#!/bin/python3

import itertools

def main():
	return ''.join(map(str, sorted(itertools.permutations(range(10), 10))[999999]))

print(main())
