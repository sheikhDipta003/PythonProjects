from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x400+400+200")
root.title("My Second Calculator")
root.config(bg="dark grey")
root.maxsize(width=600, height=400)
root.minsize(width=600, height=400)

# global variables
txt = ""
answer = 0


# functions corresponding to buttons
def zero():
    global txt
    txt = txt + "0"
    display.config(text=txt)


def one():
    global txt
    txt = txt + "1"
    display.config(text=txt)


def two():
    global txt
    txt = txt + "2"
    display.config(text=txt)


def three():
    global txt
    txt = txt + "3"
    display.config(text=txt)


def four():
    global txt
    txt = txt + "4"
    display.config(text=txt)


def five():
    global txt
    txt = txt + "5"
    display.config(text=txt)


def six():
    global txt
    txt = txt + "6"
    display.config(text=txt)


def seven():
    global txt
    txt = txt + "7"
    display.config(text=txt)


def eight():
    global txt
    txt = txt + "8"
    display.config(text=txt)


def nine():
    global txt
    txt = txt + "9"
    display.config(text=txt)


def plus():
    global txt
    txt = txt + "+"
    display.config(text=txt)


def minus():
    global txt
    txt = txt + "-"
    display.config(text=txt)


def multiply():
    global txt
    txt = txt + "x"
    display.config(text=txt)


def div():
    global txt
    txt = txt + "/"
    display.config(text=txt)


def mod():
    global txt
    txt = txt + "%"
    display.config(text=txt)


def dot():
    global txt
    txt = txt + "."
    display.config(text=txt)


def equals():
    global txt
    global answer

    operands = []
    operators_pos = [txt.find("+"), txt.find("-"), txt.find("x"), txt.find("/"), txt.find("%")]

    if operators_pos.count(-1) != 4:
        if operators_pos.count(-1) < 4:
            tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
        elif operators_pos.count(-1) > 4:
            txt = ""
    else:
        if txt.find("+") != -1:
            if txt.find("+") != txt.rfind("+"):
                tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
            else:
                if txt[0] == '+':
                    tmsg.showerror("Syntax Error!", "Left operand required!")
                elif txt[len(txt) - 1] == '+':
                    tmsg.showerror("Syntax Error!", "Right operand required!")
                else:
                    operands = txt.split("+")

                    if operands[0].find(".") == -1 and operands[1].find(".") == -1:
                        result = int(operands[0]) + int(operands[1])
                    else:
                        result = float(operands[0]) + float(operands[1])

                    display.config(text=str(result))
                    answer = result
        elif txt.find("-") != -1:
            if txt.find("-") != txt.rfind("-"):
                tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
            else:
                if txt[0] == '-':
                    tmsg.showerror("Syntax Error!", "Left operand required!")
                elif txt[len(txt) - 1] == '-':
                    tmsg.showerror("Syntax Error!", "Right operand required!")
                else:
                    operands = txt.split("-")

                    if operands[0].find(".") == -1 and operands[1].find(".") == -1:
                        result = int(operands[0]) - int(operands[1])
                    else:
                        result = float(operands[0]) - float(operands[1])

                    display.config(text=str(result))
                    answer = result
        elif txt.find("x") != -1:
            if txt.find("x") != txt.rfind("x"):
                tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
            else:
                if txt[0] == 'x':
                    tmsg.showerror("Syntax Error!", "Left operand required!")
                elif txt[len(txt) - 1] == 'x':
                    tmsg.showerror("Syntax Error!", "Right operand required!")
                else:
                    operands = txt.split("x")

                    if operands[0].find(".") == -1 and operands[1].find(".") == -1:
                        result = int(operands[0]) * int(operands[1])
                    else:
                        result = float(operands[0]) * float(operands[1])

                    display.config(text=str(result))
                    answer = result
        elif txt.find("/") != -1:
            if txt.find("/") != txt.rfind("/"):
                tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
            else:
                if txt[0] == '/':
                    tmsg.showerror("Syntax Error!", "Left operand required!")
                elif txt[len(txt) - 1] == '/':
                    tmsg.showerror("Syntax Error!", "Right operand required!")
                else:
                    operands = txt.split("/")

                    if float(operands[1]) == 0.0:
                        # result = "Cannot divide by zero!"
                        tmsg.showerror("Math Error!", "Cannot divide by zero!")
                    else:
                        if operands[0].find(".") == -1 and operands[1].find(".") == -1:
                            result = int(operands[0]) / int(operands[1])
                        else:
                            result = float(operands[0]) / float(operands[1])

                        display.config(text=str(result))
                        answer = result
        elif txt.find("%") != -1:
            if txt.find("%") != txt.rfind("%"):
                tmsg.showerror("Cannot solve!", "Multiple operators not allowed!")
            else:
                if txt[0] == '%':
                    tmsg.showerror("Syntax Error!", "Left operand required!")
                elif txt[len(txt) - 1] == '%':
                    tmsg.showerror("Syntax Error!", "Right operand required!")
                else:
                    operands = txt.split("%")

                    if operands[0].find(".") == -1 and operands[1].find(".") == -1:
                        result = int(operands[0]) % int(operands[1])

                        display.config(text=str(result))
                        answer = result
                    else:
                        # result = "Cannot take mod of fractions"
                        tmsg.showerror("Math Error!", "Cannot take mod of fraction!")

    # print(operands)
    txt = ""


