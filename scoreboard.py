from turtle import Turtle as T


class Scoreboard(T):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))


    def inc_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))


