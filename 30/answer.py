#!/bin/python3

# Here, the word 'property' indicates that a given number is greater than the
# sum of the fifth powers of its digits.

# If 'n' designates the raw number, 'k' designates the number of its digits, and
# 'd' designates the sum of those digits, suppose:

# 1:	n > d

# Then, we would like to prove the following:

# 2:	a * 10 ** k + n > a ** 5 + d

# If the following is true (using the maximum digit value of 'a = 9' to maximize
# the value of the RHS):

# 3:	9 * 10 ** k > 9 ** 5

# Then (2) will certainly be true as well. Solving for 'k':

#	9 * 10 ** k > 9 ** 5
#	10 ** k > 9 ** 4
#	10 ** k > 10 ** log(9 ** 4, 10)
#	10 ** k > 10 ** (4 * log(9, 10))
#	k > 4 * log(9, 10)
# 4:	k > 3.81697

# So, in order for prepended digit to be worth more on the LHS than the effect
# of that same digit upon the RHS, that digit must add a value of (roughly) 90,000
# or more to the LHS. This would mean that a digit '1' representing 100,000, or
# any greater-valued digit, were it to be prepended to the number, would maintain
# the LHS being greater than the RHS. This would then be true of any larger number
# as well. So, if the initial slack from the RHS can be overcome, then almost any
# integer of the form 'm * 100,000' would maintain the property (practically, this
# becomes 'm >= 4'). Additionally, this means that once the number is sufficiently
# large, the addition of any integer less than 100,000 will be tolerated for the
# following reason:

# Suppose that we want to prove:

#	n + p > d + c
# 5:	n + (p - c) > d

# We know that if:

#	0 < p < 90,000
#	0 < c < 90,000

# Then:

#	p - c > -90,000

# So, assuming a worst-case scenario:

#	p - c = -90,000

# Then:

#	n + p > d + c
#	n + (p - c) > d
#	n - 90,000 > d

# And if 'n' is already 90,000 greater or more than 'd', the property will still
# apply to these new numbers.

# The least such number that provides us all of these assurances is about
# 1,000,000 (though this is an intentionally conservative guess), so this is the
# maximum number that we must search up to for numbers that can be equal to
# the sum of the fifth powers of their digits, since every greater number can't
# have such an equivalence property.

def main():
	print(sum([
		x
		for x
		in range(2, 1000000 + 1)
		if x == sum(map(
			lambda d: int(d) ** 5,
			list(str(x)),
		))
	]))

main()
