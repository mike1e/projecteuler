"""
Michael Le
Project Euler
Problem 2: Even Fibonacci Numbers
Python
"""

prev, next = 1, 1
total = 0
MAX = 4000000

while next < MAX:
    if next % 2 == 0:
        total += next
    prev, next = next, prev + next

print total
