import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
finish_line = 280
num_cars = 1
screen.tracer(0)
scoreboard = Scoreboard()
car_manager = CarManager()
player = Player()

screen.onkey(player.move_up, "w")

screen.listen()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.spawn_car()
    car_manager.move_car()

    if player.ycor() > finish_line:
        player.finish_line()
        scoreboard.update_score()
        car_manager.increase_diff()

    for car in car_manager.all_cars:
        if player.distance(car) < 10:
            scoreboard.game_over()
            player.finish_line()

    screen.update()
