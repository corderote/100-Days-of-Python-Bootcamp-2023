# ----------------------------------------------------------------------------- #
# The Quiz Project.
# This will be a simple True/False Quiz game using OOP.
from question_model import Question
from quiz_brain import QuizBrain
import data

# Creating a Question bank, a list of Question objects.
questions_bank = []
for question in data.question_data:
    new_question_text = question["text"]
    new_question_answer = question["answer"]
    new_question = Question(new_question_text, new_question_answer)
    questions_bank.append(new_question)

q_brain = QuizBrain(questions_bank)

while q_brain.still_has_questions():
    q_brain.next_question()

print("You have completed THE QUIZ!")
print(f"Your final score is: {q_brain.score}/{q_brain.questions_number}.")

# ----------------------------------------------------------------------------- #
# TODO: Update data.py and the_quiz_project.py it to work with:
#  https://opentdb.com/
#  You already have a question_data_from_opentdb variable to try.
# ----------------------------------------------------------------------------- #
