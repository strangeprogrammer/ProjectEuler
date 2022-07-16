#!/bin/python3

from itertools import count

fname = "./p042_words.txt"
triangleNums = []

def triangleGenerator():
	global triangleNums
	
	for i in count(1):
		v = i * (i + 1) / 2
		triangleNums += [v]
		yield v

triangleGenerator = triangleGenerator()

def genTriangles(n):
	while next(triangleGenerator) < n:
		pass

def isTriangleNum(n):
	global triangleNums
	
	genTriangles(n)
	return n in triangleNums

def rankChar(c):
	return ord(c) - ord("A") + 1 # We subtract ord("A") and add '1' since that ranks the letter 'A' as '1' (AKA we're messing with the origin point)

def isTriangleWord(w):
	return isTriangleNum(
		sum(map(
			rankChar,
			w
		))
	)

def getWords():
	global fname
	with open(fname, "r") as fd:
		return eval("[" + fd.read() + "]")

def main():
	return len(list(
		filter(
			isTriangleWord,
			getWords()
		)
	))

print(main())
