#!/usr/bin/env python3

def main():
	fibos = [1, 2]
	
	while fibos[-1] < 4000000:
		fibos.append(fibos[-1] + fibos[-2])
	
	return sum(filter(
		lambda x: x % 2 == 0,
		fibos
	))

print(main())
