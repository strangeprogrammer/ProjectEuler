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

words = {
	(1,):		"one",
	(2,):		"two",
	(3,):		"three",
	(4,):		"four",
	(5,):		"five",
	(6,):		"six",
	(7,):		"seven",
	(8,):		"eight",
	(9,):		"nine",
	(10,):		"ten",
	(11,):		"eleven",
	(12,):		"twelve",
	(13,):		"thirteen",
	(14,):		"fourteen",
	(15,):		"fifteen",
	(16,):		"sixteen",
	(17,):		"seventeen",
	(18,):		"eighteen",
	(19,):		"nineteen",
	(20,):		"twenty",
	(30,):		"thirty",
	(40,):		"forty",
	(50,):		"fifty",
	(60,):		"sixty",
	(70,):		"seventy",
	(80,):		"eighty",
	(90,):		"ninety",
	(1000,):	"onethousand"
}

@memoize(words)
def findwords(n):
	result = ""
	l = n % 100
	u = n // 100
	# if n == 1000: # We don't need to care about this case since it's already memoized
	if u:
		result += findwords(u) + "hundred"
		if l:
			result += "and"
	if l:
		if (l,) not in words.keys():
			result += findwords(l // 10 * 10) + findwords(l % 10)
		else:
			result += findwords(l)
	assert result != 0, str(n) + " casused an error."
	return result

def main():
	for i in range(1, 1001):
		findwords(i)
	f = list(filter(lambda t: t[0][0] < 1001, words.items()))
	vals = list(map(lambda t: len(t[1]), f))
	return sum(vals)

print(main())
