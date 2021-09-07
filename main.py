import turtle
from turtle import Turtle
import pandas as pd
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
tim = Turtle()
tim.hideturtle()
score_tim = Scoreboard()
file = pd.read_csv("50_states.csv")
file_states = file.state
file_states_list = file_states.tolist()
file_x_cor = file.x
file_x_cor_list = file_x_cor.tolist()
file_y_cor = file.y
file_y_cor_list = file_y_cor.tolist()
guessed_states = []
not_guessed = []
data_dict = {
    "states not guessed": []
}
while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        data_dict["states not guessed"] = [state for state in file_states_list if state not in guessed_states]
        not_guessed_data = pd.DataFrame(data_dict)
        not_guessed_data.to_csv("States not Guessed.csv")
        break

    if answer_state in file_states_list:
        score_tim.increase_score()
        guessed_states.append(answer_state)
        index = file_states_list.index(answer_state)
        x = file_x_cor_list[index]
        y = file_y_cor_list[index]

        tim.penup()
        tim.goto(x=x, y=y)
        tim.pendown()
        tim.pencolor("black")
        tim.write(f"{answer_state}", align="center")


