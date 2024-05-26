# ## List Comprehension
# numbers = [1, 2, 3]
# # Create a new list from numbers, where you added 1 to each value
# new_list = [number + 1 for number in numbers]
# print(new_list)

# name = "Python Bootcamp"
# letter_list = [letter for letter in name]
# print(letter_list)

# # Create a new list from a range, where the list items are double the values in the range
# double_list = [num * 2 for num in range(1, 5)]
# print(double_list)

# ## Conditional List Comprehension
# ## new_list = [new_item for item in list if test]
# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
# # Create a new list that contains the names longer than 5 characters in ALL CAPS
# capitalized_names = [name.upper() for name in names if len(name) > 5]
# print(capitalized_names)


## Dictionary Comprehension
# import random

# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)

# passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
# print(passed_students)


## Iterate over a Panadas DataFrame
student_dict = {
   "student": ["Angela", "James", "Lily"],
   "score": [56, 76, 98]
}

# Loop through dictionaries
# for (key, value) in students_dict.items():
#    print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a data frame
for (key, value) in student_data_frame.items():
   print(key)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
   # print(row)
   # print(row.student)
   if row.student == "Angela":
      print(row.score)
