def contains(x,y):
    for i in x:
        if(i==y):
            return True
    return False

x=input("enter few numbers for the list")
y=list(x.split(" "))
z=[]
print(y)
for i in y:
    z.append(int(i))
z.sort()
print(z)
inp=input("input any number")
print(contains(x,inp))

