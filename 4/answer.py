#!/bin/python3

from math import floor

def chopnum(x):
	if x == 0:
		return []
	
	d = floor(x / 10)
	r = x % 10
	return [*chopnum(d), r]

def searcher():
	maximum = 0
	
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			totem = i * j
			
			if chopnum(totem) == chopnum(totem)[::-1] and totem > maximum:
				maximum = totem
	
	return maximum

print(searcher())
