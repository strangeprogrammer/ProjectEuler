#!/usr/bin/env python3

from math import sqrt

primes = [2, 3, 5, 7, 11]

def isPrime(n):
	global primes
	
	while primes[-1] < n:
		makePrime()
	
	if n in primes:
		return True
	else:
		return False

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

def explodeInt(n):
	return tuple(str(n))

def implodeInt(r):
	return int(''.join(r))

def lrTrunc(n):
	narr = explodeInt(n)
	
	return all(map(
		lambda n: isPrime(implodeInt(n)),
		map( # Omits the empty explosion and the full explosion
			lambda i: narr[i:],
			range(1, len(narr))
		)
	))

def rlTrunc(n):
	narr = explodeInt(n)
	
	return all(map(
		lambda n: isPrime(implodeInt(n)),
		map( # Omits the empty explosion and the full explosion
			lambda i: narr[:i],
			range(1, len(narr))
		)
	))

def main():
	global primes
	tprimes = []
	
	while len(tprimes) < 11:
		n = primes[-1]
		
		if lrTrunc(n) and rlTrunc(n): # We don't need to check that 'n' is prime since it came directly from 'primes'
			tprimes.append(n)
		
		makePrime()
	
	return sum(tprimes)

print(main())
