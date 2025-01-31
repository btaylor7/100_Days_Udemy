import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
player = Player()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

scoreboard = Scoreboard()

counter = 0
global_speed = 1.0
cars = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    counter += 1
    if counter % 6 == 0:
        new_car = CarManager()
        new_car.set_speed(global_speed)
        cars.append(new_car)

    for car in cars:
        car.move_car()
        if player.distance(car) < 20:
            scoreboard.game_over()
            screen.update()
            time.sleep(2)
            game_is_on = False

    player_reset = player.reset_position()
    if player_reset:
        scoreboard.level +=1
        scoreboard.update_scoreboard()
        global_speed += 0.25
        for car in cars:
            car.set_speed(global_speed)





