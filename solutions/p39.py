"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

from https://projecteuler.net/problem=39
"""
from math import ceil, sqrt


def pythagoras(a: int, b: int):
    """Get integer length of long side of right triangle using pythagoras' theorom."""
    return sqrt((a**2) + (b**2))


def get_triangle_count(p: int):
    options = []
    for a in range(1, int(p / 3)):
        for b in range(a+1, int((p-a)/2) - 1):
            c = p - a - b
            if c > b:
                c2 = pythagoras(a, b)
                p2 = a+b+c
                if (c == c2) and (c2 % 1 == 0) and (p == p2):
                    line = [p, a, b, c, c2, p2]
                    if line not in options:
                        options.append(line)
    return len(options)

long_c = 0
long_p = 0
max_p = 1000

for p in range(3,max_p + 1):
    c = get_triangle_count(p)
    if c > long_c:
        long_c = c
        long_p = p
    if p % 100 == 0:
        print(f'{round(p/max_p*100, 0)}%')

print(f'maximum at p={long_p} with len={long_c}')