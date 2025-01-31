#import colorgram
from turtle import Turtle, Screen, colormode
from random import choice
# colours = colorgram.extract('wallpaper-colours.jpg', 10)
#
# rgb_colours = []
# for colour in colours:
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     rgb_colours.append((r, g, b))

colour_palette = [(4, 19, 42), (215, 1, 0), (160, 160, 159), (237, 237, 236), (108, 104, 104), (201, 4, 10), (23, 103, 191), (0, 254, 254), (60, 9, 22), (0, 190, 249)]

timmy = Turtle()
screen = Screen()
colormode(255)
screen.bgcolor(10,10,10)
timmy.speed("fastest")

last_colour = None
for row in range(10):
    timmy.penup()
    timmy.goto(-600, 300 - (row * 150))
    timmy.pendown()
    for col in range(10):
        current_colour = choice(colour_palette)
        while current_colour == last_colour:
            current_colour = choice(colour_palette)
        timmy.pencolor(current_colour)
        timmy.fillcolor(current_colour)
        timmy.begin_fill()

        timmy.circle(50)
        timmy.end_fill()

        timmy.penup()
        timmy.forward(125)
        timmy.pendown()

        last_colour = current_colour

timmy.hideturtle()
screen.exitonclick()



