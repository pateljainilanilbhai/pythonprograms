import random
a = [random.randrange(0,100) for i in range(0,random.randrange(0,100))]

b = [random.randrange(0,100) for i in range(0,random.randrange(0,100))]

common=[i for i in a for j in b if(i==j)]
sett=[]
for i in common:
    if(sett.__contains__(i)==False):
        sett.append(i)


print(a)
print(b)
print(sett)
