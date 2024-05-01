rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computerInput = random.randint(0,2)

if userInput == computerInput:
  print("It's a tie!")
elif userInput == 0 and computerInput == 2:
  print("You win!")
elif userInput == 1 and computerInput == 0:
  print("You win!")
elif userInput == 2 and computerInput == 1:
  print("You win!")
else:
  print("You lose!")