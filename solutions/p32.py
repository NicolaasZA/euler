#!/usr/bin/python3

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n 
exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, 
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be 
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from https://projecteuler.net/problem=32

correct is 45228
"""

from resources.lib import get_digit_counts


def is_pan(text: str):
    counts = get_digit_counts(int(text), 9)
    for bit in counts:
        if bit != 1:
            return False
    return True


def wrapper(text: str):
    if (len(text) != 9):
        return False
    return is_pan(text)


values = []
for a in range(1, 9877):
    max = int(10000/a)
    for b in range(1, max):
        c = a * b
        s = '{}{}{}'.format(a, b, c)
        if len(s) == 9:
            if wrapper(s) and c not in values:
                values.append(c)

print(sum(values))