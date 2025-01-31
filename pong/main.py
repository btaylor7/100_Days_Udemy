from turtle import Screen
from message import Message
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("green")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

padawan = Paddle()
padawan.color("red")
padawan.set_up(350,220)

jedi = Paddle()
jedi.color("blue")
jedi.set_up(-350,0)

ball = Ball()

scoreboard = Scoreboard()

message = Message()

screen.listen()
screen.onkey(padawan.move_up,"Up")
screen.onkey(padawan.move_down,"Down")
screen.onkey(jedi.move_up,"w")
screen.onkey(jedi.move_down,"s")
screen.onkey(jedi.move_up,"W")
screen.onkey(jedi.move_down,"S")

running = True


while running:
    screen.update()
    time.sleep(0.05)

    ball.move()

    #Collision detection with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision detecting with paddles.
    if ball.distance(padawan) < 50 and ball.xcor() > 320 or ball.distance(jedi) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Player miss detection.
    if ball.xcor() > 380:
        scoreboard.increase_right_score()
        message.print_update("Left")
        ball.reset_ball()

    if ball.xcor() < -380:
        scoreboard.increase_left_score()
        message.print_update("Right")
        ball.reset_ball()

    if scoreboard.score_1 >= 10:
        running = False
        message.print_winner("Left")

    if scoreboard.score_2 >=10:
        running = False
        message.print_winner("Right")




screen.exitonclick()