from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)    # update the screen

# TODO 1: Create a snake body
# Each turtle should be a white square (default size: 20x20)
snake = Snake()

# TODO 3: Create snake food
food = Food()

# TODO 5: Create a scoreboard
scoreboard = Scoreboard()

# TODO 2: Move the snake
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()   # update the screen only once all the segments having moved forward
    time.sleep(0.1)  # 0.1 sec delay to see each movement
    snake.move()

    # TODO 4: Detect collision with food
    if snake.head.distance(food) < 15:  # food (10x10)
        # print("nom nom nom")
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # TODO 6: Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # TODO 7: Detect collision with tail
    # if head collides with any segment in the tail:
        # trigger game_over
    for segment in snake.segments:
        # exclude the head
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()