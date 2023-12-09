import turtle
from turtle import Turtle, Screen
import random
import colorgram

rgb_colors = []
colors = colorgram.extract('books.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")
timmy_the_turtle.hideturtle()

def hirst_diagram(height, width, dot_size):
    timmy_the_turtle.up()
    timmy_the_turtle.setpos(-width/2 + dot_size / 2, height/2 - dot_size / 2)
    for index in range(1, int(height / (dot_size + 10)) + 1):
        for _ in range(int(width/(dot_size + 10))):
            timmy_the_turtle.down()
            timmy_the_turtle.dot(dot_size, random.choice(rgb_colors))
            timmy_the_turtle.up()
            timmy_the_turtle.forward(dot_size + 10)
        timmy_the_turtle.setpos(-width / 2 + dot_size / 2, height/2 - index * (dot_size + 10) - dot_size / 2)

screen = Screen()

hirst_diagram(screen.window_height(), screen.window_width(), 30)

screen.exitonclick()

