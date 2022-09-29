from turtle import Turtle

ALIGNMENT = "Center"
FONT = "Arial"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        text_position_xaxis = 240
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = 0
        self.goto(0, text_position_xaxis)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.text()

    def text(self):
        self.write(f"Score:{self.score} ", move=False, align=ALIGNMENT, font=(FONT, 30, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", move=False, align=ALIGNMENT, font=(FONT, 30, "normal"))
