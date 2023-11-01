# tkinter, based on any topic create labels and 3 buttons-clicked,cancel,quit

from tkinter import *


class Student:
    def __init__(self):
        self.l1 = Label(root, text="Name")
        entry1 = Entry(root)
        self.l1.grid(row=1, column=0)
        entry1.grid(row=1, column=1)

        self.l2 = Label(root, text="Rollno")
        entry2 = Entry(root)
        self.l2.grid(row=2, column=0)
        entry2.grid(row=2, column=1)

        self.l3 = Label(root, text="School")
        entry3 = Entry(root)
        self.l3.grid(row=3, column=0)
        entry3.grid(row=3, column=1)

        frame = Frame(root)
        frame.grid(row=4, columnspan=2)
        self.pbtn = Button(frame, text="Clicked",fg="blue",bg="white", command=self.msg)
        self.pbtn.grid(row=0, column=0,padx=5,pady=5)
        self.cbtn = Button(frame, text="Cancel",fg="red",bg="grey", command=self.cancelled)
        self.cbtn.grid(row=0, column=1,padx=5,pady=5)
        self.qbtn = Button(frame, text="Exit",fg="black",bg="red", command=root.quit)
        self.qbtn.grid(row=0, column=2,padx=5,pady=5)

    def msg(self):
        print("Clicked me!!!")

    def cancelled(self):
        print("Canceled me!!!")


root = Tk()
obj = Student()
root.mainloop()
