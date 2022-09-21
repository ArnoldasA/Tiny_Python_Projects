import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
new_turtle = Turtle()
new_turtle.home()
new_turtle.shape("turtle")
new_turtle.color("green")
new_turtle.width(.5)
new_turtle.speed(0)


def random_color():
    r = random.randint(1, 255)
    b = random.randint(1, 255)
    g = random.randint(1, 255)
    rgb = (r, g, b)
    return rgb


def spirograph():
    iterations = 0
    rgb = random_color()
    for iterations in range(30):
        new_turtle.circle(100, 370, )
        new_turtle.color(rgb)
        new_turtle.left(5)


spirograph()
screen = Screen()
screen.exitonclick()
