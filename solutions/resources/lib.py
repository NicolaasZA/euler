import itertools

def get_factors(n):
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
