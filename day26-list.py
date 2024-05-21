## List Comprehension
numbers = [1, 2, 3]
# Create a new list from numbers, where you added 1 to each value
new_list = [number + 1 for number in numbers]
print(new_list)

name = "Python Bootcamp"
letter_list = [letter for letter in name]
print(letter_list)

# Create a new list from a range, where the list items are double the values in the range
double_list = [num * 2 for num in range(1, 5)]
print(double_list)

## Conditional List Comprehension
## new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
# Create a new list that contains the names longer than 5 characters in ALL CAPS
capitalized_names = [name.upper() for name in names if len(name) > 5]
print(capitalized_names)
