#!/usr/bin/env python3

# Suppose that we want to form a predicate indicating whether or not an input value 'fn' is a Triangular, Pentagonal, or Hexagonal Number. Then, we should be able to take the function inverse of 'fn' and find a positive integer. We essentially do this by re-writing each function's expression and solve for 'n' using the quadratic formula.
# Note that we can simply change the '+-' particle to '+' when solving for each since not doing so would result in either some fraction or a negative number, which we certainly know won't be Triangular, Pentagonal, nor Hexagonal.
# Furthermore, since square-root sub-expression for each must make the final result an integer, we can use a bit of modular arithmetic to perform some early checking for each predicate.

from itertools import count
from math import sqrt

#	T_n	= n * (n + 1) / 2
#	2 * T_n	= n ** 2 + n
#	0	= n ** 2 + n - 2 * T_n
#	n	= (-1 +- sqrt(1 ** 2 - 4 * 1 * (-2 * T_n))) / (2 * 1)
#	n	= (-1 +- sqrt(1 + 8 * T_n)) / 2

def istriang(tn):
	k = sqrt(1 + 8 * tn)
	if k % 2 == 1:
		return True
	else:
		return False

#       P_n     = n * (3 * n - 1) / 2
#       2 * P_n = n * (3 * n - 1)
#       2 * P_n = 3 * n ** 2 - n
#       0       = 3 * n ** 2 - n - 2 * P_n
#       n       = (-(-1) +- sqrt((-1)**2 - 4 * 3 * (-2 * P_n))) / (2 * 3)
#       n       = (1 +- sqrt(1 + 24 * P_n)) / 6

def ispenta(pn):
	k = sqrt(1 + 24 * pn)
	if k % 6 == 5:
		return True
	else:
		return False

def hexag(n):
	return n * (2 * n - 1)

#	H_n	= n * (2 * n - 1)
#	H_n	= 2 * n ** 2 - n
#	0	= 2 * n ** 2 - n - H_n
#	n	= (-(-1) +- sqrt((-1) ** 2 - 4 * 2 * (-H_n))) / (2 * 2)
#	n	= (1 +- sqrt(1 + 8 * H_n)) / 4

def main():
	for i in count(143 + 1):
		hn = hexag(i)
		if ispenta(hn) and istriang(hn): # We check for pentagonality first since it's less likely and will short-circuit more often
			return hexag(i)

print(main())
