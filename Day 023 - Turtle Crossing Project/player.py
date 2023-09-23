import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
COLORS = [(25, 255, 25), (120, 255, 90)]


class Player(turtle.Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.create()

    def create(self):
        self.penup()
        self.goto(STARTING_POSITION)
        self.color(COLORS[0])
        self.setheading(90)

    def move(self):
        if self.heading() != 90:
            self.setheading(90)
        else:
            self.forward(MOVE_DISTANCE)

    def down(self):
        if self.heading() != 270:
            self.setheading(270)
        else:
            self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
