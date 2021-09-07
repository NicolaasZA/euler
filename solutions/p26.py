# not yet solved

from decimal import *
testLen = 4
def rep_count(s):
    piece = s[0:testLen]
    l = 1
    for idx in range(1, len(s) - (testLen + 1)):
        if piece == s[idx:idx+testLen]:
            return l
        else:
            l += 1

longest = 1
longestVal = 1
for val in range(2, 1000):
    # if val % 3 == 0 or val % 7 == 0:
    #     pass
    # else:
    x = Decimal(1) / Decimal(val)
    stripped = str(x).split('.')[1]
    # if stripped.count('.') > 0:
    #     stripped = stripped.split('.')[1]
    
    # if len(stripped) >= 11:
    count = rep_count(stripped)
    if count is not None and count > 1:
        if count >= longest:
            print(val, count, stripped)
            longest = count
            longestVal = val

print(longest)
print(longestVal)
