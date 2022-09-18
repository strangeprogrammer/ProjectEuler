#!/usr/bin/env sed -e 3q;d;

# DO NOT RUN THIS FILE DIRECTLY - import it instead

from math import sqrt

__all__ = [
	'primes',
	'isPrime',
	'makePrimes',
]

rawprimes = [2, 3, 5, 7, 11]
primesset = set(rawprimes)

class primesproxy:
	def __init__(self):
		global rawprimes, primesset
		self.p = rawprimes
		self.q = primesset
	
	def _genindex(self, i):
		while len(self.p) < i + 1:
			makePrime()
	
	def __getitem__(self, i):
		if type(i) == slice:
			if i.stop < i.start:
				self._genindex(i.start)
			else:
				self._genindex(i.stop)
			return self.p[i]
		else:
			self._genindex(i)
			return self.p[i]
	
	def __iter__(self):
		i = 0
		while True:
			yield self[i]
			i += 1
	
	def __contains__(self, x):
		if x < 1000000:
			makePrimes(x)
			return x in self.q
		else:
			i = 0
			limit = sqrt(x) + 1
			makePrimes(limit)
			while self[i] < limit:
				if x % self[i] == 0:
					return False
				i += 1
			return True

primes = primesproxy()

def isPrime(n):
	global primesset
	
	makePrimes(n)
	
	return n in primesset

def makePrimes(n):
	global rawprimes
	while rawprimes[-1] < n:
		makePrime()

def makePrime():
	global rawprimes, primesset
	
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
			rawprimes += [i]
			primesset |= {i}
			return
		else:
			i += 2
