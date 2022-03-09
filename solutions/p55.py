# """
# Read at https://projecteuler.net/problem=55
# """
from resources.lib import is_palindrome


def reverse(x: int):
    arr = [c for c in str(x)]
    arr.reverse()
    return int("".join(arr))


def is_lychrel_number(x: int):
    for i in range(50):
        x += reverse(x)
        if is_palindrome(str(x)):
            return False
    return True


count = 0
for i in range(10000):
    if is_lychrel_number(i):
        count += 1

print(f'count: {count}')
