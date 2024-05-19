from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        # to bounce a ball
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        """ bounce horizontally """
        self.x_move *= -1
        self.move_speed *= 0.9  # increase the ball speed

    def bounce_y(self):
        """ bounce vertically """
        self.y_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1  # reset the ball speed
        self.bounce_x()