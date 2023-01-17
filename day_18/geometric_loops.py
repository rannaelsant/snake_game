from turtle import Turtle, Screen
import random as rd


random_turtle = Turtle()
random_turtle.shape("turtle")
random_turtle.color("green")

colours = ["Green", "Red", "Blue", "Black"]
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        random_turtle.forward(100)
        random_turtle.right(angle)

for shape_side_number in range(3, 10):
    random_turtle.color(rd.choice(colours))
    draw_shape(shape_side_number)

screen = Screen()
screen.exitonclick()