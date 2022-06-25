from tkinter import *
from PyDictionary import PyDictionary
import os

# create an object of PyDictionary() class
my_dict = PyDictionary()

root = Tk()
root.title("My Dictionary")
root.config(bg="light green")
root.geometry('1200x600+100+100')

# listbox to store previously typed words
lbx = Listbox(root, bd=5, bg="yellow", fg="dark blue", relief="sunken", font=("Veranda", 16), selectmode=SINGLE)
lbx.place(x=820, y=100, width=370, height=415)

if os.path.exists("search_history.txt"):
    with open("search_history.txt", "r") as f:
        lines = f.readlines()
        lines.reverse()

        for line in lines:
            line = line.strip()
            lbx.insert(0, line)
    f.close()


# delete listbox
def del_history():
    lbx_len = lbx.size()
    lbx.delete(0, lbx_len)
    os.remove("search_history.txt")


# delete a specific word
def del_word():
    lbx.delete(ACTIVE)


# delete history
Button(root, text="Delete\nHistory", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"),
       command=del_history, relief="raised").place(x=820, y=525, height=60)

# delete a specific word
Button(root, text="Delete", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"),
       command=del_word, relief="raised").place(x=960, y=525)

# global vars
pos = 0


# auto-select word from history
def select():
    global pos

    word_entry.delete(0, len(word.get()))
    pos = lbx.curselection()[0]
    word_entry.insert(0, lbx.get(pos))


# select button
Button(root, text="Select", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"), command=select,
       relief="raised").place(x=1100, y=525)


# search function
def search_word():
    # make a list from listbox; first search the listbox if there is any duplicate; delete if any
    for i in range(lbx.size()):
        if lbx.get(i) == word.get():
            lbx.delete(i)

    global pos

    searched_text.delete('1.0', "end")
    if lbx.get(pos) == word.get():
        lbx.delete(pos)
    lbx.insert(0, word.get())

    meaning = my_dict.meaning(word.get())
    # print("meaning:", meaning)
    list_keys = meaning.keys()

    # search if any keys match the menu currently selected
    match = False
    for key in list_keys:
        if key == clicked.get():
            match = True

    if not match:
        for key in list_keys:
            L = len(meaning[key])

            # display the key
            searched_text.insert(END, key + "\n")
            for i in range(L):
                searched_text.insert(END, f"({i + 1}) " + meaning[key][i].capitalize() + "\n")
            searched_text.insert(END, "\n")
    else:
        searched_text.delete('1.0', "end")
        searched_text.insert(END, clicked.get() + "\n")
        searched_text.update()

        L = len(meaning[clicked.get()])
        for i in range(L):
            searched_text.insert(END, f"({i + 1}) " + meaning[clicked.get()][i].capitalize() + "\n")
        searched_text.insert(END, "\n")


def find_syn():
    list_syn = my_dict.synonym(word.get())
    searched_text.insert(END, "Synonyms\n")
    # print(list_syn)

    for i in range(len(list_syn)):
        searched_text.insert(END, f"({i + 1}) " + list_syn[i] + "\n")


def find_ant():
    list_syn = my_dict.antonym(word.get())
    searched_text.insert(END, "\nAntonyms\n")
    # print(list_syn)

    for i in range(len(list_syn)):
        searched_text.insert(END, f"({i + 1}) " + list_syn[i] + "\n")


def exit_app():
    """with open("dummy_history.txt", "w") as f2:
        for i in range(lbx.size()):
            f2.write(lbx.get(i) + "\n")
    f2.close()"""

    # create list from data of search_history.txt file
    f3 = open("temp.txt", "a")
    f4 = open("search_history.txt", "w")

    if os.path.getsize("temp.txt") != 0:
        lines_3 = f3.readlines()

        for j in range(len(lines_3)):  # strip newlines
            lines_3[j] = lines_3[j].strip()

        # list from the current listbox
        lines_4 = []
        for i in range(lbx.size()):
            lines_4[i] = lbx.get(i)

        # insert those words from lines_4[] which are not duplicate in lines3[]
        for i in range(len(lines_4)):
            if len(lines_3) != 0:
                if lines_3.count(lines_4[i]) == 0:
                    f3.write(lines_4[i] + "\n")
                else:
                    f4.write(lines_4[i] + "\n")
            else:
                f4.write(lines_4[i] + "\n")

        # list of words from temp.txt file
        lines_5 = f4.readlines()
        for j in range(len(lines_5)):  # strip newlines
            lines_5[j] = lines_5[j].strip()

        for i in range(len(lines_3)):
            if lines_5.count(lines_3[i]) == 0:
                f4.write(lines_3[i] + "\n")
    else:
        for i in range(lbx.size()):
            f4.write(lbx.get(i) + "\n")

    f3.close()
    f4.close()
    exit()


# Enter the word
Label(root, text="Enter the word", fg="black", bg="light green", font=("MS Sans Serif", 20, "bold")).place(x=20, y=20)

word = StringVar()
word_entry = Entry(root, textvariable=word, font=("Helvetica", 20))
word_entry.place(x=230, y=15, height=50)


# clear entry widget
def del_word2(event):
    word_entry.delete(0, len(word.get()))


# binding word_entry widget to 'Delete' key
word_entry.bind('<Delete>', del_word2)

Button(root, text="Search", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"), command=search_word,
       relief="raised").place(x=550, y=18)

# synonyms
Button(root, text="Synonym", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"), command=find_syn,
       relief="raised").place(x=650, y=18)

# antonyms
Button(root, text="Antonym", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"), command=find_ant,
       relief="raised").place(x=760, y=18)

# exit
Button(root, text="Exit", bd=5, bg="orange", fg="black", font=("Fixedsys", 15, "bold"), command=exit_app,
       relief="raised").place(x=870, y=18)


# Select parts of speech
parts_of_speech = ["All", "Noun", "Pronoun", "Verb", "Adverb", "Adjective", "Preposition", "Conjunction",
                   "Interjection"]
clicked = StringVar()
clicked.set("All")
drop = OptionMenu(root, clicked, *parts_of_speech)
drop.place(x=10, y=70)

# text where the results of the search will be written
searched_text = Text(root, bd=4, bg="white", fg="black", font=("Helvetica", 16), wrap=WORD)
searched_text.place(x=10, y=100, width=800, height=490)

root.mainloop()
