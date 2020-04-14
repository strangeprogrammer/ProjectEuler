#!/bin/python3

def factorial(n):
	product = 1
	for i in range(1, n + 1):
		product *= i
	return product

def main():
	return sum(map(lambda c: int(c), str(factorial(100)))) # Arbitrary-precision arithmetic is very nice

print(main())
