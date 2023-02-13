from gettext import install
from turtle import Turtle, Screen, forward
import random
import turtle

ninja = Turtle()
turtle.colormode(255)
#ninja.shape("turtle")
turtle.title("Spiral Art")

def random_color():
    col = random.choices(range(256), k=3)
    ninja.pencolor(col)

def create_colorful_shapes():
    ninja.speed(0)
    for x in range(3,30):
        random_color()
        angle = 360 / x
        for y in range(x):
            ninja.forward(100)
            ninja.right(angle)
        for y in range(x):
            ninja.forward(100)
            ninja.left(angle)

def random_walk():
    angle = 90
    walk_size = 30
    ninja.pensize(10)
    ninja.speed(8)
    for _ in range(200):
        random_color()
        dir = random.choice([0, 90, 180, 270])
        ninja.setheading(dir)
        ninja.forward(walk_size)

def spiral():
    ninja.speed(0)
    for _ in range(360):
        random_color()
        ninja.circle(130)
        ninja.left(1)

# create_colorful_shapes()

# random_walk()

spiral()

    
   


screen = Screen()

screen.exitonclick()