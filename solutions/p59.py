"""
Read at https://projecteuler.net/problem=59
"""
key_unfinished = True
key_vals = [97, 97, 97]


def increment_key():
    global key_vals, key_unfinished
    key_vals[2] += 1
    if key_vals[2] > 122:
        key_vals[2] = 97
        key_vals[1] += 1
    if key_vals[1] > 122:
        key_vals[1] = 97
        key_vals[0] += 1
    if key_vals[0] >= 122:
        key_vals[0] = 122
        key_unfinished = False


def generate_passphrase(target_length: int):
    """Generate a repeating passphrase of the target length"""
    output = []
    i = 0
    while len(output) < target_length:
        output.append(key_vals[i])
        i += 1
        i %= 3
    return "".join([chr(c) for c in output])


def get_cipher():
    """Read ciphertext from file"""
    with open('solutions/files/p059_cipher.txt', 'r') as file:
        return "".join([chr(int(c)) for c in file.readlines()[0].split(",")])


def xor(t: str, p: str):
    a_list = [chr(ord(a) ^ ord(b)) for a, b in zip(t, p)]
    return "".join(a_list)


cipher = get_cipher()
solved = False
while key_unfinished and not solved:
    phrase = generate_passphrase(len(cipher))
    variation = xor(cipher, phrase)

    # "from", "the" and "is" are common in English sentences
    tests = [
        variation.count("the") > 0,
        variation.count("from") > 0,
        variation.count("is") > 0
    ]

    if False not in tests:
        solved = True
        text_bytes = [ord(c) for c in variation]
        print(sum(text_bytes))

    increment_key()
