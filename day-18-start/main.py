import turtle
import random

tim = turtle.Turtle()
tim.shape("turtle")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# Challenge 1:
# for number in range(4):
#     tim.forward(100)
#     tim.right(90)

# Challenge 2
# for number in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()

# Challenge 3:
# num_of_sides = 3
# while num_of_sides < 11:
#     tim.color(random.choice(colors))
#     angle = 360 / num_of_sides
#     for number in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)
#     num_of_sides += 1

# Challenge 4
# tim.pensize(10)
# for number in range(500):
#     tim.color(random_color())
#     directions = [0, 90, 180, 270]
#     tim.setheading(random.choice(directions))
#     tim.forward(20)

# Challenge 5:
tim.speed("fastest")
for number in range(100):
    tim.color(random_color())
    tim.circle(100)
    tim.left(3.6)

screen = turtle.Screen()
screen.exitonclick()
