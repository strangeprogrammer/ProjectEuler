#!/bin/python3

denominations = [
	200,
	100,
	50,
	20,
	10,
	5,
	2,
	1,
]

def numdenoms_(index, n):
	if len(denominations) <= index or n < 0:
		return 0
	
	if n == 0:
		return 1
	
	return sum([
		numdenoms_(dex, n - val)
		for [dex, val]
		in enumerate(denominations)
		if index <= dex
	])

def numdenoms(n): return numdenoms_(0, n)

def main():
	print(numdenoms(200))

main()
