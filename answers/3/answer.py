#!/usr/bin/env python3

from itertools import count

def divideit(todiv):
	alldivs = []
	
	while 1 < todiv:
		for divisor in count(2):
			if todiv % divisor == 0:
				alldivs.append(divisor)
				todiv //= divisor
				break # Continue the outer loop, not the inner one
	
	return alldivs

def main():
	return sorted(divideit(600851475143))[-1]

print(main())
