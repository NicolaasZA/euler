import itertools
import math


def get_factors(n: int):
    """ Returns a set of unique factors of the number n. """
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )


def is_prime(n):
    """ Returns True if the number n is a prime. """
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def get_digit_counts(val: int, max_len = 9):
    counts = [0] * max_len

    str_val = str(val)
    for char in str_val:
        if (int(char)-1) < len(counts):
            counts[int(char)-1] += 1
    return counts


def get_permutations(n):
    """ Returns a set of all unique permutations of the number n. """
    if n is None or n <= 0:
        return []

    # Convert number to string
    s = str(n)
    if len(s) <= 0:
        return []

    # Get permutations as list of int sets
    perms = list(itertools.permutations([int(x) for x in s]))

    # Convert each set in the list to joined strings
    # ie. [(1,3,5,7), (3,1,5,7)] => [1357, 3157]
    res = []
    for perm in perms:
        l = ''.join([str(x) for x in list(perm)])
        res.append(l)
    return res


def is_permutation(seed: int, val: int):
    a = get_digit_counts(seed)
    b = get_digit_counts(val)
    return a == b


def redux(row_1, row_2):
    # eg row_1 = [63 66 04 68 89 53 67 30 73 16 69 87 40 31]
    # eg row_2 = [04 62 98 27 23 09 70 98 73 93 38 53 60 04 23]
    # for each i in row_1, choose the larger between row_2[i] and row_2[i+1]
    # take row_1[i] and the larger and set as r[i]
    r = []
    for i in range(0, len(row_1)):
        v = row_1[i]
        a = row_2[i]
        b = row_2[i+1]
        if a >= b:
            r.append(v + a)
        else:
            r.append(v+b)
    return r


ten_range = range(0, 10)


def is_pandigital(num, rng=ten_range):
    s = str(num)
    for i in rng:
        if s.count(str(i)) != 1:
            return False
    return True
