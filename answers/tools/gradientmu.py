#!/usr/bin/env sed -e 3q;d

# DO NOT RUN THIS FILE - Import it instead

from itertools import count

# WARNING: Every function in this file assumes that the input list is sorted; specifically that there are some sublists 'j' and 'k' such that:
# 	j + k == l
# And the following is always true:
#	not any(map(predicate, j)) and all(map(predicate, k))

def expmu(l, predicate):
	for exp in count():
		i = 2 ** exp - 1
		if predicate(l[i]):
			return i

def binarymu(l, lo, hi, predicate):
	# We assume that there is at least 1 'e' in 'l' for which the predicate is true.
	# At the beginning of the function, we assume that:
	#	not predicate(l[lo]) and predicate(l[hi])
	
	while lo < hi:
		midpoint = (lo + hi) // 2
		if predicate(l[midpoint]):
			# First 'e' is at or below midpoint
			hi = midpoint # We intentionally don't use 'hi = midpoint - 1' since progress was already guaranteed during the midpoint calculation, and since the first 'e' could be at the midpoint already
			continue
		else: # not predicate(l[midpoint]):
			# First 'e' is above midpoint
			lo = midpoint + 1
			continue
	
	return lo # Eventually, 'lo' will contain the index of the first 'e' by either natural course, or by having been 1 less than 'hi' 1 step earlier

def mu(l, predicate):
	# Return the first index 'i' where 'predicate(l[i]) == True', as well as a flag indicating whether or not any 'l[i]' actually qualified
	hi = expmu(l, predicate)
	lo = (hi + 1) // 2 - 1
	i = binarymu(l, lo, hi, predicate)
	return [i, predicate(l[i])]
