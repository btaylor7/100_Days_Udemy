from turtle import Turtle



class Message(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,0)



    def print_update(self, side):
        self.clear()  # Clear any previous messages
        self.write(f"{side} player gets a point!", align="center", font=("Courier", 20, "normal"))
        self.screen.update()
        self.screen.ontimer(self.clear, 1000)

    def print_winner(self,side):
        self.clear()
        self.write(f"{side} is the winner!!", align="center", font=("Courier", 20, "normal"))