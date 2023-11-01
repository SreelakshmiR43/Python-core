from tkinter import *
from tkinter import messagebox
root=Tk()

messagebox.showinfo('title',"showing information")
messagebox.showwarning('title',"showing warning message")
messagebox.showerror('title',"showing some error")
messagebox.askquestion('title',"Asking Questions")
messagebox.askyesno('title',"Asking Yes or No")
messagebox.askretrycancel('title',"Asking Retry or Cancel")
root.mainloop()