#!/bin/python3

import operator
import functools
import itertools

def explodeInt(n):
	return list(str(n))

def genDigits():
	for i in itertools.count(1):
		for d in explodeInt(i):
			yield d

def genLimit(g, n):
	for i, v in zip(range(n), g):
		yield v

def genExtract(g, s):
	for i, v in enumerate(g):
		if i in s:
			s -= {v}
			yield v

def main():
	return functools.reduce(
		operator.mul,
		map(
			int,
			genExtract(
				genLimit(
					genDigits(),
					1000000
				), {
					0,
					9,
					99,
					999,
					9999,
					99999,
					999999,
				}
			)
		),
		1
	)

print(main())
