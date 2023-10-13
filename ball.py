from turtle import Turtle


class Bally(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.speed(0)  # Set animation speed to 0 (fastest)
        self.penup()
        self.vx = 0.2  # Initial x velocity
        self.vy = 0.2  # Initial y velocity

    def move(self):
        # Move the ball by its current velocity
        new_x = self.xcor() + self.vx
        new_y = self.ycor() + self.vy
        self.goto(new_x, new_y)

    def bounce(self):
        # Check if the ball has hit a wall
        if self.ycor() > 290 or self.ycor() < -290:
            # Change the ball's y velocity
            self.vy = -self.vy

    def paddle_bounce(self):
        self.vx = -self.vx
        self.vx += 0.03

    def ball_detect(self):
        if self.ycor() > 300 or self.ycor() < -300:
            self.reset_position()
        if self.xcor() > 400 or self.xcor() < -400:
            self.reset_position()

    def reset_position(self):
        self.goto(0, 0)
