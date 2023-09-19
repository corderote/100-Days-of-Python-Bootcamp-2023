# ----------------------------------------------------------------------------- #
import random
import turtle

TURTLES_COLORS = ["green", "blue", "orange", "purple", "red", "grey"]

turtle_screen = turtle.Screen()
turtle_screen.setup(width=500, height=400)
exit_program = False


def get_user_bet():
    bet = ""
    title_text = "Make your bet."
    prompt_text = ("Which turtle will win the race? Enter a Color: "
                   "['green', 'blue', 'orange', 'purple', 'red', 'grey']")
    while bet.lower() not in TURTLES_COLORS:
        bet = turtle_screen.textinput(title_text, prompt_text)
        if bet not in TURTLES_COLORS:
            prompt_text = ("ERROR: Invalid Color, try again.\n"
                           "Which turtle will win the race? Enter a Color: \n"
                           "['green', 'blue', 'orange', 'purple', 'red', 'grey']")
    return bet.lower()


def set_up_turtles():
    turtles_list = []
    start_position_x = -225
    start_position_y = -125
    for color in TURTLES_COLORS:
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.setposition(start_position_x, start_position_y)
        start_position_y += 50
        turtles_list.append(new_turtle)
    return turtles_list


def turtle_race():
    user_bet = get_user_bet()
    turtles = set_up_turtles()
    winner_position = 200
    winner_turtle = ""
    while winner_turtle not in TURTLES_COLORS:
        for turtle_index in range(len(turtles)):
            turtles[turtle_index].forward(random.randint(5, 15))
            if turtles[turtle_index].xcor() > winner_position:
                winner_turtle = TURTLES_COLORS[turtle_index]
                winner_position = turtles[turtle_index].xcor()

    if user_bet == winner_turtle:
        print("Congratulations!\n"
              f"{winner_turtle.title()} turtle WON the race!")
    else:
        print("Sorry!\n"
              f"{winner_turtle.title()} turtle WON the race!\n"
              "Better luck next time.")


turtle_race()
turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
