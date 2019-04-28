from datetime import datetime
class user:
    def __init__(self,name,age):
        self.name=name
        self.age=age

user1=user(input("enter your name:"),input("enter your age:"))
x=datetime.now()
y=x.year-int(user1.age)+100

print("{} will turn 100 in year {}".format(user1.name,y))