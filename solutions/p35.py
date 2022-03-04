"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

from https://projecteuler.net/problem=35
"""
from resources.lib import is_prime

def get_rotations(val: int):
    s = str(val)
    rotas = []
    for n in range(0, len(s)):
        rotas.append(int(s[n:] + s[:n]))
    return rotas

def is_circular(val: int):
    variants = get_rotations(val)
    return False not in [is_prime(v) for v in variants]

count = 1 # count 2 (which is a prime)
for n in range(3, 10**6, 2):
    if is_prime(n):
        if is_circular(n):
            count += 1

print(count)