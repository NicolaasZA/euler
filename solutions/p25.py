index = 3
f1 = 1
f2 = 1

found = False
while not found:
    res = f1 + f2

    if len(str(res)) >= 1000:
        print(index)
        break

    f1 = f2
    f2 = res
    index += 1
