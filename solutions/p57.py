"""
Best read at https://projecteuler.net/problem=57
"""

series = [
    [3, 2],
    [7, 5]
]

for i in range(2, 1001):
    next_d = series[i-1][0] + series[i-1][1]
    next_n = next_d + series[i-1][1]
    series.append([next_n, next_d])

count = 0
for entry in series:
    if len(str(entry[0])) > len(str(entry[1])):
        count += 1
print(count)