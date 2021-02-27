#!/usr/bin/env python3

#1) Inductive basis: 'k' digit cutoff point
#Suppose there are two numbers, 'a(k)' and 'b(k)', of the form '100...00' and '999...99', each 'k' digits long.
#Also, suppose that the digit-factorial-sum (DFS) of 'b(k)' is strictly less than 'a(k)' (or 'DFS(b(k)) < a(k)').
#Then, since any 'k' digit number 'l' is greater than or equal to 'a(k)', it is also greater than 'b(k)'.
#Taking any 'k' digit number 'm', since 'DFS(m) <= DFS(b(k))', then 'DFS(m) < a(k)'.
#Taking the previous 2 statements together, suppose that 'm = l'. Then, 'DFS(l) < a(k) < l' for any 'k' digit number 'l'.

#2) Inductive hypothesis (IH)
#It is hypothesized that if two 'k' digit numbers 'a(k)' and 'b(k)' exist that hold the property shown in section 1, then two similar numbers, 'c' and 'd', each of 'k+1' digits, will also hold the property, for sufficiently large 'k'.

#3) Proof of IH
#If there are an 'a' and 'b(k)' that hold the property, then we can express a 'c' and 'DFS(d)' like so:
#'c = 10 * a(k)' and 'DFS(d) = 9! + DFS(b(k))'
#However, if we are to achieve 'DFS(d) < c', then the following must be true:
#'9! + DFS(b(k)) < 10 * a(k)'
#'DFS(b(k)) < 10 * a(k) - 9!'
#And, since we can see that the property is true for sufficiently large 'a(k)' and 'b(k)', then there are a smallest 'a(k)' and 'b(k)' for which the property is true, after which it is permanently true, and all 'k' digit numbers 'l' are guaranteed to be greater than 'DFS(l)' (or 'DFS(l) < l').

#This proof establishes a fixed upper bound on the search space required of this problem.

import math

a = 1
b = 9

def quickfact(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 6
	elif n == 4:
		return 24
	elif n == 5:
		return 120
	elif n == 6:
		return 720
	elif n == 7:
		return 5040
	elif n == 8:
		return 40320
	elif n == 9:
		return 362880
	else:
		raise Exception(n, "This wasn't supposed to happen...")

# Returns a little-endian array of all the digits in a number
def numarr(n, base = 10):
	result = []
	while 0 < n:
		result.append(n % base)
		n = int(n / base)
	
	if result == []:
		result = [0]
	
	return result

DFS = lambda n: sum(map(quickfact, numarr(n)))

def main():
	global a, b
	
	# Perform search for smallest 'a' and 'b'
	while a <= DFS(b):
		a *= 10
		b = b * 10 + 9
	
	print(sum(
		filter(lambda n: n == DFS(n),
			range(3, a))))

main()
