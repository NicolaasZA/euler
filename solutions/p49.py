#!/usr/bin/python3

"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
    (i) each of the three terms are prime, and, 
    (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

from https://projecteuler.net/problem=49
"""

from resources.lib import is_prime, is_permutation


def run():
    seed = 1
    for n in range(seed, 10000):
        if is_prime(n):
            for term in range(1, 5000):
                if is_permutation(n, n+term) and is_permutation(n, n+term+term) and is_prime(n+term) and is_prime(n+term+term) and n != 1487:
                    return [n, n + term, n + term + term]
    return [None, None, None]


vals = run()
print('Solution is {}{}{}'.format(vals[0], vals[1], vals[2]))
