from tkinter import *


def random(event):
    print(f"You have clicked the button at {event.x}, {event.y}")


root = Tk()
root.title("Events in Tkinter")
root.geometry("644x344")

widget = Button(root, text="Click me please!!")
widget.pack()

widget.bind('<Button-1>', random)
widget.bind('<Double-1>', quit)

root.mainloop()
