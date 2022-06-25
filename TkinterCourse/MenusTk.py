from tkinter import *


def myfunc():
    print("This has been executed")


root = Tk()
root.geometry("600x400+400+200")

# use these to create a non-dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

newmenu = Menu(root)

m1 = Menu(newmenu, tearoff=0)
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Exit", command=myfunc)
root.config(menu=newmenu)
newmenu.add_cascade(label="File", menu=m1)

root.mainloop()
