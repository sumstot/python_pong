from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.tracer(0)

ball = Ball()

scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    scoreboard
    ball.move()
    screen.update()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.xcor() > 330 and ball.distance(paddle_r) < 60 or ball.xcor() < -330 and ball.distance(paddle_l) < 60:
        ball.bounce_paddle()

    if ball.xcor() > 390:
        scoreboard.clear()
        scoreboard.increase_left_score()
        ball.speed_reset()
        ball.reset()

    if ball.xcor() < -390:
        scoreboard.clear()
        scoreboard.increase_right_score()
        ball.speed_reset()
        ball.reset()














screen.exitonclick()