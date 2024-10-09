from random import randint
import turtle as t
from Board import BOTTOM_MARGIN, Board
from Paddle import Paddle
from Ball import Ball
from Bricks import Brick, BrickManager


def setup(board: Board) -> Board:
    right_edge = board.width / 2
    upper_edge = board.height / 2
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(board.left_edge, board.bottom)
    pen.pendown()
    pen.write("Press q to quit")
    pen.goto
    pen.penup()
    return board


def setup_paddle_control(paddle: Paddle):
    game_board.screen.onkey(fun=paddle.move_right, key="l")
    game_board.screen.onkey(fun=paddle.move_left, key="h")


game_being_played: bool = True
game_board = setup(Board())
brick_manager = BrickManager()
player = Paddle(start_x=0, start_y=game_board.bottom, board=game_board)
ball = Ball()
# brick_manager.build_bricks(n=3, board=game_board)
setup_paddle_control(player)
print(ball.turtlesize())
collisions = 0
while game_being_played:
    ball.move_ball()
    if ball.collided_with_paddle(player):
        if collisions > 1:
            game_being_played = False
        else:
            print("ball should be bouncing now")
            ball.bounce_back()
            collisions += 1
print(ball.pos())
print(player.pos())


game_board.screen.exitonclick()
