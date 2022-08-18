#!/usr/bin/env python3

from itertools import count
from itertools import takewhile

from primes import primes

def spiralcorners():
	sizegen = count(1, step = 2)
	sidedeltagen = count(0, step = 2)
	
	next(sidedeltagen)
	next(sizegen)
	
	while True:
		size = next(sizegen)
		sidedelta = next(sidedeltagen)
		value = size ** 2
		yield [
			size,
			value - 3 * sidedelta,
			value - 2 * sidedelta,
			value - 1 * sidedelta,
			#yield [size, value - 0 * sidedelta]	# Skip all numbers which are known squares
		]

def main():
	corners = spiralcorners()
	
	diagallcnt = 1
	diagprimescnt = 0
	
	while True:
		[size, a, b, c] = next(corners)
#		print('------------')
#		print(size)
#		print(a)
#		print(b)
#		print(c)
		
		diagallcnt += 4 # Implicitly also count each square number, which wouldn't've been returned by 'spiralcorners'
		
		if a in primes:
			diagprimescnt += 1
		if b in primes:
			diagprimescnt += 1
		if c in primes:
			diagprimescnt += 1
		
		if diagprimescnt / diagallcnt < 0.1:
			return size

print(main())
