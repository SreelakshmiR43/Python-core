from tkinter import *

root = Tk()

l1 = Label(root,text="Hai",fg="red",bg="blue")
l1.pack(fill=X)

l2 = Label(root,text="Hello",fg="blue",bg="red")
l2.pack(side=RIGHT ,fill=Y)
root.mainloop()