# -----------------------------------------------------------------------------
import turtle
import random
from snake import SNAKE_SIZE

FOOD_COLOR = (125, 125, 255)


class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.shape("circle")
        self.penup()
        self.color(FOOD_COLOR)
        self.shapesize(0.5, 0.5)

    def relocate(self, limit_x, limit_y, items=None):
        if items is None:
            items = []
        offset = (-1) ** random.randint(1, 2)
        new_pos_x = (limit_x / 2) - SNAKE_SIZE
        new_pos_y = (limit_y / 2) - SNAKE_SIZE
        new_pos_x = random.randint(0, int(new_pos_x/SNAKE_SIZE))
        new_pos_y = random.randint(0, int(new_pos_y/SNAKE_SIZE))
        new_pos_x = (new_pos_x * SNAKE_SIZE)*offset
        new_pos_y = (new_pos_y * SNAKE_SIZE)*offset
        self.goto(new_pos_x, new_pos_y)
        for item in items:
            if self.distance(item) < 5:
                self.relocate(limit_x, limit_y, items)
