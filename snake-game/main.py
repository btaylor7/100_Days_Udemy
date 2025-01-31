from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake!")
screen.tracer(0) #Tracer n refers to number of turtle instructions before updating screen.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

running = True

while running:
    screen.update()
    time.sleep(0.1)

    if snake.segments[0].distance(food) < 15:
        scoreboard.update_score()
        print("Nom!")
        food.refresh()
        snake.extend()

    #Detect collision.
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() >280 or snake.segments[0].ycor() < -280:
        running = False
        scoreboard.clear()
        scoreboard.write("Game over!", align="center", font=("Courier", 24, "normal"))

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            running = False
            scoreboard.clear()
            scoreboard.write("Game over!", align="center", font=("Courier", 24, "normal"))

    snake.move_snake()







screen.exitonclick()