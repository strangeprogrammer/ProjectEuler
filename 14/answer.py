#!/bin/python3

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

def collatz(n):
	if n % 2 == 0:
		return int(n / 2)
	else:
		return n * 3 + 1

collatzscore = {(1,): 0}

@memoize(collatzscore)
def scoreit(n):
	return 1 + scoreit(collatz(n))

def scoremany(n):
	for i in range(1, n):
		scoreit(i)

def maxVquery(d):
	result = []
	
	vmax = max(d.values())
	for k in d:
		if d[k] == vmax:
			result.append(k)
	
	return result

def main():
	scoremany(1000000)
	global colltazscore
	return maxVquery(collatzscore)[0][0]

print(main())
