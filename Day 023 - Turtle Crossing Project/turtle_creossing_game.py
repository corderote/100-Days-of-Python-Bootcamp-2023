import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

turtle.colormode(255)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_manager = CarManager(screen.window_width())

user_turtle = Player()
user_score = Scoreboard(screen.window_width(), screen.window_height())

screen.listen()
screen.onkey(user_turtle.move, "Up")
# screen.onkey(user_turtle.down, "Down")

game_is_on = True
while game_is_on:
    car_manager.update()
    # Turtle reaches finish line.
    if user_turtle.ycor() >= screen.window_height()/2:
        user_turtle.reset()
        user_score.increase_score()
        car_manager.speed_up()
    # Turtle - Cars Collision.
    for car in car_manager.cars:
        horizontal_distance = user_turtle.xcor() - car.xcor()
        vertical_distance = user_turtle.ycor() - car.ycor()
        if -15 < vertical_distance < 15 and -20 < horizontal_distance < 20:
            game_is_on = False

    time.sleep(0.1)
    screen.update()

car_manager.end()
user_score.game_over()
screen.update()

screen.exitonclick()
