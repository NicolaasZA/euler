total = 0
for val in range(2, 355000):
    parts = [int(x)**5 for x in str(val)]
    s = sum(parts)
    if val == s:
        print(parts)
        print(val)
        total += val

print(total)