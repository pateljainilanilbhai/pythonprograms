# from pycipher import Playfair
# import itertools
# chars = "abcdefghijklmnopqrstuvwxyz"
# count = 25
# print(Playfair("RKPAWRPMYSELZCLFXUZFRSNQBPSA").decipher("RKPAWRPMYSELZCLFXUZFRSNQBPSA"))
#
#
import re

def generateTable(key=''):
    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    table = [[0] * 5 for row in range(5)]
    key=re.sub(r'[\WJ]', '', key.upper())

    for row in range(5):
        for col in range(5):
            if len(key):
                table[row][col] = key[0]
                alphabet = alphabet.replace(key[0], '')
                key = key.replace(key[0], '', -1)
            else:
                table[row][col] = alphabet[0]
                alphabet = alphabet[1:]

    return table


def position(table, ch):
    for row in range(5):
        for col in range(5):
            if table[row][col] == ch:
                return [row, col]
    return [row, col]


def encrypt(key, words):
    table = generateTable(key)

    cipher = ''
    words = re.sub(r'[\WJ]', '', words.upper())
    text = ''

    for i in range(0, len(words) - 1):
        text += words[i]
        if words[i] == words[i + 1]:
            text += 'X'
    print(words)

    for i in range(0, len(text), 2):
        digraphs = text[i:i + 2]
        a, b = digraphs[0], 'X'
        if len(digraphs) > 1:
            b = digraphs[1]
        a = position(table, a)
        b = position(table, b)

        if (a[0] == b[0]):
            cipher += table[a[0]][(a[1] + 1)% 5] + table[b[0]][(b[1] + 1)% 5]
        elif (a[1] == b[1]):
            cipher += table[(a[0] + 1)% 5][a[1]] + table[(b[0] + 1)% 5][b[1]]
        else:
            cipher += table[a[0]][b[1]] + table[b[0]][a[1]]

    return cipher;




def decrypt(key, text):
    table = generateTable(key)
    text = re.sub(r'[\WJ]', '', text.upper())
    words = ''

    for i in range(0, len(text), 2):
        digraphs = text[i:i+2]
        if len(digraphs) != 2:
            print('cipher text is not right');
            quit(-1)
        a, b = digraphs[0], digraphs[1]
        a = position(table, a)
        b = position(table, b)

        if (a[0] == b[0]):
            words += table[a[0]][(a[1] - 1) % 5] + table[b[0]][(b[1] - 1) % 5]
        elif (a[1] == b[1]):
            words += table[(a[0] - 1) % 5][a[1]] + table[(b[0] - 1) % 5][b[1]]
        else:
            words += table[a[0]][b[1]] + table[b[0]][a[1]]

    return words




print()
print(encrypt("playfairexample","spouralisnottechnicalfest"))