from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect ball collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right player misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if left player misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()