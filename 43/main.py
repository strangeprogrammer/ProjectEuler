#!/bin/python3

from itertools import permutations as perms
from functools import reduce as reduce

def maybePan(candidate):
	try:
		digits = {*list(range(10))}		# Make a set containing every digit
		
		for digit in candidate:			# Ensure that each digit only occurs 1 time at maximum
			digits.remove(int(digit))	#
		
		return True				# If no digit occurred more than once, this *could* possibly form a pandigital number
	except:
		return False				# If any digit occurred more than once, this can't possibly form a pandigital number

def initCandidates():
	return map(
		lambda t: ''.join(map(
			str,
			t
		)),
		perms(
			range(10),
			3
		)
	)

def filterPan(candidates):
	for candidate in candidates:
		if maybePan(candidate):
			yield candidate

def filterPrime(candidates, prime):
	for candidate in candidates:
		if int(candidate[:3]) % prime == 0:
			yield candidate

def addRound(candidates):
	for candidate in candidates:
		for i in range(10):
			yield str(i) + candidate

def doRound(candidates, prime):
	return filterPan(
		addRound(
			filterPrime(
				candidates,
				prime
			)
		)
	)

def main():
	return sum(map(
		int,
		reduce(
			lambda candidates, p: doRound(candidates, p),
			[
				17,
				13,
				11,
				7,
				5,
				3,
				2,
			],
			initCandidates()
		)
	))

print(main())
