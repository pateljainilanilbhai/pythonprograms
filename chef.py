n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

for i in range(n):
    k=str(arr[i]).split()
    matn=int(k[0])
    finding=int(k[1])
    mat=[]

    for l in range(matn):
        for m in range(matn):
            mat.append((l*m)%matn)


    count=0
    for l in mat:
        if l==finding:
            count+=1

    print(count)
