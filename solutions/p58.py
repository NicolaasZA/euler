"""
Best read at https://projecteuler.net/problem=58
"""

from resources.lib import is_prime

prime_count = 3
current_value = 9
side = 5
found = False

while not found:
    s1 = current_value + (1 * (side-1))
    s2 = current_value + (2 * (side-1))
    s3 = current_value + (3 * (side-1))
    s4 = current_value + (4 * (side-1))

    if is_prime(s1):
        prime_count += 1
    if is_prime(s2):
        prime_count += 1
    if is_prime(s3):
        prime_count += 1
    if is_prime(s4):
        prime_count += 1

    current_value = s4

    ratio = prime_count / ((2 * side) - 1)
    if ratio < 0.1:
        found = True
    else:
        side += 2

print(side)
