import turtle as t
from Board import Board
from Paddle import Paddle


def setup(board: Board):
    right_edge = board.width / 2
    upper_edge = board.height / 2
    board.screen.listen()
    board.screen.onkey(fun=quit, key="q")
    pen = t.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.goto(board.width/2*-.95, board.height/2*-.95)
    pen.pendown()
    pen.write("Press q to quit")
    pen.penup()
    
board = Board()
setup(board)

paddle = Paddle(start_x=0, start_y=board.bottom)

board.screen.exitonclick()
