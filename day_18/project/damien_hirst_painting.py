"""import colorgram

rgb_colors = []
colors = colorgram.extract('damien_hirst.jpg', 30)
# Part of program for extract the color off picture.
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)"""
import turtle as module_turtle
import random as rd

module_turtle.colormode(255)
random_turtle = module_turtle.Turtle()
color_list = [(253, 251, 247), (254, 249, 252), (234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188),
              (238, 227, 5), (39, 216, 68), (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14),
              (16, 153, 17), (199, 15, 11), (242, 34, 164), (226, 19, 120), (74, 9, 31), (60, 15, 8), (223, 141, 208),
              (11, 97, 62), (220, 160, 10), (18, 18, 43), (52, 211, 230), (11, 228, 239), (80, 73, 214),
              (238, 156, 217), (73, 212, 168), (81, 234, 202), (61, 233, 241), (5, 67, 42)]
random_turtle.penup()
random_turtle.setheading(225)
random_turtle.forward(300)
random_turtle.setheading(0)
numbers_of_dots = 100


for dot_count in range(1, numbers_of_dots + 1):
    random_turtle.dot(20, rd.choice(color_list))
    random_turtle.forward(50)

    if dot_count % 10 == 0:
        random_turtle.setheading(90)
        random_turtle.forward(50)
        random_turtle.setheading(180)
        random_turtle.forward(500)
        random_turtle.setheading(0)

screen = module_turtle.Screen()
screen.exitonclick()