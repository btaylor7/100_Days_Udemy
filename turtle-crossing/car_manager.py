import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.car_speed = MOVE_INCREMENT

        self.sety(random.randint(-250, 250))
        self.setx(300)

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE)
        if self.xcor() < -300:
            self.hideturtle()
        else:
            self.forward(self.car_speed)

    def set_speed(self, multiplier):
        self.car_speed = 5 * multiplier