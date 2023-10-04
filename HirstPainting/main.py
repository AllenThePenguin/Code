# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]

import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.colormode(255)

tim = Turtle()
tim.up()
tim.hideturtle()
tim.setx(-225)
tim.sety(-225)
for number1 in range(10):
    for number2 in range(10):
        tim.color(random.choice(color_list))
        tim.dot(20)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.back(500)


my_screen.exitonclick()
