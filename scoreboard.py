from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(-90, 250)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}/50", align="left", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()