from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(200, 250)
        self.write(self.score, align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
