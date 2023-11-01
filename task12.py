# tkinter 5 cascade and give them each 6 command and display the msg
from tkinter import *
root = Tk()

main_menu = Menu(root)
root.config(menu=main_menu)
submenu = Menu(main_menu)

def newproject():
    print("Create a new project")
def new():
    print("Select file type")
def scratch():
    print("Create a new scratch file")
def opn():
    print("Open the file")
def save():
    print("Save the file with a name")
def recent():
    print("Recent projects")
def undo():
    print("Undo project")
def cut():
    print("Cut the line")
def copy():
    print("Copied")
def paste():
    print("Pasted")
def delete():
    print("Delete the line")
def find():
    print("Find the line")
def tool():
    print("Tools")
def app():
    print("Appearance")
def quick():
    print("Quick")
def rfiles():
    print("Files")
def active():
    print("Active")
def reset():
    print("Reset")
def back():
    print("Back")
def classn():
    print("Class...")
def filen():
    print("File...")
def symbol():
    print("Symbol...")
def textn():
    print("Text...")
def filep():
    print("File path")
def gen():
    print("Generate")
def codecom():
    print("Code Completion")
def cleanup():
    print("Cleanup")
def acode():
    print("Analyze code")
def down():
    print("Move line down")



main_menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="NewProject",command=newproject)
submenu.add_command(label="New...",command=new)
submenu.add_separator()
submenu.add_command(label="New Scratch File",command=scratch)
submenu.add_command(label="Open",command=opn)
submenu.add_separator()
submenu.add_command(label="Save As",command=save)
submenu.add_command(label="Recent Projects",command=recent)

submenu2 = Menu(main_menu)
main_menu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="undo",command=undo)
submenu2.add_command(label="cut",command=cut)
submenu2.add_separator()
submenu2.add_command(label="copy",command=copy)
submenu2.add_command(label="paste",command=paste)
submenu2.add_separator()
submenu2.add_command(label="delete",command=delete)
submenu2.add_command(label="find",command=find)

submenu3 =Menu(main_menu)
main_menu.add_cascade(label="View",menu=submenu3)
submenu3.add_command(label="tool",command=tool)
submenu3.add_command(label="appearance",command=app)
submenu3.add_separator()
submenu3.add_command(label="quick",command=quick)
submenu3.add_command(label="recent projects",command=rfiles)
submenu3.add_separator()
submenu3.add_command(label="active editor",command=active)
submenu3.add_command(label="reset",command=reset)

submenu4 = Menu(main_menu)
main_menu.add_cascade(label="Navigate",menu=submenu4)
submenu4.add_command(label="back",command=back)
submenu4.add_command(label="class...",command=classn)
submenu4.add_separator()
submenu4.add_command(label="file...",command=filen)
submenu4.add_command(label="symbol...",command=symbol)
submenu4.add_separator()
submenu4.add_command(label="text...",command=textn)
submenu4.add_command(label="file path",command=filep)

submenu5 = Menu(main_menu)
main_menu.add_cascade(label="Code",menu=submenu5)
submenu5.add_command(label="generate",command=gen)
submenu5.add_command(label="Code completion",command=codecom)
submenu5.add_separator()
submenu5.add_command(label="Clean Up",command=cleanup)
submenu5.add_command(label="analyze code",command=acode)
submenu5.add_separator()
submenu5.add_command(label="move line down",command=down)
submenu5.add_command(label="Exit",command=submenu5.quit)

root.mainloop()






