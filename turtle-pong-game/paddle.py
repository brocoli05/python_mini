from turtle import Turtle

""" Create a paddle.py file for the Paddle class. 
The Paddle class needs to inherit from Turtle.
Paddle objects need to be initialised with a tuple for the X and Y coordinates.
The l_paddle needs to move up and down with the "w" and "s" keys."""


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        if new_y < 270:  # ensure the paddle doesn't move off the top of the screen
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        if new_y > -270:  # ensure the paddle doesn't move off the bottom of the screen
            self.goto(self.xcor(), new_y)
