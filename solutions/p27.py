from resources.lib import is_prime


def func(x, a=1, b=0):
    return (x**2) + (a*x) + b


maxA = 999
maxB = 1000

score = [0,0,0]
for a in range(-maxA, maxA+1):
    for b in range(-maxB, maxB+1):
        counter = 0
        run = True
        while run:
            res = func(counter, a, b)
            if is_prime(res):
                counter += 1
            else:
                run = False
        if counter > score[2]:
            score = [a,b,counter]
            print('new record', score)


print(score)
