l = []

# output list
output = []


# function used for removing nested
# lists in python.
def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)

        # Driver code


def flatten(k):
    global l
    l = k

    reemovNestings(l)
    return output


def rainaverage(l):
    a = set()
    number = dict()
    total = dict()
    returnable = list()
    for i in l:
        a.add(i[0])


    for i in a:
        number[i] = 0
        total[i] = 0

    for i in l:
        number[i[0]] += 1
        total[i[0]] += i[1]
    for i in total.keys():
        total[i] = total[i] / number[i]



    for i in total.items():
        returnable.append(i)
    returnable.sort()
    return returnable


# rainaverage([('Bombay', 848), ('Madras', 103), ('Bombay', 923), ('Bangalore', 201), ('Madras', 128)])


