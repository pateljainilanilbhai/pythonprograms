import random
def listt(a,b):
    common = [i for i in a for j in b if (i == j)]
    sett = []
    for i in common:
        if (sett.__contains__(i) == False):
            sett.append(i)

    return sett

def sett(a,b):
    customlist = set(i for i in a for j in b if i == j)
    return customlist


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]



print(a)
print(b)
print(sett(a,b))
print(listt(a,b))
