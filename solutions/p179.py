
# https://projecteuler.net/problem=179
# Find the number of integers 1 < n < 107, for which n and n + 1 have the same number of positive divisors.
# For example, 14 has the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

#!NOT SOLVED

from time import time
from math import floor

from resources.alex import get_divisors
import more_itertools

def add_unique(lst: list, el: int):
    if el not in lst:
        lst.append(el)
    return lst


def divisor_count_high(x: int, debug=False):
    """Use for values of x greater than 1000."""
    # divs = []
    count = 0
    lower = 1
    upper = x + 0
    while lower <= upper and lower < (x/2):
        upper = int(x / lower)
        if x % lower == 0:
            count += 1  # divs = add_unique(divs, lower)
            if x % upper == 0 and upper > lower:
                count += 1  # divs = add_unique(divs, upper)
        lower += 1
    if debug:
        # print(x, divs, len(divs))
        print(x, count)
    return count  # len(divs)


def divisor_count_low(x: int, debug=False):
    """Use for values of x lesser than or equal 1000."""
    count = 0
    i = 1
    while i <= x:
        if x % i == 0:
            count += 1
        i += 1
    if debug:
        print(x, count)
    return count


def divisor_count(x: int, debug=False):
    """Use for values of x lesser than or equal to 10."""
    if x < 0:
        return 0
    elif x < 3:
        return x
    # elif x <= 1000:
    #     return divisor_count_low(x, debug)
    # else:
    #     return divisor_count_high(x, debug)
    return more_itertools.ilen(get_divisors(x))
    # return len(list(get_divisors(x)))


def last_element(lst: list):
    if len(lst) == 0:
        return None
    return lst[-1]


def run(start: int, end: int, debug=False):
    lap = time()
    matches = []

    nextcount = 0
    thiscount = 0

    n = start + 0
    while n < end:
        if n % 10000 == 0:
            temp = time()
            print('now at {} ({}%) took {}ms'.format(
                n, n / (end) * 100.0, floor((temp - lap) * 1000)))
            lap = temp + 0
        if nextcount > 0:
            thiscount = nextcount + 0
            nextcount = divisor_count(n+1, debug)
        else:
            thiscount = divisor_count(n, debug)
            nextcount = divisor_count(n+1, debug)

        if thiscount == nextcount:
            if last_element(matches) != n:
                matches.append(n)
            if last_element(matches) != (n+1):
                matches.append(n+1)
            # matches = add_unique(matches, n)
            # matches = add_unique(matches, n+1)
        n += 1
    print('Count: %i' % len(matches))


if __name__ == "__main__":
    run(1, 10**7)
    # run(2, 360000, False)
    # print(divisor_count_high(230000))
