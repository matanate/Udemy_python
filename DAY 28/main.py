from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
checkmarks_text = ""
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global checkmarks_text
    window.after_cancel(timer)
    title_lable.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    checkmarkes_lable.config(text="")
    reps = 0
    checkmarks_text = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        title_lable.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps%2 == 0:
        title_lable.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        title_lable.config(text="Work", fg=GREEN)
        countdown(work_sec)
        
    


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global checkmarks_text
    minuts = int(count/60)
    secounds = count % 60 

    if minuts < 10:
        minuts = f"0{minuts}"
    if secounds < 10:
        secounds = f"0{secounds}"
    
    canvas.itemconfig(timer_text, text=f"{minuts}:{secounds}")

    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        if reps%2 == 0:
            checkmarks_text += "✔"
            checkmarkes_lable.config(text = checkmarks_text)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg = YELLOW)

# Tomato Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold" ))
canvas.grid(row=1, column=1)

# Title

title_lable = Label(text="Timer", font=(FONT_NAME, 35, "bold"),bg=YELLOW, fg=GREEN)
title_lable.grid(row=0, column=1)

#Start Button

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"),bg=YELLOW, fg="blue", command=start_timer)
start_button.grid(row=2, column=0)

#Reset Button

reset_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"),bg=YELLOW, fg="blue", command=reset_timer)
reset_button.grid(row=2, column=2)

# Checkmarkes

checkmarkes_lable = Label(font=(FONT_NAME, 10, "bold"),bg=YELLOW, fg=GREEN)
checkmarkes_lable.grid(row=3, column=1)


window.mainloop()