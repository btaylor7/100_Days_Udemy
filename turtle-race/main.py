from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

timmy = Turtle(shape="turtle")
tommy = Turtle(shape="turtle")
tammy = Turtle(shape="turtle")
jimmy = Turtle(shape="turtle")
jonny = Turtle(shape="turtle")
jammy = Turtle(shape="turtle")

all_turtles = [timmy, tommy, tammy, jimmy, jonny, jammy]

timmy.color("red")
tommy.color("blue")
tammy.color("green")
jimmy.color("orange")
jonny.color("purple")
jammy.color("cyan")



def position_turtles():
    timmy.penup()
    timmy.goto(-220, 150)


    tommy.penup()
    tommy.goto(-220, 100)


    tammy.penup()
    tammy.goto(-220, 50)


    jimmy.penup()
    jimmy.goto(-220, 0)


    jonny.penup()
    jonny.goto(-220, -50)

    jammy.penup()
    jammy.goto(-220, -100)




position_turtles()
is_race_on = False
user_bet = screen.textinput("Make your bet","Which turtle will win the race? Enter a colour, case and spelling sensitive! (blue,red,orange,purple,cyan,green): ")
print(user_bet)
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

    turtle_choice = random.choice([timmy, tommy, tammy, jimmy, jonny, jammy])
    turtle_choice.forward(random.randint(0, 10))


#Not the most efficient code, but it works.
screen.exitonclick()