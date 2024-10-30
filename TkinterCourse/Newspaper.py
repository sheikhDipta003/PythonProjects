from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Game logic here
root.geometry("1500x750")

# headline
label = Label(text="THE DAILY ASTER", bg="red", fg="white", font="comicsansms 20 bold", borderwidth=3, relief=SUNKEN)
label.pack()
# Date
label = Label(text="12th February, 2021, Friday", fg="blue", font="comicsansms 10 italic")
label.pack()

articles = {1: {"img": "Text&Images/1.jpg", "text": "Text&Images/1.txt"},
            2: {"img": "Text&Images/2.jpg", "text": "Text&Images/2.txt"},
            3: {"img": "Text&Images/3.jpg", "text": "Text&Images/3.txt"},
            4: {"img": "Text&Images/4.jpg", "text": "Text&Images/4.txt"},
            5: {"img": "Text&Images/5.jpg", "text": "Text&Images/5.txt"}
            }

labels = {}

# ----->     Article 1     <-----
# image
image = Image.open(articles[1]["img"])
photo = ImageTk.PhotoImage(image)
label_img = Label(image=photo)
# text
f = open(articles[1]["text"], "rt")
content = f.read()
# print(content)
label_txt = Label(text=content)
labels[1] = {"iLab": label_img, "tLab": label_txt}

# print(type(labels))
labels[1]["iLab"].pack(side=TOP, anchor=N, padx=300)
labels[1]["tLab"].pack(side=LEFT, anchor=N, padx=5)

# ----->     Article 5     <-----
# image
image = Image.open(articles[5]["img"])
photo = ImageTk.PhotoImage(image)
label_img = Label(image=photo)
# text
f = open(articles[5]["text"], "rt")
content = f.read()
# print(content)
label_txt = Label(text=content)
labels[5] = {"iLab": label_img, "tLab": label_txt}

# print(labels)
labels[5]["iLab"].pack(anchor=N, side=LEFT, padx=300)
labels[5]["tLab"].pack(anchor=N, side=LEFT, padx=5)

# ----->     Article 2     <-----
# image
image = Image.open(articles[2]["img"])
photo = ImageTk.PhotoImage(image)
label_img = Label(image=photo)
# text
f = open(articles[2]["text"], "rt")
content = f.read()
# print(content)
label_txt = Label(text=content)
labels[2] = {"iLab": label_img, "tLab": label_txt}

# print(labels)
labels[2]["iLab"].pack(side=TOP, anchor=N, padx=300)
labels[2]["tLab"].pack(side=LEFT, anchor=N, padx=5)

# ----->     Article 4     <-----
# image
image = Image.open(articles[4]["img"])
photo = ImageTk.PhotoImage(image)
label_img = Label(image=photo)
# text
f = open(articles[4]["text"], "rt")
content = f.read()
# print(content)
label_txt = Label(text=content)
labels[4] = {"iLab": label_img, "tLab": label_txt}

# print(labels)
labels[4]["iLab"].pack(side=LEFT, padx=300)
labels[4]["tLab"].pack(side=LEFT, padx=5)

# ----->     Article 3     <-----
# image
image = Image.open(articles[3]["img"])
photo = ImageTk.PhotoImage(image)
label_img = Label(image=photo)
# text
f = open(articles[3]["text"], "rt")
content = f.read()
# print(content)
label_txt = Label(text=content)
labels[3] = {"iLab": label_img, "tLab": label_txt}

print(labels)
labels[3]["iLab"].pack(anchor=SW, side=BOTTOM, padx=300)
labels[3]["tLab"].pack(anchor=SW, side=BOTTOM, padx=5)

# root.minsize(400, 200)
# root.maxsize(1200, 700)

root.mainloop()
