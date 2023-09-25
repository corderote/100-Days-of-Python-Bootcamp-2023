# -----------------------------------------------------------------------------
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
import snake
import food
import user_interface

SCREEN_SIZE = (600, 600)
# Limits for the North, South, East & West Collisions.
SNAKE_BOUNDS = {
    "NORTH": 300 - snake.SNAKE_SIZE,
    "SOUTH": -300 + snake.SNAKE_SIZE,
    "EAST": 300 - snake.SNAKE_SIZE,
    "WEST": -300 + snake.SNAKE_SIZE,
}

game_is_on = True


def turn_off():
    global game_is_on
    game_is_on = False


def snake_start():
    global user_snake
    user_snake.start_moving()
    user_interface.clear_start()


turtle.colormode(255)
turtle_screen = turtle.Screen()
turtle_screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
turtle_screen.bgcolor("black")
turtle_screen.title("Snake")
turtle_screen.tracer(0)

bound_value_x = SCREEN_SIZE[0] - snake.SNAKE_SIZE
bound_value_y = SCREEN_SIZE[1] - snake.SNAKE_SIZE

user_interface.draw_snake_maze(SNAKE_BOUNDS)
user_interface.draw_start()
user_score = user_interface.Scoreboard(0, SNAKE_BOUNDS["NORTH"])

user_snake = snake.Snake()
snake_food = food.Food()
snake_food.relocate(bound_value_x, bound_value_y, user_snake.segments)

turtle_screen.update()

turtle_screen.listen()
turtle_screen.onkeypress(key="Up", fun=user_snake.up)
turtle_screen.onkeypress(key="Down", fun=user_snake.down)
turtle_screen.onkeypress(key="Right", fun=user_snake.right)
turtle_screen.onkeypress(key="Left", fun=user_snake.left)
turtle_screen.onkeypress(key="space", fun=snake_start)
turtle_screen.onkeypress(key="Escape", fun=turn_off)

while game_is_on:
    while (user_snake.is_in_bounds(bound_value_x, bound_value_y)
           and user_snake.self_collision() and game_is_on):
        time.sleep(0.1)
        user_snake.move()
        turtle_screen.update()
        if user_snake.head.distance(snake_food) < 5:
            user_snake.extend()
            snake_food.relocate(bound_value_x, bound_value_y, user_snake.segments)
            user_score.increases_score()
            user_score.update()
    user_snake.reset()
    user_score.reset()
    user_interface.draw_start()
    turtle_screen.update()
