import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.hideturtle()
timmy.pensize(10)
timmy.speed(10)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
def random_step():
    timmy.pencolor(random_color())
    direction = random.choice([0, 90, 180, 270])
    timmy.setheading(direction)
    timmy.forward(50)

while True:
    random_step()
screen = t.Screen()
screen.exitonclick()