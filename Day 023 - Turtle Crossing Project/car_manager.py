import random
import turtle

COLORS = ["red", "orange", "yellow", "grey", "blue", "purple"]
INITIAL_SPEED = 5
SPEED_INCREMENT = 5
MAX_NUM_OF_CARS = 50


class Car(turtle.Turtle):
    def __init__(self, screen_w):
        super().__init__("square")
        self.move_speed = INITIAL_SPEED
        self.is_moving = False
        self.limit_x = screen_w/2 + 50
        self.create()

    def create(self):
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(1, 2)
        self.setposition(self.limit_x, 0)
        self.setheading(180)

    def move(self):
        self.penup()
        self.forward(self.move_speed)

    def start(self):
        self.is_moving = True

    def stop(self):
        self.is_moving = False


class CarManager:

    def __init__(self, screen_width):
        self.num_moving_cars = 0
        self.cars = []
        for _ in range(MAX_NUM_OF_CARS):
            new_car = Car(screen_width)
            self.cars.append(new_car)
        self.set_cars()

    def update(self):
        for car in self.cars:
            if car.is_moving:
                car.move()
            if car.xcor() < -car.limit_x:
                car.setposition(car.limit_x, car.ycor())

    def set_cars(self):
        for car in self.cars:
            new_pos_y = random.randint(-9, 9) * 25
            new_pos_x = random.randint(0, 13) * 50
            car.setposition(new_pos_x, new_pos_y)
            car.is_moving = True

    def end(self):
        for car in self.cars:
            car.setposition(car.limit_x, 0)
            car.is_moving = False

    def speed_up(self):
        for car in self.cars:
            car.move_speed += SPEED_INCREMENT
