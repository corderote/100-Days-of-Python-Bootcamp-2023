import turtle

FONT = ("Courier", 12, "normal")
ALIGNMENT = "center"


class Scoreboard(turtle.Turtle):

    def __init__(self, screen_width=0, screen_height=0):
        super().__init__()
        self.score = 0
        self.create(screen_width, screen_height)

    def create(self, screen_w, screen_h):
        self.hideturtle()
        self.penup()
        self.goto(- (screen_w/2 - 50), screen_h/2 - 20)
        self.write(f"Level: {self.score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)
