from turtle import Screen
from player import Player
from car_manager import CarManger
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)  # 600px x 600px
screen.tracer(0)  # turn off tracer

# TODO 1: Move the turtle with keypress
player = Player()
car_manager = CarManger()

# TODO 5: Create a scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)  # refresh the screen every 0.1s
    screen.update()

    # TODO 2: Create and move the cars
    car_manager.create_car()
    car_manager.move_cars()

    # TODO 3: Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # TODO 4: Detect when turtle reaches the other side
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car_manager.level_up()

screen.exitonclick()
