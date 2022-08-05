#!/usr/bin/env python3

from itertools import combinations

from primes import primes

def findgroups(n):
	tracker = {
		'0': [],
		'1': [],
		'2': [],
		'3': [],
		'4': [],
		'5': [],
		'6': [],
		'7': [],
		'8': [],
		'9': [],
	}
	
	for [index, digit] in enumerate(str(n)):
		tracker[digit] += [index]
	
	return list(filter(
		lambda v: 0 < len(v),
		tracker.values()
	))

def getreplacements(prime, indeces):
	if any(map(
		lambda index: index == len(str(prime)) - 1,
		indeces
	)):
		return [1, 3, 7, 9]
	if any(map(
		lambda index: index == 0,
		indeces
	)):
		return [1, 2, 3, 4, 5, 6, 7, 8, 9]
	else:
		return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def doreplacement(n, indeces, replacement):
	n = list(str(n))
	replacement = str(replacement)
	
	for index in indeces:
		n[index] = replacement
	
	return int(''.join(n))

def identifyfamilies(prime, groups):
	families = []
	for group in groups:
		for numindeces in range(1, len(group) + 1):
			for indeces in combinations(group, numindeces):
				families += [set()]
				
				for replacement in getreplacements(prime, indeces):
					candidate = doreplacement(prime, indeces, replacement)
					if candidate in primes:
						families[-1] |= {candidate}
	
	return families

def main():
	for prime in primes:
		g = findgroups(prime)
		if len(g) == 0:
			continue
		
		families = identifyfamilies(prime, g)
		for family in families:
			if len(family) == 8:
				return sorted(family)[0]

print(main())
