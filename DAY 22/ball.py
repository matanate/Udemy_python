from turtle import Turtle
from scoreboard import BOARDER_X, BOARDER_Y
import random

START_DIRECTION = [45, 135, 225, 315]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.6, stretch_wid=0.6)
        self.color("blue")
        self.reset_pos()

    def move(self):
        self.forward(10)

    def turn_left(self):
        self.left(90)

    def turn_right(self):
        self.right(90)

    def reset_pos(self):
        self.goto(0, random.randint(-BOARDER_Y, BOARDER_Y))
        self.setheading(random.choice(START_DIRECTION))
