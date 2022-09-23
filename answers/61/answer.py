#!/usr/bin/env python3

from math import sqrt

from gentools import ffable

def istriangle(k):
#	k	== n * (n + 1) / 2
#	2 * k	== n ** 2 + n
#	0	== n ** 2 + n - 2 * k
#	n	== (-1 +- sqrt(1 - 4 * 1 * -2 * k)) / 2
#	n	== (-1 +- sqrt(1 + 8 * k)) / 2
#	The square-root term must be positive in order for 'n' to be a positive integer.
	n	= (-1 + sqrt(1 + 8 * k)) / 2
	
	return n == int(n)

def issquare(k):
	n = sqrt(k)
	return n == int(n)

def ispentagon(k):
#	k	== n * (3 * n - 1) / 2
#	2 * k	== 3 * n ** 2 - n
#	0	== 3 * n ** 2 - n - 2 * k
#	n	== (-(-1) +- sqrt((-1) ** 2 - 4 * 3 * -2 * k)) / (2 * 3)
#	n	== (1 +- sqrt(1 + 24 * k)) / 6
#	The square-root term must be positive in order for 'n' to be a positive integer.
	n	= (1 + sqrt(1 + 24 * k)) / 6
	
	return n == int(n)

def ishexagon(k):
#	k	== n * (2 * n - 1)
#	k	== 2 * n ** 2 - n
#	0	== 2 * n ** 2 - n - k
#	n	== (-(-1) +- sqrt((-1) ** 2 - 4 * 2 * -1 * k)) / (2 * 2)
#	n	== (1 +- sqrt(1 + 8 * k)) / 4
#	The square-root term must be positive in order for 'n' to be a positive integer.
	n	= (1 + sqrt(1 + 8 * k)) / 4
	
	return n == int(n)

def isheptagon(k):
#	k	== n * (5 * n - 3) / 2
#	2 * k	== 5 * n ** 2 - 3 * n
#	0	== 5 * n ** 2 - 3 * n - 2 * k
#	n	== (-(-3) +- sqrt((-3) ** 2 - 4 * 5 * -2 * k)) / (2 * 5)
#	n	== (3 +- sqrt(9 + 40 * k)) / 10
#	The square-root term must be positive in order for 'n' to be a positive integer.
	n	= (3 + sqrt(9 + 40 * k)) / 10
	
	return n == int(n)

def octagon():
	n = 1
	while True:
		yield n * (3 * n - 2)
		n += 1

def findlegs(k, fs):
	k = str(k)[0:2] # Get largest 2 digits
	for i in range(10, 99):
		candidate = int(str(i) + k)
		for f in fs:
			if f(candidate):
				yield [candidate, fs  ^ {f}]

def crawler(orig, k, fs0):
	# This is an interesting recursive function that will return a non-empty list iff it is part of a call branch which has reached the original octagonal number and every number in that call branch is one of the figurate numbers on the checklist.
	if len(fs0) == 0:
		if len(list(findlegs( # Is one of the legs the original?
			k,
			{lambda candidate: candidate == orig}
		))) == 1:
			return [k]
		return []
	else:
		for [candidate, fs] in findlegs(k, fs0):
			path = crawler(orig, candidate, fs)
			if path != []:
				return path + [k]
		return []

def main():
	# We iterate over the candidate octagonal numbers since they are the sparsest sequence which fulfills a checklist predicate (and thus helps minimize the search space).
	for k in ffable(octagon()).ff(lambda ki: 1010 <= ki): # 1010 is the first 4-digit number that can cycle only with other 4-digit numbers.
		path = crawler(k, k,
			{istriangle, issquare, ispentagon, ishexagon, isheptagon} # Checklist of figurate predicates
		)
		if path != []:
			return sum(path)

if __name__ == '__main__':
	print(main())
else:
	# Unit test against the data given by Project Euler
	def testfunc(f, l):
		assert all(map(
			f,
			l
		)), "Error testing function %s." % f.__name__
	testfunc(istriangle,	[1, 3, 6, 10, 15])
	testfunc(issquare,	[1, 4, 9, 16, 25])
	testfunc(ispentagon,	[1, 5, 12, 22, 35])
	testfunc(ishexagon,	[1, 6, 15, 28, 45])
	testfunc(isheptagon,	[1, 7, 18, 34, 55])
