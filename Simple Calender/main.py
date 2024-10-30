from tkinter import *
import calendar

root = Tk()
root.geometry("600x400+400+200")
root.title("Creating my first calender GUI")
root.config(bg="yellow")

Label(root, text="Calender", bg="dark grey", fg="dark blue",
      font="calibri 40 bold").place(x=0, y=0, width=600, height=50)

# entry widget for receiving year input by the user
Label(root, text="Enter a year", bg="yellow", fg="black",
      font="calibri 20 bold").place(x=140, y=90, width=150, height=50)

year_value = StringVar()
Entry(root, textvariable=year_value, font="veranda 20").place(x=300, y=90, width=150, height=50)


# go to calender button
def calender():
    new_window = Toplevel(root)
    new_window.geometry("1200x700+100+50")
    new_window.title = "My Calender"
    new_window.config(bg="gold")

    # welcome text
    Label(new_window, text="Welcome to " + year_value.get(), fg="red", bg="gold",
          font=("MS Sans Serif", 40, "bold")).place(x=400, y=20)

    # place all 12 months of the year "year_value"
    # January, February, March, April
    Label(new_window, text=calendar.month(int(year_value.get()), 1), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=10, y=50 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 2), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=300, y=50 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 3), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=590, y=50 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 4), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=880, y=50 + 60, width=280, height=165)

    # May, June, July, August
    Label(new_window, text=calendar.month(int(year_value.get()), 5), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=10, y=225 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 6), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=300, y=225 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 7), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=590, y=225 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 8), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=880, y=225 + 60, width=280, height=165)

    # September, October, November, December
    Label(new_window, text=calendar.month(int(year_value.get()), 9), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=10, y=400 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 10), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=300, y=400 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 11), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=590, y=400 + 60, width=280, height=165)
    Label(new_window, text=calendar.month(int(year_value.get()), 12), fg="dark blue", font="veranda 10 bold",
          bd=6, relief="raised", bg="silver").place(x=880, y=400 + 60, width=280, height=165)


Button(root, text="Go to calender", bg="orange", fg="black", font="veranda 20 bold", command=calender,
       relief="raised").place(x=170, y=200, width=250, height=50)


# exit button
def Exit():
    quit(1)


Button(root, text="Exit", bg="orange", fg="black", font="veranda 20 bold", command=Exit,
       relief="raised").place(x=250, y=270, width=80, height=50)

root.mainloop()

