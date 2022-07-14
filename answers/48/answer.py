#!/usr/bin/env python3

# Let the least ten digits of any number be known as the 'digit space'.

# The first thing to note about this problem is that every term with a mantissa divisible by 10 in the series doesn't contribute to the digit space of the total since that term's final product will contain only 0's in the digit space. Thus, we can simply skip these terms entirely when trying to find the answer.

# The second thing to note about this problem is that, when calculating the value for a term, if some of the digits of a multiplication sub-calculation fall outside of the digit space, then those digits can be disregarded when continuing the calculation since their multiplication will never again affect the digit space.

# Note that, though there are other optimizations that can be made, such as memoization of powers and digit space cyclicality discoverey, these optimizations likely wouldn't significantly impact the running time of this solution, and I'm too lazy to implement them right now.

from itertools import dropwhile

digitspace = 10 ** 10

def slowpower(n):
	global digitspace
	
	product = 1
	for garbage in range(0, n):
		product *= n
		if digitspace <= product:
			product %= digitspace
	
	return product

def main():
	global digitspace
	
	return sum(map(
		slowpower,
		dropwhile(
			lambda x: x % 10 == 0,
			range(1, 1000 + 1)
		)
	)) % digitspace

print(main())
