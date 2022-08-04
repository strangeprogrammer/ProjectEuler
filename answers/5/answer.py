#!/usr/bin/env python3

from functools import reduce
from operator import mul

# 1	= 1
# 2	= 2
# 3	= 3
# 4	= 2^2
# 5	= 5
# 6	= 2 * 3
# 7	= 7
# 8	= 2^3
# 9	= 3^2
# 10	= 2 * 5
# 11	= 11
# 12	= 2^2 * 3
# 13	= 13
# 14	= 2 * 7
# 15	= 3 * 5
# 16	= 2^4
# 17	= 17
# 18	= 2 * 3^2
# 19	= 19
# 20	= 2^2 * 5

# Primes:			2  3  5  7  11 13 17 19
# Greatest Power of Each Prime:	4  2  1  1  1  1  1  1
# Primes Taken to Powers:	16 9  5  7  11 13 17 19
# Total Multiple:		232792560

def main():
	return reduce(
		mul,
		[
			2	** 4,
			3	** 2,
			5	** 1,
			7	** 1,
			11	** 1,
			13	** 1,
			17	** 1,
			19	** 1,
		]
	)

print(main())
