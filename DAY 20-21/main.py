from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from difficulty import Difficulty
import time


def key_inputs():
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


screen = Screen()
screen.setup(width=610, height=650)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Set difficulty
difficulty = Difficulty()
difficulty.set_difficulty(screen)
difficulty_num = difficulty.difficulty_num
# Create the snake, food and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard(difficulty=difficulty.difficulty)

# Define the inputs
key_inputs()

game_on = True
while game_on:
    # move the snake
    screen.update()
    time.sleep(difficulty_num)
    snake.move()

    # Detect colission with food
    if snake.head.distance(food) < 5:
        scoreboard.increase_score()
        food.refresh()
        snake.extend_snake()

    # Detect colission with wall
    if (
        snake.head.xcor() > 295
        or snake.head.ycor() > 295
        or snake.head.xcor() < -295
        or snake.head.ycor() < -295
    ):
        difficulty.set_difficulty(screen)
        difficulty_num = difficulty.difficulty_num
        scoreboard.difficulty = difficulty.difficulty
        scoreboard.reset_score()
        snake.reset_score()
        food.refresh()
        key_inputs()

    # Detect colisson with snake body
    for seg in snake.snake_body[1:]:
        if snake.head.distance(seg) < 5:
            difficulty.set_difficulty(screen)
            difficulty_num = difficulty.difficulty_num
            scoreboard.difficulty = difficulty.difficulty
            scoreboard.reset_score()
            snake.reset_score()
            food.refresh()
            key_inputs()


screen.exitonclick()