def clear():
    global txt
    txt = ""
    display.config(text=txt)


def ans():
    global txt
    global answer
    txt += str(answer)
    display.config(text=txt)


def delete():
    global txt
    txt = txt[0:len(txt) - 1]
    display.config(text=txt)


# display
display = Label(root, bd=5, relief="groove", fg="dark blue", bg="yellow",
                font="calibri 20")
display.place(x=0, y=0, width=600, height=50)

# Number pad
# 1, 2, 3
Button(root, bd=5, bg="orange", fg="black", text="1", relief="raised", command=one,
       font="veranda 20").place(x=20, y=70, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="2", relief="raised", command=two,
       font="veranda 20").place(x=130, y=70, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="3", relief="raised", command=three,
       font="veranda 20").place(x=240, y=70, width=100, height=60)

# 4, 5, 6
Button(root, bd=5, bg="orange", fg="black", text="4", relief="raised", command=four,
       font="veranda 20").place(x=20, y=140, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="5", relief="raised", command=five,
       font="veranda 20").place(x=130, y=140, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="6", relief="raised", command=six,
       font="veranda 20").place(x=240, y=140, width=100, height=60)

# 7, 8, 9
Button(root, bd=5, bg="orange", fg="black", text="7", relief="raised", command=seven,
       font="veranda 20").place(x=20, y=210, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="8", relief="raised", command=eight,
       font="veranda 20").place(x=130, y=210, width=100, height=60)
Button(root, bd=5, bg="orange", fg="black", text="9", relief="raised", command=nine,
       font="veranda 20").place(x=240, y=210, width=100, height=60)

# 0, dot(.), clear
Button(root, bd=5, bg="orange", fg="black", text="0", relief="raised", command=zero,
       font="veranda 20").place(x=20, y=280, width=100, height=60)
Button(root, bd=5, bg="gold", fg="black", text=".", relief="raised", command=dot,
       font="veranda 20").place(x=130, y=280, width=100, height=60)
Button(root, bd=5, bg="#22ef12", fg="black", text="Clear", relief="raised", command=clear,
       font="veranda 20").place(x=240, y=280, width=100, height=60)

# arithmetic operators
Button(root, bd=5, bg="magenta", fg="black", text="+", relief="raised", command=plus,
       font="veranda 20").place(x=370, y=70, width=100, height=60)
Button(root, bd=5, bg="magenta", fg="black", text="-", relief="raised", command=minus,
       font="veranda 20").place(x=370, y=140, width=100, height=60)
Button(root, bd=5, bg="magenta", fg="black", text="x", relief="raised", command=multiply,
       font="veranda 20").place(x=370, y=210, width=100, height=60)
Button(root, bd=5, bg="magenta", fg="black", text="/", relief="raised", command=div,
       font="veranda 20").place(x=370, y=280, width=100, height=60)
Button(root, bd=5, bg="magenta", fg="black", text="%", relief="raised", command=mod,
       font="veranda 20").place(x=480, y=70, width=100, height=60)
Button(root, bd=5, bg="silver", fg="black", text="=", relief="raised", command=equals,
       font="veranda 20").place(x=480, y=140, width=100, height=60)

# answer button
Button(root, bd=5, bg="blue", fg="black", text="Ans", relief="raised", command=ans,
       font="veranda 20").place(x=480, y=210, width=100, height=60)

# delete button
Button(root, bd=5, bg="red", fg="black", text="Del", relief="raised", command=delete,
       font="veranda 20").place(x=480, y=280, width=100, height=60)

root.mainloop()
