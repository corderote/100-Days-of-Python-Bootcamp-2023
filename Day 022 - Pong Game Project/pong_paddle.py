import turtle

PADDLE_SIZE = 4
PADDLE_COLOR = (125, 125, 125)
PADDLE_SPEED = 20


class Paddle(turtle.Turtle):

    def __init__(self, position=(0, 0)):
        super().__init__()
        self.create(position)
        self.has_limit = False
        self.limit = 0

    def create(self, pos):
        self.shape("square")
        self.penup()
        self.color(PADDLE_COLOR)
        self.shapesize(PADDLE_SIZE, 1)
        self.setposition(pos)

    def set_limit(self, limit_value=None, has_limit=True):
        if limit_value is None:
            self.has_limit = False
        if has_limit is True:
            self.limit = limit_value - PADDLE_SIZE*10
            self.has_limit = has_limit
        else:
            self.limit = 0

    def up(self):
        print(self.limit)
        if self.has_limit is False or self.ycor() < self.limit:
            self.setposition(self.xcor(), self.ycor() + PADDLE_SPEED)

    def down(self):
        if self.has_limit is False or self.ycor() > -self.limit:
            self.setposition(self.xcor(), self.ycor() - PADDLE_SPEED)
