# ----------------------------------------------------------------------------- #
import turtle

turtle_cursor = turtle.Turtle()
turtle_screen = turtle.Screen()


def move_forward():
    turtle_cursor.forward(10)


def move_backwards():
    turtle_cursor.backward(10)


def rotate_right():
    turtle_cursor.right(10)
    # turtle_cursor.setheading(turtle_cursor.heading() - 10)


def rotate_left():
    turtle_cursor.left(10)
    # turtle_cursor.setheading(turtle_cursor.heading() + 10)


def clear_screen():
    turtle_cursor.reset()
    # turtle_cursor.home()
    # turtle_cursor.clear()


turtle_screen.listen()
turtle_screen.onkeypress(key="Up", fun=move_forward)
turtle_screen.onkey(key="w", fun=move_forward)
turtle_screen.onkeypress(key="Down", fun=move_backwards)
turtle_screen.onkey(key="s", fun=move_backwards)
turtle_screen.onkeypress(key="Right", fun=rotate_right)
turtle_screen.onkey(key="d", fun=rotate_right)
turtle_screen.onkeypress(key="Left", fun=rotate_left)
turtle_screen.onkey(key="a", fun=rotate_left)

turtle_screen.onkey(key="c", fun=clear_screen)

turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
