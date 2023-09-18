# ----------------------------------------------------------------------------- #
# Hirst Painting Project:
# For this project we are going to be working with the colorgram extension.
# Colorgram is A Python module for extracting colors from images.
# More info & download: https://pypi.org/project/colorgram.py
# Installation in cmd Windows:py -m pip install colorgram.py
# Installation in cmd MAC:python3 -m pip install colorgram.py
# PyCharm Windows:
# File > Settings > Project"ProjectName" > PythonInterpreter > "+"button
# module name search & add.
# PyCharm Windows:
# PyCharm > Preferences > Project"ProjectName" > PythonInterpreter > "+"button
# module name search & add.

import colorgram
import random
import turtle

PAINTING_COLUMNS = 10
PAINTING_ROWS = 10
CIRCLE_RADIUS = 15
H_DISTANCE_BETWEEN_CIRCLES = 50
V_DISTANCE_BETWEEN_CIRCLES = 50

# Extract colors from images to our color palette sample.
colors_palette = colorgram.extract("color_palette_1.jpg", 5)
colors_palette += colorgram.extract("color_palette_2.jpg", 5)
colors_palette += colorgram.extract("color_palette_3.jpg", 5)
# Change the colors format to set them as tuples for our GUI.
rgb_colors = []
for color in colors_palette:
    single_color = (color.rgb[0], color.rgb[1], color.rgb[2])
    rgb_colors.append(single_color)

turtle_cursor = turtle.Turtle()
turtle_screen = turtle.Screen()
turtle.colormode(255)
turtle_cursor.speed(0)
start_position_x = ((PAINTING_COLUMNS * H_DISTANCE_BETWEEN_CIRCLES)/2) * -1
start_position_y = ((PAINTING_ROWS * V_DISTANCE_BETWEEN_CIRCLES)/2) * -1
start_position_x += (0.5 * H_DISTANCE_BETWEEN_CIRCLES)
start_position_y += (0.5 * V_DISTANCE_BETWEEN_CIRCLES)

turtle_cursor.penup()
turtle_cursor.setposition(start_position_x, start_position_y)

for rows in range(PAINTING_ROWS):
    for cols in range(PAINTING_COLUMNS):
        turtle_cursor.pendown()
        random_color = random.choice(rgb_colors)
        turtle_cursor.color(random_color)
        turtle_cursor.fillcolor(random_color)
        turtle_cursor.begin_fill()
        turtle_cursor.circle(CIRCLE_RADIUS)
        turtle_cursor.end_fill()
        turtle_cursor.penup()
        turtle_cursor.forward(H_DISTANCE_BETWEEN_CIRCLES)
    vertical_position = start_position_y + V_DISTANCE_BETWEEN_CIRCLES * (rows+1)
    turtle_cursor.setposition(start_position_x, vertical_position)

turtle_cursor.home()
turtle_cursor.hideturtle()

turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
