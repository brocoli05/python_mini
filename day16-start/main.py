# import another_module
# print(another_module.another_variable)

# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")  # show a turtle
# timmy.color("coral")
# timmy.forward(100)
#
# my_screen = Screen()  # create an object
# print(my_screen.canvheight)  # object.attribute
# my_screen.exitonclick()  # object.method

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"  # text alignment
print(table)

