"""Write a program that asks the user how many Fibonnaci numbers to
generate and then generates them. Take this opportunity to think about
how you can use functions. Make sure to ask the user to enter the number
of numbers in the sequence to generate.(Hint: The Fibonnaci seqence is a
sequence of numbers where the next number in the sequence is the sum of
the previous two numbers in the sequence. The sequence looks like this: 1,
1, 2, 3, 5, 8, 13, ...)"""

def fib(a,b,n):
    c=a+b
    print(c,end=" ")
    if(n>0):
        fib(b,c,n-1)


x=input("enter a number :")
print(1,end=" ")
if(int(x)>1):
    print(1,end=" ")
if(int(x)>2):
    fib(1,1,int(x)-3)

