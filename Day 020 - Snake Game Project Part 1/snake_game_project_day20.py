# ----------------------------------------------------------------------------- #
# Snake Project:
# Breaking the problem in different steps:
# 1 > Create our snake body. Create a number of squares that are grouped
#     together.
# 2 > Move the snake. Always forwards.
# 3 > Control the snake.
# 4 > Spawn the food and check collision.
# 5 > Create a scoreboard drawing text on our screen.
# 6 > Detect collisions with walls or yourself.

import turtle
import time

SNAKE_COLOR = (125, 125, 125)
SNAKE_INITIAL_SIZE = 3

# Step One.
turtle.colormode(255)
turtle_screen = turtle.Screen()
turtle_screen.setup(width=600, height=600)
turtle_screen.bgcolor("black")
turtle_screen.title("Snake")
turtle_screen.tracer(0)


def init_snake():
    segments = []
    snake_pos_x = 0
    snake_pos_y = 0
    for _ in range(SNAKE_INITIAL_SIZE):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.setposition(snake_pos_x, snake_pos_y)
        segments.append(new_segment)
        snake_pos_x -= 20
    return segments


def move_snake(snake):
    for index in range(len(snake)-1, 0, -1):
        new_pos_x = snake[index-1].xcor()
        new_pos_y = snake[index-1].ycor()
        snake[index].setposition(new_pos_x, new_pos_y)
    snake[0].forward(20)


snake_segments = init_snake()
turtle_screen.update()

while snake_segments[0].xcor() < 300:
    time.sleep(0.2)
    move_snake(snake_segments)
    turtle_screen.update()

turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
