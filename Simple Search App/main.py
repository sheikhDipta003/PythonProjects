from tkinter import *
import wikipedia
import tkinter.messagebox as tmsg


class SearchApp():
    def __init__(self, s_root):
        self.root = s_root
        self.root.title("Hello, there!")
        self.root.geometry("1200x600+200+100")
        self.root.config(bg="light green")
        self.search_word = StringVar()

        # set title
        Label(self.root, text="Simple Search App", font="calibri 40 bold", bg="black",
              fg="red").place(x=0, y=0, relwidth=1)

        # word to search
        Label(self.root, text="Enter word", font="calibri 30 bold", bg="light green",
              fg="blue").place(x=10, y=100)

        # entry widget for typing the keyword to be searched
        Entry(self.root, textvariable=self.search_word, font="lucida 20").place(x=250, y=110, width=300)

        # search button
        Button(self.root, text="Search", font="Verdana 20 bold", bg="orange", command=self.search,
               fg="black").place(x=570, y=108, width=150, height=40)

        # clear button
        Button(self.root, text="Clear", font="Verdana 20 bold", bg="orange", command=self.clear,
               fg="black").place(x=730, y=108, width=150, height=40)

        # enable write mode button
        Button(self.root, text="Enable\nWrite Mode", font="Verdana 10 bold", bg="orange",
               command=self.enable, fg="black").place(x=890, y=108, width=150, height=40)

        # disable write mode button
        Button(self.root, text="Disable\nWrite Mode", font="Verdana 10 bold", bg="orange",
               command=self.disable, fg="black").place(x=1050, y=108, width=150, height=40)

        # frame for text and scrollbar
        frame1 = Frame(self.root, bd=2, relief=RIDGE)
        frame1.place(x=10, y=190, width=1180, height=430)

        # scrollbar
        myScroll = Scrollbar(frame1)
        myScroll.pack(side="right", fill="y")

        # creating text-area
        self.txt_area = Text(frame1, font="times 15", yscrollcommand=myScroll.set)
        self.txt_area.pack(fill="both", expand=True)
        myScroll.config(command=self.txt_area.yview)

        # status bar
        self.stat_lbl = Label(self.root, font=("MS Serif", 15, "bold"), fg="dark blue", bg="light green")
        self.stat_lbl.place(x=10, y=160)

    def enable(self):
        self.txt_area.config(state=NORMAL)
        self.stat_lbl.config(text="MODE: ENABLED", fg="dark blue", bg="light green")

    def disable(self):
        self.txt_area.config(state=DISABLED)
        self.stat_lbl.config(text="MODE: DISABLED", fg="grey", bg="light green")

    # search
    def search(self):
        if self.search_word.get() == "":
            tmsg.showerror("Error!", "Search bar should not be empty!")
        else:
            content = wikipedia.summary(self.search_word.get())
            self.txt_area.insert('1.0', content)

    # clear
    def clear(self):
        self.search_word.set("")
        self.txt_area.delete('1.0', 'end')
        self.stat_lbl.config(text="")


root = Tk()
obj = SearchApp(root)
root.mainloop()
