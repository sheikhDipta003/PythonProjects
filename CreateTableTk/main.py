from tkinter import *


class Table():
    def __init__(self, my_root):
        for i in range(6):
            for j in range(4):
                self.entry = Entry(my_root, fg="dark blue", bg="orange", bd=6, relief="groove",
                                   width=20, font=("arial", 10, "bold"))
                self.entry.grid(row=i, column=j)
                self.entry.insert(END, data[i][j])


data = [
    (1905001, "Sadat", "Dhaka", "20"),
    (1905002, "Nafis", "Dhaka", "19"),
    (1905003, "Dipta", "Ctg", "20"),
    (1905004, "Asif", "Dhaka", "19"),
    (1905005, "Ashraf", "Dhaka", "20"),
    (1905006, "Nabil", "Rajshahi", "20")
]

root = Tk()
root.geometry("600x450+200+100")
obj = Table(root)
root.mainloop()
