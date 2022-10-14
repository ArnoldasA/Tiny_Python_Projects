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
        with open("score.txt") as file:
            self.old_high_score = file.read()
        self.high_score = int(self.old_high_score)
        self.score = 0
        self.goto(0, text_position_xaxis)
        self.increase_score()


    def increase_score(self):
        self.clear()
        self.score += 1
        self.text()

    def text(self):
        self.write(f"Score:{self.score} " f"High Score: {self.high_score}", move=False, align=ALIGNMENT,
                   font=(FONT, 30, "normal"))

    # def game_over(self):
    #    self.goto(0, 0)
    #   self.write("Game over!", move=False, align=ALIGNMENT, font=(FONT, 30, "normal"))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            with open ("score.txt",mode="w") as file:
                self.high_score = self.score
                file.write(str(self.high_score))

        self.score = 0
        self.increase_score()
