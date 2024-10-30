from tkinter import *


def add():
    global i    # by default, we can only USE global var, not MODIFY them; hence, "global" keyword necessary
    lbx.insert(0, f"Item No --> {i + 1}")
    i += 1


root = Tk()
root.geometry("600x400+400+200")
root.title("Learning about Listbox")

# empty listbox
lbx = Listbox(root)
lbx.pack()

# inserting values in that listbox
i = 0
Button(root, text="Add Item", command=add).pack()

if lbx.size() > 10:
    print("asm: ", lbx.get(3, 6))

root.mainloop()
