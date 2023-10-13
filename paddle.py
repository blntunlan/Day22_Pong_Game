from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

    def set_player_1_position(self):
        # Set the initial position of player 1's paddle to the right side of the screen
        self.setpos(x=350, y=0)

    def set_player_2_position(self):
        # Set the initial position of player 2's paddle to the left side of the screen
        self.setpos(x=-350, y=0)

    def move_up(self):
        # Move the paddle up by 20 units
        new_y = self.ycor() + 40
        self.sety(new_y)

    def move_down(self):
        # Move the paddle down by 20 units
        new_y = self.ycor() - 40
        self.sety(new_y)
