# ----------------------------------------------------------------------------- #
class QuizBrain:
    def __init__(self, qb_questions_list):
        self.questions_number = 0
        self.questions_list = qb_questions_list
        self.score = 0

    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        q_number = self.questions_number + 1
        user_answer = input(f"Q.{q_number}: {current_question.text} "
                            "Is it True or False?\n")
        user_answer = user_answer.lower()
        if user_answer == "true" or user_answer == "false":
            self.questions_number += 1
            self.check_answer(user_answer, current_question.answer)
        else:
            print("ERROR: Invalid answer")
            self.next_question()

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)

    def check_answer(self, given_answer, question_answer):
        if given_answer.lower() == question_answer.lower():
            print("You got it RIGHT!")
            self.score += 1
        else:
            print("That´s wrong.")
        print(f"The correct answer was {question_answer}.")
        print(f"Your current score is: {self.score}/{self.questions_number}.")
# ----------------------------------------------------------------------------- #
