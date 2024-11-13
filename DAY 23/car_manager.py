from turtle import Turtle
import random
import time


COLORS = ["red", "green", "blue", "orange", "yellow", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 15


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def new_car(self):
        new = Turtle()
        new.shape("square")
        new.shapesize(stretch_len=2, stretch_wid=1)
        new.color(random.choice(COLORS))
        new.penup()
        new.goto(350, random.randint(-250, 251))
        new.setheading(180)
        self.cars.append(new)

    def move(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def next_level(self):
        for car in self.cars:
            car.hideturtle()
        self.cars = []
        self.move_distance += 1

    def cars_position(self):
        cars_position = []
        for car in self.cars:
            cars_position.append(car.pos())
