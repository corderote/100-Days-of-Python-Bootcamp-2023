# ----------------------------------------------------------------------------- #
# Turtle Graphics
# Turtle graphics is a Graphic User Interface (GUI) module that comes with of
# the python installations. Turtle allows us to draw graphics on our screen.
# For more information on the turtle module you can read the API at:
# https://docs.python.org/3/library/turtle.html
import random
import turtle

turtle_cursor = turtle.Turtle()
turtle_screen = turtle.Screen()

# ----------------------------------------------------------------------------- #
# Turtle Challenge Number 1:
# Draw a Square using TurtleGraphics.

for _ in range(4):
    turtle_cursor.forward(100)
    turtle_cursor.right(90)

turtle_cursor.reset()

# ----------------------------------------------------------------------------- #
# Turtle Challenge Number 2:
# Draw a Dashed Line.

turtle_cursor.pencolor("red")
turtle_pen_position = "down"
for _ in range(30):
    turtle_cursor.forward(10)
    if turtle_pen_position == "up":
        turtle_pen_position = "down"
        turtle_cursor.pendown()
    elif turtle_pen_position == "down":
        turtle_pen_position = "up"
        turtle_cursor.penup()

turtle_cursor.reset()


# ----------------------------------------------------------------------------- #
# Turtle Challenge Number 3:
# Draw different shapes, starting form a triangle and ending on a decagon.
# All shapes have to be visible and start on the same point, and the color of
# each shape has to be randomized.


def calculate_angle_rotation(number_of_sides):
    angle_value = 360 / number_of_sides
    return angle_value


def get_random_color():
    random_red = random.randint(0, 255)
    random_green = random.randint(0, 255)
    random_blue = random.randint(0, 255)
    rgb = (random_red, random_green, random_blue)
    return rgb


def draw_shape(num_sides):
    turn_angle = calculate_angle_rotation(num_sides)
    for _ in range(num_sides):
        turtle_cursor.forward(100)
        turtle_cursor.right(turn_angle)


turtle.colormode(255)

for shape_sides in range(3, 11):
    turtle_cursor.pencolor(get_random_color())
    draw_shape(shape_sides)

turtle_cursor.reset()

# ----------------------------------------------------------------------------- #
# Turtle Challenge Number 4:
# Draw a random walk. Make the turtle go north, south, east or west, and move
# a specific distance, change the color every time you move the turtle and add
# some thickness to the line.


def get_random_direction(number_of_options):
    rotation_angle = calculate_angle_rotation(number_of_options)
    rotation_times = random.randint(0, 3)
    total_cursor_rotation = rotation_angle*rotation_times
    return total_cursor_rotation


turtle_cursor.pensize(10)
turtle_cursor.speed(0)

for _ in range(100):
    turtle_cursor.pencolor(get_random_color())
    turtle_cursor.right(get_random_direction(4))
    turtle_cursor.forward(25)

turtle_cursor.reset()

# ----------------------------------------------------------------------------- #
# Turtle Challenge Number 5:
# Make a spirograph. Use the turtle graphics library to draw multiple circles
# and tilting the circle direction a bit every time.

circle_draw_times = 50
cursor_angle_rotation = calculate_angle_rotation(circle_draw_times)

for _ in range(circle_draw_times):
    turtle_cursor.pencolor(get_random_color())
    turtle_cursor.speed(0)
    turtle_cursor.circle(100)
    turtle_cursor.setheading(turtle_cursor.heading() + cursor_angle_rotation)

turtle_screen.exitonclick()

# ----------------------------------------------------------------------------- #
# Importing Modules:
# We have already seen the simple import, using the keyword 'import' and adding
# the name of the document or module we want to add to our project. And we have
# also used the 'from ...  import ...' mode, that allows us to not have to use
# the module name every time we need to use an item from the module, but we
# need to add all the classes and methods or variables that we are going to be
# using. Using the asterisk '*' as a value for the import in this method allows
# us to use everything that is in that module as it was on our own document.
# This 'from ...  import *' is not used as it may lead to confusion in our code
# but is good to know that it exists. Try to avoid this kind of import.

# Aliasing modules:
# By using 'import ... as "something"' we give the module another name that we
# can use to refer to it. This comes handy when the modules have long names,
# and you do not want to specify their names everytime you use them.

# Installing modules:
# There will be times when you can not just import a module. That just means
# the module does not belong to the package that you are using right now.
# To fix it you just need to install it, PyCHarm can give you the prompt to
# install the package you are looking for most of the time, other times you
# will need to download it and install it manually or add it to your project
# folder.

# ----------------------------------------------------------------------------- #
# Python Tuples:
# Tuples are like python lists, but these lists do not accept modifications.
# You can not add, take, or modify its components. Once you have created your
# tuple, it will keep its values forever.
# Python lists, but IMMUTABLE.
# ----------------------------------------------------------------------------- #
