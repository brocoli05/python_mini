from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    # update the screen

# TODO 1: Create a snake body
# Each turtle should be a white square (default size: 20x20)

starting_positions = [(0,0), (-20, 0), (-40, 0)]
segments = []

for position in starting_positions:
    segment = Turtle("square")
    # segment.shape("square")
    segment.color("white")
    segment.penup()    # delete the line
    segment.goto(position)
    segments.append(segment)


# TODO 2: Move the snake
screen.update()
game_is_on = True

while game_is_on:
    screen.update()   # update the screen only once all the segments having moved forward
    time.sleep(0.1)  # 0.1 sec delay to see each movement
    # for segment in segments:
    #     segment.forward(10)
    for seg_num in range(len(segments) - 1, 0, -1):
        # start from the last (start = the last index, stop = the first index, step = each movement)
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        # save the previous index of x and y value
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)

# TODO 3: Create snake food

# TODO 4: Detect collision with food

# TODO 5: Create a scoreboard

# TODO 6: Detect collision with wall

# TODO 7: Detect collision with tail


screen.exitonclick()