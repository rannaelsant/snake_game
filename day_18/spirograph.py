import turtle as t
import random as rd

random_turtle = t.Turtle()
random_turtle.shape("turtle")
random_turtle.color("green")
random_turtle.pensize(2)
t.colormode(255)


# Generator of random color
def random_color():
    r = rd.randint(0, 255)
    g = rd.randint(0, 255)
    b = rd.randint(0, 255)
    color = (r, g, b)
    return color


for _ in range(100):
    random_turtle.color(random_color())
    random_turtle.circle(80)
    random_turtle.setheading(random_turtle.heading() + 5)
    random_turtle.speed("fast")

screen = t.Screen()
screen.exitonclick()