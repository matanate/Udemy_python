from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-250, 290)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT, align="center")

    def next_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", font=FONT, align="center")
