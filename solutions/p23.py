#!/usr/bin/python3

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 
28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be 
written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that
 all integers greater than 28123 can be written as the sum of two abundant numbers. However, 
 this upper limit cannot be reduced any further by analysis even though it is known that the 
 greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from https://projecteuler.net/problem=23
"""

from resources.lib import get_factors


def is_abundant(val: int) -> bool:
    # if (val > 10):
    #     return fast_factor_sum(val) > val
    # else:
    return sum(get_factors(val)) > (val * 2)


# print('Preparing bits')
# 0 means "cannot be written as the sum of two abundant numbers"
bits = [0] * 28124

# print("Calculating abundant numbers below or equal 28123")
abundants = []
for n in range(1, 28124):
    if is_abundant(n):
        abundants.append(n)
# print('{} found'.format(len(abundants)))

# print('Flipping bits')
for l in range(0, len(abundants)):
    for r in range(0, len(abundants)):
        tot = abundants[l] + abundants[r]
        if tot < len(bits):
            bits[tot] = 1
    # if l % 100 == 0:
    #     print('> now at', l)

# print('Calculating Totals')
count = 0
total = 0
for n in range(1, 28124):
    if bits[n] == 0:
        total += n
        count += 1

print('{} values totalling {}'.format(count, total))
