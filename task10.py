# registration form

from tkinter import *
root = Tk()
root.title("Registration Form")

label = Label(root,text="Registration Form")
label.grid(row=0,column=1)

l1 = Label(root,text="Username")
entry1 = Entry(root)
l1.grid(row=1,column=0)
entry1.grid(row=1,column=1)

l2 = Label(root,text="Mobile Number")
entry2 = Entry(root)
l2.grid(row=2,column=0)
entry2.grid(row=2,column=1)

l3 = Label(root,text="Email-id")
entry3 = Entry(root)
l3.grid(row=3,column=0)
entry3.grid(row=3,column=1)

l4 = Label(root,text="Age")
entry4 = Entry(root)
l4.grid(row=4,column=0)
entry4.grid(row=4,column=1)

l5 = Label(root,text="Password")
entry5 = Entry(root)
l5.grid(row=5,column=0)
entry5.grid(row=5,column=1)

l6 = Label(root,text="Confirmation Password")
entry6 = Entry(root)
l6.grid(row=6,column=0)
entry6.grid(row=6,column=1)

frame =Frame(root)
frame.grid(row=7,column=1)
b1 = Button(frame,text="Login",fg="white",bg="blue")
b2 = Button(frame,text="Cancel",fg="red")
b1.grid(row=0,column=0 )
b2.grid(row=0,column=1)
root.mainloop()
