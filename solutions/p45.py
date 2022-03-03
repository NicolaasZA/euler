#!/usr/bin/python3
import resources.numbers as gen

max_n = 5000**2

found = False
n = 286
while not found and n < max_n:
    t = gen.triangle(n)

    if gen.is_hexagonal(t) and gen.is_pentagonal(t):
        print(t)
        found = True

    n += 1
