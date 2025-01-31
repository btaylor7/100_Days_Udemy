from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_board()

    def update_board(self):
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))

    def update_score(self):
            self.score += 1
            self.clear()
            self.update_board()