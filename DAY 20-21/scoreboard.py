from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self, difficulty):
        super().__init__()
        self.difficulty = difficulty
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 300)
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        with open(f"{self.difficulty}_high_score.txt") as file:
            self.high_score = int(file.read())
        self.write(
            arg=f"Score: {self.score}   High Score: {self.high_score}",
            font=FONT,
            align=ALIGNMENT,
        )

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.high_score:
            with open(f"{self.difficulty}_high_score.txt", "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.update_score()
