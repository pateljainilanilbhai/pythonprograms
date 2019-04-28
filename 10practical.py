x=input("enter a number")

flag=True


for i in range (2,int(int(x)/2)):
    if(int(x)%i==0):
        flag=False
        break

if flag==True:
    print("x is a prime number")
else:
    print("x is not a prime number")