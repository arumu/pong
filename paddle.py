from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(position)

    def up(self):
        y_position = self.ycor() + 20
        self.setposition(x=self.xcor(), y=y_position)

    def down(self):
        y_position = self.ycor() - 20
        self.setposition(x=self.xcor(), y=y_position)

