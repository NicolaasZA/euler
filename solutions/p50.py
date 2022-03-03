#!/usr/bin/python3

"""
The prime 41, can be written as the sum of six consecutive primes:
    41 = 2 + 3 + 5 + 7 + 11 + 13
    
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

from https://projecteuler.net/problem=50
"""
from resources.lib import is_prime


primes = []
roof = 10**6

# List all primes lesser than 1000000
for n in range(1, roof):
    if is_prime(n):
        primes.append(n)

print('{} primes found'.format(len(primes)))

max_tot = 0
max_len = 0
max_start = 0
max_end = 0

for n in range(0, len(primes) - 1):
    start = primes[n]

    chain_len = 1
    chain_tot = start

    a = n + 1
    while a < len(primes) and chain_tot < roof:
        current = primes[a]
        
        chain_tot += current
        chain_len += 1

        if is_prime(chain_tot):

            if chain_len > max_len:
                max_len = chain_len
                max_tot = chain_tot
                max_start = start
                max_end = current
        a += 1

print('> chain from {} to {} yields {} with length {}'.format(max_start, max_end, max_tot, max_len))