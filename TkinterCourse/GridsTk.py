from tkinter import *


def getvals():
    print(user_value.get())
    print(pass_value.get())


root = Tk()
root.geometry("655x333")

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

# variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar
user_value = StringVar()
pass_value = StringVar()

user_entry = Entry(root, textvariable=user_value)
pass_entry = Entry(root, textvariable=pass_value)

user_entry.grid(row=0, column=1)
pass_entry.grid(row=1, column=1)

Button(text="Submit", command=getvals).grid()

root.mainloop()
