from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Lable

my_lable = Label(text="I am a Lable!", font=("Ariel", 24, "bold"))
my_lable.grid(row=0, column=0)


def comd():
    my_lable.config(text=input.get())


# Button

button = Button(text="Click Me", command=comd)
button.grid(row=1, column=1)

# Button2

button2 = Button(text="new button", command=comd)
button2.grid(row=0, column=2)

# Entry

input = Entry(width=30)
input.grid(row=2, column=3)


window.mainloop()
