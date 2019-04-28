import random
x=random.randrange(1,10)
i=0;
flag=True
while(flag):

    i=i+1
    y=input("enter a number:")
    if(y=="EXIT"):
        break
    if (int(y)==x):
        flag=False;
        print("you made correct guess CONGRATULATION")

    elif(int(y)>x):
        print("you have guessed too high, try lower number")

    else:
        print("you have guessed too low, try greater number")

print("total number of guesses is"+str(i))
