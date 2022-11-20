#!/bin/python3

def main():
	for i in range(1, 1001):
		for j in range(1, 1001 - i):
			k = 1000 - j - i
			if i ** 2 + j ** 2 == k ** 2:
				return i * j * k

print(main())
