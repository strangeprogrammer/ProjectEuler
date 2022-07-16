#!/bin/python3

from memoize import memoize

def addfactor(n, d):
	if n in d:
		d[n] += 1
	else:
		d[n] = 1

import math

def factor(n):
	factors = {}
	contflag = True
	while n > 1 and contflag:
		contflag = False
		for i in range(2, math.floor(math.sqrt(n)) + 1):
			if n % i == 0:
				addfactor(i, factors)
				n = int(n / i)
				contflag = True
				break
	
	if n > 1:
		addfactor(n, factors)
	
	return list(factors.items())

import itertools

def divisors_(d):
	try:
		k, v = d.pop()
	except IndexError:
		return [1]
	divs = []
	for i in range(0, v + 1):
		divs.append(k ** i)
	return list(map((lambda t: t[0] * t[1]), itertools.product(divs, divisors_(d))))

def divisors(n):
	return sorted(divisors_(factor(n))[:-1])

@memoize({})
def getsumdivs(n):
	return sum(divisors(n))

amicables = {}

@memoize(amicables)
def isamicable(n):
	if n == getsumdivs(n):
		return False
	elif n == getsumdivs(getsumdivs(n)):
		return True
	else:
		return False

def main():
	return sum([ i for i in range(1, 10000) if isamicable(i) ])

print(main())
