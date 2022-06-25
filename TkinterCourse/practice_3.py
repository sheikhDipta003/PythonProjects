from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title(os.getcwd())

# GUI logic here

# width x height
root.geometry("500x400")

label = Label(width=100, text="READY!!", bg="yellow", fg="red", font="comicsansms 16 bold", borderwidth=4, relief=SUNKEN)
label.pack(anchor="sw", side=BOTTOM, fill=Y)

# width, height
root.minsize(400, 100)  # lock the minimum size

# width, height
root.maxsize(1200, 988)  # lock the maximum size

root.mainloop()
