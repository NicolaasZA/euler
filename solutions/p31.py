#!/usr/bin/python3

"""
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

from https://projecteuler.net/problem=31
"""

combos = [[0, 0, 0, 0, 0, 0, 0, 1]]  # 1 x e2
for p1 in range(0, 201, 1):
    for p2 in range(0, 201 - p1, 2):
        total = p1 + p2
        for p5 in range(0, 201 - total, 5):
            total = p1 + p2 + p5
            for p10 in range(0, 201 - total, 10):
                total = p1 + p2 + p5 + p10
                for p20 in range(0, 201 - total, 20):
                    total = p1 + p2 + p5 + p10 + p20
                    for p50 in range(0, 201 - total, 50):
                        total = p1 + p2 + p5 + p10 + p20 + p50
                        for e1 in range(0, 201 - total, 100):
                            total = p1 + p2 + p5 + p10 + p20 + p50 + e1
                            if total == 200:
                                combos.append(
                                    [p1, p2, p5, p10, p20, p50, e1, 0])

print(len(combos))
