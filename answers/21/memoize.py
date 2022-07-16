#!/bin/python3

def freezeargs(*args):
	try:
		hash(args)
		return args
	except:
		if isinstance(args[0], dict):
			thispart = frozenset({*freezeargs(*(args[0].items()))})
		elif isinstance(args[0], set):
			thispart = frozenset({*freezeargs(*args[0])})
		elif isinstance(args[0], list):
			thispart = freezeargs(*args[0])
		else:
			thispart = args[0]
		return (thispart, *freezeargs(*args[1:]))

def freezeallargs(*args, **kwargs):
	return freezeargs(*args) + freezeargs(tuple(kwargs.items()))

def memoize(d):
	def memoize_internal(f):
		def wrapper(*args, **kwargs):
			k = freezeallargs(*args, **kwargs)
			
			if k in d:
				return d[k]
			else:
				v = f(*args, **kwargs)
				d[k] = v
				return v
		
		return wrapper
	
	return memoize_internal

# Tests for 'freezeargs'

if __name__ == "__main__":
	
	testnumstart = 0
	def testnum():
		global testnumstart
		testnumstart += 1
		return testnumstart
	
	def deathstr(n, e, args, r):
		return "Failed test %d...\n" % n + "e was: " + str(e) + "\n" + "args was: " + str(args) + "\n" + "r was: " + str(r) + "\n"
	
	def dotest(e, args):
		n = testnum()
		# print("TEST %d:" % n)
		r = freezeargs(*args)
		assert r == e, deathstr(n, e, args, r)
	
	def testing():
		
		e = ()
		args = ()
		dotest(e, args)
		
		e = (132, 534)
		args = (132, 534)
		dotest(e, args)
		
		e = ((4, 5, 6),)
		args = ((4, 5, 6),)
		dotest(e, args)
		
		e = ((4, 5, 6),)
		args = ([4, 5, 6],)
		dotest(e, args)
		
		e = (frozenset({'a', 'b'}),)
		args = ({'a', 'b'},)
		dotest(e, args)
		
		e = (frozenset({'a', 'b'}),)
		args = (frozenset({'a', 'b'}),)
		dotest(e, args)
		
		e = (frozenset({('a', 1), ('b', 2)}),)
		args = ({'a': 1, 'b': 2},)
		dotest(e, args)
		
		e = ((23, 2534, (9, 'g'), (0,)), 456, 6, frozenset({('a', 5), ('b', 9)}), (6, 7, 8))
		args = ((23, 2534, (9, 'g'), (0,)), 456, 6, {'a': 5, 'b': 9}, [6, 7, 8],)
		dotest(e, args)
	
	testing()
