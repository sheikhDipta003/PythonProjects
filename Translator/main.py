from tkinter import *
from googletrans import Translator

translator = Translator()

root = Tk()

entry1 = Entry(root, font=("Times New Roman", 30))
entry1.pack()


def translate():
    label1 = Label(root, text=translator.translate(entry1.get(), src='pt', dest='id'), font=("Times New Roman", 30))
    label1.pack()


button1 = Button(root, text='Translate', font=("Times New Roman", 30), command=translate)
button1.pack()

root.mainloop()
