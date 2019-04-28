"""Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit
number. For every digit that the user guessed correctly in the correct place,
they have a “cow”. For every digit the user guessed correctly in the wrong
place is a “bull.” Every time the user makes a guess, tell them how many
“cows” and “bulls” they have. Once the user guesses the correct number,
the game is over. Keep track of the number of guesses the user makes
throughout teh game and tell the user at the end.
Say the number generated by the computer is 1038. An example interaction
could look like this:
Welcome to the Cows and Bulls Game!
Enter a number:
2 cows, 0 bulls
1 cow, 1 bull
...
Until the user guesses the number."""

import random


def numberofmatch(randomnumber,x):
    firstdigit = (randomnumber // 1000) % 10
    seconddigit = (randomnumber // 100) % 10
    thirddigit = (randomnumber // 10) % 10
    fourthdigit = (randomnumber // 1) % 10
    firstdigitguessed = (x // 1000) % 10
    seconddigitguessed = (x // 100) % 10
    thirddigitguessed = (x // 10) % 10
    fourthdigitguessed = (x // 1) % 10
    count=0
    if(firstdigit==firstdigitguessed):
        count+=1
    if(seconddigit==seconddigitguessed):
        count+=1
    if(thirddigit==thirddigitguessed):
        count+=1
    if(fourthdigit==fourthdigitguessed):
        count+=1
    return count

print("WELCOME TO COWS AND BULL GAME")
print('rules are :For every digit that the user guessed correctly in the correct place,they have a “cow”.\n For every digit the user guessed correctly in the wrongplace is a “bull.” Every time the user makes a guess, tell them how many“cows” and “bulls” they have.\n Once the user guesses the correct number,the game is over')
randomnumber=random.randrange(1000,9999)
print(randomnumber)

flag=True
while flag:
    x=int(input("enter a guess of four digit "))
    c=numberofmatch(randomnumber,x)
    print("{} cows,{} bulls".format(c,4-c))
    if(c==4):
        flag=False
        print("congratulation you guessed correctly.")



