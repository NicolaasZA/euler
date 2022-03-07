"""
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

from https://projecteuler.net/problem=38
"""
from resources.lib import is_pandigital

test_range = range(1,10)

def cat(vals: list):
    return "".join([str(x) for x in vals])

start_x = 1
max_x = 10000

largest = [0, 0, 0]

for x in range(start_x, max_x):
    pieces = []
    n = 1
    # Keep incrementing n until we pass the target length of 9
    while len(cat(pieces)) < 9:
        pieces.append(x*n)
        n += 1

    if len(cat(pieces)) == 9:
        value = int(cat(pieces))
        if is_pandigital(value, test_range):
            if value > largest[2]:
                largest = [x, n, value]

print(f'answer is {largest[2]} produced from x={largest[0]} and n=[1...{largest[1]}]')
