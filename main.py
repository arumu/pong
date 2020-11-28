from turtle import Screen, Turtle
from score import Score
from paddle import Paddle
from ball import Ball
import time

game_is_on = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score_player1 = Score((150, 240))
score_player2 = Score((-150, 240))
paddle1 = Paddle((350, 0))
paddle2 = Paddle((-350, 0))

for y in range(280, -300, -50):
    new_square = Turtle("square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(0, y=y)

#screen.tracer(1)
ball = Ball()



screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()

    if ball.distance(paddle1) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 340:
        score_player1.update_score()
        ball.reset_position()

    if ball.xcor() < -340:
        score_player2.update_score()
        ball.reset_position()

screen.exitonclick()
