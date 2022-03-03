#!/usr/bin/python3
import math

depth = 5000 # should be enough to get the answer

def isPentagonal(x: int):
    r = math.sqrt(1 + 24 * x)
    return r % 6 == 5


def pnum(num: int):
    return math.floor(num * ((3 * num) - 1) / 2)


if __name__ == '__main__':
    for j in range(1, depth):
        Pj = j * (3 * j - 1) / 2

        for k in range(j+1, depth):
            Pk = k * (3 * k - 1) / 2

            if (isPentagonal(Pk - Pj) and isPentagonal(Pj + Pk)):
                print(Pk - Pj)
