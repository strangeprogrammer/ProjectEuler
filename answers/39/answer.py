#!/usr/bin/env python3

import itertools
import math

def makesides():
	return filter(
		lambda t: t[0] <= t[1],
		itertools.product(
			range(1, 1000),
			range(1, 1000),
		)
	)

def makehypotenuse():
	return map(
		lambda t: (
			t[0],
			t[1],
			math.sqrt(			# Generate the hypotenuse
				t[0] ** 2 + t[1] ** 2	#
			)				#
		),
		makesides()
	)

def filterhypotenuse():
	return filter(
		lambda t: sum(t) <= 1000, # (a requirement of this problem)
		makehypotenuse()
	)

def filtertriples():
	return map(
		lambda t: (t[0], t[1], int(t[2])),
		filter(
			lambda t: t[2] == int(t[2]), # Find only those triangles with an integer-length hypotenuse (a requirement of this problem)
			filterhypotenuse()
		)
	)

def scoreall():
	scores = {}
	for perimeter in map(sum, filtertriples()):
		scores[perimeter] = \
		scores.get(
			perimeter,
			0 # default value
		) + 1
	return scores

def getmaxscore():
	scores = scoreall()
	return max(
		scores.keys(),
		key = lambda k: scores[k]
	)

def main():
	return getmaxscore()

print(main())
