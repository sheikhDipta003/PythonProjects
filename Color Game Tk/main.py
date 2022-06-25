from tkinter import *
import tkinter.messagebox as tmsg
import random
import time

Rem_time = 30
tests = 0

root = Tk()
root.geometry("600x400+400+200")
root.title("My Color Game")
root.config(bg="light blue")

# start_time = int(time.strftime("%S"))     --> First attempt
start_time = int(time.time())


# print("start_time = " + str(start_time))


def help_user():
    # print("This has been executed")
    help_page = Toplevel(root)
    help_page.geometry("1025x325+200+50")
    help_page.title("Help")
    help_page.config(bg="light green")

    # lock the geometry
    help_page.maxsize(width=1025, height=325)
    help_page.minsize(width=1025, height=325)

    # rules Menu
    Label(help_page, text="RULES", fg="dark blue", bg="light green",
          font="System 30 bold").place(x=460, y=10)

    rules = "1. This is a simple color game where you have to write the correct name\nof the color of the text" \
            " appearing on the screen.\n" \
            "2. The names of the colors are: Red, Green, Blue, Orange, Yellow, Purple, Pink, Black, Brown & White.\n" \
            "3. Keep in mind, the particular color implied by the text\nneed not match with the color of the text.\n" \
            "4. The name of the colors must be written exactly as mentioned in rule no. 2;\nThat is, the name of the" \
            " colors must start with a capital letter.\nOtherwise, the answer will be considered incorrect.\n" \
            "5. The duration of the game is 30 seconds.\n" \
            "6. For each correct answer, the player will get +10\n" \
            "7. For each wrong answer, the player will get -6\n" \
            "8. The goal is to give as many correct answers as possible within the 30 seconds."
    Label(help_page, text=rules, fg="black", bg="light green",
          font="Fixedsys 15").place(x=0, y=60)


def about_info():
    about_page = Toplevel(root)
    about_page.geometry("590x150+400+15")
    about_page.title("About Us")
    about_page.config(bg="light green")

    # lock the geometry
    about_page.maxsize(width=590, height=150)
    about_page.minsize(width=590, height=150)

    name_game = "Name of the game: Color Game"
    maker = "Created by: Sheikh Intiser Uddin Dipta, BUET-CSE, 1-1"
    date_time = "Date-time of creation: February 19, 2021; Friday; 11:00 am"
    lang = "Used language: python(tkinter)"

    Label(about_page, text=name_game, fg="black", bg="light green", font="Fixedsys 15").grid(row=0, column=0)
    Label(about_page, text=maker, fg="black", bg="light green", font="Fixedsys 15").grid(row=1, column=0)
    Label(about_page, text=date_time, fg="black", bg="light green", font="Fixedsys 15").grid(row=2, column=0)
    Label(about_page, text=lang, fg="black", bg="light green", font="Fixedsys 15").grid(row=3, column=0)


def show_credits():
    credits_page = Toplevel(root)
    credits_page.geometry("430x100+1010+350")
    credits_page.title("Credits")
    credits_page.config(bg="light green")

    credit = "1. Learning: Code With Harry (YouTube channel)\n" \
             "2. Idea: GeeksForGeeks (Website)\n" \
             "3. Motivation: Time pass during vacation!\n" \
             "4. Images: None\n"

    Label(credits_page, text=credit, fg="black", bg="light green", font=("MS Serif", 15)).grid(row=0, column=0)


def save():
    save_page = Toplevel(root)
    save_page.geometry("350x100+40+350")
    save_page.title("Save")
    save_page.config(bg="light green")

    Label(save_page, text="Name:", font=("Fixedsys", 30), fg="black", bg="light green").grid(row=0, column=0)
    player_name = StringVar()
    player_entry = Entry(save_page, textvariable=player_name, font="30")
    player_entry.grid(row=0, column=1, ipady=10)

    # send button
    # Button(save_page, text="Send", fg="black", bg="orange", command=save_to_disk(player_name)).grid(row=1, column=0)
    # print("Player_name.get() = ", player_name.get())

    player_data = f"{player_name.get()}, {score}, {tests}\n"

    with open("records_color_game.txt", "a") as f:
        f.write(player_data)

    f.close()


# Menu
my_menu = Menu(root)
my_menu.add_command(label="Help", command=help_user)
my_menu.add_command(label="About", command=about_info)
my_menu.add_command(label="Credits", command=show_credits)
my_menu.add_command(label="Save", command=save)
my_menu.add_command(label="Exit", command=quit)
root.config(menu=my_menu)


# timing
def clock():
    # curr_time = int(time.strftime("%S"))  --> First attempt
    curr_time = int(time.time())

    # if curr_time == 0:                        --> First attempt
    # curr_time = int(time.strftime("%S")) + 60

    show_time = 30 - (curr_time - start_time)
    if show_time < 0:
        game_over()

    # print("show_time = " + str(show_time))
    # print("curr_time = " + str(curr_time))
    countdown.config(text="Remaining: " + str(show_time) + "s")
    countdown.after(200, clock)


# score
score = 0
show_score = Label(root, text="Score: " + str(score), font="Helvetica 20", bg="light blue", fg="Purple")
show_score.place(x=240, y=150)

colors = ["Red", "Green", "Blue", "Orange", "Yellow", "Purple", "Pink", "Black", "Brown", "White"]

# headline
Label(root, text="Type in the correct name of the color of the text,\ndon't be fooled!!", fg="dark blue", bd=4,
      bg="grey", relief="raised", font="calibri 20 bold").place(x=10, y=10, width=580, height=80)

# main text
key = colors[random.randint(0, 9)]
appearance = colors[random.randint(0, 9)]
txt = Label(root, text=key, fg=appearance, bg="light blue", font="calibri 30 bold")
txt.place(x=215, y=225, width=150, height=80)

# user entry
user_value = StringVar()
user_entry = Entry(root, textvariable=user_value, font="calibri 15", bg="gold", bd=5, relief="groove")
user_entry.place(x=220, y=300, width=150, height=50)


# print("User_value.get() = ", user_value.get())


# event handling
def enter(event):
    global key
    global appearance
    global user_value
    global score
    global tests

    # print("key = ", key)
    # print("appearance = ", appearance)

    if user_value.get() == appearance:
        score += 10
    else:
        score -= 6

    tests += 1

    show_score.config(text="Score: " + str(score))

    key = colors[random.randint(0, 9)]
    appearance = colors[random.randint(0, 9)]
    txt.config(text=key, fg=appearance)
    user_value.set("")

    # print("SCORE: ", score)


user_entry.bind('<Return>', enter)

# configuring time
countdown = Label(root, text="Remaining: " + str(30) + "s", font="Helvetica 20", bg="light blue", fg="red")
countdown.place(x=200, y=100)

clock()


# game over
def game_over():
    # root.config(bg="white")
    # over_txt = Label(root, text="Game Over!", font="comicsansms 20", bg="white", fg="dark blue")
    # over_txt.place(x=280, y=350)
    time.sleep(2)
    print("Your Score is: ", score)
    print("Total tests you have completed: ", tests)
    exit(1)

    # feedback = tmsg.askyesno("Save score", "Do you want to save your score?")
    # print(feedback)
    # print(type(feedback))
    # save()
    # if feedback:
    # save()
    # print("from if: ", feedback)
    # else:
    # exit(1)
    # print("from else: ", feedback)


root.mainloop()
