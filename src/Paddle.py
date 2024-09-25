import turtle as t

from Board import Board
# Paddle is 160 wide and 100 tall
class Paddle(t.Turtle):
    def __init__(self, start_x: int|float,
                 start_y: int|float,
                 board: Board) -> None:
        super().__init__()
        self.board = board
        self.paddle_width = round(self.board.width*.05*.2, 0)
        self.penup()
        self.shape("square")
        self.shapesize(0.5, self.paddle_width)
        self.goto(start_x, start_y)

    def move_right(self):
        current_x, current_y = self.pos()
        move_distance = 10
        new_x = current_x + move_distance
        self.goto(new_x, current_y)

    def move_left(self):
        current_x, current_y = self.pos()
        move_distance = -10
        new_x = current_x + move_distance
        self.goto(new_x, current_y)
