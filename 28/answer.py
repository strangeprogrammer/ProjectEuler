#!/bin/python3

# There is a faster way for a *programmer* to solve this problem, but this is (one of) the fastest solution(s) for a *program*

sumlines = lambda n: int(n * (n + 1) / 2)
sumsquares = lambda n: int(n * (n + 1) * (2 * n + 1) / 6)

getlinediag = lambda n: 2 * sumlines(int((n - 1) / 2))
getsquarediag = lambda n: sumsquares(n) - 4 * sumsquares(int((n - 1) / 2))

getalldiags = lambda n: 4 * getsquarediag(n) - 6 * getlinediag(n) - 3

main = lambda: getalldiags(1001)

print(main())
