from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(arg=f"{self.score}", align="center", font=("Courier", 44, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", align="center", font=("Teletype", 44, "normal"))



