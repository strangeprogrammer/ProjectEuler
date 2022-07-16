#!/bin/python3

from math import sqrt as sqrt

primes = [2, 3]

def isprimenow(x):
	for i in primes:
		if i > sqrt(x):
			break
		
		if x % i == 0:
			return False
	
	return True

def makeprime():
	global primes
	searched = primes[-1] + 2
	
	while not isprimenow(searched):
		searched += 2
	
	primes.append(searched)

def makeprimes(cutoff):
	global primes
	while primes[-1] < cutoff:
		makeprime()

makeprimes(2000000)
print(sum(primes[:-1]))
