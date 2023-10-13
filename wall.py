from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=40)
        self.penup()

    def wall_up(self):
        self.goto(x=0, y=300)

    def wall_down(self):
        self.goto(x=0, y=-290)
