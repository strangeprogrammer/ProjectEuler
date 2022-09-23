#!/usr/bin/env python3

### Demonstration of Process:

# sqrt(7) = 2 + sqrt(7) - 2

# sqrt(7) - 2 = 1 / (1 / (sqrt(7) - 2))
# sqrt(7) - 2 = 1 / ((sqrt(7) + 2) / ((sqrt(7) + 2) * (sqrt(7) - 2)))
# sqrt(7) - 2 = 1 / ((sqrt(7) + 2) / (7 - 4))
# sqrt(7) - 2 = 1 / ((sqrt(7) + 2) / 3)
# sqrt(7) - 2 = 1 / (1 + ((sqrt(7) - 1) / 3))

# (sqrt(7) - 1) / 3 = 1 / (3 / (sqrt(7) - 1))
# (sqrt(7) - 1) / 3 = 1 / (3 * (sqrt(7) + 1) / ((sqrt(7) + 1) * (sqrt(7) - 1)))
# (sqrt(7) - 1) / 3 = 1 / (3 * (sqrt(7) + 1) / (7 - 1))
# (sqrt(7) - 1) / 3 = 1 / (3 * (sqrt(7) + 1) / 6)
# (sqrt(7) - 1) / 3 = 1 / ((sqrt(7) + 1) / 2)
# (sqrt(7) - 1) / 3 = 1 / (1 + (sqrt(7) - 1) / 2)

# (sqrt(7) - 1) / 2 = 1 / (2 / (sqrt(7) - 1))
# (sqrt(7) - 1) / 2 = 1 / (2 * (sqrt(7) + 1) / ((sqrt(7) + 1) * (sqrt(7) - 1)))
# (sqrt(7) - 1) / 2 = 1 / (2 * (sqrt(7) + 1) / (7 - 1))
# (sqrt(7) - 1) / 2 = 1 / (2 * (sqrt(7) + 1) / 6)
# (sqrt(7) - 1) / 2 = 1 / ((sqrt(7) + 1) / 3)
# (sqrt(7) - 1) / 2 = 1 / (1 + ((sqrt(7) - 2) / 3))

# (sqrt(7) - 2) / 3 = 1 / (3 / (sqrt(7) - 2))
# (sqrt(7) - 2) / 3 = 1 / (3 * (sqrt(7) + 2) / ((sqrt(7) + 2) * (sqrt(7) - 2)))
# (sqrt(7) - 2) / 3 = 1 / (3 * (sqrt(7) + 2) / (7 - 4))
# (sqrt(7) - 2) / 3 = 1 / (3 * (sqrt(7) + 2) / 3)
# (sqrt(7) - 2) / 3 = 1 / (sqrt(7) + 2)
# (sqrt(7) - 2) / 3 = 1 / (4 + (sqrt(7) - 2))

# sqrt(7) - 2 = 1 / (1 / (sqrt(7) - 2))
# (See above)

### Programmatic Answer

from math import sqrt, floor

def maxremove(n):
	return floor(sqrt(n))

def fracnormalizebottom(numerator, n, add):
	return (n - add ** 2) // numerator # We just use double slash since otherwise python starts using floats instead of ints
	# Side Note: We can be sure that we will never have to deal with a numerator and denominator that doesn't reduce to '1 / n' since every fraction generated through this process has a denominator which is evenly divisible by the numerator, since the numerator is a factor of the previous denominator, which is the same as the current denominator.

def extractterm(n, add, denom):
	mr = maxremove(n)
	term = 0
	while add >= -mr:
		add -= denom
		term += 1
	
	add += denom
	term -= 1
	
	return [term, add]

def exnext(n, add, denom):
	[term, add] = extractterm(n, add, denom)
	
	[add, denom] = [-add, fracnormalizebottom(denom, n, add)]
	
	return [term, add, denom]

def getperiod(n):
	results = []
	add = 0
	denom = 1
	while True:
		nexthop = exnext(n, add, denom)
		[term, add, denom] = nexthop
		try:
			return len(results) - results.index(nexthop)
		except ValueError:
			results.append(nexthop)

def main():
	truesquares = set(map(
		lambda x: x ** 2,
		range(1, 101)
	))
	
	return len(list(filter(
		lambda x: x not in truesquares \
			and getperiod(x) % 2 == 1,
		range(1, 10001)
	)))

if __name__ == '__main__':
	print(main())
else:
	assert exnext(7, 0, 1) == [2, 2, 3]
	assert exnext(7, 2, 3) == [1, 1, 2]
	assert exnext(7, 1, 2) == [1, 1, 3]
	assert exnext(7, 1, 3) == [1, 2, 1]
	assert exnext(7, 2, 1) == [4, 2, 3]
	
	assert getperiod(2)	== 1
	assert getperiod(3)	== 2
	assert getperiod(5)	== 1
	assert getperiod(6)	== 2
	assert getperiod(7)	== 4
	assert getperiod(8)	== 2
	assert getperiod(10)	== 1
	assert getperiod(11)	== 2
	assert getperiod(12)	== 2
	assert getperiod(13)	== 5
	assert getperiod(23)	== 4
