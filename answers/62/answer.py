#!/usr/bin/env python3

from itertools import count

cubes = {}

def main():
	global cubes
	for n in count(1):
		cube = n ** 3
		key = tuple(sorted(str(cube)))
		value = cubes.get(key, [])
		value += [cube]
		if len(value) == 5:
			return value[0]
		else:
			cubes[key] = value

print(main())
