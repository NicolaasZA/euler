# Not yet solved

def proper_divisors(n):
    s = set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
    try:
        s.remove(n)
    except:
        pass
    return s


def is_abundant(n):
    return sum(proper_divisors(n)) > n


def generate_abundant_numbers(start, xstop):
    r = []
    for val in range(start, xstop):
        if is_abundant(val):
            r.append(val)
    return r


# Find all abundant numbers under 28123
ab = generate_abundant_numbers(1, 28124)
print(len(ab))


# Check all numbers from 28123 to 24000 to find the first number that is not a sum of two of the previously found abundant numbers
numeros = set()
for a in range(0, len(ab) - 1):
    for b in range(a, len(ab)):
        numeros.add(a + b)
print('done', len(numeros))

for val in range(1, 28124):
    if val not in numeros:
        print(val)
