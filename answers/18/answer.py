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

pyramid = [	                            [75],
		                          [95, 64],
		                        [17, 47, 82],
		                      [18, 35, 87, 10],
		                    [20,  4, 82, 47, 65],
		                  [19,  1, 23, 75,  3, 34],
		                [88,  2, 77, 73,  7, 63, 67],
		              [99, 65,  4, 28,  6, 16, 70, 92],
		            [41, 41, 26, 56, 83, 40, 80, 70, 33],
		          [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
		        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
		      [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
		    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
		  [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
		[ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23]
]

bestpaths = {}

def initpaths():
	global pyramid, bestpaths
	bestpaths[(0, 0)] = ("", pyramid[0][0])

def outofbounds(y, x):
	if -1 < x and -1 < y and y < len(pyramid) and x < len(pyramid[y]):
		return False
	else:
		return True

@memoize(bestpaths)
def findpath(y, x):
	global pyramid
	if outofbounds(y, x):
		return None
	ur = findpath(y - 1, x)
	ul = findpath(y - 1, x - 1)
	if ur is None:
		retval = ("l" + ul[0], pyramid[y][x] + ul[1])
	elif ul is None:
		retval = ("r" + ur[0], pyramid[y][x] + ur[1])
	else:
		if ul[1] > ur[1]:
			retval = ("l" + ul[0], pyramid[y][x] + ul[1])
		else:
			retval = ("r" + ur[0], pyramid[y][x] + ur[1])
	return retval

from functools import reduce

def main():
	global pyramid, bestpaths
	initpaths()
	for x, junk in enumerate(pyramid[-1:][0]):
		findpath(len(pyramid) - 1, x)
	return max(list(map((lambda x: x[1][1]), filter((lambda t: t[0][0] == len(pyramid) - 1), bestpaths.items()))))

print(main())
