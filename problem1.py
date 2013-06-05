# Project Euler Problem 1
# Multiples of 3 and 5
# python

sum = 0
for number in range(0,1000):
	if number % 3 == 0 or number % 5 == 0:
		sum += number

print sum
