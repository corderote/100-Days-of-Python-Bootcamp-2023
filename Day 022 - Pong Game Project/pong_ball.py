import turtle

BALL_COLOR = (200, 200, 200)
BALL_SPEED = 10


class Ball(turtle.Turtle):
    def __init__(self, position=(0, 0)):
        super().__init__()
        self.create(position)
        self.is_moving = False
        self.speed = [BALL_SPEED, BALL_SPEED]
        self.size = 20

    def create(self, pos):
        self.shape("circle")
        self.penup()
        self.color(BALL_COLOR)
        self.setposition(pos)

    def reset(self):
        self.goto(0, 0)
        self.stop()

    def start(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False

    def move(self):
        if self.is_moving:
            new_pos_x = self.xcor() + self.speed[0]
            new_pos_y = self.ycor() + self.speed[1]
            self.setposition(new_pos_x, new_pos_y)

    def bounce(self, index):
        self.speed[index] = -self.speed[index]
