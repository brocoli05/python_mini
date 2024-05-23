import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
# set the background using image file
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

# TODO 2: Check if the guess is among the 50 states
all_states = data.state.to_list()
guessed_states = []

# TODO 4: Use a loop to allow the user to keep guessing
while len(guessed_states) < 50:
    # TODO 1: Convert the guess to Title case
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # title(): make first letter capitalize

    if answer_state == "Exit":
        # Save the missing states to a.csv
        # list comprehension ==> make code shorter
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("a.csv")
        break

    # TODO 5: Record the correct guesses in a list
    if answer_state in all_states:
        # TODO 6: Keep track of the score
        guessed_states.append(answer_state)

        # TODO 3: Write correct guesses onto the map
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))  # int(): avoid bad screen distance
        t.write(state_data.state.item())

# screen.exitonclick()
