#!/usr/bin/python
# Project Euler #3 : Largest Prime Factor

import time


def find_largest_prime(num):
    x = 2
    if num == 2:
        return num
    while x < num:
        if num % x == 0:
            num = num / x
        x += 1
    return x

start = time.time()
print find_largest_prime(600851475143)
print time.time() - start, "seconds"
