import parser
from tkinter import *

root = Tk()
root.title("Calculator")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W + E)
button_width = 4
button_height = 2
button_padding = 3
i = 0

def get_variable(num):
    global i
    display.insert(i, num)
    i += 1

def clear_all():
    display.delete(0, END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0, new_string)
    else:
        display.insert(0, 'ERROR')

def operators(opr):
    global i
    length = len(opr)
    display.insert(i, opr)
    i += length

def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0, result)
    except Exception:
        clear_all()
        display.insert(0, "Error")


# Adding buttons
Button(root, text='exp', command=lambda: operators('**'), width=button_width, height=button_height, bg='grey').grid(row=2, column=0, padx=button_padding, pady=button_padding)
Button(root, text='π', command=lambda: operators('*3.14'),width=button_width,height=button_height,bg='grey').grid(row=2, column=1, padx=button_padding, pady=button_padding)
Button(root, text='x^2', command=lambda: operators('**2'),width=button_width,height=button_height,bg='grey').grid(row=2, column=2, padx=button_padding, pady=button_padding)
Button(root, text='<-', command=undo,width=button_width,height=button_height,bg='grey').grid(row=2, column=3, padx=button_padding, pady=button_padding)

Button(root, text='(', command=lambda: operators('('),width=button_width,height=button_height,bg='grey').grid(row=3, column=0, padx=button_padding, pady=button_padding)
Button(root, text=')', command=lambda: operators(')'),width=button_width,height=button_height,bg='grey').grid(row=3, column=1, padx=button_padding, pady=button_padding)
Button(root, text='%', command=lambda: operators('%'),width=button_width,height=button_height,bg='grey').grid(row=3, column=2, padx=button_padding, pady=button_padding)
Button(root, text='/', command=lambda: operators('/'),width=button_width,height=button_height,bg='grey').grid(row=3, column=3, padx=button_padding, pady=button_padding)

Button(root, text='7', command=lambda: get_variable(7),width=button_width,height=button_height,bg='grey').grid(row=4, column=0, padx=button_padding, pady=button_padding)
Button(root, text='8', command=lambda: get_variable(8),width=button_width,height=button_height,bg='grey').grid(row=4, column=1, padx=button_padding, pady=button_padding)
Button(root, text='9', command=lambda: get_variable(9),width=button_width,height=button_height,bg='grey').grid(row=4, column=2, padx=button_padding, pady=button_padding)
Button(root, text='*', command=lambda: operators('*'),width=button_width,height=button_height,bg='grey').grid(row=4, column=3, padx=button_padding, pady=button_padding)

Button(root, text='4', command=lambda: get_variable(4),width=button_width,height=button_height,bg='grey').grid(row=5, column=0, padx=button_padding, pady=button_padding)
Button(root, text='5', command=lambda: get_variable(5),width=button_width,height=button_height,bg='grey').grid(row=5, column=1, padx=button_padding, pady=button_padding)
Button(root, text='6', command=lambda: get_variable(6),width=button_width,height=button_height,bg='grey').grid(row=5, column=2, padx=button_padding, pady=button_padding)
Button(root, text='-', command=lambda: operators('-'),width=button_width,height=button_height,bg='grey').grid(row=5, column=3, padx=button_padding, pady=button_padding)

Button(root, text='1', command=lambda: get_variable(1),width=button_width,height=button_height,bg='grey').grid(row=6, column=0, padx=button_padding, pady=button_padding)
Button(root, text='2', command=lambda: get_variable(2),width=button_width,height=button_height,bg='grey').grid(row=6, column=1, padx=button_padding, pady=button_padding)
Button(root, text='3', command=lambda: get_variable(3),width=button_width,height=button_height,bg='grey').grid(row=6, column=2, padx=button_padding, pady=button_padding)
Button(root, text='+', command=lambda: operators('+'),width=button_width,height=button_height,bg='grey').grid(row=6, column=3, padx=button_padding, pady=button_padding)

Button(root, text='AC', command=clear_all,width=button_width,height=button_height,bg='orange').grid(row=7, column=0, padx=button_padding, pady=button_padding)
Button(root, text='0', command=lambda: get_variable(0),width=button_width,height=button_height,bg='grey').grid(row=7, column=1, padx=button_padding, pady=button_padding)
Button(root, text='.', command=lambda: operators('.'),width=button_width,height=button_height,bg='grey').grid(row=7, column=2, padx=button_padding, pady=button_padding)
Button(root, text='=', command=calculate,width=button_width,height=button_height,bg='grey').grid(row=7, column=3, padx=button_padding, pady=button_padding)

root.mainloop()
