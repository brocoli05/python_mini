import random
from turtle import Turtle, Screen
# import turtle
# from turtle import *  # using everything(*) in turtle module
# import turtle as t  # give alias (t)

my_timmy = Turtle()
my_timmy.color("coral")

######## Challenge 1 - Draw a Square ############
# for i in range(4):
#     my_timmy.forward(100)
#     my_timmy.right(90)
#
# screen = Screen()
# screen.onclick(my_timmy.goto)


########### Challenge 2 - Draw a Dashed Line ########
# for i in range(15):
#     my_timmy.forward(10)
#     my_timmy.penup()
#     my_timmy.forward(10)
#     my_timmy.pendown()


########### Challenge 3 - Draw Shapes ########
# for i in range(3, 11):
#     angle = int(360 / i)
#     for j in range(i):
#         my_timmy.forward(100)
#         my_timmy.right(angle)

# colours = ["dark green", "lime green", "light green", "steel blue", "orange", "light pink",
#            "pale violet red", "orange red", "dark orchid", "black", "yellow", "slate blue", "firebrick"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         my_timmy.forward(100)
#         my_timmy.right(angle)
#
# for shape_side_n in range(3, 11):
#     my_timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)


########### Challenge 4 - Random Walk ########
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]
# my_timmy.width(10)
# # my_timmy.pensize(10)
# my_timmy.speed("fastest")
#
# # Turtle Graphics uses normalized colours - floating point values from 0.0 to 1.0.
# # ==> need to tell TG to use 8 bit colours.
# screen = Screen()
# screen.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
#
# for i in range(200):
#     # my_timmy.color(random.choice(colours))
#     my_timmy.color(random_color())
#     my_timmy.forward(30)
#     my_timmy.setheading(random.choice(directions))
#
# # for i in range(10):
# #     steps = int(random.random() * 100)
# #     angle = int(random.choice(directions))
# #     my_timmy.color(random.choice(colours))
# #     my_timmy.right(angle)
# #     my_timmy.forward(steps)


########### Challenge 5 - Spirograph ########
screen = Screen()
screen.colormode(255)
my_timmy.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        my_timmy.color(random_color())
        my_timmy.circle(100)
        my_timmy.setheading(my_timmy.heading() + size_of_gap)


draw_spirograph(5)  # 5 degrees of each time

screen.exitonclick()