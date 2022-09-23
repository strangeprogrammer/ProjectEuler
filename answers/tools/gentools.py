#!/usr/bin/env sed -e 3q;d

# DO NOT RUN THIS FILE - Import it instead

__all__ = [
	'multiGen',
	'threshLimit',
	'ffable',
	'indexable',
	'lazylenlt',
	'lazylenge',
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
		if self.forwarded and predicate(self.recent):
			return self
		
		for item in self.gen:
			if predicate(item):
				[self.recent, self.forwarded] = [item, True]
				break
		return self

class indexable():
	def __init__(self, gen):
		if type(gen) == str:
			raise Exception("This class cannot be used with 'str' type objects since they are concatenated atypically in python.")
		self.gen = iter(gen)
		self.nextidx = 0
		self.extracted = []
	
	def reset(self):
		self.nextidx = 0
		return self
	
	def __iter__(self): return self
	
	def _generate(self):
		try:
			self.extracted.append(next(self.gen))
			return True
		except StopIteration:
			return False
	
	def __len__(self): # NOTE: 'indexable.__len__' and 'indexable.__getitem__' are co-recursive
		while self._generate(): pass
		return len(self.extracted)
	
	def __getitem__(self, i): # NOTE: 'indexable.__len__' and 'indexable.__getitem__' are co-recursive
		if type(i) == slice:
			if i.start < 0 or i.stop < 0:
				i = slice(*i.indices(len(self)))
			
			end = max(i.start, i.stop)
		else:
			end = i + 1
		
		for garbage in range(len(self.extracted), end):
			if not self._generate():
				break
		
		return self.extracted[i] # If the generator had fewer than 'i' elements, a simple 'IndexError' will be thrown
	
	def __next__(self):
		try:
			retval = self[self.nextidx]
		except IndexError:
			raise StopIteration()
		
		self.nextidx += 1
		return retval

def lazylenlt(x, gen): # WARNING: This function WILL advance the iterable that it operates upon
	try:
		for garbage in range(x):
			next(gen)
	except StopIteration:
		return True
	
	return False

def lazylenge(x, gen): # WARNING: This function WILL advance the iterable that it operates upon
	return not lazylenlt(x, gen)
