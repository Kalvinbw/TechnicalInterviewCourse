# Write a function that calculates the power of a number given a base number and exponent using recursion

from os import pread


def exponent(base, exp):
    if exp == 0:
        return 1
    return base * exponent(base, exp - 1)

print(exponent(2, 2))

def practice(base, exp):
    if exp == 0:
        return 1
    return base * practice(base, exp-1)

print(practice(3,3))