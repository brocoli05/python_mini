from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Write a for loop to iterate over the quesiton_data.
# Create a Question object from each entry in quesiton_data.
# Append each Question object to the question_bank.
question_bank = []
for question in question_data:
    # question_text = question["text"]
    # question_answer = question["answer"]
    # advantage of using OOP - modularity, only need to modify main file according to the data key value
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].answer)

quiz = QuizBrain(question_bank)
quiz.next_question()

# Use the while loop to show the next question until the end.
while quiz.still_has_questions():  # if quiz still has questions remaining:
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")