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

NUM_DOTS = 100
DOT_SIZE = 15
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
turtle_cursor.penup()
turtle_cursor.hideturtle()
turtle_cursor.speed("fastest")

backwards_movement = 5 * H_DISTANCE_BETWEEN_CIRCLES
down_movement = 5 * V_DISTANCE_BETWEEN_CIRCLES
backwards_movement -= (0.5 * H_DISTANCE_BETWEEN_CIRCLES)
down_movement -= (0.5 * V_DISTANCE_BETWEEN_CIRCLES)

turtle_cursor.setheading(180)
turtle_cursor.forward(backwards_movement)
turtle_cursor.setheading(270)
turtle_cursor.forward(down_movement)
turtle_cursor.setheading(0)

for dot_count in range(1, NUM_DOTS+1):
    turtle_cursor.dot(DOT_SIZE, random.choice(rgb_colors))
    turtle_cursor.forward(H_DISTANCE_BETWEEN_CIRCLES)
    if dot_count % 10 == 0:
        turtle_cursor.setheading(90)
        turtle_cursor.forward(V_DISTANCE_BETWEEN_CIRCLES)
        turtle_cursor.setheading(180)
        turtle_cursor.forward(H_DISTANCE_BETWEEN_CIRCLES*10)
        turtle_cursor.setheading(0)

turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
