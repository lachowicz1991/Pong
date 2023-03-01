from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.l_score = 0
        self.r_score = 0
        self.write(f"Score: {self.l_score} | Score: {self.r_score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))

    def show(self):
        self.clear()
        self.write(f"Score: {self.l_score} | Score: {self.r_score}", align="center", font=("Courier", 24, "normal"))