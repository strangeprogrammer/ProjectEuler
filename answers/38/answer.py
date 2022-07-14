#!/usr/bin/env python3

# We will define the terms Initiator and Applicants to be an 'n' and '(1, 2, 3, 4, ...)' such that the following is always true:
#	'n' and '(1, 2, 3, 4, ...)' is a Concatenated Product.

# POINT 1:
# We know that the Concatenated Product of '1' and '(1, 2, 3, 4, 5, 6, 7, 8, 9)' is '123456789'.
# Since any greater Initiator with these same Applicants would form a Concatenated Product of greater or equal length to '123456789', then we know that the largest possible tuple of Applicants that could successfully form a Pandigital Number must be '(1, 2, 3, 4, 5, 6, 7, 8, 9)'.

# POINT 2:
# We can see because of the logarithm property:
#	log(n * m, base) = log(n , base) + log(m, base)
# that the number of digits in a multiple of two numbers is roughly proportional to the sum of the number digits of each of those two numbers. Thus, if the Initiator is 3 digits long, for example, then the number of applicants must be 3 or fewer, since the concatenation of 3 arbitrary 3-digit numbers (each formed from the product of the Initiator with each of its Applicants) would end up forming a 9-digit-long number at most.

# POINT 3: FIXME
# The largest base 10 pandigital number that could exist is '987654321'.  Since this is simply the Concatenated Product of Initiator '987654321' and Applicants '(1)', then we know that the largest valid Initiator must be less than '987654321' since any larger Initiator would not be able to form a Pandigital Concatenated Product, regarless of the Applicants. However, since this problem requires that the number of applicants be greater than '1', we know that the smallest possible tuple of applicants must be '(1, 2)'. Using this information together with that of POINT 2, this would mean that the largest initiator possible would have to be fewer than '5' digits long, since a '5' digit long initiator would form a '10' digit pandigital number, which is invalid.

import math
import functools

globinit = 9999
allapplicants = (
	(1, 2),
	(1, 2, 3),
	(1, 2, 3, 4),
	(1, 2, 3, 4, 5),
	(1, 2, 3, 4, 5, 6),
	(1, 2, 3, 4, 5, 6, 7),
	(1, 2, 3, 4, 5, 6, 7, 8),
	(1, 2, 3, 4, 5, 6, 7, 8, 9),
)

def explodeInt(n):
	return tuple(str(n))

def implodeInt(r):
	return int(''.join(r))

def calcConcProd(initiator, applicants):
	return ''.join(map(
		lambda applicant: str(initiator * applicant),
		applicants
	))

def searcher():
	global globinit, allapplicants
	for initiator in range(globinit, 1, -1):
		for applicants in allapplicants:
			if 9 < math.floor(math.log10(initiator) + 1) * len(applicants): # I don't think that we need to use 'math.floor' here, but we don't want to accidentally skip any cases which *would* create a pandigital number on accident
				break
			else:
				concProd = calcConcProd(initiator, applicants)
				if sorted(concProd) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
					yield int(concProd)

def main():
	return max(*list(searcher()))

print(main())
