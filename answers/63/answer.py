#!/usr/bin/env python3

# Definition:
#	If 'n' is a positive integer, then:
#		digits(n) = floor(log(n, 10) + 1)



# Proof 1:

# Suppose:
#	b > digits(a ** b)	# Assumption 1
#	10 > a			# Assumption 2
#	a is a positive integer # Assumption 3
#	b is a positive integer # Assumption 4
# Hypothesis:
#	b + 1 > digits(a ** (b + 1))
# Proof:
#				b	>	digits(a ** b)				# 1
#				b	>	floor(log(a ** b, 10) + 1)		# 2	1, Definition of 'digits(n)'
#
#				10	>	a					# 3
#			log(10, 10)	>	log(a, 10)				# 4
#				1	>	log(a, 10)				# 5
#	floor(log(a ** b, 10) + 1)	>=	floor(log(a ** b, 10) + log(a, 10))	# 6
#
#				b	>	floor(log(a ** b, 10) + log(a, 10))	# 5	2, 6
#				b	>	floor(log(a ** b * a, 10))		# 6
#				b	>	floor(log(a ** (b + 1), 10))		# 7
#				b + 1	>	floor(log(a ** (b + 1), 10)) + 1	# 8
#				b + 1	>	floor(log(a ** (b + 1), 10) + 1)	# 9	floor(x) + 1 == floor(x + 1)
#				b + 1	>	digits(a ** (b + 1))			# 10	9, Definition of 'digits(n)'

# From Proof 1 we can infer that upon reaching a point where the exponent of a mantissa (less than 10) is greater than the number of digits in the result, further incrementing that exponent will not yield any new result with a number of digits equal to that new exponent.
# The previous statement helps finitize the algorithm's search space.



# Proof 2:

# Suppose:
#	'b' is a positive integer	# Assumption 1
# Hypothesis:
#	digits(10 ** b) > b
# Proof:
#			b		=	b	# 1
#		b * log(10, 10)		=	b	# 2
#		log(10 ** b, 10)	=	b	# 3
#		log(10 ** b, 10) + 1	=	b + 1	# 4
#	floor(log(10 ** b, 10) + 1)	=	b + 1	# 5	4, Assumption 1 (basically)
#		digits(10 ** b)		=	b + 1	# 6	Definition of 'digits(n)'
#		digits(10 ** b)		>	b	# 7

# From Proof 2 we can infer that the number 10 raised to 'b' will never produce a result that is 'b' digits long.
# The previous statement helps reduce the algorithm's search space.



# Proof 3:

# Suppose:
#	a > 10				# Assumption 1
#	b >= 1				# Assumption 2
#	'a' is a positive integer	# Assumption 3
#	'b' is a positive integer	# Assumption 4
# Hypothesis:
#	digits(a ** b) > b
# Proof:
#				a	>	10		# 1
#			log(a, 10)	>	log(10, 10)	# 2
#			log(a, 10)	>	1		# 3
#			b * log(a, 10)	>	b		# 4
#			log(a ** b, 10)	>	b		# 5
#		log(a ** b, 10) + 1	>	b + 1		# 6
#	floor(log(a ** b, 10) + 1)	>	b		# 7
#			digits(a ** b)	>	b		# 8

# From Proof 3 we can infer that the number 'a' raised to 'b' will never produce a result that is 'b' digits long.
# The previous statement helps finitize the algorithm's search space.

from itertools import count

def digits(n):
	return len(str(n))

def main():
	result = 0
	for a in range(1, 10):
		for b in count(1):
			if digits(a ** b) == b:
				result += 1
			elif b > digits(a ** b):
				break
	
	return result

print(main())
