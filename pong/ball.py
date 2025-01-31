from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("orange")
        self.shape("circle")

        self.x_move = 10
        self.y_move = 10

        self.penup()
        self.goto(0,0)

    def move(self):
        self.setx(self.xcor() + self.x_move)
        self.sety(self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()