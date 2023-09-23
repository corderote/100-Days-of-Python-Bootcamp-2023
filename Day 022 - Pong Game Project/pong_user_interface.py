# -----------------------------------------------------------------------------
import turtle

ALIGNMENT = "center"
FONT = ('Arial', 15, 'bold')


class UserInterface(turtle.Turtle):

    def __init__(self, screen_width=0, screen_height=0):
        super().__init__()
        self.score_player_1 = 0
        self.score_player_2 = 0
        self.screen_size = (screen_width, screen_height)
        self.create()

    def create(self):
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def increase_score(self, player_number):
        if player_number == 1:
            self.score_player_1 += 1
        elif player_number == 2:
            self.score_player_2 += 1

    def update(self):
        self.clear()
        self.goto(-self.screen_size[0]/4, self.screen_size[1]/2 - 60)
        self.write(f"{self.score_player_1}", False, ALIGNMENT, FONT)
        self.goto(self.screen_size[0]/4, self.screen_size[1]/2 - 60)
        self.write(f"{self.score_player_2}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def draw_ui(self):
        cursor = turtle.Turtle("square")
        cursor.hideturtle()
        cursor.color("white")
        cursor.penup()
        cursor.shapesize(1.5, 0.25)
        for y_value in range(0, self.screen_size[1], 50):
            cursor.goto(0, y_value)
            cursor.stamp()
            cursor.goto(0, -y_value)
            cursor.stamp()

        cursor.goto(-self.screen_size[0]/4, self.screen_size[1]/2 - 30)
        cursor.pendown()
        cursor.write(f"PLAYER 1", False, ALIGNMENT, FONT)
        cursor.penup()
        cursor.goto(self.screen_size[0]/4, self.screen_size[1]/2 - 30)
        cursor.pendown()
        cursor.write(f"PLAYER 2", False, ALIGNMENT, FONT)
        cursor.penup()

# -----------------------------------------------------------------------------
