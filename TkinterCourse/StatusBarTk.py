from tkinter import *
import time


def state():
    statusvar.set("Busy...")
    stat_lbl.update()   # must be updated, otherwise the upper statement will not be executed

    time.sleep(2)
    statusvar.set("Ready!")


root = Tk()
root.geometry("600x400+400+200")
root.title("Learning about Status bars")

statusvar = StringVar()
statusvar.set("What???!")
# print(statusvar.get())

stat_lbl = Label(root, textvariable=statusvar, relief="sunken", anchor="w")
stat_lbl.pack(side="bottom", fill="x")

Button(root, text="Upload", command=state).pack()

root.mainloop()
