#!/bin/python3

from misc import mu

def divchain(n, d, l):
	if n == 0 :
		return 0
	r = n % d * 10 # Pseudo-remainder
	i = mu(lambda x: x == r, l)
	if i is not None:
		return len(l) - i
	return divchain(r, d, l + [r])

main = lambda: max(range(2, 1000), key = (lambda d: divchain(1, d, [])))

print(main())
