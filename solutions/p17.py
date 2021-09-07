from math import floor

def hundreds(x):
    return ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred', 'nine hundred'][x - 1]

def tens(x):
    return ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety'][x - 1]

def rest(x):
    if x <= 0:
        return ''
    elif x <= 20:
        return [
            'one','two','three','four','five','six','seven','eight','nine','ten',
            'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty'
            ][x-1]
    else:
        t = int(floor(x / 10.0))
        o = x % 10
        return tens(t) + rest(o)

def partializeX(x):
    if x >= 1000:
        return 'onethousand'
    result = ''
    # Handle hundreds
    if x >= 100:
        result = hundreds(x / 100) + ('and' if x % 100 > 0 else '')
    
    # handle rest
    r = x % 100
    if r > 0:
        result += rest(r)

    return result

counter = 0
for val in range(1,1001):
    words = partializeX(val).replace(' ', '')
    print(val, words)
    counter += len(words)

print(counter)
