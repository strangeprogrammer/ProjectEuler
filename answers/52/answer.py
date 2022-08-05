#!/usr/bin/env python3

from itertools import count

def listdigits(n):
	return sorted(list(str(n)))

def main():
	for n in count(1):
		if listdigits(n)	\
		== listdigits(n * 2)	\
		== listdigits(n * 3)	\
		== listdigits(n * 4)	\
		== listdigits(n * 5)	\
		== listdigits(n * 6):
			return n

print(main())
