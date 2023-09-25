# -----------------------------------------------------------------------------
import turtle

ALIGNMENT = "center"
FONT = None

maze = turtle.Turtle()
start = turtle.Turtle()


def draw_snake_maze(screen_bounds):
    global maze
    maze.color("red")
    maze.penup()
    maze.goto(screen_bounds["EAST"], screen_bounds["NORTH"])
    maze.pendown()
    maze.goto(screen_bounds["EAST"], screen_bounds["SOUTH"])
    maze.goto(screen_bounds["WEST"], screen_bounds["SOUTH"])
    maze.goto(screen_bounds["WEST"], screen_bounds["NORTH"])
    maze.goto(screen_bounds["EAST"], screen_bounds["NORTH"])
    maze.hideturtle()


def draw_start():
    global start
    start.color("white")
    start.penup()
    start.goto(0, -50)
    start.write("-- PRESS [ SPACE ] TO START --", False, ALIGNMENT, FONT)
    start.hideturtle()


def clear_start():
    global start
    start.clear()


class Scoreboard(turtle.Turtle):

    def __init__(self, position_x=0, position_y=0):
        super().__init__()
        self.score = 0
        snake_data = open("snake_data.txt", "r")
        self.high_score = int(snake_data.read())
        snake_data.close()
        self.create(position_x, position_y)

    def create(self, pos_x=0, pos_y=0):
        self.hideturtle()
        self.penup()
        self.goto(pos_x, pos_y)
        self.color("white")
        self.update()

    def increases_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}\t\t\t High Score: {self.high_score}",
                   False, ALIGNMENT, FONT)

    def reset(self):
        with open("snake_data.txt", "w") as snake_data:
            snake_data.write(f"{self.high_score}")
        self.score = 0
        self.update()

# -----------------------------------------------------------------------------
