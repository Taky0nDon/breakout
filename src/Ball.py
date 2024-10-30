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

    def move_ball(self):
        self.forward(3)

    def collided_with_paddle(self, other: Brick | Paddle) -> bool:
        ball_y = self.pos()[1]
        other_y = other.pos()[1]
        min_distance = 20  # 10px ball radius + 5 px 0.5 paddle height
        distance = ball_y - other_y
        if int(distance) < min_distance:
            return True
        return False

    def collided_with_brick(self, other: Brick) -> tuple[bool, str]:
        ball_x, ball_y = self.pos()
        dist_from_ball_to_bottom = int(other.bottom_edge - ball_y)
        dist_from_ball_to_top = int(other.top_edge - ball_y)
        ball_in_horizontal_bounds = ball_x >= other.left_edge\
                and ball_x <= other.right_edge
        hit_bottom =  dist_from_ball_to_bottom in range(0, 11) and ball_in_horizontal_bounds
        hit_top = dist_from_ball_to_top in range(-10,1) and ball_in_horizontal_bounds
        if hit_bottom:
            return True, 'b'
        elif hit_top:
            return True, 't'
        else:
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

        elif surface == "R":
            self.change_heading(
                    right_wall_heading_change[initial_heading]
                    )

        elif surface == "T":
            self.change_heading(
                    ceiling_heading_change[initial_heading]
                    )

        elif surface == "b":
            self.change_heading(self.heading() - 180.0)


    def change_heading(self, new_h: float):
        self.speed(0)
        self.seth(new_h)
        self.speed(BASE_SPEED)
