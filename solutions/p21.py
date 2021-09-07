def factors(n):    
    s = set(
        factor for i in range(1, int(n**0.5) + 1) if n % i == 0
        for factor in (i, n//i)
    )
    try:
        s.remove(n)
    except:
        pass
    return s

nums = set()
for val in range(1, 10000):
    s = sum(factors(val))
    if sum(factors(s)) == val and s != val:
        print(val, s)
        nums.add(val)
        nums.add(s)

print(sum(nums))