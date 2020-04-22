#!/bin/sed -e 3q;d;

# Do not run this file directly - include it instead

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
	return sorted(divisors_(factor(n))[:-1])
