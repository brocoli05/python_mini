############DEBUGGING#####################

# # Describe Problem
# def my_function():
# #   for i in range(1, 20):
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# # print(dice_imgs[dice_num]) #IndexError: list index out of range
# print(dice_imgs[dice_num - 1])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# # elif year > 1994:
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# # age = input("How old are you?") # TypeError: '>' not supported between instances of 'str' and 'int'
# age = int(input("How old are you?")) 
# if age > 18:
# # print("You can drive at age {age}.") # Indentation and format
#    print(f"You can drive at age {age}.")

# Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # ==
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(f"pages = {pages}")
print(f"total_words = {total_words}")
print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # indentation
#   b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
