from tkinter import *

root = Tk()
root.geometry("600x400+400+200")
root.title("Learning about Scrollbars")
# For connecting a widget to scrollbar
# step - 1: widget(yscrollcommand = scrollbar.set)
# step - 2: scrollbar.config(command = widget.yview)

# create scrollbar
myScroll = Scrollbar(root)
myScroll.pack(side="right", fill=Y)
# myScroll.place(x=300, y=100)

# creating a listbox
lbx = Listbox(root, yscrollcommand=myScroll.set)
for i in range(300):
    lbx.insert(END, f"Item No --> {i + 1}")

lbx.pack(fill="both")

# connect lbx widget to myScroll
myScroll.config(command=lbx.yview)

root.mainloop()
