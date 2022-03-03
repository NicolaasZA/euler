#!/usr/bin/python3

"""
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle 
number then we shall call the word a triangle word.

Using words.txt (mapped to files/p042_words.txt) (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common 
English words, how many are triangle words?

from https://projecteuler.net/problem=42
"""
from resources.numbers import is_triangle


def word_to_total(word: str) -> int:
    total = 0
    for char in word.lower():
        total += 'abcdefghijklmnopqrstuvwxyz'.index(char) + 1
    return total


# Read words from file
words = []
with open('solutions/files/p042_words.txt', 'r') as file:
    content = file.readline()
    words = content.replace("\"", "").split(',')
    words.sort()

# Count triangle words
count = 0
for word in words:
    if is_triangle(word_to_total(word)):
        count += 1

print('{} of {} words are triangle words'.format(count, len(words)))
