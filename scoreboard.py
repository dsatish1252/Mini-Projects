from turtle import Turtle


FONT = ("Arial", 20, "normal")
ALIGN = "center"


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.sc = 0
        with open("high_score.txt", "r+") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.update_score()

    def inc_score(self):
        self.sc += 1
        self.update_score()

    def reset_score(self):
        if self.sc > self.high_score:
            self.high_score = self.sc
            with open("high_score.txt", "r+") as d:
                d.write(str(self.high_score))
        self.sc = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"SCORE : {self.sc}  HIGH SCORE : {self.high_score}", align=ALIGN, font=FONT)
