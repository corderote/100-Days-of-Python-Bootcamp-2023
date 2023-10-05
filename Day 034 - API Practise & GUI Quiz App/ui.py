# ----------------------------------------------------------------------------- #
from tkinter import *
from quiz_brain import QuizBrain

# ---------------------------- CONSTANTS -------------------------------------- #
THEME_COLOR_1 = "#375362"
THEME_COLOR_2 = "#F0F0F0"
TRUE_COLOR = "#00FF00"
FALSE_COLOR = "#FF0000"
THEME_FONT = ("Arial", 15, "italic")
SCORE_FONT = ("Arial", 10, "bold")
THEME_FONT_COLOR = "#0F0F0F"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Added the quiz brain parameter and the 'self.quiz' variable as part of point 4
        # for the exercise, the rest is for the point 3.
        # We import the QuizBrain type as we need to check that we are passing it as that
        # type in order to work. To specify the type, we add it to the parameter using
        # the ':' sign to assign the parameter type.
        # We use this kind of nomenclature when we want to fix the type of variable or parameter.
        # Example: 'my_var : int' or my_function(my_parameter: my_type)
        # If we want to fix the return from a function we use the '->' followed by the
        # type that we want to assign to the return
        # EXAMPLE: 'my_function(my_par: float) -> str:' will return a string.
        # Both signs are known in Python as TYPE HINTS.
        self.quiz = quiz_brain
        self.score = 0

        self.window = Tk()
        self.window.title("Quiz APP")
        self.window.config(padx=50, pady=50, bg=THEME_COLOR_1)
        self.window.resizable(False, False)

        self.score_label = Label(text="SCORE: 0", font=SCORE_FONT, bg=THEME_COLOR_1)
        self.score_label.grid(row=0, column=0, columnspan=2)

        self.ui_canvas = Canvas(width=300, height=250, bg=THEME_COLOR_2)
        self.question_text = self.ui_canvas.create_text(
            150,
            125,
            text="Insert Question Here",
            width=250,
            font=THEME_FONT,
            fill=THEME_FONT_COLOR)
        self.ui_canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=(40, 50))

        self.true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=self.true_button_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        self.false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=self.false_button_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    # Point 4 of the main.py exercise. *Modified also in part 5.
    def get_next_question(self):
        self.ui_canvas.config(bg=THEME_COLOR_2)
        if self.quiz.still_has_questions():
            question_text = self.quiz.next_question()
            self.ui_canvas.itemconfig(self.question_text, text=question_text)
        else:
            self.ui_canvas.itemconfig(self.question_text, text="Congratulations! You have reach the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Point 5 of the main.py exercise.
    def true_pressed(self):
        answer = self.quiz.check_answer("True")
        self.answer_feedback(answer)

    def false_pressed(self):
        answer = self.quiz.check_answer("False")
        self.answer_feedback(answer)

    def answer_feedback(self, is_right: bool):
        if is_right is True:
            self.ui_canvas.config(bg=TRUE_COLOR)
            self.score += 1
            score_to_str = "SCORE: " + str(self.score)
            self.score_label.config(text=score_to_str)
        elif is_right is False:
            self.ui_canvas.config(bg=FALSE_COLOR)

        self.window.after(2000, self.get_next_question)

# ----------------------------------------------------------------------------- #
