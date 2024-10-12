import turtle as t
from Board import Board
from Paddle import Paddle
from Ball import Ball
from Bricks import BrickManager


def setup(board: Board) -> Board:
    txt_writer = t.Turtle()
    txt_writer.hideturtle()
    txt_writer.penup()
    txt_writer.goto(board.left_edge, board.bottom)
    txt_writer.pendown()
    txt_writer.write("Press q to quit")
    return board


def setup_paddle_control(paddle: Paddle):
    game_board.screen.onkey(fun=paddle.move_right, key="l")
    game_board.screen.onkey(fun=paddle.move_left, key="h")


game_board = setup(Board())
player = Paddle(start_x=0, start_y=game_board.bottom, board=game_board)
setup_paddle_control(player)
ball = Ball()
brick_manager = BrickManager()
brick_manager.build_bricks(n=1, board=game_board)
game_being_played: bool = True
game_board.screen.onkey(fun=quit, key="q")
while game_being_played:
    ball_x, ball_y = ball.pos()
    ball.move_ball()
    if ball.collided_with_wall(game_board):
        ball.bounce_back("right")
    if ball.collided_with_paddle(player):
        if ball_x < player.pos()[0]:
            ball.bounce_back("left")
        elif ball_x > player.pos()[1]:
            ball.bounce_back("right")
        else:
            ball.bounce_back("up")
    for brick in brick_manager.bricks:
        if ball.collided_with_brick(brick):
            brick.ht()
            brick_manager.destroy_brick(brick)
            ball.bounce_back("down")


game_board.screen.exitonclick()
