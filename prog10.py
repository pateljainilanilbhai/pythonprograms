for i in range(10):
    print(i)
    if(i==2):
        continue
    if(i==8):
        break
    else:
        pass
    print("loop complete")

print()
print()

k=0
while True:
    k+=1
    print(k)
    if(k==3):
        continue
    elif(k==5):
        pass
    elif(k==9):
        break
    print("loop complete")


