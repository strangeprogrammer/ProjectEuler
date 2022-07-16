#!/bin/python3

from functools import reduce

def getnames():
	with open('p022_names.txt', 'r') as fnames:
		namelist = fnames.readline().replace("\"", "").split(sep = ",")
	return sorted(namelist)

scoreletter = lambda c: ord(c) - ord('A') + 1

scorename = lambda s: sum(map(lambda c: scoreletter(c), s))

main = lambda: sum(map(lambda t: t[0] * scorename(t[1]), enumerate(getnames(), start = 1)))

print(main())
