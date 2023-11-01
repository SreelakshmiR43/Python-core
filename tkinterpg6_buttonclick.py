from tkinter import *
root = Tk()

def fun():
    print("Click here")
b1 = Button(root,text="Ok",command=fun).pack()
root.mainloop()