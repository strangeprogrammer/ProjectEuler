#!/usr/bin/env python3

# I create an algorithm based upon the information in this wikipedia entry in order to solve the problem:
# https://en.wikipedia.org/wiki/Pell%27s_equation#Fundamental_solution_via_continued_fractions

from fractions import Fraction
from math import sqrt
from itertools import count

from gradientmu import mu
from gentools import indexable

naturals = indexable(count(1))

def simplify(f):
	major = f.numerator // f.denominator
	return [major, f - major]

def seqtofrac(seq):
	seq = reversed(seq)
	sofar = Fraction(0)
	
	for e in seq:
		sofar = 1 / (e + sofar)
	
	return 1 / sofar

def sqconvergents(D):
	# Given a number 'D', this function returns the simplified results of the continued fractions approximating 'sqrt(D)'
	global naturals
	
	seq = []
	countup = lambda k: D < seqtofrac(seq + [k]) ** 2
	countdown = lambda k: D > seqtofrac(seq + [k]) ** 2
	
	while True:
		[nextterm, success] = mu(naturals, countup)
		seq.append(nextterm)
		convergent = seqtofrac(seq)
		yield [convergent.numerator, convergent.denominator]
		
		[nextterm, success] = mu(naturals, countdown)
		seq.append(nextterm)
		convergent = seqtofrac(seq)
		yield [convergent.numerator, convergent.denominator]

def solve(D):
	for [x, y] in sqconvergents(D):
		if x ** 2 - D * y ** 2 == 1:
			return x

def main():
	global scores, IN
	
	for D in IN:
		scores[D] = solve(D)
	
	maxD = 2
	maxx = 3
	
	for [k, v] in scores.items():
		if maxx < v:
			maxD = k
			maxx = v
	
	return maxD

scores = {}

IN = list(filter(
	lambda D: not sqrt(D) == int(sqrt(D)),
	range(1, 1001)
))

if __name__ == '__main__':
	print(main())
