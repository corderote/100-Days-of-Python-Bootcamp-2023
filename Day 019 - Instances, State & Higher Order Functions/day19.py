# ----------------------------------------------------------------------------- #
# Event Listeners:
# Is the way we use to let the user interact with our programs. With this the
# user will trigger events that we program for him inside our code.

# With turtle graphics to allow this we need to call the 'listen()' function
# from our screen.
import turtle

turtle_cursor = turtle.Turtle()
turtle_screen = turtle.Screen()


def move_forward():
    turtle_cursor.forward(50)


turtle_screen.listen()
turtle_screen.onkey(key="space", fun=move_forward)

turtle_screen.exitonclick()

# ----------------------------------------------------------------------------- #
# Higher order functions are functions that can work with other functions
# inside them in our case, 'onkey()' is a higher order function as it can work
# with the functions that we create.

# ----------------------------------------------------------------------------- #
# Instances & States:
# When we create objects from a class, we can create multiple of them from the
# same class, each one of them is going to have its own behaviour, and we call
# this objects INSTANCES. Both are examples of the same object from the same
# class, but they can have different attributes and can be doing different
# things. This differences in attributes are known as STATES.
# ----------------------------------------------------------------------------- #
