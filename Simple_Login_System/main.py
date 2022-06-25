from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk


class Login_System:
    def __init__(self, a_root):
        self.s_root = a_root
        self.s_root.title("Login System")
        self.s_root.geometry("1350x700+0+0")  # place top-left corner of tk window at (0, 0) position of pycharm window

        # variables to store username and password entered
        self.user_val = StringVar()
        self.pass_val = StringVar()

        # load images
        self.bg_icon = ImageTk.PhotoImage(file="images_lib/bg.jpg")
        self.user_icon = PhotoImage(file="images_lib/user.png")
        self.pass_icon = PhotoImage(file="images_lib/password.png")
        self.me_icon = PhotoImage(file="images_lib/me.png")

        # set title
        title = Label(self.s_root, text="LOGIN SYSTEM", font="timesnewroman 40 bold", borderwidth=10, relief=GROOVE,
                      fg="red", bg="yellow", width=100)
        title.pack()

        # pack bg image
        bg_lbl = Label(self.s_root, image=self.bg_icon)
        bg_lbl.pack(anchor=N, fill=Y)

        # frame
        login_frame = Frame(self.s_root, bg="white")
        login_frame.place(x=400, y=150)

        # my avatar
        me_lbl = Label(login_frame, image=self.me_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        # username
        user_lbl = Label(login_frame, text="Username", image=self.user_icon, compound=LEFT,
                         font="timesnewroman 20 bold", bg="white").grid(row=1, column=0, padx=20,pady=10)
        # input username
        user_entry = Entry(login_frame, bd=5, relief=GROOVE, font=("", 15), textvariable=self.user_val)
        user_entry.grid(row=1, column=1, padx=20)

        # password
        pass_lbl = Label(login_frame, text="Password", image=self.pass_icon, compound=LEFT,
                         font="timesnewroman 20 bold", bg="white").grid(row=2, column=0, padx=20, pady=10)
        # input password
        pass_entry = Entry(login_frame, bd=5, relief=GROOVE, font=("", 15), textvariable=self.pass_val)
        pass_entry.grid(row=2, column=1, padx=20)

        # create login button
        btn_login = Button(login_frame, text="Login", width=15, font="timesnewroman 14 bold", bg="yellow", fg="red",
                           command=self.login)
        btn_login.grid(row=3, column=1, pady=10)

    # function to be executed when login button would be pressed
    def login(self):
        if self.user_val.get() == "" or self.pass_val.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        elif self.user_val.get() == "Dipta" and self.pass_val.get() == "RH206003":
            messagebox.showinfo("Success", f"{self.user_val.get()}")
        else:
            messagebox.showerror("Error", "Invalid username or password!!")


root = Tk()
obj = Login_System(root)
root.mainloop()
