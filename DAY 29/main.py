from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = emailuser_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please dont leave empty fields!")
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?",
        )
        if is_ok:
            try:
                with open("data.json", "r") as f:
                    # Reading old data
                    data = json.load(f)
            except FileNotFoundError:
                with open("data.json", "w") as f:
                    # Saving data to new file
                    json.dump(new_data, f, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)
                with open("data.json", "w") as f:
                    # Saving updated data
                    json.dump(data, f, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as f:
            # Reading data
            data = json.load(f)
            website_data = data[website]
    except KeyError:
        messagebox.showerror(title="Website Error", message="Website was not found.")
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Datafile found.")
    else:
        email = website_data["email"]
        password = website_data["password"]
        messagebox.showinfo(
            title=website, message=f"Email: {email}\nPassword: {password}"
        )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Lock Image
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)

canvas.grid(row=0, column=1, sticky="ew")

# Website label
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, sticky="ew")

# Email/Username label
emailuser_label = Label(text="Email/Username:")
emailuser_label.grid(row=2, column=0, sticky="ew")

# Password label
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, sticky="ew")

# Website Entry
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, sticky="ew")
website_entry.focus()

# Email/Username Entry
emailuser_entry = Entry(width=35)
emailuser_entry.grid(row=2, column=1, columnspan=2, sticky="ew")
emailuser_entry.insert(0, "matan@gmail.com")

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="ew")

# Search button
search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2, sticky="ew")

# Generate Password button
gen_password_button = Button(text="Generate Password", command=generate_password)
gen_password_button.grid(row=3, column=2, sticky="ew")

# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
