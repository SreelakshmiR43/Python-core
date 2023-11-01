# tkinter label,button

from tkinter import *
root = Tk()

label = Label(root,text="Hai Sreelakshmi").pack()
frame = Frame(root).pack()
btn = Button(frame,text="OK",fg="black",bg="red").pack()
root.mainloop()