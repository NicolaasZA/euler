"""
Read at https://projecteuler.net/problem=53
"""
from math import factorial


def func(n: int, r: int):
    return int((factorial(n)) / (factorial(r) * factorial(n-r)))


count = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        s = func(n, r)
        if s > 1000000:
            count += 1

print(count)
