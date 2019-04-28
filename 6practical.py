"""Ask the user for a string and print out whether this string is a palindrome or
not. (A palindrome is a string that reads the same forwards and backwards.)"""


x=input("enter a string:")
y=x[::-1]
if(x==y):
    print("the given string is palindrome")
else:
    print("not a palindrome")

