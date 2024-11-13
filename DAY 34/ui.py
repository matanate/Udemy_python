from tkinter import *
from tkinter import messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_NAME = "Courier"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title = "Quizzler"
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Hello",
            fill="black",
            font=(FONT_NAME, 15, "italic"),
            width=280,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        # Score label:
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=(FONT_NAME, 10, "normal"),
        )
        self.score_label.grid(row=0, column=1)

        # False button
        self.false_image = PhotoImage(file="images\\false.png")
        self.false_button = Button(
            image=self.false_image, pady=20, command=lambda: self.check_answer("false")
        )
        self.false_button.grid(row=2, column=1)

        # True button
        self.true_image = PhotoImage(file="images\\true.png")
        self.true_button = Button(
            image=self.true_image, pady=20, command=lambda: self.check_answer("true")
        )
        self.true_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def check_answer(self, user_answer):
        a_response = self.quiz.check_answer(user_answer)
        if a_response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_label.config(
            text=f"Score: {self.quiz.score}/{self.quiz.question_number}"
        )
        if self.quiz.still_has_questions():
            self.window.after(1000, self.get_next_question)
        else:
            messagebox.showinfo(
                title="You've completed the quiz",
                message=f"Your final score was: {self.quiz.score}/{self.quiz.question_number}",
            )
            self.window.destroy()
