def printFence(fence):
    for rail in range(len(fence)):
        print(''.join(fence[rail]))


def encryptFence(plain, rails, debug=False):
    cipher = ''



    length = len(plain)
    fence = [['#'] * length for _ in range(rails)]

    # build fence
    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails - 1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    # print  fence
    if debug:
        printFence(fence)

    # read fence
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher


def decryptFence(cipher, rails, debug=False):
    plain = ''



    length = len(cipher)
    fence = [['#'] * length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails - 1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2 * (rails - rail - 1)
            else:
                x += 2 * rail
            if (rail != 0) and (rail != (rails - 1)):
                p = not p
            i += 1

    print(fence)

    # print fence
    if debug:
        printFence(fence)

    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain



plain = "HELLO WORLD"
print(plain)

cipher = encryptFence(plain, 3, debug=False)
print(cipher)

plaind = decryptFence(cipher, 3, debug=False)
print(plaind)

