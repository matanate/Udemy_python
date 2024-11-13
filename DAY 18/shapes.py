from turtle import Turtle, Screen
import random

screen = Screen()
screen.colormode(255)

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

def draw_shape(num):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy_the_turtle.pencolor(r,g,b)
    angle = 360/num
    for i in range(num):
        timmy_the_turtle.forward(100)
        timmy_the_turtle.right(angle)

for num in range(3 , 11):
    draw_shape(num)



screen.exitonclick()