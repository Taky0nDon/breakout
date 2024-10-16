import turtle as t

from Board import Board

class Brick(t.Turtle):
    def __init__(self, board: Board=Board()) -> None:
        super().__init__()
        self.speed(0)
        self.board = board
        self.width = round(board.width * .05 * 0.1, 0) + 1
        self.width_px = self.width * 20
        self.height = round(board.height * .05 * .07, 0)
        self.height_px = self.height * 20
        self.gap = self.width # This is the same as multiplying width by 20 and .05
        self.left_edge = 0
        self.right_edge = 0
        self.bottom_edge = 0
        self.top_edge = 0
        self.penup()
        self.shape("square")
        self.shapesize(self.height, self.width)

class BrickManager:
    margin = 0.9
    bricks = []
    vertical_gap = 20

    @classmethod
    def destroy_brick(cls, brick: Brick):
        cls.bricks.remove(brick)
        del(brick)

    @classmethod
    def spawn_brick(cls, x: int|float, y:int|float, board: Board=Board()) -> None:
        new_brick = Brick(board)
        new_brick.hideturtle()
        new_brick.goto(x, y)
        new_brick.bottom_edge = int(new_brick.pos()[1] - (new_brick.height_px  // 2))
        new_brick.top_edge = int(new_brick.pos()[1] + (new_brick.height_px  // 2))
        new_brick.left_edge = int(new_brick.pos()[0] - (new_brick.width_px // 2))
        new_brick.right_edge = int(new_brick.pos()[0] + (new_brick.width_px // 2))
        new_brick.showturtle()
        cls.bricks.append(new_brick)


    @classmethod
    def make_line(cls, board: Board, y: int|float, x_offset: int|float):
        next_brick_position_x = board.left_edge + x_offset
        cls.spawn_brick(next_brick_position_x, y, board)
        current_brick_position_x = 20 * cls.bricks[0].width + cls.bricks[0].gap
        while next_brick_position_x < board.right_edge:
            cls.spawn_brick(next_brick_position_x, y, board)
            next_brick_position_x += current_brick_position_x

    @classmethod
    def build_bricks(cls, n: int, board: Board):
        y_0 = board.height // 4
        for line_n in range(n):
            x_offset = 0
            if line_n % 2 == 1:
                x_offset = 20 * cls.bricks[0].width // 2
            cls.make_line(board, y_0, x_offset) 
            y_0 -= cls.bricks[0].height * 20 + cls.bricks[0].gap

