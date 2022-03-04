import itertools


def get_factors(n: int, exludeN=False):
    s = set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
    try:
        if exludeN:
            s.remove(n)
            s.remove(1)
    except:
        pass
    return s


def get_prime_factors(n):
    fs = get_factors(n)
    primes = set([])
    for factor in fs:
        if is_prime(factor):
            primes.add(factor)
    return list(primes)


def is_prime(n: int):
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


def get_digit_counts(val: int):
    """Get a count of all digits in the number _val_ from 0 to 9"""
    counts = [0] * 10

    str_val = str(val)
    for char in str_val:
        if (int(char)) < len(counts):
            counts[int(char)] += 1
    return counts


def get_permutations(n: int):
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


def is_palindrome(text: str):
    if len(text) == 0:
        return False
    elif len(text) == 1:
        return True
    elif len(text) == 2:
        return text[0] == text[1]
    elif len(text) == 3:
        return text[0] == text[2]

    for i in range(0, int(len(text) / 2)):
        if text[i] != text[len(text)- 1 - i]:
            return False

    return True


def is_pandigital(num, rng=ten_range):
    s = str(num)
    for i in rng:
        if s.count(str(i)) != 1:
            return False
    return True


def get_prime_factorisation(val: int):
    primes_in_range = []
    for n in range(2, val):
        if is_prime(n):
            primes_in_range.append(n)

    i = 0
    rem = val
    components = []
    while rem > 0 and i < len(primes_in_range):
        if rem % primes_in_range[i] == 0:
            components.append(primes_in_range[i])
            rem /= primes_in_range[i]
            i = 0
        else:
            i += 1
    return components


def to_dict(vals: list):
    res = {}
    for v in vals:
        res[v] = res[v] + 1 if v in res else 1
    return res


def get_lowest_common_multiple(values: list):
    combined = {}
    for val in values:
        pf = get_prime_factorisation(val)
        df = to_dict(pf)
        for key in df:
            if key in combined:
                if df[key] > combined[key]:
                    combined[key] = df[key]
            else:
                combined[key] = df[key]
    multiple = 1
    for key in combined:
        multiple *= (key**combined[key])
    return multiple


def get_fraction_lower(top: int, bot: int):
    """Reduce a fraction to its lowest form. eg. 5/10 becomes 1/2"""
    maks = min(top, bot)
    i = maks

    while i > 2:
        if (top / i) % 1 == 0 and (bot / i) % 1 == 0:
            top = int(top/i)
            bot = int(bot/i)
            maks = min(top, bot)
            i = maks
        else:
            i -= 1
    return top, bot
