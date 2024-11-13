import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=680, height=680)
screen.tracer(0)

# Create player object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Define the inputs
screen.listen()
screen.onkeypress(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    i = random.randint(1, 6)
    if i == 1:
        car_manager.new_car()
    car_manager.move()

    # Detect finish line
    if player.ycor() > 340:
        scoreboard.next_level()
        player.reset_pos()
        car_manager.next_level()

    # Detect colission with cars
    for car in car_manager.cars:
        if (
            player.distance(car.xcor() - 10, car.ycor()) < 20
            or player.distance(car.xcor() + 10, car.ycor()) < 20
        ):
            scoreboard.game_over()
            game_on = False

screen.exitonclick()
