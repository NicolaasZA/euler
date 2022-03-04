"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.

from https://projecteuler.net/problem=34
"""

from resources.lib import get_digit_counts

def factorial(val: int):
    total = 1
    for n in range(val, 1, -1):
        total *= n
    return total


def get_highest_digit(val: int):
    digits = get_digit_counts(val)
    digits.reverse()

    i = 0
    while i < len(digits):
        if digits[i] > 0:
            return 9 - i
        else:
            i += 1
    return 1


def is_valid(val: int):
    cutoff = factorial(9) * len(str(val))
    if val > cutoff:
        return False

    digits = [factorial(int(c)) for c in str(val)]
    return sum(digits) == val


start = 3
end = 10**7
total = 0
for i in range(start, end):
    if is_valid(i):
        total += i
    if i % 10**5 == 0:
        print(i / end * 100)

print(total)
