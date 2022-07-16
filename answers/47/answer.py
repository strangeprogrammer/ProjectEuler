#!/usr/bin/env python3

from itertools import count

from factors import factors
from memoize import memoize

@memoize({})
def predfactors(*args, **kwargs):
	return 4 == len(factors(*args, **kwargs))

def main():
	for i in count(3):
		if all([
			predfactors(i),
			predfactors(i + 1),
			predfactors(i + 2),
			predfactors(i + 3),
		]):
			return i

print(main())
