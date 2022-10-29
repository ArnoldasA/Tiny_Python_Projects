import random
from turtle import Turtle
from random import Random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.start_speed = -5
        self.increment_speed = -3
        self.all_cars = []

    def spawn_car(self):  # keynotes = first all you needed to do was create a new car turtle variable and then
        # append that to a list rather than a car manager
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=.5, stretch_len=1)
            new_ycor = random.randint(-200, 300)
            color_select = random.choice(COLORS)
            new_car.color(color_select)
            new_car.goto(300, new_ycor)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.start_speed)

    def increase_diff(self):
        self.start_speed += self.increment_speed



