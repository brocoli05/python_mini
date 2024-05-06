#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

# print(logo)
# print(
#     "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
# )

# difficulty = input("Chosse a difficulty. Type 'easy' or 'hard': ")
# if difficulty == "hard":
#     attempt = 5
# else:
#     attempt = 10

# number = random.randint(1, 100)
# should_continue = True
# while should_continue:
#     print(f"You have {attempt} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if guess == number:
#         print(f"You got it! The answer was {number}.")
#         should_continue = False
#     else:
#         if guess > number:
#             print("Too high.")
#         else:
#             print("Too low.")
#         attempt -= 1

#         if attempt == 0:
#             print("You've run out of guesses, you lose.")
#             should_continue = False

## Method 2 ###############################################
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
    """ checks answer against guess. Returns the number of turns remaining. """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Function to set difficulty.
def set_difficulty():
    level = input("Chosse a difficulty. Type 'easy' or 'hard': ")
    if level == "hard":
        return HARD_LEVEL_TURNS
    else:
        return EASY_LEVEL_TURNS


def game():
    # Choosing a random number between 1 and 100.
    print(logo)
    print(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100."
    )
    answer = random.randint(1, 100)

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've run out of guesses, you lose.")
            return  #exit game
        elif guess != answer:
            print("Guess again.")


game()
