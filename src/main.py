import turtle as t
from Board import Board
from Paddle import Paddle


def setup(board: Board):
    right_edge = board.width / 2
    upper_edge = board.height / 2
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(board.width/2*-.95, board.height/2*-.95)
    pen.pendown()
    pen.write("Press q to quit")
    pen.penup()
    
def setup_paddle_control(paddle: Paddle):
    board.screen.onkey(fun=paddle.move_right, key="l")
    board.screen.onkey(fun=paddle.move_left, key="h")
board = Board()
setup(board)

paddle = Paddle(start_x=0, start_y=board.bottom)
setup_paddle_control(paddle)

board.screen.exitonclick()
