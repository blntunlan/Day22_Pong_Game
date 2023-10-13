from turtle import Screen
from paddle import Paddle  # Use a consistent naming style for imports
from ball import Bally
from wall import Wall
from scoreboard import ScoreBoard


def main():
    # Create the screen
    screen = Screen()
    screen.title("PONG GAME")
    screen.bgcolor("black")
    screen.setup(width=800, height=600)  # Use named arguments for clarity
    screen.tracer(0)

    # Create paddle instances
    player_1_paddle = Paddle()  # Use descriptive variable names
    player_1_paddle.set_player_1_position()
    player_2_paddle = Paddle()
    player_2_paddle.set_player_2_position()

    ball = Bally()

    wall_up = Wall()
    wall_up.wall_up()
    wall_down = Wall()
    wall_down.wall_down()

    scoreboard = ScoreBoard()

    # Listen for key events and assign control keys
    screen.listen()
    screen.onkeypress(player_2_paddle.move_up, "w")
    screen.onkeypress(player_2_paddle.move_down, "s")
    screen.onkeypress(player_1_paddle.move_up, "Up")
    screen.onkeypress(player_1_paddle.move_down, "Down")

    # Run the game loop
    is_game = True

    while is_game:
        screen.update()
        ball.move()
        ball.bounce()
        ball.ball_detect()

        if ball.xcor() > 390:
            scoreboard.player1_score()
            ball.reset_position()


        if ball.xcor() < -390:
            scoreboard.player2_score()
            ball.reset_position()


        if ball.distance(player_2_paddle) < 40 and ball.xcor() < -340 or ball.distance(
                player_1_paddle) < 40 and ball.xcor() > 340:
            ball.paddle_bounce()



if __name__ == "__main__":
    main()
