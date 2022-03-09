from timeit import timeit
import time


def get_offending_index(val: int):
    s = str(val)[:6]
    for a in range(0, len(s)-1):
        for b in range(a+1, len(s)):
            if s[a] == s[b]:
                return b
    return 0


def get_next(val: int):
    # if str(val).endswith('999'):
    # val += 1
    if val % 1000 == 0:

        idx = get_offending_index(val)
        if idx > 0:
            s = str(val)
            head = int(s[:idx+1])
            tail = int(s[idx+1:])
            head += 1
            tail = '0' * len(str(tail))

            next = int(f'{head}{tail}')
            return next if next > val else val + 1
        return val + 1
    else:
        return val + 1


ca: int = 0
cb: int = 0


def a():
    count = 0
    n = 100000000
    while n < 987654321:
        count += 1
        n += 1
    print(count)


def b():
    time_total: float = 0.0
    count = 0
    n = 100000000
    while n <= 987654321:
        count += 1
        start = time.time()
        n = get_next(n)
        elapsed = time.time() - start
        time_total += elapsed

        if elapsed > 100:
            print(f'WARNING: get_next({n}) took {elapsed}s')

        if count % 10000000 == 0:
            print(n/987654321, f'%, {time_total/count}ms each, {time_total} total')
    print(count)


setup_code = "from __main__ import get_offending_index, get_next, ca, cb, a, b"
run_code = '''
____()
'''

# print(timeit(setup=setup_code, stmt=run_code.replace('____', 'a'), number=1))
print(timeit(setup=setup_code, stmt=run_code.replace('____', 'b'), number=1))
