import turtle
import pandas

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"

game_is_on = True

game_screen = turtle.Screen()
game_screen.title("U.S. States Game")
image_path = "blank_states_img.gif"
game_screen.addshape(image_path)
game_screen.setup(width=725, height=550)

turtle.shape(image_path)
s_title = "Guess the State"
s_prompt = "What is another state's name?"

states_data = pandas.read_csv("50_states.csv")
# We could addd the .to_list() method to work with states_list as a list
# But we are going to work with the panda's version to know it better.
states_list = states_data.state

game_cursor = turtle.Turtle()
game_cursor.penup()
game_cursor.color("black")
game_cursor.hideturtle()

user_states = []
user_score = 0

while game_is_on:
    user_input = game_screen.textinput(title=s_title, prompt=s_prompt)
    if user_input is not None:
        user_input = user_input.title()
        if states_data[states_data.state == user_input].empty:
            print("USER ERROR.")
        else:
            if user_input not in user_states:
                map_x = int(states_data[states_data.state == user_input].x)
                map_y = int(states_data[states_data.state == user_input].y)
                game_cursor.goto(map_x, map_y)
                game_cursor.write(user_input, False, ALIGNMENT, FONT)
                user_score += 1
                user_states.append(user_input)
                s_title = f"{user_score}/50 States Correct"
                if user_score == 50:
                    game_is_on = False

    else:
        game_is_on = False

if user_score == 50:
    game_screen.exitonclick()
else:
    for state in user_states:
        states_data.drop(axis="index", labels=states_data[states_data.state == state].index)
    # Convert the states we did not guessed into a csv file to learn them.
    # states_data.state.to_csv("states_to_learn.csv")


# The following code allows us to check what are the coordinates our
# mouse clicks on the turtle screen.

# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)

# We do not use this anymore as we already have the coordinates for
# each state in the .csv file.

# game_screen.exitonclick()
# turtle.mainloop() keeps the screen working to allow user inputs.
# turtle.mainloop()
