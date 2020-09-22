#!/bin/sed -e 3q;d;

# Do not run this file directly - include it instead

def addfactor(n, d):
	if n in d:
		d[n] += 1
	else:
		d[n] = 1

import math

def pfactor_(n):
	if n <= 1:
		return []
	
	divisor = n
	for i in range(2, math.floor(math.sqrt(n)) + 1):
		if n % i == 0:
			divisor = i
			break
	
	return [divisor, *pfactor_(n // divisor)]

import itertools

def pfactor(n):
	if n == 1:
		return [(1, 1)]
	l0 = sorted(pfactor_(n))
	facts = []
	while 0 < len(l0):
		l1 = list(itertools.dropwhile(lambda x: x == l0[0], l0))
		facts.append((l0[0], len(l0) - len(l1)))
		l0 = l1
	
	return facts

import operator

def divisors_(d):
	try:
		k, v = d.pop()
	except IndexError:
		return [1]
	divs = []
	for i in range(0, v + 1):
		divs.append(k ** i)
	return list(itertools.starmap(operator.mul, itertools.product(divs, divisors_(d))))

def divisors(n):
	return sorted(divisors_(pfactor(n))[:-1])
