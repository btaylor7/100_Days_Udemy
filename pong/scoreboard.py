from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.score_1 = 0
        self.score_2 = 0

        self.update_board()

    def update_board(self):
        # Write Score 1
        self.goto(-250, 190)  # Position near the top-left
        self.write(self.score_1, align="left", font=("Courier", 80, "normal"))

        # Write Score 2
        self.goto(250, 190)  # Position near the top-right
        self.write(self.score_2, align="right", font=("Courier", 80, "normal"))

    def increase_right_score(self):
        self.score_1 += 1
        self.clear()
        self.update_board()

    def increase_left_score(self):
        self.score_2 += 1
        self.clear()
        self.update_board()

