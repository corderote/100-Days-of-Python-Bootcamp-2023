# -----------------------------------------------------------------------------
import turtle

SNAKE_COLOR = (125, 125, 125)
SNAKE_SEGMENTS = 3
SNAKE_SIZE = 20
SNAKE_INITIAL_POSITION = (0, 0)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        snake_pos_x = SNAKE_INITIAL_POSITION[0]
        snake_pos_y = SNAKE_INITIAL_POSITION[1]
        for _ in range(SNAKE_SEGMENTS):
            self.add_segment((snake_pos_x, snake_pos_y))
            snake_pos_x -= 20

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_pos_x = self.segments[index - 1].xcor()
            new_pos_y = self.segments[index - 1].ycor()
            self.segments[index].setposition(new_pos_x, new_pos_y)
        self.head.forward(20)

    def add_segment(self, position):
        new_segment = turtle.Turtle("square")
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def is_in_bounds(self, screen_width, screen_height):
        limit_x = (screen_width/2) - SNAKE_SIZE
        limit_y = (screen_height/2) - SNAKE_SIZE
        if self.head.xcor() >= limit_x or -limit_x >= self.head.xcor():
            return False
        elif self.head.ycor() >= limit_y or -limit_y >= self.head.ycor():
            return False
        else:
            return True

    def self_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 5:
                return False
        return True
