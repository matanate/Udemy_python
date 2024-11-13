import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.speed(30)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)
def circle_step(angle, radius):
    for i in range(0, 360, angle):
        timmy.pencolor(random_color())
        timmy.circle(radius)
        timmy.left(angle)

circle_step(1, 100)


screen = t.Screen()
screen.exitonclick()