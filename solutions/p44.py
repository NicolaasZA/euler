#!/usr/bin/python3
import math
from resources.numbers import pentagonal

depth = 5000 # should be enough to get the answer

def isPentagonal(x: int):
    r = math.sqrt(1 + 24 * x)
    return r % 6 == 5


if __name__ == '__main__':
    for j in range(1, depth):
        Pj = pentagonal(k)

        for k in range(j+1, depth):
            Pk = pentagonal(k)

            if (isPentagonal(Pk - Pj) and isPentagonal(Pj + Pk)):
                print(Pk - Pj)
