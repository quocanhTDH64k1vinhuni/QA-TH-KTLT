print("Nguyễn Quốc Anh")
print("MSV 235752021610084")
from tkinter import *
def NewFile():
 print("New File!")
def open_file():
    print("Open File!")
def insert_text():
    print("Insert Text!")

def insert_picture():
    print("Insert Picture!")


root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_separator()

filemenu.add_command(label="Open", command=open_file)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="Text", command=Text)

helpmenu.add_command(label="Picture", command=insert_picture)
mainloop()

