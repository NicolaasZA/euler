from math import factorial

num = factorial(100)

parts = [int(p) for p in str(num)]

print(sum(parts))