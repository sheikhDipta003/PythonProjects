from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x400+400+200")
root.title("Learning about Sliders")

# text
Label(root, text="Rate Us!", font="calibri 20 bold").place(x=245, y=60)

# horizontal slider
mysliderH = Scale(root, from_=0, to=10, bg="light green", fg="red", bd=4, orient="horizontal", label="HELLO, THERE!!",
                  highlightbackground="blue", cursor="arrow", tickinterval=1)
# mysliderH.set(200)
mysliderH.place(x=200, y=100, width=200)


def recordRating():
    rating = mysliderH.get()

    with open("Rating.txt", "at") as f:
        f.write(f"Our Rating is {rating}\n")
    f.close()

    tmsg.showinfo("Rate Us!", "Thanks for your feedback!")


# Button
Button(root, text="Send", font="century 10 bold", bg="red", command=recordRating).place(x=250, y=200, width=100)

root.mainloop()
