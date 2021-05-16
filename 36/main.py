#!/usr/bin/env python3

def explodeInt(n):
	return tuple(str(n))

def implodeInt(r):
	return int(''.join(r))

def lIsPalindrome(l):
	l = tuple(l)
	return l == tuple(reversed(l))

def main():
	result = []
	for i in range(1, 1000000):
		if i % 10 == 0 \
		or i % 2 == 0: # Skip anything with a leading zero, which would occur whenever there is a trailing zero
			continue
		elif lIsPalindrome(bin(i)[2:]) \
		and lIsPalindrome(explodeInt(i)): # https://stackoverflow.com/a/3647418
			result.append(i)
	return sum(result)

print(main())
