from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=8, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

L = Label(f1, text="Project Tkinter - PyCharm")
L.pack(pady=142)

L = Label(f2, text="Welcome to Sublime text")
L.pack()

root.mainloop()
