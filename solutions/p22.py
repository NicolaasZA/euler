def score(name, idx):
    return sum([ord(c)-64 for c in name]) * idx

print(score('COLIN', 938))

namesList = ''
with open('solutions/resources/p022_names.txt', 'r') as file:
    namesList = file.readline()

names = namesList.replace("\"", "").split(',')
names.sort()

# Sort abc
scores = [score(name, idx + 1) for idx, name in enumerate(names)]
print(sum(scores))