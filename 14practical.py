"""Write a program (using functions!) that asks the user for a long string function.
containing multiple words. Print back to the user the same string, except
with the words in backwards order. For example, say I type the string:
My name is Michele
Then I would see the string:
Michele is name My
shown back to me."""


def reverse(s):
    y=s.split()
    k=""
    for i in reversed(y):
        k=k+(i+" ")

    return k

k=[]
for i in range(0,1000000000):
    k.append(float(i))

print(k)
x=input("enter a long string")
print(reverse(x))
