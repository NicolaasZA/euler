"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

Note: 2, 3, 5, and 7 are not considered to be truncatable primes.

from https://projecteuler.net/problem=37
"""
import timeit
from resources.lib import is_prime


def is_truncable(val: int):
    s = str(val)

    if val <= 7:
        return False

    # All primes above 5 end with digit 1, 3, 7 or 9, so a right-truncatable prime can only contain those digits after the leading digit.
    for char in '24568':
        if char in s[1:]:
            return False

    if not is_prime(val):
        return False

    # test left-trunc
    for l in range(0, len(s)):
        if not is_prime(int(s[l:])):
            return False

    # test left-trunc
    for r in range(len(s), 0, -1):
        if not is_prime(int(s[:r])):
            return False

    return True


def run():
    entries = []
    for x in range(1, 10**6):
        if is_truncable(x):
            entries.append(x)
    return entries

print(sum(run()))
