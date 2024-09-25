from random import randint
import turtle as t
from Board import Board
from Paddle import Paddle
from Ball import Ball
from Bricks import Brick, BrickManager


def setup(board: Board) -> Board:
    right_edge = board.width / 2
    upper_edge = board.height / 2
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(board.width/2*-.95, board.height/2*-.95)
    pen.pendown()
    pen.write("Press q to quit")
    pen.penup()
    return board
    
def setup_paddle_control(paddle: Paddle):
    board.screen.onkey(fun=paddle.move_right, key="l")
    board.screen.onkey(fun=paddle.move_left, key="h")


board = setup(Board())
brick_manager = BrickManager()
paddle = Paddle(start_x=0, start_y=board.bottom, board=board)
ball = Ball()
brick_x = board.width//2 * -1
for n in range(10):
    brick_manager.spawn_brick(x=brick_x, y=0)
    brick_x += brick_manager.bricks[0].width*20
setup_paddle_control(paddle)

board.screen.exitonclick()
