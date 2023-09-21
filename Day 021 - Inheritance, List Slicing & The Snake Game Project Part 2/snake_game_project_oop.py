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
import scoreboard

SCREEN_SIZE = (600, 600)
# Limits for the North, South, East & West Collisions.
SNAKE_BOUNDS = {
    "NORTH": 300 - snake.SNAKE_SIZE,
    "SOUTH": -300 + snake.SNAKE_SIZE,
    "EAST": 300 - snake.SNAKE_SIZE,
    "WEST": -300 + snake.SNAKE_SIZE,
}


def draw_snake_maze():
    cursor = turtle.Turtle()
    cursor.color("red")
    cursor.penup()
    cursor.goto(SNAKE_BOUNDS["EAST"], SNAKE_BOUNDS["NORTH"])
    cursor.pendown()
    cursor.goto(SNAKE_BOUNDS["EAST"], SNAKE_BOUNDS["SOUTH"])
    cursor.goto(SNAKE_BOUNDS["WEST"], SNAKE_BOUNDS["SOUTH"])
    cursor.goto(SNAKE_BOUNDS["WEST"], SNAKE_BOUNDS["NORTH"])
    cursor.goto(SNAKE_BOUNDS["EAST"], SNAKE_BOUNDS["NORTH"])
    cursor.hideturtle()


# Step One.
turtle.colormode(255)
turtle_screen = turtle.Screen()
turtle_screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
turtle_screen.bgcolor("black")
turtle_screen.title("Snake")
turtle_screen.tracer(0)

draw_snake_maze()

bound_value_x = SCREEN_SIZE[0] - snake.SNAKE_SIZE
bound_value_y = SCREEN_SIZE[1] - snake.SNAKE_SIZE

user_snake = snake.Snake()
user_score = scoreboard.Scoreboard(0, SNAKE_BOUNDS["NORTH"])
snake_food = food.Food()
snake_food.relocate(bound_value_x, bound_value_y, user_snake.segments)

turtle_screen.update()

turtle_screen.listen()
turtle_screen.onkeypress(key="Up", fun=user_snake.up)
turtle_screen.onkeypress(key="Down", fun=user_snake.down)
turtle_screen.onkeypress(key="Right", fun=user_snake.right)
turtle_screen.onkeypress(key="Left", fun=user_snake.left)


while (user_snake.is_in_bounds(bound_value_x, bound_value_y)
       and user_snake.self_collision()):
    time.sleep(0.1)
    user_snake.move()
    turtle_screen.update()
    if user_snake.head.distance(snake_food) < 5:
        user_snake.extend()
        snake_food.relocate(bound_value_x, bound_value_y, user_snake.segments)
        user_score.increases_score()
        user_score.update()


user_score.game_over()

turtle_screen.exitonclick()
