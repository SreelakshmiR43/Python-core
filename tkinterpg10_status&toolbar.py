from tkinter import *
root = Tk()

def function():
    print("undo!!!!!")


mymenu = Menu(root)
root.config(menu=mymenu)
submenu = Menu(mymenu)

mymenu.add_cascade(label="File",menu=submenu)
submenu.add_command(label="save")

submenu.add_command(label="save1")
submenu.add_separator()
submenu.add_command(label="save2")
submenu.add_command(label="save3")

newmenu = Menu(mymenu)
mymenu.add_cascade(label="Edit",menu=newmenu)
newmenu.add_command(label="undo",command=function)

# Statu&toolbar
toolbar = Frame(root,bg='pink')
btn = Button(toolbar,text="crop")
btn.pack(side=LEFT,padx=5,pady=5)
toolbar.pack(side=TOP,fill=X)

statusbar = Label(root,text="This is a status bar",relief=SUNKEN,anchor=W,bd=1)
statusbar.pack(side=BOTTOM,fill=X)
root.mainloop()




