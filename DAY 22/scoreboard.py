from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Calibri", 50, "bold")
SCREEN_W = 1000
SCREEN_H = 600
BOARDER_X = SCREEN_W / 2 - 10
BOARDER_Y = SCREEN_H / 2 - 10
MIDLE_DASH_SIZE = (BOARDER_Y * 2) / 19


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_user_1 = 0
        self.score_user_2 = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.midleline()
        self.boarder()
        self.update_score()

    def boarder(self):
        boarder = Turtle()
        boarder.hideturtle()
        boarder.penup()
        boarder.color("yellow")
        boarder.goto(-BOARDER_X, -BOARDER_Y)
        boarder.pendown()
        boarder.goto(-BOARDER_X, BOARDER_Y)
        boarder.goto(BOARDER_X, BOARDER_Y)
        boarder.goto(BOARDER_X, -BOARDER_Y)
        boarder.goto(-BOARDER_X, -BOARDER_Y)

    def midleline(self):
        midleline = Turtle()
        midleline.hideturtle()
        midleline.penup()
        midleline.goto(0, BOARDER_Y - MIDLE_DASH_SIZE)
        midleline.setheading(-90)
        midleline.color("white")
        midleline.pensize(5)
        while midleline.ycor() >= -(BOARDER_Y - MIDLE_DASH_SIZE):
            midleline.pendown()
            midleline.forward(MIDLE_DASH_SIZE)
            midleline.penup()
            midleline.forward(MIDLE_DASH_SIZE)

    def update_score(self):
        self.goto(50, BOARDER_Y - 75)
        self.write(arg=f"{self.score_user_1}", font=FONT, align=ALIGNMENT)
        self.goto(-50, BOARDER_Y - 75)
        self.write(arg=f"{self.score_user_2}", font=FONT, align=ALIGNMENT)

    def increase_score_user_1(self):
        self.score_user_1 += 1
        self.clear()
        self.update_score()

    def increase_score_user_2(self):
        self.score_user_2 += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over.", font=FONT, align=ALIGNMENT)
