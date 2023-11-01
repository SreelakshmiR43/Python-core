from tkinter import *
root = Tk()

canvas = Canvas(root,width=400,height=400 ,bg='black')
canvas.pack()
line0 = canvas.create_line(0,0,400,400,fill='red')
line1 = canvas.create_line(0,400,400,0,fill='white')
line2 = canvas.create_line(200,0,200,400,fill='yellow')
line3 = canvas.create_line(0,200,400,200,fill='purple')





root.mainloop()