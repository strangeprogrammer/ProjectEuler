#!/bin/python3

total = 0

for i in range(1, 101):
	for j in range(1, 101):
		if i != j:
			total += i * j

print(total)
