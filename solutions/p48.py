def series(n):
    return sum([x**x for x in range(1,n+1)])


s = str(series(1000))

print(s[-10:])
