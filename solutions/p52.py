"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

from https://projecteuler.net/problem=52
"""
from resources.lib import get_digit_counts


def run():
    x = 1
    while x < 99999999999:
        d = [
            get_digit_counts(x),
            get_digit_counts(x*2),
            get_digit_counts(x*3),
            get_digit_counts(x*4),
            get_digit_counts(x*5),
            get_digit_counts(x*6)
        ]

        if d[0] == d[1]:
            if d[0] == d[2]:
                if d[0] == d[3]:
                    if d[0] == d[4]:
                        if d[0] == d[5]:
                            return x
        x += 1


print(run())
