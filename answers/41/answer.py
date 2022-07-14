#!/bin/python3

# The largest pseudo-pandigital number that can exist is '987654321', so this is the upmost limit upon the search space. However,
#	987654321 % 3 == 0
# And, furthermore, if the sum of a number's digits is divisible by 3, then so is the number itself. Thus, since the sum of any re-arrangement of this upper-limit pseudo-pandigital's digits has the same value, that rearrangement must also be divisible by 3. Thus, no rearrangement of this upmost limit is prime, so no number with 9 digits can be considered as the greatest pseudo-pandigital number. Thus, the upper search limit for the greatest pseudo-pandigital number must actually be '87654321' (over an order of magnitude less).
# However, the pseudo-pandigital number '87654321' also has this property, so that would make the *true* upper limit to the search space '7654321', since it does *not* fulfill this property (over 2 orders of magnitude less!).
# This property is also exploited with some other, lower-value pseudo-pandigital numbers as well.

from math import sqrt
from itertools import permutations

primes = [2, 3, 5, 7, 11]

#def genLimit(g, n):
#	for i, v in zip(range(n), g):
#		yield v

def isPrime(n):
	global primes
	
	while primes[-1] < sqrt(n):
		makePrime()
	
	if any(map(
		lambda p: n % p == 0,
		primes
	)):
		return False
	else:
		return True

def makePrime():
	global primes
	
	i = primes[-1] + 2
	while True:
		canappend = True
		chkbound = sqrt(i)
		
		for j in primes:
			if chkbound < j: # We only need to search up through 'sqrt(i)' inclusive, since, if there is number that divides 'i' successfully, then there are actually 2 numbers that do so, 1 above or equal to 'sqrt(i)', and 1 below or equal to 'sqrt(i)'
				# canappend = True # This is technically redundant
				break
			elif i % j == 0: # 'i' is divisable by a prime, so it is not prime
				canappend = False
				break
		
		if canappend:
			primes.append(i)
			return
		else:
			i += 2

#def isPPandig(n):
#	"""isPseudoPandigital"""
#	n = str(n)
#	
#	# Create a set to keep track of each relevant digit
#	s = {
#		list(map(
#			str,
#			range(1, len(n) + 1)
#		))
#	}
#	
#	# If there are any digits in 'n' which are greater than its length, it can't be pseudo-pandigital
#	try:
#		for digit in n:
#			s.remove(digit)
#	except:
#		return False
#	
#	# If 'n' is pseudo-pandigital, it should contain all of the relevant digits exactly once, so nothing should be left in 's'
#	return len(s) == 0

def multiGen(*gens):
	for g in gens:
		for v in g:
			yield v

def main():
	global primes
	
	return max(
		filter(
			lambda suspect: isPrime(suspect),
			map(
				lambda suspect: int(''.join(suspect)),
				multiGen(
					# permutations('987654321'),
					# permutations('87654321'),
					permutations('7654321'),
					# permutations('654321'),
					# permutations('54321'),
					permutations('4321'),
					# permutations('321'),
					# permutations('21'),
					permutations('1'),
				)
			)
		)
	)

print(main())
