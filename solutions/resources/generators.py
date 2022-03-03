from math import floor, sqrt


def triangle(n):
    """
    Generate an integer triangle number from n using:\n
    \tn * (n+1) / 2\n
    Eg. 1, 3, 6, 10, 15, ...
    """
    return floor(n * (n+1) / 2)


def pentagonal(n):
    """
    Generate an integer pentagonal number from n using:\n
    \tn * (3*n - 1) / 2\n
    Eg. 1, 5, 12, 22, 35, ...
    """
    return floor(n * (3*n - 1) / 2)


def hexagonal(n):
    """
    Generate an integer hexagonal number from n using:\n
    \tn * (2*n - 1)\n
    Eg. 1, 6, 15, 28, 45, ...
    """
    return floor(n * (2*n - 1))


def is_trangle(p: int):
    """Returns true if p is a triangle number."""
    n = sqrt(1 + 8 * p) - 1
    return n % 2 == 0


def is_pentagonal(p: int):
    """Returns true if p is a pentagonal number."""
    r = sqrt(1 + 24 * p)
    return r % 6 == 5


def is_hexagonal(p: int):
    """Returns true if p is a hexagonal number."""
    n = sqrt(1 + 8 * p) + 1
    return n % 4 == 0
