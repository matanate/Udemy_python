from turtle import Turtle
from scoreboard import BOARDER_X, BOARDER_Y

START_POS_1 = [
    (BOARDER_X - 5, -25),
    (BOARDER_X - 5, -15),
    (BOARDER_X - 5, -5),
    (BOARDER_X - 5, 5),
    (BOARDER_X - 5, 15),
    (BOARDER_X - 5, 25),
]
START_POS_2 = [
    (-BOARDER_X + 5, -25),
    (-BOARDER_X + 5, -15),
    (-BOARDER_X + 5, -5),
    (-BOARDER_X + 5, 5),
    (-BOARDER_X + 5, 15),
    (-BOARDER_X + 5, 25),
]


class Raquets:
    def __init__(self):
        self.user_1 = []
        self.user_2 = []
        self.create_users()

    def create_users(self):
        for pos in START_POS_1:
            self.add_segment(pos, self.user_1)
        for pos in START_POS_2:
            self.add_segment(pos, self.user_2)

    def add_segment(self, position, user):
        seg = Turtle("square")
        seg.shapesize(stretch_len=0.5, stretch_wid=0.5)
        seg.color("white")
        seg.penup()
        seg.goto(position)
        seg.setheading(90)
        user.append(seg)

    def up_1(self):
        if self.user_1[-1].ycor() < (BOARDER_Y - 5):
            for seg in self.user_1:
                seg.forward(10)

    def down_1(self):
        if self.user_1[0].ycor() > -(BOARDER_Y - 5):
            for seg in self.user_1:
                seg.backward(10)

    def up_2(self):
        if self.user_2[-1].ycor() < (BOARDER_Y - 5):
            for seg in self.user_2:
                seg.forward(10)

    def down_2(self):
        if self.user_2[0].ycor() > -(BOARDER_Y - 5):
            for seg in self.user_2:
                seg.backward(10)

    def top_user_1(self):
        return self.user_1[-1].ycor() + 5

    def bottom_user_1(self):
        return self.user_1[0].ycor() - 5

    def top_user_2(self):
        return self.user_2[-1].ycor() + 5

    def bottom_user_2(self):
        return self.user_2[0].ycor() - 5
