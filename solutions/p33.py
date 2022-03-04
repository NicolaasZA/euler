#!/usr/bin/python3

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in 
attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, 
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, 
find the value of the denominator.

from https://projecteuler.net/problem=33
"""
from resources.lib import get_fraction_lower

def get_at(val: int, index: int):
    str_val = str(val)
    if index < 0 or index >= len(str_val):
        raise ArithmeticError('Invalid index {}'.format(index))
    return int(str_val[index])


fractions_to_consider = []
for num in range(10, 100):
    for den in range(num+1, 100):
        frac = float(num) / float(den)

        n1 = get_at(num, 0)
        n2 = get_at(num, 1)
        d1 = get_at(den, 0)
        d2 = get_at(den, 1)

        frac2 = 0
        process = ''
        if n1 == d1 and d2 > 0 and n1 > 0:
            frac2 = n2 / d2
            process = '{}/{} is same as {}/{} by cancelling {} and {}'.format(
                num, den, n2, d2, n1, d1)
        elif n1 == d2 and d1 > 0 and n1 > 0:
            frac2 = n2 / d1
            process = '{}/{} is same as {}/{} by cancelling {} and {}'.format(
                num, den, n2, d1, n1, d2)
        elif n2 == d1 and d2 > 0 and n2 > 0:
            frac2 = n1 / d2
            process = '{}/{} is same as {}/{} by cancelling {} and {}'.format(
                num, den, n1, d2, n2, d1)
        elif n2 == d2 and d1 > 0 and n2 > 0:
            frac2 = n1 / d1
            process = '{}/{} is same as {}/{} by cancelling {} and {}'.format(
                num, den, n1, d1, n2, d2)
        if frac == frac2:
            fractions_to_consider.append([num, den])

# Build new fraction
final_numerator = 1
final_denominator = 1
for i in range(0, len(fractions_to_consider)):
    final_numerator *= fractions_to_consider[i][0]
    final_denominator *= fractions_to_consider[i][1]

# Divide to lowest common terms
final_numerator, final_denominator = get_fraction_lower(
    final_numerator, final_denominator)

print(final_denominator)