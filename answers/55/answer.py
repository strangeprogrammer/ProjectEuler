#!/usr/bin/env python3

def ispalindrome(s):
	i = 0
	j = len(s) - 1
	while i < j:
		if s[i] != s[j]:
			return False
		i += 1
		j -= 1
	
	return True

def flipdigits(n):
	return int(''.join(list(
		reversed(str(n))
	)))

def isLychrel(n):
	for garbage in range(50):
		n += flipdigits(n)
		if ispalindrome(str(n)):
			return False
	
	return True

def main():
	return len(list(filter(
		lambda n: isLychrel(n),
		range(1, 10000)
	)))

print(main())
