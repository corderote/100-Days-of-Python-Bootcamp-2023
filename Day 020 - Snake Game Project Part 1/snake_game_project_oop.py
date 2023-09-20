# ----------------------------------------------------------------------------- #
# Snake Project:
# ----------------------------------------------------------------------------- #
# Breaking the problem in different steps:
# 1 > Create our snake body. Create a number of squares that are grouped
#     together.
# 2 > Move the snake. Always forwards.
# 3 > Control the snake.
# 4 > Spawn the food and check collision.
# 5 > Create a scoreboard drawing text on our screen.
# 6 > Detect collisions with walls or yourself.
# ----------------------------------------------------------------------------- #

import turtle
import time
import snake

SCREEN_SIZE = (600, 600)
WALL_SIZE = (50, 50)


def draw_snake_maze():
    cursor = turtle.Turtle()
    cursor.color("red")
    cursor.penup()
    pos_x = (SCREEN_SIZE[0] - WALL_SIZE[0])/2
    pos_y = (SCREEN_SIZE[1] - WALL_SIZE[1])/2
    cursor.goto(pos_x, pos_y)
    cursor.pendown()
    cursor.goto(pos_x, -pos_y)
    cursor.goto(-pos_x, -pos_y)
    cursor.goto(-pos_x, pos_y)
    cursor.goto(pos_x, pos_y)
    cursor.hideturtle()


# Step One.
turtle.colormode(255)
turtle_screen = turtle.Screen()
turtle_screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
turtle_screen.bgcolor("black")
turtle_screen.title("Snake")
turtle_screen.tracer(0)

draw_snake_maze()

user_snake = snake.Snake()
turtle_screen.update()

turtle_screen.listen()
turtle_screen.onkeypress(key="Up", fun=user_snake.up)
turtle_screen.onkeypress(key="Down", fun=user_snake.down)
turtle_screen.onkeypress(key="Right", fun=user_snake.right)
turtle_screen.onkeypress(key="Left", fun=user_snake.left)

bound_value_x = SCREEN_SIZE[0] - WALL_SIZE[0]
bound_value_y = SCREEN_SIZE[1] - WALL_SIZE[1]

while user_snake.is_in_bounds(bound_value_x, bound_value_y):
    time.sleep(0.1)
    user_snake.move()
    turtle_screen.update()

turtle_screen.exitonclick()
# ----------------------------------------------------------------------------- #
