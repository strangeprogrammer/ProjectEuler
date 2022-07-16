#!/bin/python3

__all__ = [
	'multiGen',
	'threshLimit',
	'ffable',
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

class ffable:
	# Fast-Forward-able
	def __init__(self, gen):
		self.gen = iter(gen)
		[self.recent, self.forwarded] = [None, False]
	
	def __iter__(self): return self
	
	def __next__(self):
		if self.forwarded:
			self.forwarded = False
			return self.recent
		else:
			return next(self.gen)
	
	def ff(self, predicate):
		for item in self.gen:
			if predicate(item):
				[self.recent, self.forwarded] = [item, True]
				break
