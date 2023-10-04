from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
screen.update()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

delay_time = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(delay_time)

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        delay_time *= 0.8

    # Detect a miss
    if ball.xcor() > 380:
        ball.miss()
        scoreboard.l_point()
        delay_time = 0.1

    if ball.xcor() < -380:
        ball.miss()
        scoreboard.r_point()
        delay_time = 0.1

screen.exitonclick()
