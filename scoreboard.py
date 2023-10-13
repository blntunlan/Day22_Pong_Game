from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(x=250, y=250)
        self.write(arg=f"{self.score1}", align="center", font=('Arial', 15, 'normal'))
        self.goto(x=-250, y=250)
        self.write(arg=f"{self.score2}", align="center", font=('Arial', 15, 'normal'))
        self.middle_draw()

    def player1_score(self):
        self.score2 += 1
        self.update_score()

    def player2_score(self):
        self.score1 += 1
        self.update_score()

    def middle_draw(self):
        self.goto(x=0, y=-300)
        self.down()
        self.goto(x=0, y=300)
        self.up()
