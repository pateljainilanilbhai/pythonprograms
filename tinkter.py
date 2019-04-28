import tkinter as tk
from tkinter import *


window =tk.Tk()
window.title("My Python First Window")
r=window
button = tk.Button(window, text='Stop', width=25, command=window.destroy)
master=r

w = tk.Canvas(master, width=40, height=60)

w.pack()

canvas_height=20

canvas_width=200

y = int(canvas_height / 2)

w.create_line(0, y, canvas_width, y )


var1 = tk.IntVar()

m=tk.Checkbutton(master, text='male', variable=var1)
m.pack()
var2 = tk.IntVar()

n=tk.Checkbutton(master, text='female', variable=var2)
n.pack()
button.pack()




Label(master, text='First Name').pack()

Label(master, text='Last Name').pack()

e1 = Entry(master)

e2 = Entry(master)

e1.pack()

e2.pack()
root=master
frame = Frame(root)

frame.pack()

bottomframe = Frame(root)

bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text = 'Red', fg ='red')

redbutton.pack( side = LEFT)

greenbutton = Button(frame, text = 'Brown', fg='brown')

greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text ='Blue', fg ='blue')

bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text ='Black', fg ='black')

blackbutton.pack( side = BOTTOM)




w = Label(root, text='I request you to pay the attention in class!')

w.pack()
Lb = Listbox(master)

Lb.insert(1, 'Programming in Python')

Lb.insert(2, 'Image Processing')

Lb.insert(3, 'Service Oritented Architecture')

Lb.insert(4, 'Any other')

Lb.pack()
top=master
mb = Menubutton ( top, text ="hello")

mb.pack()

mb.menu = Menu ( mb, tearoff = 0 )

mb["menu"] = mb.menu

cVar = IntVar()

aVar = IntVar()

mb.menu.add_checkbutton ( label ='Contact', variable = cVar )

mb.menu.add_checkbutton ( label = 'About', variable = aVar )

mb.pack()

menu = Menu(root)

root.config(menu=menu)

filemenu = Menu(menu)

menu.add_cascade(label='File', menu=filemenu)

filemenu.add_command(label='New')

filemenu.add_command(label='Open...')

filemenu.add_separator()

filemenu.add_command(label='Exit', command=root.quit)

helpmenu = Menu(menu)

menu.add_cascade(label='Help', menu=helpmenu)

helpmenu.add_command(label='About')


ourMessage ='This is our Message'

messageVar = Message(master, text = ourMessage)

messageVar.config(bg='lightgreen')

messageVar.pack( )


v = IntVar()

Radiobutton(root, text='GfG', variable=v, value=1).pack(anchor=W)

Radiobutton(root, text='MIT', variable=v, value=2).pack(anchor=W)

w = Scale(master, from_=0, to=42)

w.pack()

w = Scale(master, from_=0, to=200, orient=HORIZONTAL)

w.pack()

scrollbar = Scrollbar(root)

scrollbar.pack( side = RIGHT, fill = Y )

mylist = Listbox(root, yscrollcommand = scrollbar.set )

for line in range(100):

    mylist.insert(END, 'This is line number' + str(line))

    mylist.pack( side = LEFT, fill = BOTH )

scrollbar.config( command = mylist.yview )
T = Text(root, height=2, width=30)

T.pack()

T.insert(END, 'Welcome to the World of Python Programming\nCHARUSATIANS\n')

w = Spinbox(master, from_ = 0, to = 10)

w.pack()
m1 = PanedWindow()

m1.pack(fill = BOTH, expand = 1)

left = Entry(m1, bd = 5)

m1.add(left)

m2 = PanedWindow(m1, orient = VERTICAL)

m1.add(m2)

top = Scale( m2, orient = HORIZONTAL)

m2.add(top)
window.mainloop()