import turtle as t
import random as rd

random_turtle = t.Turtle()
random_turtle.shape("turtle")
random_turtle.color("green")
random_turtle.pensize(5)
t.colormode(255)


# Generator of random color
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    random_color = (r, g, b)
    return random_color
1

colours = ["Green", "Red", "Blue", "Black"]
directions = [0, 90, 180, 270]

for _ in range(300):
    random_turtle.color(random_color())
    random_turtle.forward(30)
    random_turtle.setheading(rd.choice(directions))

screen = Screen()
screen.exitonclick()