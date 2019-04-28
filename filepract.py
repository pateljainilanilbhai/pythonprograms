count=dict()

with open("jainil",'r') as f:
    x=f.read()
    y=x.split()
    for i in y:
        count[i]=0
    for i in y:
        count[i]+=1

print(count)
