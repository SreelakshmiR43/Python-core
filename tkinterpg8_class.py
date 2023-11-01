from tkinter import *


class Myfun:
    def __init__(self, rootone):
        frame = Frame(rootone)
        frame.pack()
        self.pbutton = Button(frame, text="Click me!", command=self.pmsg)
        self.pbutton.pack()

        self.qbutton = Button(frame, text="Exit", command=frame.quit)
        self.qbutton.pack(side=LEFT)

    def pmsg(self):
        print("Clicked")


root = Tk()
obj = Myfun(root)
root.mainloop()
