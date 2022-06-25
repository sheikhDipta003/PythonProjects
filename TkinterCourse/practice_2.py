from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title(os.getcwd())

# GUI logic here

# width x height
root.geometry("1200x650")

# important Label options
# text = adds the text
"""bd = background
fg = foreground
font = sets the font
--> font=("comicsansms", 9, "bold")
--> font="comicsansms 9 bold"
padx = x-padding
paddy = y-padding
relief = border styling --> SUNKEN, RAISED, GROOVE, RIDGE"""

title_label = Label(text='''ADVANTAGES OF RECURSION:
\n1. A complex problem seems logically convincible when we solve it using recursion.
\n2. Recursion uses fairly lesser programming constructs to solve the problem than its iterative counterpart.
\nDISADVANTAGES OF RECURSION:
\n1. Fairly slower than its iterative solution.
\n2. For each step we make a recursive call to a function. For which it occupies significant amount of stack memory.
\n3. May cause stack-overflow if the recursion goes too deep to solve the problem.
\n4. Difficult to debug and trace the values with each step of recursion.
\nPS: I used the term step for each recursive calls(recursion depth) to make it sound familiar.''', bg="red", fg="white"
                    , padx=20, pady=20, font="comicsansms 9 bold", borderwidth=3, relief=SUNKEN)

# important pack options
# anchor = nw, ne, sw, se
# side = top, bottom, left, right
# fill
# padx
# pady

title_label.pack(side=RIGHT, fill=Y)

# width, height
root.minsize(400, 100)  # lock the minimum size

# width, height
root.maxsize(1200, 988)  # lock the maximum size

root.mainloop()
