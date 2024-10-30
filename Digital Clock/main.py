# A reminder app: shows a digital clock and rings an alarm at the times of the tasks in tasks.txt

from tkinter import *
import time
from pygame import mixer

tasks_file_path = "tasks.txt"

root = Tk()

# Global vars
alarms = []
labels = []
count = 0

# title
root.title("DIGITAL CLOCK")

# window set-up
root.geometry("800x600+250+50")
root.config(bg="light green")

# alarm tone
mixer.init()
mixer.music.load('beep.ogg')


# alarm
def raise_alarm(hour, min, sec, noon):
    global alarms
    global labels
    i = 0

    if count == 0:
        f = open(tasks_file_path, "r")
        lines = f.readlines()
        # print(lines)
        for line in lines:
            lines[i] = line.strip()
            i += 1
        # print(lines)

        for line in lines:
            temp = line.split("-")
            # print(temp)
            a = temp[1].split(":")
            # print(a)
            alarms.append(a)
            labels.append(temp[0])
        # print(alarms)
        # print(len(alarms))
        # print(labels)
        # print(alarms[0][1])

    for row in range(len(alarms)):
        if hour == int(alarms[row][0]) and min == int(alarms[row][1]) and noon == alarms[row][2]:
            if sec == 0:
                show_alarm(row)
            # mixer.music.play(-1)
            # mixer.music.set_volume(1.0)

        # print("min = ", min, "; alarms[0][1] = ", alarms[row][1])
        if hour == int(alarms[row][0]) and min > int(alarms[row][1]) and noon == alarms[row][2]:
            # print("stopped")
            mixer.music.stop()


def show_alarm(alarm_no):
    mixer.music.play(-1)
    mixer.music.set_volume(1.0)

    global alarms

    w_root = Toplevel(root)
    w_root.geometry("600x300+200+100")
    w_root.config(bg="light blue")
    w_root.title("Alarm Clock")
    st = StringVar()

    t = labels[alarm_no]
    Label(w_root, text=t, bd=8, relief="sunken", fg="dark blue", bg="yellow",
          font=("Fixedsys", 15, "bold")).place(x=10, y=10, width=580)

    def kill_alarm():
        w_root.destroy()
        mixer.music.stop()

    def save_snooze_time():
        f1 = open("snooze.txt", "w")
        f1.write(st.get())
        f1.close()

    def snooze():
        f1 = open("snooze.txt", "r")
        temp1 = int(alarms[alarm_no][1]) + int(f1.read().strip())
        f1.close()

        if temp1 >= 60:
            temp1 %= 60
            temp2 = int(alarms[alarm_no][0]) + 1
            alarms[alarm_no][0] = str(temp2)

        alarms[alarm_no][1] = str(temp1)

        # print(alarms)

        kill_alarm()

    # slider
    Scale(w_root, from_=3, to=15, label="Set Snooze Time", bg="light green", fg="red", bd=6, variable=st,
          orient="horizontal", tickinterval=2, length=400, highlightbackground="black").place(x=100, y=70)

    # kill alarm button
    Button(w_root, text="Kill Alarm", fg="black", bg="orange", bd=6, relief="raised", command=kill_alarm,
           font=("MS Sans Serif", 15, "bold")).place(x=10, y=200, width=120, height=50)

    # snooze button
    Button(w_root, text="Snooze", fg="black", bg="orange", bd=6, relief="raised", command=snooze,
           font=("MS Sans Serif", 15, "bold")).place(x=500, y=200, width=90, height=50)

    # set button
    Button(w_root, text="Set", fg="black", bg="orange", bd=6, relief="raised", command=save_snooze_time,
           font=("MS Sans Serif", 15, "bold")).place(x=270, y=200, width=60, height=50)


# function to update time
def clock():
    global count

    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    # print(h, m, s)

    # check if am or pm
    if int(h) >= 12:
        if int(h) == 12:
            h = 12
        else:
            h = str(int(h) % 12)
        lbl_ap.config(text="PM")
        raise_alarm(int(h), int(m), int(s), "pm")
    else:
        lbl_ap.config(text="AM")
        raise_alarm(int(h), int(m), int(s), "am")

    lbl_hr.config(text=h)
    lbl_min.config(text=m)
    lbl_sec.config(text=s)

    # keep running the clock in background without disturbing current program
    lbl_hr.after(1000, clock)
    count += 1


# --->  time labels (numeric)   <---
# hours
lbl_hr = Label(root, text="12", font=("comicsansms", "50", "bold"), bg="orange", fg="blue")
lbl_hr.place(x=50, y=200, width=150, height=150)

# minutes
lbl_min = Label(root, text="00", font=("comicsansms", "50", "bold"), bg="orange", fg="blue")
lbl_min.place(x=210, y=200, width=150, height=150)

# seconds
lbl_sec = Label(root, text="00", font=("comicsansms", "50", "bold"), bg="orange", fg="blue")
lbl_sec.place(x=370, y=200, width=150, height=150)

# am/pm
lbl_ap = Label(root, text="AM", font=("comicsansms", "50", "bold"), bg="orange", fg="blue")
lbl_ap.place(x=530, y=200, width=150, height=150)

# --->  time labels (headlines)   <---
# hours
txt_hr = Label(root, text="HOUR", font=("comicsansms", "40", "bold"), bg="light green", fg="black")
txt_hr.place(x=50, y=360, width=150, height=50)

# minutes
txt_min = Label(root, text="MIN", font=("comicsansms", "40", "bold"), bg="light green", fg="black")
txt_min.place(x=210, y=360, width=150, height=50)

# seconds
txt_sec = Label(root, text="SEC", font=("comicsansms", "40", "bold"), bg="light green", fg="black")
txt_sec.place(x=370, y=360, width=150, height=50)

# am/pm
txt_ap = Label(root, text="NOON", font=("comicsansms", "40", "bold"), bg="light green", fg="black")
txt_ap.place(x=530, y=360, width=150, height=50)

clock()

root.mainloop()
