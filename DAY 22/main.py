from turtle import Screen
from raquets import Raquets
from scoreboard import Scoreboard, SCREEN_W, SCREEN_H, BOARDER_X, BOARDER_Y
from ball import Ball
import time

screen = Screen()
screen.setup(width=SCREEN_W, height=SCREEN_H)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

# Create users raquets
raquets = Raquets()
ball = Ball()
scoreboard = Scoreboard()

# Define the inputs
screen.listen()
screen.onkeypress(raquets.up_1, "Up")
screen.onkeypress(raquets.down_1, "Down")
screen.onkeypress(raquets.up_2, "w")
screen.onkeypress(raquets.down_2, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    # Detect colission with walls
    y = ball.ycor()
    x = ball.xcor()
    heading = ball.heading()
    if y < -(BOARDER_Y - 10):
        if heading == 315:
            ball.turn_left()
        if heading == 225:
            ball.turn_right()

    if y > (BOARDER_Y - 10):
        if heading == 45:
            ball.turn_right()
        if heading == 135:
            ball.turn_left()

    # Detect colission with raquet

    if (
        y > raquets.bottom_user_1()
        and y < raquets.top_user_1()
        and x > (BOARDER_X - 10)
    ):
        if ball.heading() == 45:
            ball.turn_left()
        if ball.heading() == 315:
            ball.turn_right()
    if (
        y > raquets.bottom_user_2()
        and y < raquets.top_user_2()
        and x < -(BOARDER_X - 10)
    ):
        if ball.heading() == 135:
            ball.turn_right()
        if ball.heading() == 225:
            ball.turn_left()

    # Detect point

    if x > SCREEN_W / 2:
        scoreboard.increase_score_user_2()
        time.sleep(0.5)
        ball.reset_pos()
        screen.update()
        time.sleep(0.5)

    if x < -SCREEN_W / 2:
        scoreboard.increase_score_user_1()
        time.sleep(0.5)
        ball.reset_pos()
        screen.update()
        time.sleep(0.5)

screen.exitonclick()
