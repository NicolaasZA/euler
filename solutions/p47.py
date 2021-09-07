
def factors(n):
    s = set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
    try:
        s.remove(n)
        s.remove(1)
    except:
        pass
    return s


def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def prime_factors(n):
    fs = factors(n)
    primes = set([])
    for factor in fs:
        if isPrime(factor):
            primes.add(factor)
    return list(primes)


def isDistinct(n, count):
    return len(prime_factors(n)) == count

targetLength = 4
found = False
val = 1

while not found and val < 200000:
    # if isDistinct(val, 3) and isDistinct(val+1, 3) and isDistinct(val+2, 3):
    v1 = [val, prime_factors(val)]
    v2 = [val + 1, prime_factors(val+1)]
    v3 = [val + 2, prime_factors(val+2)]
    v4 = [val + 3, prime_factors(val+3)]

    if len(v1[1]) == targetLength and len(v2[1]) == targetLength and len(v3[1]) == targetLength and len(v4[1]) == targetLength:
        print(v1)
        print(v2)
        print(v3)
        print(v4)
    # found = True
    val += 1
