#!/bin/python3

__all__ = [
	'multiGen',
]

def multiGen(*gens):
	for g in gens:
		for v in g:
			yield v
