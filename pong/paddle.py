from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def set_up(self,position_x,position_y):
        self.penup()
        self.goto(position_x,position_y)

    def move_up(self):
        self.sety(self.ycor() + 40)

    def move_down(self):
        self.sety(self.ycor() - 40)
