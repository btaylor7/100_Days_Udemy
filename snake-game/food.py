from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")

        random_x = randint(-300, 300)
        random_y = randint(-300, 300)
        self.goto(random_x, random_y)


    def refresh(self):
        random_x = randint(-300, 300)
        random_y = randint(-300, 300)
        self.goto(random_x, random_y)