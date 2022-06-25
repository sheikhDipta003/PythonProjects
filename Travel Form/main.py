from tkinter import *

root = Tk()


# function to store input
def getvals():
    print("Submitted.. Wish you enjoy the journey :)")

    print(f"{name_val.get(), phone_val.get(), gender_val.get(), emergency_val.get(), payment_mode_val.get()}")

    with open("records.txt", "a") as f:
        f.write(f"{name_val.get(), phone_val.get(), gender_val.get(), emergency_val.get(), payment_mode_val.get()}\n")


# GUI logic
root.geometry("644x344+400+200")

# heading
Label(root, text="Welcome to MESH TRAVELS", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

# text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
payment_mode = Label(root, text="Payment Mode")

# pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
payment_mode.grid(row=5, column=2)

# tkinter variable classes for storing entries
name_val = StringVar()
phone_val = StringVar()
gender_val = StringVar()
emergency_val = StringVar()
payment_mode_val = StringVar()
foodServe_val = IntVar()

# creating the entries
name_entry = Entry(root, textvariable=name_val)
phone_entry = Entry(root, textvariable=phone_val)
gender_entry = Entry(root, textvariable=gender_val)
emergency_entry = Entry(root, textvariable=emergency_val)
payment_mode_entry = Entry(root, textvariable=payment_mode_val)

# packing the entries
name_entry.grid(row=1, column=3)
phone_entry.grid(row=2, column=3)
gender_entry.grid(row=3, column=3)
emergency_entry.grid(row=4, column=3)
payment_mode_entry.grid(row=5, column=3)

# checkbox
foodServe = Checkbutton(text="Want to prebook your meals?", variable=foodServe_val)
foodServe.grid(row=6, column=3)

# submit button
Button(text="Submit to MESH TRAVELS", command=getvals).grid(row=7, column=3)

root.mainloop()
