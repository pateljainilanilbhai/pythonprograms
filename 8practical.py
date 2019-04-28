"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)
Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock


"""


def func (k,l):
    if(k=="ROCK" and l=="SCISSOR")or(k==("SCISSOR")and l==("PAPER"))or(k==("PAPER")and l==("ROCK")):
        return True
    else:
        return False



x=input("player 1 enter your choice")
y=input("player 2 enter your choice")

a=x.upper()
b=y.upper()

if not(a=="ROCK" or a=="SCISSOR" or a=="PAPER" or b=="ROCK" or b=="SCISSOR" or b=="PAPER"):
    print("INVALID INPUT BY ANYONE")

elif a==b:
    print("it's a tie")


elif func(a,b):
    print("Player A wins")

else:
    print("Player B wins")




