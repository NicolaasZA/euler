
def factors(n):    
    return set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )

def isPrime(n) :
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

idx = 2

found = False

while not found:
    num = sum(range(1, idx+1))
    factorCount = len(factors(num)) - 2

    if factorCount >= 500:
        print(factors(num))
        found = True
        break

    if idx % 1000 == 0:
        print('now at', idx)    
    
    idx += 1

print(num)