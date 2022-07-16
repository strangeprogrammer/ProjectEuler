#!/bin/python3

from memoize import memoize

@memoize({})
def fibo(n):
	if n < 3:
		return 1
	else:
		return fibo(n - 1) + fibo(n - 2)

def mu(predicate, iterable):
	for n, e in enumerate(iterable):
		if predicate(e):
			return n
	return None

def genfibo():
	x = 0
	while True:
		yield fibo(x)
		x += 1

def main():
	return mu((lambda s: 999 < len(str(s))), genfibo())

print(main())
