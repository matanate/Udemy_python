from turtle import Turtle

START_POS = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.reset_pos()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(START_POS)
