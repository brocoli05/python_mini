from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # constants
MOVE_DISTANCE = 20
UP = 90     # direction constants
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []  # attributes in Snake class
        self.create_snake()
        self.head = self.segments[0]  # for setheading

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle("square")  # no need to make 'segment.shape("square")'
        segment.color("white")
        segment.penup()  # delete the line
        segment.goto(position)
        self.segments.append(segment)  # refer to an attribute

    def extend(self):
        """ add a new segment to the snake. """
        self.add_segment(self.segments[-1].position())  # -1: end of the list

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # start from the last (start = the last index, stop = the first index, step = each movement)
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # save the previous index of x and y value
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)