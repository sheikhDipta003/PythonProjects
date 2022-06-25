from tkinter import *
from tkinter import filedialog
import os

# Global variables
global filename
global temp_filename
temp_filename = False
global untitled_file_obj
global file_no

root = Tk()
root.title("MyNotepad")
root.geometry('800x600+300+100')
root.config(bg="blue")

# create status bar
current_status = StringVar()

# text-field
text_area = Text(root, bg="light green", bd=6, fg="black", font=("calibri", 15), wrap=WORD, state=DISABLED,
                 relief="groove")
text_area.place(x=10, y=10, width=780, height=540)

# Collect Untitled File No. from "list_untitled_files.txt" file
f = open("list_untitled_files.txt", "r")
index_untitled_file = f.read()
file_no = int(index_untitled_file) + 1


def new_file():
    global untitled_file_obj
    global file_no

    text_area.delete('1.0', 'end')  # Delete anything already written on Tk window

    # check if untitled files < file_no exists or not
    temp = file_no - 1
    while True and temp >= 1:
        if os.path.exists(f"C:/Users/HP/Desktop/MyNotepad Texts/Untitled{temp}.txt"):
            break
        else:
            temp -= 1
            file_no -= 1

    f.close()

    # Enable "Save" and :Save As" menu
    file_menu.entryconfig("Save", state="normal")
    file_menu.entryconfig("Save As", state="normal")

    text_area.config(state=NORMAL)
    untitled_file_obj = open(f"Untitled{file_no}.txt", "w")

    current_status.set(f"Untitled{file_no}.txt")
    status_bar.update()


# functions
def open_file():
    global filename

    # Enable "Save" and :Save As" menu
    file_menu.entryconfig("Save", state="normal")
    file_menu.entryconfig("Save As", state="normal")

    text_area.config(state=NORMAL)

    filename = filedialog.askopenfilename(initialdir="C:/Users/HP/Desktop/MyNotepad Texts", title="Select A File",
                                          filetypes=(("All Files", "*.*"), ("Text Files", "*.txt*")))
    # check if the filename is specified
    if filename:
        text_area.delete('1.0', 'end')  # Create a new window for opened file

        global temp_filename
        temp_filename = filename

        print(filename)
        with open(filename, "r") as f:
            content = f.read()
            # print(content)
            text_area.insert(END, content)  # When I wrote like this: text_area.insert(END, f.read()) ,nothing was being
            # written on text_area

        current_status.set(os.path.basename(filename))
        status_bar.update()


def save_file():
    global filename

    if temp_filename:  # check if the file of name "filename" exists, i.e. if "filename != NULL"
        reopen_file = open(filename, "w")
        reopen_file.write(text_area.get('1.0', 'end'))
        reopen_file.close()


def save_file_as():
    global file_no

    save_file_name = filedialog.asksaveasfilename(defaultextension=".*", initialfile=f"Untitled{file_no}.txt",
                                                  initialdir="C:/Users/HP/Desktop/MyNotepad Texts",
                                                  title="Save File As",
                                                  filetypes=(("All Files", "*.*"), ("Text Files", "*.txt*")))

    if save_file_name:  # check if the file of name "save_file_name" exists
        # print(save_file_name)
        if save_file_name != f"C:/Users/HP/Desktop/MyNotepad Texts/Untitled{file_no}.txt":
            current_status.set(os.path.basename(save_file_name))
            status_bar.update()

        saveAs_file = open(save_file_name, "w")
        saveAs_file.write(text_area.get('1.0', 'end'))
        saveAs_file.close()


def exit_notepad():
    f = open("list_untitled_files.txt", "w")
    f.write(f"{file_no}")
    f.close()
    exit(0)


# create menus
my_menubar = Menu(root)
file_menu = Menu(my_menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)

# Disable "save", close and "save as" menu when no new file has been created
file_menu.entryconfig("Save", state="disabled")
file_menu.entryconfig("Save As", state="disabled")

file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_notepad)

root.config(menu=my_menubar)
my_menubar.add_cascade(label="File", menu=file_menu)

status_bar = Label(root, bd=4, relief="sunken", textvariable=current_status, bg="blue", fg="white",
                   font=("Century", 15, "bold"))
status_bar.place(x=10, y=555, width=780)

root.mainloop()

# Keep track of the last "Untitled-" file no and save it
f1 = open("list_untitled_files.txt", "w")
f1.write(f"{file_no}")
f1.close()

