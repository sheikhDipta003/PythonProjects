from tkinter import *
from pygame import mixer

root = Tk()
root.geometry("600x300+200+100")
root.config(bg="light blue")
root.title("Alarm Clock")
st = StringVar()

mixer.init()
mixer.music.load('beep.ogg')
# mixer.music.play(-1)
# mixer.music.set_volume(1.0)

t = "Hello world! My name is Sheikh Intiser Uddin Dipta"
Label(root, text=t, bd=8, relief="sunken", fg="dark blue", bg="yellow",
      font=("Fixedsys", 15, "bold")).place(x=10, y=10, width=580)


def kill_alarm():
    root.destroy()


def save_snooze_time():
    print(st.get())


# slider
my_slider = Scale(root, from_=3, to=15, label="Set Snooze Time", bg="light green", fg="red", bd=6, variable=st,
                  orient="horizontal", tickinterval=2, length=400, highlightbackground="black").place(x=100, y=70)

# kill alarm button
Button(root, text="Kill Alarm", fg="black", bg="orange", bd=6, relief="raised", command=kill_alarm,
       font=("MS Sans Serif", 15, "bold")).place(x=10, y=200, width=120, height=50)

# snooze button
Button(root, text="Snooze", fg="black", bg="orange", bd=6, relief="raised", command=kill_alarm,
       font=("MS Sans Serif", 15, "bold")).place(x=500, y=200, width=90, height=50)

# set button
Button(root, text="Set", fg="black", bg="orange", bd=6, relief="raised", command=save_snooze_time,
       font=("MS Sans Serif", 15, "bold")).place(x=270, y=200, width=60, height=50)

root.mainloop()
