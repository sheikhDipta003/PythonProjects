from tkinter import *

root = Tk()

root.geometry("655x333")


def Hello():
    print("Hello tkinter buttons !!")


def Name():
    print("Name is Dipta")


frame = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor=N)

b1 = Button(frame, fg="red", text="Print Now", command=Hello)
b1.pack(side=LEFT, padx=23)

b2 = Button(frame, fg="red", text="Tell me name Now", command=Name)
b2.pack(side=LEFT, padx=23)

b3 = Button(frame, fg="red", text="Print Now")
b3.pack(side=LEFT, padx=23)

b4 = Button(frame, fg="red", text="Print Now")
b4.pack(side=LEFT, padx=23)

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")
print(x)

root.mainloop()
