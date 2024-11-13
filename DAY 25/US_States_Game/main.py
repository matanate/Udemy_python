from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("US_States_Game\\50_states.csv")
data = data.set_index("state")

screen = Screen()
screen.setup(height=491, width=725)
screen.title("U.S. States Game")
image = "US_States_Game\\blank_states_img.gif"
screen.addshape(image)

img = Turtle(shape=image)
print_name = Turtle()
print_name.hideturtle()
print_name.penup()

game_on = True
currect_states = 0
while game_on == True:
    if currect_states == 0:
        answer_state = screen.textinput(
            title="guess the State", prompt="What's another state name"
        ).title()
    else:
        answer_state = screen.textinput(
            title=f"{currect_states}/50 States Correct",
            prompt="What's another state name",
        ).title()
    if answer_state == "Exit":
        break
    if answer_state in data.index.values:
        x = data.x[answer_state]
        y = data.y[answer_state]
        print_name.goto(x, y)
        print_name.write(answer_state)
        data = data.drop(answer_state)
        currect_states += 1

data = data.reset_index()
data = data.state
pd.DataFrame.to_csv(data, "US_States_Game\\states_to_learn.csv")
