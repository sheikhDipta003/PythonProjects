from tkinter import *
from PIL import Image, ImageTk
import os

root = Tk()
root.title(os.getcwd())
os.chdir("random_images/")
root.title(os.getcwd())

# GUI logic here

# width x height
root.geometry("1200x650")

for img_root, dirs, files in os.walk('/random_images'):
    for __file in files:
        if __file.endswith('.png') and os.path.exists(__file):
            label = Label(image=PhotoImage(file=str(__file)))
            label.pack()

"""# adding text
label = Label(text="Dipta is the dumbest boy in the world and this is his GUI !!")
label.pack()

# adding image to our GUI"""
# photo = PhotoImage(file="2.png")

""""# for jpg images
image = Image.open("bird.jpg")
photo = ImageTk.PhotoImage(image)"""

# label_img = Label(image=photo)
# label_img.pack()

# width, height
root.minsize(400, 100)  # lock the minimum size

# width, height
root.maxsize(1200, 988)  # lock the maximum size

root.mainloop()
