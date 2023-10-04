from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, start_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(start_pos)
        self.left(90)
        self.shapesize(1, 5, 0)

    def move_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
