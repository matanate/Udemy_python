from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)


# Miles Entry

input = Entry(width=10)
input.grid(row=0, column=1)

# Miles Lable

miles_lable = Label(text="Miles")
miles_lable.grid(row=0, column=2)

# is equal to Lable

equal_lable = Label(text="is equal to")
equal_lable.grid(row=1, column=0)

# Result Lable
result_lable = Label(text="0")
result_lable.grid(row=1, column=1)

# Km Lable

km_lable = Label(text="Km")
km_lable.grid(row=1, column=2)

# Calculate Button


def calculate():
    result = float(input.get()) * 1.609344
    result_lable.config(text=f"{result}")


button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
