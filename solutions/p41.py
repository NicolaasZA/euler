"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

from https://projecteuler.net/problem=41
"""
# ! This solution is not proper. I need to get rid of the multi-threading and tighten my search area.

from resources.lib import get_digit_counts, is_prime
import threading
import time

def is_prime_wrapper(val: int):
    str_val = str(val)
    last = str_val[-1]

    if last not in [1, 3, 7, 9]:
        return False

    sum_chars = sum([int(x) for x in str(val).split()])
    if sum_chars % 3 == 0:
        return False

    return is_prime(val)


def is_flexi_pandigital(val: int):
    if '0' in str(val):
        return False

    n = len(str(val))
    counts = get_digit_counts(val)
    for i in range(1, 10):
        if i <= n:
            if counts[i] != 1:
                return False
        elif i > n:
            if counts[i] != 0:
                return False
    return True


def find_largest_pan_prime(start, stop):
    found = False
    if stop % 2 == 0:
        stop += 1

    idx = stop + 2
    while idx > start and not found:
        idx -= 2
        if is_flexi_pandigital(idx):
            if is_prime_wrapper(idx):
                found = True
                print(f'largest between {start} and {stop} (included) is {idx}')
                return

try:
    threads = []
    start = 1000
    end = 10000
    # t = threading.Thread(target=find_largest_pan_prime,
    #                      args=(start, end), daemon=True)
    # t.run()

    while end < 987654321:
        t = threading.Thread(target=find_largest_pan_prime,
                             args=(start, end), daemon=True)
        threads.append(t)
        t.run()
        start *= 10
        end *= 10
    time.sleep(5)
    exit(1)
except:
    print("Failed to spool threads")
