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
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "wheat", "SlateGray", "SeaGreen"]
angle = [0, 90, 180, 270, 360]
my_timmy.width(3)
for i in range(10):
    steps = int(random.random() * 100)
    angle = int(random.choice(angle))
    my_timmy.color(random.choice(colours))
    my_timmy.right(angle)
    my_timmy.forward(steps)