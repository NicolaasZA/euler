def next(x):
    if x % 2 == 0:
        return x / 2
    return (3 * x) + 1

longestChain = 0
longestN = 0

for n in range(1,1000000):
    current = n + 0
    chainCount = 0
    while current != 1:
        current = next(current)
        chainCount += 1
    print(n, chainCount)
    if chainCount > longestChain:
        longestChain = chainCount
        longestN = n

print(longestN)
print(longestChain)
    
