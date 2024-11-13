from tkinter import *
from tkinter import messagebox
import pandas as pd
import os


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Courier"


# ---------------------------- Card Mechanisem ------------------------------- #
def new_card():
    global timer
    french_word = data["French"][word_index]
    canvas.itemconfig(image_container, image=card_front_img)
    canvas.itemconfig(language_text, text="French", fill="black")
    canvas.itemconfig(word_text, text=french_word, fill="black")
    window.after_cancel(timer)
    timer = window.after(3000, flip_card)


def flip_card():
    english_word = data["English"][word_index]
    canvas.itemconfig(image_container, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=english_word, fill="white")


# ---------------------------- Tik and X Functions ------------------------------- #
def known_word():
    global word_index
    global data
    data = data.drop([word_index])
    data.to_csv(to_learn_data_path, index=False)
    word_index += 1
    if data.empty:
        messagebox.showinfo(title="Finished", message="You have learned all the words")
        os.remove(to_learn_data_path)
        raise SystemExit
    elif word_index == data.index[-1]:
        refresh_data()
    new_card()


def unknown_word():
    global word_index
    global data
    if word_index == data.index[-1]:
        refresh_data()
    new_card()
    word_index += 1


def refresh_data():
    global word_index
    global data
    data = data.sample(frac=1).reset_index(drop=True)
    word_index = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

# images definition
card_front_img = PhotoImage(file="images\card_front.png")
card_back_img = PhotoImage(file="images\card_back.png")
x_img = PhotoImage(file="images\wrong.png")
tik_img = PhotoImage(file="images\\right.png")

# Fetch Data

data_path = "data\\french_words.csv"
to_learn_data_path = "data\\french_words_to_learn.csv"
try:
    data = pd.read_csv(to_learn_data_path)
except FileNotFoundError:
    data = pd.read_csv(data_path)
finally:
    refresh_data()


# Canvas items, Card and card text
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)

image_container = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(
    395, 150, text="French", fill="black", font=(FONT_NAME, 30, "italic")
)

word_text = canvas.create_text(
    395, 250, text=data["French"][0], fill="black", font=(FONT_NAME, 35, "bold")
)
canvas.grid(row=0, column=0, columnspan=6)
# X button
x_button = Button(image=x_img, command=unknown_word)
x_button.grid(row=1, column=1)

# Tik button
tik_button = Button(image=tik_img, command=known_word)
tik_button.grid(row=1, column=4)

# Set timer
timer = window.after(3000, flip_card)

window.mainloop()
