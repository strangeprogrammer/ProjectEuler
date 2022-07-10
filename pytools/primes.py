#!/bin/python3

from math import sqrt

__all__ = [
	'primes',
	'isPrime',
	'makePrimes',
]

primes = [2, 3, 5, 7, 11]

def isPrime(n):
	global primes
	
	makePrimes(n)
	
	return n in primes

def makePrimes(n):
	global primes
	while primes[-1] < n:
		makePrime()

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
