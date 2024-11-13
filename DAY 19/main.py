import turtle
from turtle import Turtle, Screen
import random

colors = ["black", "blue", "green", "red", "yellow", "orange", "purple", "pink", "turquoise", "beige"]
set_number = 0
def create_turtles(number):
    turtles = []
    global winner
    win = False
    for i in range(0, number):
        turtles.append(Turtle(shape = "turtle"))
        if i == 0:
            turtles[i].penup()
            turtles[i].setpos(450,350)
            turtles[i].pendown()
            turtles[i].setpos(450,-350)
            turtles[i].penup()
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].setpos(-450, 300 - i*pos_step)
    
    while win == False:
        for i in range(0, number):
            turtles[i].forward(random.randint(0,10))
            if turtles[i].pos()[0] >= 430:
                 winner = colors[i]
                 win = True

screen = Screen()

while set_number < 2 or set_number > 10:
    set_number = int(turtle.numinput("Set number of turtles", "how many colors will be racing? (2-10)"))
colors_str = "\\".join(map(str, colors[0:set_number]))
bet = turtle.textinput("Make your bet!", f"who will win the race? Enter a color: \n{colors_str}")
pos_step = 600 / (set_number - 1)

create_turtles(set_number)
if bet == winner:
    outcom = "Won"
else:
    outcom = "Lost"
print(f"You've {outcom}!, the winner is {winner}")

screen.exitonclick()