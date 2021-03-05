#!/usr/bin/env python3

from math import sqrt
from itertools import cycle

primes = [2, 3]

def isprime(n):
	global primes
	
	if primes[-1] < n:
		makeprimes(n)
	
	if n in primes:
		return True
	else:
		return False

def makeprimes(n):
	global primes
	
	for i in range(primes[-1] + 2, n, 2):
		canappend = True
		chkbound = sqrt(i)
		
		for j in primes:
			if chkbound < j: # We only need to search up through 'sqrt(i)' inclusive, since, if there is number that divides 'i' successfully, then there are actually 2 numbers that do so, 1 above or equal to 'sqrt(i)', and 1 below or equal to 'sqrt(i)'
				# canappend = True # This is technically redundant
				break
			elif i % j == 0: # 'i' is divisable by a prime, so it is not prime
				canappend = False
				break
		
		if canappend == True:
			primes.append(i)

def explode(n):
	return tuple(str(n))

def implode(r):
	return int(''.join(r))

def rotator(a):
	a = tuple(a)
	for i in range(len(a)):
		yield a[i:len(a)] + a[0:i]

# If there are any even digits, then at least one of the rotations won't be prime, so we disregard them
def oddfilter(a):
	return filter(
		lambda r: not any(map(
			lambda d: d in ['0', '2', '4', '6', '8'],
			explode(r))),
		a)

# If 0's could be included in valid rotations, we would have to worry, but they can't be, so we don't
def maprots(f, n):
	return map(lambda r: f(implode(r)),
		rotator(explode(n)))

def ensurerots(n, s):
	return all(maprots(lambda r: r in s, n))

def delrots(n, s):
	list(maprots(lambda r: s.discard(r), n)) # Calling 'list' removes laziness and forces action

def main():
	global primes
	makeprimes(1000000 + 1)
	
	s = {2} | set(oddfilter(primes)) # We have to add '2' back in since it gets removed by 'oddfilter'
	
	for n in s.copy(): # Use a copy of 's' since we mutate it within the loop
		ensurerots(n, s) or delrots(n, s)
	
	print(len(s))

if __name__ == "__main__":
	main()
