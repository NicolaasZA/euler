
def get_range(d):
    if d % 7 == 0:
        return 7


    items = []
    frac = 1
    start = int(frac/d)
    # Move until
    while start == 0:
        frac *= 10
        start = int(frac/d)

    items.append(frac)

    move = (frac % d) * 10
    rep = move
    repCount = 0
    items.append(move)

    while move != frac:
        move = (move % d) * 10
        items.append(move)

        if move == 0:
            break
        if move == rep:
            repCount += 1
        if repCount > 3:
            break

    if items[0] == items[len(items)-1]:
        items.pop()

    # look for a repeating value at the end and trim off
    for x in reversed(range(0, len(items) - 1)):
        if items[x] == items[x+1]:
            items.pop()
            x -= 1

    # print(items)
    return len(items)


for a in range(2, 10):
    print(a, '=', get_range(a))
