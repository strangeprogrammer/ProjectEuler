#!/usr/bin/env sed -e 3q;d;

# DO NOT RUN THIS FILE DIRECTLY - import it instead

from math import sqrt

__all__ = [
	'primes',
	'isPrime',
	'makePrimes',
]

rawprimes = [2, 3, 5, 7, 11]

class primesproxy:
	def __init__(self):
		global rawprimes
		self.p = rawprimes
	
	def _genindex(self, i):
		while len(self.p) < i + 1:
			makePrime()
	
	def __get__(self, i):
		self._genindex(i)
		return self.p[i]
	
	def __set__(self, i, v):
		self._genindex(i)
		self.p[i] = v
	
	def __iter__(self):
		i = 0
		while True:
			yield self.__get__(i)
			i += 1
	
	def __contains__(self, x):
		makePrimes(x)
		return x in self.p

primes = primesproxy()

def isPrime(n):
	global rawprimes
	
	makePrimes(n)
	
	return n in rawprimes

def makePrimes(n):
	global rawprimes
	while rawprimes[-1] < n:
		makePrime()

def makePrime():
	global rawprimes
	
	i = rawprimes[-1] + 2
	while True:
		canappend = True
		chkbound = sqrt(i)
		
		for j in rawprimes:
			if chkbound < j: # We only need to search up through 'sqrt(i)' inclusive, since, if there is number that divides 'i' successfully, then there are actually 2 numbers that do so, 1 above or equal to 'sqrt(i)', and 1 below or equal to 'sqrt(i)'
				# canappend = True # This is technically redundant
				break
			elif i % j == 0: # 'i' is divisable by a prime, so it is not prime
				canappend = False
				break
		
		if canappend:
			rawprimes.append(i)
			return
		else:
			i += 2
