from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_change = 10
        self.y_change = 10

    def move(self):
        self.goto(self.xcor() + self.x_change, self.ycor() + self.y_change)

    def bounce_y(self):
        self.y_change *= -1

    def bounce_x(self):
        self.x_change *= -1

    def miss(self):
        self.goto(0, 0)
        self.x_change *= -1
