from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.25, stretch_wid = 0.25)
        self.color("blue")
        self.speed("fastest")
        rand_x = random.choice(range(-290, 300, 10))
        rand_y = random.choice(range(-290, 300, 10))
        self.goto(rand_x, rand_y)
        self.refresh()

    def refresh(self):
        rand_x = random.choice(range(-290, 300, 10))
        rand_y = random.choice(range(-290, 300, 10))
        self.goto(rand_x, rand_y)