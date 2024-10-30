from tkinter import *

result_txt = ""

root = Tk()

# variables
a_val = StringVar()
b_val = StringVar()

# GUI logic here
root.geometry("400x400+600+100")

# title
root.title("My Calculator")

# screen
screen_frame = Frame(root, bd=10, relief=GROOVE, bg="light green")
screen_frame.grid(row=0, columnspan=2)
# result frame
res_frame = Frame(root, bd=10, relief=GROOVE, bg="light green")
res_frame.grid(row=1, columnspan=2)


# function to display a label
def dis_lab():
    l = Label(res_frame, text=result_txt, font="timesnewroman 10 bold", bd=0, width=47)
    l.grid(row=0, column=0)


# methods for different buttons
def add():
    global result_txt
    res = int(a_val.get()) + int(b_val.get())
    # print("a_val = " + a_val.get())
    # print("b_val = " + b_val.get())
    # print("Result = " + str(res))
    result_txt = str(res)


def sub():
    global result_txt
    res = int(a_val.get()) - int(b_val.get())
    # print("a_val = " + a_val.get())
    # print("b_val = " + b_val.get())
    # print("Result = " + str(res))
    result_txt = str(res)


def mult():
    global result_txt
    res = int(a_val.get()) * int(b_val.get())
    # print("a_val = " + a_val.get())
    # print("b_val = " + b_val.get())
    # print("Result = " + str(res))
    result_txt = str(res)


def div():
    global result_txt
    if int(b_val.get()) != 0:
        res = int(a_val.get()) / int(b_val.get())
        # print("a_val = " + a_val.get())
        # print("b_val = " + b_val.get())
        # print("Result = " + str(res))
        result_txt = str(res)
    else:
        result_txt = "Can't divide by zero"


# input
a_entry = Entry(screen_frame, textvariable=a_val)
a_entry.grid(row=0, column=0, ipady=50, ipadx=33)
b_entry = Entry(screen_frame, textvariable=b_val)
b_entry.grid(row=0, column=1, ipady=50, ipadx=33)

if a_val.get() == "":
    result_txt = "0"

# buttons
plus = Button(root, text="+", bd=6, command=add, font="timesnewroman 20 bold")
plus.grid(row=2, column=0, ipadx=60)

minus = Button(root, text="-", bd=6, command=sub, font="timesnewroman 20 bold")
minus.grid(row=2, column=1, ipadx=60)

multiply = Button(root, text="x", bd=6, command=mult, font="timesnewroman 20 bold")
multiply.grid(row=3, column=0, ipadx=60)

divide = Button(root, text="/", bd=6, command=div, font="timesnewroman 20 bold")
divide.grid(row=3, column=1, ipadx=60)

equals = Button(root, text="=", bd=6, command=dis_lab, font="timesnewroman 20 bold")
equals.grid(row=4, columnspan=2, ipadx=120)

root.mainloop()

