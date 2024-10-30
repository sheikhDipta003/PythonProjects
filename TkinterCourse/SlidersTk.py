from tkinter import *

root = Tk()
root.geometry("600x400+400+200")
root.title("Learning about Sliders")

# vertical slider
mysliderV = Scale(root, from_=0, to=400, bg="light green", fg="red", bd=4, orient="vertical", troughcolor="orange",
                  sliderlength=30, cursor="dot", tickinterval=100)
# mysliderV.set(100)
mysliderV.grid(row=0, column=0)

# horizontal slider
mysliderH = Scale(root, from_=0, to=400, bg="light green", fg="red", bd=4, orient="horizontal", label="HELLO, THERE!!",
                  highlightbackground="blue", cursor="arrow", tickinterval=200)
# mysliderH.set(200)
mysliderH.grid(row=1, column=1, pady=50, padx=100)

root.mainloop()
