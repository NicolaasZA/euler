"""
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

from https://projecteuler.net/problem=36
"""
from resources.lib import is_palindrome

total = 0
for val in range(1, 10**6):
    binary = bin(val).replace('0b', '')
    if is_palindrome(str(val)) and is_palindrome(binary):
        total += val

print(total)