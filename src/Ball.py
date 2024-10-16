import turtle as t
from math import floor
from Board import Board
from Paddle import Paddle
from Bricks import Brick


BASE_SPEED = 10

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed(BASE_SPEED)
        self.seth(270)
        self.x_change = 0
        self.y_change = -0.9

    def move_ball(self):
        self.forward(3)
        # self.goto(0, self.pos()[1] + self.y_change)

    def collided_with_paddle(self, other: Brick | Paddle) -> bool:
        ball_y = self.pos()[1]
        other_y = other.pos()[1]
        min_distance = 20  # 10px ball radius + 5 px 0.5 paddle height
        distance = ball_y - other_y
        if int(distance) < min_distance:
            return True
        return False

    def collided_with_brick(self, other: Brick) -> bool:
        ball_x, ball_y = self.pos()
        if ball_y > other.bottom_edge and ball_y < other.top_edge and \
                ball_x > other.left_edge and ball_x < other.right_edge:
                    return True
        return False

    def collided_with_wall(self, board: Board) -> str:
        """ Returns a string representing which edge of the board the ball hit"""
        ball_x, ball_y = self.pos()
        if ball_x <= board.left_edge:
            return "L"
        if ball_x >= board.right_edge:
            return "R"
        if ball_y >= board.upper_edge:
            return "T"
        else:
            return ""

    def bounce_back(self, surface=''):

        initial_heading = int(self.heading())

        left_wall_heading_change = {
                135: 45,
                225: 315,
                }

        right_wall_heading_change = {
                315: 225,
                45: 135,
                }

        ceiling_heading_change = {
                90: 270,
                45: 315,
                135: 225
                }

        if surface == "L":
            self.change_heading(
                    left_wall_heading_change[initial_heading]
                    )

        if surface == "R":
            self.change_heading(
                    right_wall_heading_change[initial_heading]
                    )

        if surface == "T":
            self.change_heading(
                    ceiling_heading_change[initial_heading]
                    )


    def change_heading(self, new_h: float):
        self.speed(0)
        self.seth(new_h)
        self.speed(BASE_SPEED)
