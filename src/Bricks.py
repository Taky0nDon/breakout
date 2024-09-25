import turtle as t

from Board import Board

class Brick(t.Turtle):
    def __init__(self, board: Board=Board()) -> None:
        super().__init__()
        self.board = board
        self.width = round(board.width * .05 * 0.1, 0)
        self.height = round(board.height * .05 * .07, 0)
        self.penup()
        self.shape("square")
        self.shapesize(self.height, self.width)

class BrickManager:
    def __init__(self) -> None:
        self.bricks = []
    def spawn_brick(self, x: int, y:int, board: Board=Board()) -> None:
        new_brick = Brick(board)
        new_brick.goto(x, y)
        self.bricks.append(new_brick)
