#!/bin/python3

import itertools
import operator

def main():
	print(len(
		set(itertools.starmap(
			operator.pow,
			itertools.product(
				range(2, 100 + 1),
				range(2, 100 + 1),
			)
		))
	))

main()
