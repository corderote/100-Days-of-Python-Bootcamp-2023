# -----------------------------------------------------------------------------
# Pong Game Project:
# Breaking the problem in different steps:
# 1 > Set up the Screen.
# 2 > Create and move a paddle.
# 3 > Create the second paddle.
# 4 > Create and move the ball.
# 5 > Ball Collision with the wall and bounce.
# 6 > Ball Collision with the paddle and bounce.
# 7 > Paddle miss and score update.

import time
import turtle
from pong_paddle import Paddle
from pong_paddle import PADDLE_SIZE
from pong_ball import Ball
from pong_user_interface import UserInterface

SCREEN_SIZE = (800, 600)
SCORE_TO_END_GAME = 5

turtle.colormode(255)
# Setup Screen.
pong_screen = turtle.Screen()
pong_screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
pong_screen.bgcolor("black")
pong_screen.title("Pong")
pong_screen.tracer(0)

user_interface = UserInterface(SCREEN_SIZE[0], SCREEN_SIZE[1])
user_interface.draw_ui()

# Set Paddles.
# Left Paddle
user_paddle_1 = Paddle((-(SCREEN_SIZE[0] / 2) + 50, 0))
user_paddle_1.set_limit(SCREEN_SIZE[1] / 2)
# Right Paddle
user_paddle_2 = Paddle(((SCREEN_SIZE[0] / 2) - 50, 0))
user_paddle_2.set_limit(SCREEN_SIZE[1] / 2)

# Set Ball.
ball = Ball()

# Pong Controls.
pong_screen.listen()
pong_screen.onkeypress(key="w", fun=user_paddle_1.up)
pong_screen.onkeypress(key="s", fun=user_paddle_1.down)
pong_screen.onkeypress(key="Up", fun=user_paddle_2.up)
pong_screen.onkeypress(key="Down", fun=user_paddle_2.down)
pong_screen.onkeypress(key="space", fun=ball.start)

end_game = False

pong_screen.update()

while end_game is False:

    ball.move()

    # Detect Collisions:
    # Ball - Wall
    if (ball.ycor() > (SCREEN_SIZE[1] / 2) - ball.size
            or ball.ycor() < (-SCREEN_SIZE[1] / 2) + ball.size):
        ball.bounce(1)

    # Paddles - Ball
    # Left Paddle
    if (ball.xcor() < user_paddle_1.xcor() + 20
            and ball.distance(user_paddle_1) < 10 * PADDLE_SIZE):
        ball.bounce(0)

    # Right Paddle
    if (ball.xcor() > user_paddle_2.xcor() - 20
            and ball.distance(user_paddle_2) < 10 * PADDLE_SIZE):
        ball.bounce(0)

    # Goals and End Game:
    if ball.xcor() > SCREEN_SIZE[0]/2:
        user_interface.increase_score(1)
        ball.reset()
    if ball.xcor() < -SCREEN_SIZE[0]/2:
        user_interface.increase_score(2)
        ball.reset()

    if (user_interface.score_player_1 >= SCORE_TO_END_GAME or
            user_interface.score_player_2 >= SCORE_TO_END_GAME):
        end_game = True

    user_interface.update()
    pong_screen.update()
    time.sleep(0.1)

user_interface.game_over()
pong_screen.exitonclick()
