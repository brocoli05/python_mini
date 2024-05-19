from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# TODO 1: Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

# TODO 2: Create and move a paddle
screen.tracer(0)   # turn off the animation not to show a paddle moving to the wall at the beginning

# TODO 3: Create another paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
# onkey vs. onkeypress
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# TODO 4: Create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    # time.sleep(0.1)  # slow the speed of moving ball to catch
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # TODO 5: Detect collision with wall and bounce
    """ The screen is 600px tall. Detect collisions with the top and bottom walls. 
    Change the ball's movement direction upon collision. 
    The ball size is 20x20. """
    if ball.ycor() < -280 or ball.ycor() > 280:
        # needs to bounce
        ball.bounce_y()

    # TODO 6: Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # TODO 7: Detect when paddle misses
    """ Detect if the ball goes out of bounds at the edge of the screen. 
    If yes, reset the ball's position to the center of the screen.
    The ball should then start moving towards the other player. """
    # TODO 8: Keep score
    # when R paddle misses
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    # when L paddle misses
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()