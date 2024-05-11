import random
from art import logo, vs
from game_data import data
from replit import clear


def get_random_account():
  """ Get data from random account """
  return random.choice(data)


def format_data(account):
  """ Takes the account data and returns the printable format. """
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr} from {account_country}"


def check_answer(guess, a_followers, b_followers):
  """ Take the user guess and follower counts and returns if they got it right. Or False if they got it wrong. """
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"



# Display art
print(logo)

score = 0
game_should_continue = True
account_b = get_random_account()
account_b = get_random_account()

# Make the game repeatable.
while game_should_continue:
  # Generate a random account from the game data.
  # Making account at position B become the next account at position A.
  account_a = account_b
  account_b = get_random_account()
  while account_a == account_b:
    account_b = get_random_account()

  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")

  # Ask user for a guess.
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  # Check if user is correct.
  ## Get follower count of each account.
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  # Clear the screen between rounds.
  clear()

  # Give user feedback on their guess.
  # Score keeping.
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")


## MY CODE
# is_end = False
# final_score = 0

# while not is_end:
#   a = random.randint(0, len(data) - 1)
#   b = random.randint(0, len(data) - 1)

#   is_duplicate = False
#   while not is_duplicate:
#     if a == b:
#       b = random.randint(0, len(data) - 1)
#     else:
#       is_duplicate = True

#   print(logo)
#   print(
#       f"Compare A: {data[a]['name']}, {data[a]['description']}, from {data[a]['country']}."
#   )

#   print(vs)
#   print(
#       f"Against B: {data[b]['name']}, {data[b]['description']}, from {data[b]['country']}."
#   )

#   user_choice = input("Who has more followers? Type 'A' or 'B': ")

#   if user_choice == 'A' and data[a]['follower_count'] < data[b][
#       'follower_count']:
#     print(f"Sorry, that's wrong. Final score: {final_score}")
#     is_end = True
#   else:
#     final_score += 1
#     print(f"You're right! Current score: {final_score}.")
