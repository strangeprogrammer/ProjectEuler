#!/bin/python

from math import sqrt as sqrt
from math import floor as floor

def trianglenum():
	curnat = 2
	curtri = 1
	while True:
		yield curtri
		curtri += curnat
		curnat += 1

def addfactor(n, d):
	if n in d:
		d[n] += 1
	else:
		d[n] = 1

def factor(x):
	factors = {}
	contflag = True
	while x > 1 and contflag:
		contflag = False
		for i in range(2, floor(sqrt(x)) + 1):
			if x % i == 0:
				addfactor(i, factors)
				x = int(x / i)
				contflag = True
				break
	
	if x > 1:
		addfactor(x, factors)
	
	return factors

def dictinc1(indict):
	for i in indict:
		indict[i] += 1
	
	return indict

def dictdec1(indict):
	for i in indict:
		indict[i] -= 1
	
	return indict

def proddict(d):
	prod = 1
	for i in d.values():
		prod *= i
	
	return prod

def pdicttonum(d):
	prod = 1
	for k, v in d.items():
		prod *= k ** v
	
	return prod

def main():
	factors = {}
	t = trianglenum()
	while proddict(dictinc1(factors)) < 500: # It's hard to explain
		factors = factor(t.__next__())
	
	return pdicttonum(dictdec1(factors))

print(main())
