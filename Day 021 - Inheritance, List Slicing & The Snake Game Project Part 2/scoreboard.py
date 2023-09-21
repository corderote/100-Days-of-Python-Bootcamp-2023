# -----------------------------------------------------------------------------
import turtle

ALIGNMENT = "center"
FONT = None


class Scoreboard(turtle.Turtle):

    def __init__(self, position_x=0, position_y=0):
        super().__init__()
        self.score = 0
        self.create(position_x, position_y)

    def create(self, pos_x=0, pos_y=0):
        self.hideturtle()
        self.penup()
        self.goto(pos_x, pos_y)
        self.color("white")
        self.update()

    def increases_score(self):
        self.score += 1

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.clear()
        self.write(f"GAME OVER > FINAL SCORE: {self.score}", False,
                   ALIGNMENT, FONT)

# -----------------------------------------------------------------------------
