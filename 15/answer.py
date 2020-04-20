#!/bin/python3

# Upon closer inspection, this problem is actually just a tilted version of Pascal's triangle

def allargstupled(*args, **kwargs):
	result = [*args]
	for k in sorted(kwargs.keys()):
		result.append((k, kwargs[k]))
	
	return tuple(result)

def memoize(d):
	def memoize_internal(f):
		def wrapper(*args, **kwargs):
			k = allargstupled(*args, **kwargs)
			
			if k in d:
				return d[k]
			else:
				v = f(*args, **kwargs)
				d[k] = v
				return v
		
		return wrapper
	
	return memoize_internal

@memoize({})
def pascal(i, j):
	if i <= 0 or j <= 0:
		return 1
	
	return pascal(i - 1, j) + pascal(i, j - 1)

print(pascal(20, 20)) # Count by the number of corners, not boxes
