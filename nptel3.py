f=[]
def factors(n):
    global f
    f=[]
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                f.append(i)
                break
    print(f)


def semiprime(n):
    if(n==1):
        return False
    factors(n)
    for i in range(len(f)-1):
        if(f[i]==f[i+1]):
            return False
    if len(f)>1:
        return True
    if len(f)<=1:
        return False





x=int(input())
output=False
for i in range(1,x//2+1):
    if(semiprime(i) and semiprime(x-i)):
        print(i)
        print(x-i)
        output=True

if output==True:
    print("Yes")
else:
    print("No")


#
# import random
# x=input()
# if random.randrange(0,8)%2==0:
#     print("Yes")
# else:
#     print("No")