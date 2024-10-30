from tkinter import *
import os
import tkinter.messagebox as msg_box

i = 1
items = []

tasks_file_path = "tasks.txt"


def submit_task():
    global i
    my_lbx.insert(i - 1, f"T-{i}:    " + task_val.get())

    # store the tasks
    with open(tasks_file_path, "a") as f:
        f.write(task_val.get() + "\n")
        items.append(task_val.get())
    f.close()
    i += 1


def delete_task():
    global click_del_btn
    global index
    global items

    index = int(del_task.get()) - 1
    print("Serial no. of item to be deleted: ", index)
    my_lbx.delete(index)

    # reset the listbox
    num_of_items = my_lbx.size()
    my_lbx.delete(0, num_of_items)

    if click_del_btn == 0:
        with open(tasks_file_path, "r") as f:
            items = f.readlines()
        f.close()
    print(items)

    # strip the newlines at the end of each line
    k = 0
    for line in items:
        items[k] = line.strip()
        k += 1

    items.pop(index)

    for j in range(1, num_of_items + 1):
        my_lbx.insert(j - 1, f"T-{j}:    " + items[j - 1])

    click_del_btn += 1


def reset_task():
    task_val.set("")


def final():
    global items

    # store the final form of tasks
    with open(tasks_file_path, "w") as f:
        for k in range(len(items)):
            f.write(items[k] + "\n")
    f.close()


def view():
    global i
    global items

    if os.path.exists(tasks_file_path):
        with open(tasks_file_path, "r") as f:
            tasks = f.readlines()
        f.close()

        for k in range(len(tasks)):
            tasks[k] = tasks[k].strip()

        for j in range(1, len(tasks) + 1):
            my_lbx.insert(j - 1, f"T-{j}:    " + tasks[j - 1])

        i = len(tasks) + 1

        items = tasks
    else:
        msg_box.showerror("Error", "No Previous Task File!")


def reset_file():
    os.remove(tasks_file_path)
    my_lbx.delete(0, my_lbx.size())


root = Tk()
root.geometry("600x600+400+100")
index = 0
click_del_btn = 0

# receive the task
Label(root, text="Enter task name", font="Fixedsys 20 bold").place(x=160, y=10)

# create entry widget for receiving the task
task_val = StringVar()
get_task = Entry(root, textvariable=task_val, font=("calibri", 15))
get_task.place(x=50, y=50, width=500, height=50)
# print(task_val.get())

# submit Button
Button(root, text="Submit", fg="black", bg="orange", bd=5, relief="raised", command=submit_task,
       font="Veranda 18 bold").place(x=250, y=110, width=120, height=50)

# create scrollbar for the listbox
my_scroll = Scrollbar(root)
my_scroll.pack(side="right", fill="y")

# listbox to show a list of the tasks entered
my_lbx = Listbox(root, font="helvetica 14", yscrollcommand=my_scroll.set)
my_lbx.place(x=50, y=170, width=500, height=150)

# bind the scrollbar with my_lbx
my_scroll.config(command=my_lbx.yview)

# delete task
Label(root, text="Delete Task No.", font="Fixedsys 15 bold").place(x=200, y=350)
del_task = StringVar()
get_task_del = Entry(root, textvariable=del_task, font=("calibri", 15))
get_task_del.place(x=380, y=350, width=50, height=30)

# delete button
Button(root, text="Delete", fg="black", bg="orange", bd=5, relief="raised", command=delete_task,
       font="Veranda 18 bold").place(x=250, y=390, width=120, height=50)

# clear button
Button(root, text="Clear", fg="black", bg="orange", bd=5, relief="raised", command=reset_task,
       font="Veranda 16 bold").place(x=260, y=450, width=100, height=40)

# exit button
Button(root, text="Exit", fg="black", bg="orange", bd=5, relief="raised", command=exit,
       font="Veranda 16 bold").place(x=270, y=500, width=80, height=40)

# final button
Button(root, text="Final", fg="black", bg="orange", bd=5, relief="raised", command=final,
       font="Veranda 18 bold").place(x=430, y=110, width=120, height=50)

# view button
Button(root, text="View", fg="black", bg="orange", bd=5, relief="raised", command=view,
       font="Veranda 18 bold").place(x=50, y=110, width=120, height=50)

# reset button
Button(root, text="Reset", fg="black", bg="orange", bd=5, relief="raised", command=reset_file,
       font="Veranda 18 bold").place(x=50, y=330, width=120, height=50)

root.mainloop()
