import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

colors = ["red", "yellow", "green", "pink", "purple", "blue", "orange"]
turtles = []
size_of_turtle = 2
step = 5

def move_turtles_to_initial_coordinates():
    counter = 0
    for tim in turtles:
        tim.penup()
        tim.setpos(-screen.window_width()/2 + size_of_turtle, screen.window_height()/2 - 20 - counter*size_of_turtle*15 - counter*screen.window_height()/(len(colors) + 1))
        tim.pendown()
        counter += 1

def setup():
    for _ in range(len(colors)):
        next_turtle = Turtle()
        next_turtle.color(colors[_])
        next_turtle.shape("turtle")
        next_turtle.shapesize(size_of_turtle, size_of_turtle)
        turtles.append(next_turtle)

    move_turtles_to_initial_coordinates()

def start_the_race():

    finish_x_coordinate = screen.window_width()/2 - 20
    global step

    while True:
        current_turtle = random.choice(turtles)
        current_turtle.forward(step)
        if current_turtle.pos()[0] >= finish_x_coordinate:
            return current_turtle.pencolor()


color = screen.textinput("Please, make your guess!", "Enter a turtle's color that should win")

setup()
winner = start_the_race()

if winner == color:
    print("You win!")
else:
    print(f"You loose. The winner is {winner}")

screen.exitonclick()
