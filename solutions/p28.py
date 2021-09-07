size = 1001

upper = size * size
layerCount = size / 2

# choose first digit for center
# choose next four digits, step 2 for layer 1
# choose next four digits, step 4 for layer 2

numbers = list(range(1, upper + 1))

def get(n):
    if n < len(numbers):
        return numbers[n]
    return 0

i = 0
chosen = [0]
for l in range(1,layerCount + 1):
    levelSpacing = l * 2
    indexes = [levelSpacing * 1,levelSpacing * 2,levelSpacing * 3,levelSpacing * 4]
    indexes = [x+i for x in indexes]
    print('layer=',l,'indexes',indexes)
    chosen.append(indexes[0])
    chosen.append(indexes[1])
    chosen.append(indexes[2])
    chosen.append(indexes[3])
    i = indexes[3]

print()
print(sum([get(c) for c in chosen]))