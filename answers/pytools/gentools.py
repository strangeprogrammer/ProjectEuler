#!/bin/python3

__all__ = [
	'multiGen',
	'threshLimit',
]

def multiGen(*gens):
	for g in gens:
		for v in g:
			yield v

def threshLimit(it, top):
	# Limit an iterable's contents based upon some threshhold.
        for x in it:
                if x < top:
                        yield x
                else:
                        break
