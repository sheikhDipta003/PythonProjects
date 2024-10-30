from tkinter import *
from PIL import Image, ImageTk


def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i != 0 and not (i % 100):
            final_text += "\n"
    return final_text


root = Tk()
root.title("My Newspaper")

root.geometry("1000x600")

f = open("C:\\Users\\HP\\PycharmProjects\\To_Do App\\tasks.txt", "r")
print(f.read())

texts = []
photos = []
for i in range(0, 3):
    with open(f"Text&Images/{i + 1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"Text&Images/{i + 1}.jpg")

    # TODO: Resize these images
    image = image.resize((150, 150), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=50)
Label(f0, text="The Daily IntiLab", font="lucida 23 bold").pack()

Label(f0, text="13th February, 2021, Saturday", font="lucida 10 italic").pack()
f0.pack()

# News --> 1
f1 = Frame(root, width=900, height=200)
Label(f1, text=texts[0], padx=20, pady=20).pack(side="left")
Label(f1, image=photos[0], anchor="e").pack(padx=80, pady=40)
f1.pack(anchor="w")

# News --> 2
f2 = Frame(root, width=900, height=200)
Label(f2, text=texts[1], padx=20, pady=20).pack(side="right")
Label(f2, image=photos[1], anchor="e").pack(padx=80, pady=40)
f2.pack(anchor="w")

# News --> 3
f3 = Frame(root, width=900, height=200)
Label(f3, text=texts[2], padx=20, pady=20).pack(side="left")
Label(f3, image=photos[2], anchor="e").pack(padx=80, pady=40)
f3.pack(anchor="w")

root.mainloop()
