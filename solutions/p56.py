"""
A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
from https://projecteuler.net/problem=56
"""

def get_sum(a: int, b: int):
    if a % 10 == 0:
        return 1
    return sum([int(c) for c in str(a**b)])

largest = [0, 0, 0]
for a in range(1, 100):
    for b in range(1, 100):
        s = get_sum(a,b)
        if s > largest[2]:
            largest = [a,b,s]

print(f'{largest[0]} to the power of {largest[1]} produces {largest[2]}')