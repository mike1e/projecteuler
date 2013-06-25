#!/usr/bin/python
# Project Euler #3 : Largest Prime Factor

import math


def prime_number(num):
    if num == 2:
        return True
    for x in xrange(2, int(math.sqrt(num+1))):
        if num % x == 0:
            return False
    return True


def factor(num):
    factors = []
    x = 2
    while x < math.sqrt(num):
        if num % x == 0 and prime_number(x):
            factors.append(x)
        x += 1
    print factors.pop()

factor(600851475143)
