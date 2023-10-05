# ----------------------------------------------------------------------------- #
# We are going to modify the Quiz Project from Day 17.
# 1. Take the questions from a request to the Open Trivia API.
#   - API URL: "https://opentdb.com/api.php"
#   - Ask for 10 questions to the api.
#   - No category selected
#   - True and False type of questions.
#   ONCE THIS STEP IS DONE WE SHOULD BE ABLE TO COMMENT OR DELETE THE 'data.py' FILE.
#   * Changes have been done in the 'data.py' file to test both options if we want.
#
# 2. Deal with the HTML entities.
#   When dealing with APIs they have to respect the fact that some symbols are
#   used in the daily basis of HTML coding. To respect that language symbols are
#   substituted by an entity name or number code that refers to them.
#   - HTML ENTITIES DOCUMENTATION: https://www.w3schools.com/html/html_entities.asp
#   - PYTHON HTML MODULE DOCUMENTATION: https://docs.python.org/3/library/html.html
#   ONCE THIS STEP IS DONE WE SHOULD BE ABLE TO READ AND DISPLAY PROPERLY THE QUESTIONS
#   FROM THE TRIVIA API.
#   * Changes have been done in the 'quiz_brain.py' file to test both options.
#
# 3. Create the User Interface using Tkinter:
#   - This time we are going to use a UI class for our UI.
#   * Changes have been done in the 'main.py' and the 'ui.py' file to test the UI.
#
# 4. Take the question from the brain to the UI.
#   * Changes have been done in the 'quiz_brain.py' and the 'ui.py' to meet the requirements.
#   * Information about Python TYPE HINTS int the 'ui.py' file.
#
# 5. Check the users answer.
#   - Give feedback to the user on the APP screen.
#   * Changes have been done in the 'quiz_brain.py' and the 'ui.py' to meet the requirements.
#
# ----------------------------------------------------------------------------- #
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

# ----------------------------------------------------------------------------- #
