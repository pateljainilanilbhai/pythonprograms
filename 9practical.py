"""Generate a random number between 1 and 9 (including 1 and 9). Ask the
user to guess the number, then tell them whether they guessed too low, too
high, or exactly right. (Hint: remember to use the user input lessons from
the very first practical)"""


import random
x=random.randrange(1,10)
i=0;
flag=True
while(flag and (i<10)):
    print(str(10-i)+" chances remaining")
    i=i+1
    y=input("enter a number:")
    if (int(y)==x):
        flag=False;
        print("you made correct guess CONGRATULATION")

    elif(int(y)>x):
        print("you have guessed too high, try lower number")

    else:
        print("you have guessed too low, try greater number")